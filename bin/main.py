# Copyright 2022 Arrival Robotics Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''Entry poiny.'''

import argparse
import collections
import json
import pathlib
import scenepic
import tqdm

import numpy as np
import pandas as pd

from fusion360gallerydataset.assembly.joint.dataclasses import JointSet, JointType


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--datasetdir',
                        help='Specify path to the dataset.',
                        type=pathlib.Path,
                        required=True)

    return parser.parse_args()


def main():
    args = parse_args()

    assert args.datasetdir.exists(), f'{args.datasetdir} doesn\'t exist.'
    train_test_metainfo_file = args.datasetdir / 'train_test.json'
    assert train_test_metainfo_file.exists(
    ), f'{train_test_metainfo_file} doesn\'t exist.'
    train_test_metainfo = json.loads(train_test_metainfo_file.read_text())

    statistics = []
    for split_name in tqdm.tqdm(train_test_metainfo,
                                desc='Processing meta info ...'):

        assert split_name in (
            'train', 'validation', 'test',
            'uniform_test'), f'Unexpected split name {split_name}'
        for joint_set_id in tqdm.tqdm(train_test_metainfo.get(split_name),
                                      desc=f'Processing {split_name} ...'):
            joint_set_file = (args.datasetdir / 'joint' /
                              joint_set_id).with_suffix('.json')
            assert joint_set_file.exists(), f'{joint_set_file} doesn\'t exist.'

            joint_set = JointSet.deserialize(joint_set_file.read_text())
            joint_set_stats = collections.defaultdict(int)

            joint_set_stats['id'] = joint_set_id
            joint_set_stats['body_one'] = joint_set.body_one
            joint_set_stats['body_two'] = joint_set.body_two
            joint_set_stats['split_name'] = split_name

            contains_holes = len(joint_set.holes) > 0
            joint_set_stats['contains_holes'] = contains_holes
            joint_set_stats['joints_num'] += len(joint_set.joints)

            for joint in joint_set.joints:
                joint_set_stats[joint.joint_motion.joint_type.value] += 1
                joint_set_stats[
                    joint.geometry_or_origin_one.geometry_type] += 1
                joint_set_stats[
                    joint.geometry_or_origin_two.geometry_type] += 1
                joint_set_stats["one_entity_eqvs_num"] += len(
                    joint.geometry_or_origin_one.entity_one_equivalents)
                joint_set_stats["two_entity_eqvs_num"] += len(
                    joint.geometry_or_origin_two.entity_one_equivalents)

            statistics.append(dict(joint_set_stats))

            if len(statistics) > 20000:
                break

    df = pd.DataFrame(statistics)
    show_stats(df)
    vis_dataset(args.datasetdir, df)


def show_stats(df: pd.DataFrame):
    print(df.groupby(by=['split_name', 'contains_holes']).count().transpose())

    for split_name in df['split_name'].unique():
        query = f'split_name == "{split_name}" and contains_holes == True and CylindricalJointType > 0'
        columns = [
            'id', 'JointPlanarBRepFaceGeometry', 'JointNonPlanarBRepFaceGeometry',
            'JointBRepEdgeGeometry', 'one_entity_eqvs_num', 'two_entity_eqvs_num', 'joints_num'
        ]
        print(split_name)
        print(df.query(query).sort_values('joints_num', ascending=False)[columns].head())


def vis_dataset(datasetdir: pathlib.Path, df: pd.DataFrame):
    meta_info = {}
    for split_name in df['split_name'].unique():
        meta_info[split_name] = []

        scene = scenepic.Scene()

        body_one_canvas = scene.create_canvas_3d(width=600, height=600)
        body_two_canvas = scene.create_canvas_3d(width=600, height=600)
        assembly_canvas = scene.create_canvas_2d(width=600, height=600)

        query = f'split_name == "{split_name}" and contains_holes == True and CylindricalJointType > 0 and joints_num > 2'

        for joint_set_id in df.query(query)['id'].values:
            meta_info[split_name].append(joint_set_id)

            joint_set_file = (datasetdir / 'joint' /
                              joint_set_id).with_suffix('.json')
            assert joint_set_file.exists(), f'{joint_set_file} doesn\'t exist.'

            joint_set = JointSet.deserialize(joint_set_file.read_text())

            body_one_mesh_info = scenepic.load_obj(
                str((datasetdir / 'joint' /
                     joint_set.body_one).with_suffix('.obj')))
            body_one_mesh_id = scene.create_mesh(shared_color=scenepic.Colors.Yellow)
            body_one_mesh_id.add_mesh(
                body_one_mesh_info,
                transform=scenepic.Transforms.Translate(
                    vec=-np.mean(body_one_mesh_info.positions, axis=0)))

            body_one_canvas.create_frame(meshes=[body_one_mesh_id])

            body_two_mesh_info = scenepic.load_obj(
                str((datasetdir / 'joint' /
                     joint_set.body_two).with_suffix('.obj')))
            body_two_mesh_id = scene.create_mesh(
                shared_color=scenepic.Colors.Cyan)
            body_two_mesh_id.add_mesh(
                body_two_mesh_info,
                transform=scenepic.Transforms.Translate(
                    vec=-np.mean(body_two_mesh_info.positions, axis=0)))

            body_two_canvas.create_frame(meshes=[body_two_mesh_id])

            assembly_image = scene.create_image()
            assembly_image.load(
                str((datasetdir / 'joint' / joint_set_id).with_suffix('.png')))
            assembly_frame = assembly_canvas.create_frame()
            assembly_frame.add_image(assembly_image)

        scene.link_canvas_events(body_one_canvas, body_two_canvas, assembly_canvas)
        scene.save_as_html(f'datasets/{split_name}.html')
    if not pathlib.Path('datasets').exists():
        pathlib.Path('datasets').mkdir()
    pathlib.Path('datasets/train_test.json').write_text(json.dumps(meta_info))


if __name__ == '__main__':
    main()
