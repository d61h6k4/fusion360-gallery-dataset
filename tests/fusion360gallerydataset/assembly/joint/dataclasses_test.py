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
'''Tests for fusion360gallerydataset.assembly.joint.dataclasses'''

import json
import pytest

from fusion360gallerydataset.assembly.joint.dataclasses import (JointSet,
                                                                Joint)


@pytest.fixture
def joint_set_17549(datadir):
    return (datadir / 'joint_set_17549.json').read_text()

@pytest.fixture(name='joints')
def fixture_joints(joint_set_17549):
    raw_data = json.loads(joint_set_17549)
    return raw_data.get('joints')


def test_joint_deserialize(joints):
    assert [Joint.deserialize(json.dumps(x)) for x in joints]


def test_joint_set_deserialize(joint_set_17549):
    assert JointSet.deserialize(joint_set_17549)
