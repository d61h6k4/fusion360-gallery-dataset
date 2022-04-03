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
import json
import pathlib
import tqdm


from fusion360gallerydataset.assembly.joint.dataclasses import JointSet

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
    assert train_test_metainfo_file.exists(), f'{train_test_metainfo_file} doesn\'t exist.'
    train_test_metainfo = json.loads(train_test_metainfo_file.read_text())

    for split_name in tqdm.tqdm(train_test_metainfo, desc='Processing meta info ...'):
        assert split_name in ('train', 'validation', 'test', 'uniform_test'), f'Unexpected split name {split_name}'
        for joint_set_id in tqdm.tqdm(train_test_metainfo.get(split_name), desc=f'Processing {split_name} ...'):
            joint_set_file = (args.datasetdir / 'joint' / joint_set_id).with_suffix('.json')
            assert joint_set_file.exists(), f'{joint_set_file} doesn\'t exist.'

            joint_set = JointSet.deserialize(joint_set_file.read_text())
            
            if joint_set.holes and joint_set.contacts:
                print(joint_set_id)



if __name__ == '__main__':
    main()
