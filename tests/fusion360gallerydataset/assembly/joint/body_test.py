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
'''Tests suite for fusion360gallerydataset.assembly.joint.body'''

import dataclasses
import json
import pytest
import pathlib

import numpy as np

from occwl.compound import Compound
from occwl.entity_mapper import EntityMapper

from fusion360gallerydataset.assembly.joint import body


@pytest.fixture(name='body_22666_bdaa1303_0035_2')
def load_body_22666_bdaa1303_0035_2(datadir: pathlib.Path) -> Compound:
    return Compound.load_from_step(datadir / '22666_bdaa1303_0035_2.step')


def test_entities(data_regression, body_22666_bdaa1303_0035_2):
    '''Checks funciton returns all entities of the body'''
    entity_mapper = EntityMapper(body_22666_bdaa1303_0035_2)

    materialized_entities = {
        f'{e.type}_{e.index}': dataclasses.asdict(e)
        for e in body.entities('22666_bdaa1303_0035_2',
                               body_22666_bdaa1303_0035_2, entity_mapper)
    }

    data_regression.check(json.loads(json.dumps(materialized_entities, cls=NumpyEncoder)))


class NumpyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, np.ndarray):
            return o.tolist()
        return json.JSONEncoder.default(self, o)
