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
'''Process the body (represented as Compound).'''

from typing import Generator

import numpy as np

from occwl.compound import Compound
from occwl.geometry.box import Box
from occwl.entity_mapper import EntityMapper

from fusion360gallerydataset.assembly.joint.dataclasses import EntityOne
from fusion360gallerydataset.assembly.joint.dataclasses import BoundingBox

from fusion360gallerydataset.assembly.joint.dataclasses import Point3D


def entities(body_name: str, body: Compound,
             entity_mapper: EntityMapper) -> Generator[EntityOne, None, None]:
    '''Returns face/edge as entities.
    Here we use entity mapper as a checker to guarantee that entity indexes are consistent.
    '''
    for face in body.faces():
        yield EntityOne(
            type='BRepFace',
            body=body_name,
            curve_type=None,
            surface_type=face.surface_type(),
            # we don't use this value, so I decided to not spend computation to do something smarter
            point_on_entity=Point3D(point=np.array([0., 0., 0.])),
            bounding_box=_box_to_bbox(face.exact_box()),
            index=entity_mapper.face_index(face),
            id=entity_mapper.face_index(face))

    for edge in body.edges():
        yield EntityOne(
            type='BRepEdge',
            body=body_name,
            curve_type=edge.curve_type(),
            surface_type=None,
            # see comment above
            point_on_entity=Point3D(point=np.array([0., 0., 0.])),
            bounding_box=_box_to_bbox(edge.exact_box()),
            index=entity_mapper.edge_index(edge),
            id=entity_mapper.edge_index(edge))


def _box_to_bbox(box: Box) -> BoundingBox:
    return BoundingBox(min_point=Point3D(point=box.min_point()),
                       max_point=Point3D(point=box.max_point()))
