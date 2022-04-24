# Copyright 2022 Petrov, Danil <ddbihbka@gmail.com>. All Rights Reserved.
# Author: Petrov, Danil <ddbihbka@gmail.com>
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
'''Show example - joint.'''

from typing import Mapping, Tuple

import argparse
import functools
import json
import pathlib
import tqdm

import numpy as np

from occwl.compound import Compound
from occwl.entity_mapper import EntityMapper

from fusion360gallerydataset.assembly.joint.dataclasses import EntityOne, JointSet
from fusion360gallerydataset.assembly.joint.graphs import add_positional_encoding, create_joint_set_graph
from fusion360gallerydataset.assembly.joint.body import entities

from brep2graph.configurations import simple_edge
from brep2graph.features import face_features_from_body, edge_features_from_body, coedge_features_from_body
from brep2graph.incidence_arrays import build_incidence_arrays


def parse_args():
    '''Parse args.'''
    parser = argparse.ArgumentParser()

    parser.add_argument('--datasetdir',
                        type=pathlib.Path,
                        help='Specify path to the folder with joint sets.',
                        required=True)
    parser.add_argument('--metainfo',
                        type=pathlib.Path,
                        help='Specify path to the train_test.json',
                        required=True)

    return parser.parse_args()


def main():
    args = parse_args()

    assert args.datasetdir.exists(), f'{args.datasetdir} does not exist.'
    assert args.metainfo.exists(), 'dataset dir should contain train_test.json'

    train_test_metainfo = json.loads(args.metainfo.read_text())

    for split_name in tqdm.tqdm(train_test_metainfo,
                                desc='Processing meta info ...'):

        assert split_name in (
            'train', 'validation', 'test',
            'uniform_test'), f'Unexpected split name {split_name}'
        stats = {}
        for joint_set_id in tqdm.tqdm(train_test_metainfo.get(split_name),
                                      desc=f'Processing {split_name} ...'):

            joint_set_file = (args.datasetdir / 'joint' /
                              joint_set_id).with_suffix('.json')
            assert joint_set_file.exists(), f'{joint_set_file} doesn\'t exist.'
            joint_set = JointSet.deserialize(joint_set_file.read_text())

            body_one = load_body(args.datasetdir / 'joint', joint_set.body_one)
            body_one_em = EntityMapper(body_one)
            body_one_graph = graph_from_body(body_one, body_one_em)

            body_two = load_body(args.datasetdir / 'joint', joint_set.body_two)
            body_two_em = EntityMapper(body_two)
            body_two_graph = graph_from_body(body_two, body_two_em)

            mate_graph = create_joint_set_graph(body_one_graph, body_two_graph)

            expected = 0
            got = 0
            for joint in joint_set.joints:
                expected += 1
                try:
                    body_one_chosen_entity = body_chosen_entity(
                    joint_set.body_one, body_one, body_one_em,
                    joint.geometry_or_origin_one.entity_one)
                except ValueError as e:
                    continue
                try:
                    body_two_chosen_entity = body_chosen_entity(
                    joint_set.body_two, body_two, body_two_em,
                    joint.geometry_or_origin_two.entity_one)
                except ValueError as e:
                    continue
                got += 1
                # print(body_one_chosen_entity, body_two_chosen_entity)
                # return 1
            stats[joint_set_id] = {'expected': expected, 'got': got}
        print(split_name, stats)


def load_body(datasetdir: pathlib.Path, body_one_name: str) -> Compound:
    return Compound.load_from_step(
        (datasetdir / body_one_name).with_suffix('.step'))


def graph_from_body(body: Compound,
                    em: EntityMapper) -> Mapping[str, np.ndarray]:
    g = simple_edge(face_features_from_body(body, em),
                    edge_features_from_body(body, em),
                    coedge_features_from_body(body, em),
                    build_incidence_arrays(body, em))

    assert isinstance(g, dict)
    add_positional_encoding(3, g)

    return g


def body_chosen_entity(body_name: str, body: Compound, em: EntityMapper,
                       entity: EntityOne) -> int:
    for k, v in load_entities(body_name, body, em).items():
        if (v.type == entity.type
                and np.allclose(v.bounding_box.min_point.point,
                                entity.bounding_box.min_point.point)
                and np.allclose(v.bounding_box.max_point.point,
                                entity.bounding_box.max_point.point)):
            return local_to_global_index(k, em)
    raise ValueError(
        f'{body_name} does not have entity matching with {entity}')


def local_to_global_index(local_index: Tuple[str, int],
                          em: EntityMapper) -> int:
    if local_index[0] == 'BRepFace':
        return local_index[1]
    elif local_index[0] == 'BRepEdge':
        return em.get_num_faces() + local_index[1]
    else:
        raise ValueError(f'Unexpected local index {local_index}')


@functools.cache
def load_entities(body_name: str, body: Compound,
                  em: EntityMapper) -> Mapping[Tuple[str, int], EntityOne]:
    return {(e.type, e.index): e for e in entities(body_name, body, em)}


if __name__ == '__main__':
    main()
