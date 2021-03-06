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
'''Parser of Fusion360GalleryDataset Assembly-Joint data.'''

from typing import Optional, Sequence, Text, Union

import dataclasses
import enum
import json

import numpy as np


class JointType(str, enum.Enum):
    '''Joint motion type.
    https://github.com/autodeskailab/fusion360gallerydataset/blob/master/docs/assembly_joint.md#joint-motion
    '''
    RIGID = 'RigidJointType'
    REVOLUTE = 'RevoluteJointType'
    SLIDER = 'SliderJointType'
    CYLINDRICAL = 'CylindricalJointType'
    PIN_SLOT = 'PinSlotJointType'
    PLANAR = 'PlanarJointType'
    BALL = 'BallJointType'


@dataclasses.dataclass
class Limit:
    '''Movement limits.'''
    minimum_value: float
    maximum_value: float
    rest_value: float
    is_minimum_value_enabled: bool
    is_maximum_value_enabled: bool
    is_rest_value_enabled: bool

    @staticmethod
    def deserialize(blob: Text) -> 'Limit':
        '''Deserialize limits.'''
        raw_data = json.loads(blob)

        return Limit(
            minimum_value=raw_data.get('minimum_value'),
            maximum_value=raw_data.get('maximum_value'),
            rest_value=raw_data.get('rest_value'),
            is_minimum_value_enabled=raw_data.get('is_minimum_value_enabled'),
            is_maximum_value_enabled=raw_data.get('is_maximum_value_enabled'),
            is_rest_value_enabled=raw_data.get('is_rest_value_enabled'))


@dataclasses.dataclass
class Rigid:
    '''Rigid joint motion, 0 dof.'''


@dataclasses.dataclass
class Revolute:
    '''Revolute joint motion.'''
    rotation_axis: str
    rotation_limits: Limit


@dataclasses.dataclass
class Slider:
    '''Slider joint motion.'''
    slide_direction: str
    slide_limits: Limit


@dataclasses.dataclass
class Cylindrical:
    '''Cylindrical joint motion.'''
    rotation_axis: str
    rotation_limits: Limit
    slide_limits: Limit


@dataclasses.dataclass
class PinSlot:
    '''Pin slot joint motion.'''
    rotation_axis: str
    slide_direction: str
    rotation_limits: Limit
    slide_limits: Limit


@dataclasses.dataclass
class Planar:
    '''Planar joint motion.'''
    normal_direction: str
    primary_slide_direction: str
    rotation_limits: Limit
    primary_slide_limits: Limit


@dataclasses.dataclass
class Ball:
    '''Ball joint motion.'''
    pitch_direction: str
    yaw_direction: str
    pitch_limits: Limit
    roll_limits: Limit
    yaw_limits: Limit


@dataclasses.dataclass
class JointMotion:
    '''Joint motion.
    https://github.com/autodeskailab/fusion360gallerydataset/blob/master/docs/assembly_joint.md#joint-motion
    '''
    joint_type: JointType
    motion: Union[Rigid, Revolute, Slider, Cylindrical, PinSlot, Planar, Ball]

    @staticmethod
    def deserialize(blob: Text) -> 'JointMotion':
        '''Deserialize JointMotion from json.'''
        raw_data = json.loads(blob)

        joint_type = JointType(raw_data.get('joint_type'))

        if joint_type is JointType.RIGID:
            return JointMotion(joint_type=joint_type, motion=Rigid())
        elif joint_type is JointType.REVOLUTE:
            return JointMotion(joint_type=joint_type,
                               motion=Revolute(
                                   rotation_axis=raw_data.get('rotation_axis'),
                                   rotation_limits=Limit.deserialize(
                                       json.dumps(
                                           raw_data.get('rotation_limits')))))
        elif joint_type is JointType.SLIDER:
            return JointMotion(
                joint_type=joint_type,
                motion=Slider(slide_direction=raw_data.get('slide_direction'),
                              slide_limits=Limit.deserialize(
                                  json.dumps(raw_data.get('slide_limits')))))
        elif joint_type is JointType.CYLINDRICAL:
            return JointMotion(
                joint_type=joint_type,
                motion=Cylindrical(
                    rotation_axis=raw_data.get('rotation_axis'),
                    rotation_limits=Limit.deserialize(
                        json.dumps(raw_data.get('rotation_limits'))),
                    slide_limits=Limit.deserialize(
                        json.dumps(raw_data.get('slide_limits')))))
        elif joint_type is JointType.PIN_SLOT:
            return JointMotion(
                joint_type=joint_type,
                motion=PinSlot(rotation_axis=raw_data.get('rotation_axis'),
                               slide_direction=raw_data.get('slide_direction'),
                               rotation_limits=Limit.deserialize(
                                   json.dumps(
                                       raw_data.get('rotation_limits'))),
                               slide_limits=Limit.deserialize(
                                   json.dumps(raw_data.get('slide_limits')))))
        elif joint_type is JointType.PLANAR:
            return JointMotion(
                joint_type=joint_type,
                motion=Planar(
                    normal_direction=raw_data.get('normal_direction'),
                    primary_slide_direction=raw_data.get(
                        'primary_slide_direction'),
                    rotation_limits=Limit.deserialize(
                        json.dumps(raw_data.get('rotation_limits'))),
                    primary_slide_limits=Limit.deserialize(
                        json.dumps(raw_data.get('primary_slide_limits')))))
        elif joint_type is JointType.BALL:
            return JointMotion(
                joint_type=joint_type,
                motion=Ball(pitch_direction=raw_data.get('pitch_direction'),
                            yaw_direction=raw_data.get('yaw_direction'),
                            pitch_limits=Limit.deserialize(
                                json.dumps(raw_data.get('pitch_limits'))),
                            roll_limits=Limit.deserialize(
                                json.dumps(raw_data.get('roll_limits'))),
                            yaw_limits=Limit.deserialize(
                                json.dumps(raw_data.get('yaw_limits')))))

        raise NotImplementedError(blob)


@dataclasses.dataclass
class Point3D:
    '''Point in 3D.
    We use numpy to represent it, order is x, y, z
    (means index 0 for x, index 1 for y and index 2 for z)
    '''
    point: np.ndarray

    @staticmethod
    def deserialize(blob: Text) -> 'Point3D':
        '''Deserialize Point3D from json.'''
        raw_data = json.loads(blob)
        assert raw_data.get('type') == 'Point3D', blob
        return Point3D(point=np.array(
            [raw_data.get('x'),
             raw_data.get('y'),
             raw_data.get('z')]))


@dataclasses.dataclass
class Vector3D:
    '''Vector in 3D.
    We use numpy to represent it, order is x, y, z
    (means index 0 for x, index 1 for y and index 2 for z)

    !Vector has no difference with point in representation level
    but it is important to differentiate them from math POV.
    '''
    # x, y, z
    point: np.ndarray

    @staticmethod
    def deserialize(blob: Text) -> 'Vector3D':
        '''Deserialize Vector3D from json.'''
        raw_data = json.loads(blob)
        assert raw_data.get('type') == 'Vector3D', blob
        return Vector3D(point=np.array(
            [raw_data.get('x'),
             raw_data.get('y'),
             raw_data.get('z')]))


@dataclasses.dataclass
class BoundingBox:
    '''BoundingBox.

    We represent bounding_box with min and max points.
    '''
    min_point: Point3D
    max_point: Point3D

    @staticmethod
    def deserialize(blob: Text) -> 'BoundingBox':
        '''Deserialize BoundingBox from json.'''
        raw_data = json.loads(blob)
        assert raw_data.get('type') == 'BoundingBox3D', blob

        return BoundingBox(
            min_point=Point3D.deserialize(json.dumps(
                raw_data.get('min_point'))),
            max_point=Point3D.deserialize(json.dumps(
                raw_data.get('max_point'))),
        )


@dataclasses.dataclass
class EntityOne:
    '''EntityOne describes the entity (edge or face) of the BRep
    that used for joint.
    https://github.com/AutodeskAILab/Fusion360GalleryDataset/blob/master/docs/assembly_joint.md#joint-geometry
    '''
    type: str
    body: str
    curve_type: Optional[str]
    surface_type: Optional[str]
    point_on_entity: Point3D
    index: int
    bounding_box: BoundingBox
    id: int

    @staticmethod
    def deserialize(blob: Text) -> 'EntityOne':
        '''Deserialize EntityOne from json.'''
        raw_data = json.loads(blob)
        return EntityOne(type=raw_data.get('type'),
                         body=raw_data.get('body'),
                         curve_type=raw_data.get('curve_type'),
                         surface_type=raw_data.get('surface_type'),
                         point_on_entity=Point3D.deserialize(
                             json.dumps(raw_data.get('point_on_entity'))),
                         index=raw_data.get('index'),
                         bounding_box=BoundingBox.deserialize(
                             json.dumps(raw_data.get('bounding_box'))),
                         id=raw_data.get('id'))


@dataclasses.dataclass
class Transform:
    '''Transform is function that transforms BRep
    to the assembly state.

    https://github.com/AutodeskAILab/Fusion360GalleryDataset/blob/master/docs/assembly_joint.md#joint-geometry
    '''
    origin: Point3D
    x_axis: Vector3D
    y_axis: Vector3D
    z_axis: Vector3D

    @staticmethod
    def deserialize(blob: Text) -> 'Transform':
        '''Deserialize Transform from json.'''
        raw_data = json.loads(blob)

        return Transform(
            origin=Point3D.deserialize(json.dumps(raw_data.get('origin'))),
            x_axis=Vector3D.deserialize(json.dumps(raw_data.get('x_axis'))),
            y_axis=Vector3D.deserialize(json.dumps(raw_data.get('y_axis'))),
            z_axis=Vector3D.deserialize(json.dumps(raw_data.get('z_axis'))))


@dataclasses.dataclass
class AxisLine:
    '''AxisLine, contains the origin point and direction vector on the joint axis when in an assembled state.'''
    origin: Point3D
    direction: Vector3D

    @staticmethod
    def deserialize(blob: Text) -> 'AxisLine':
        '''Deserialize AxisLine from json.'''
        raw_data = json.loads(blob)
        return AxisLine(
            origin=Point3D.deserialize(json.dumps(raw_data.get('origin'))),
            direction=Vector3D.deserialize(
                json.dumps(raw_data.get('direction'))),
        )


@dataclasses.dataclass
class JointGeometry:
    '''JointGeometry is designer-selected B-Rep faces and edges, form the geometric entites used to define joints.

    https://github.com/AutodeskAILab/Fusion360GalleryDataset/blob/master/docs/assembly_joint.md#joint-geometry
    '''
    geometry_type: str
    key_point_type: str
    origin: Point3D
    primary_axis_vector: Vector3D
    secondary_axis_vector: Vector3D
    tertiary_axis_vector: Vector3D
    entity_one: EntityOne
    transform: Transform
    axis_line: AxisLine
    entity_one_equivalents: Sequence[EntityOne]

    @staticmethod
    def deserialize(blob: Text) -> 'JointGeometry':
        '''Deserialize JointGeometry from json.'''
        raw_data = json.loads(blob)
        assert raw_data.get('type') == 'JointGeometry', blob

        return JointGeometry(
            geometry_type=raw_data.get('geometry_type'),
            key_point_type=raw_data.get('key_point_type'),
            origin=Point3D.deserialize(json.dumps(raw_data.get('origin'))),
            primary_axis_vector=Vector3D.deserialize(
                json.dumps(raw_data.get('primary_axis_vector'))),
            secondary_axis_vector=Vector3D.deserialize(
                json.dumps(raw_data.get('secondary_axis_vector'))),
            tertiary_axis_vector=Vector3D.deserialize(
                json.dumps(raw_data.get('tertiary_axis_vector'))),
            entity_one=EntityOne.deserialize(
                json.dumps(raw_data.get('entity_one'))),
            transform=Transform.deserialize(
                json.dumps(raw_data.get('transform'))),
            axis_line=AxisLine.deserialize(
                json.dumps(raw_data.get('axis_line'))),
            entity_one_equivalents=[
                EntityOne.deserialize(json.dumps(x))
                for x in raw_data.get('entity_one_equivalents', [])
            ])


@dataclasses.dataclass
class Offset:
    '''The offset between the two input geometries.'''
    role: str
    value: float

    @staticmethod
    def deserialize(blob: Text) -> 'Offset':
        '''Deserialize Offset from json.'''
        raw_data = json.loads(blob)
        assert raw_data.get('type') == 'ModelParameter', blob
        assert raw_data.get('name') in ('offset', 'd4'), blob

        return Offset(role=raw_data.get('role'), value=raw_data.get('value'))


@dataclasses.dataclass
class Angle:
    '''The angle between the two input geometries.'''
    role: str
    value: float

    @staticmethod
    def deserialize(blob: Text) -> 'Angle':
        '''Deserialize Angle from json.'''
        raw_data = json.loads(blob)
        assert raw_data.get('type') == 'ModelParameter', blob
        assert raw_data.get('name') in ('angle', 'd1'), blob

        return Angle(role=raw_data.get('role'), value=raw_data.get('value'))


@dataclasses.dataclass
class Joint:
    '''Contains joint parameter information.

    https://github.com/AutodeskAILab/Fusion360GalleryDataset/blob/master/docs/assembly_joint.md#joints
    '''
    name: str
    joint_motion: JointMotion
    geometry_or_origin_one: JointGeometry
    geometry_or_origin_two: JointGeometry
    offset: Offset
    angle: Angle
    is_flipped: bool

    @staticmethod
    def deserialize(blob: Text) -> 'Joint':
        '''Deserialize Joint from json.'''
        raw_data = json.loads(blob)
        assert raw_data.get('type') == 'Joint', blob

        return Joint(
            name=raw_data.get('name'),
            joint_motion=JointMotion.deserialize(
                json.dumps(raw_data.get('joint_motion'))),
            geometry_or_origin_one=JointGeometry.deserialize(
                json.dumps(raw_data.get('geometry_or_origin_one'))),
            geometry_or_origin_two=JointGeometry.deserialize(
                json.dumps(raw_data.get('geometry_or_origin_two'))),
            offset=Offset.deserialize(json.dumps(raw_data.get('offset'))),
            angle=Angle.deserialize(json.dumps(raw_data.get('angle'))),
            is_flipped=raw_data.get('is_flipped'))


@dataclasses.dataclass
class Contact:
    '''Contact labels that indicate which B-Rep faces are coincident or within a tolerance of 0.1mm.

    https://github.com/AutodeskAILab/Fusion360GalleryDataset/blob/master/docs/assembly_joint.md#contacts
    '''
    entity_one: EntityOne

    @staticmethod
    def deserialize(blob: Text) -> 'Contact':
        '''Deserialize Contact from json.'''
        raw_data = json.loads(blob)
        return Contact(entity_one=EntityOne.deserialize(
            json.dumps(raw_data.get('entity_one'))))


@dataclasses.dataclass
class Hole:
    '''Hole.

    https://github.com/AutodeskAILab/Fusion360GalleryDataset/blob/master/docs/assembly_joint.md#contacts
    '''
    type: str
    body: str
    diameter: float
    length: float
    origin: Point3D
    direction: Vector3D
    faces: Sequence[EntityOne]
    edges: Sequence[EntityOne]

    @staticmethod
    def deserialize(blob: Text) -> 'Hole':
        '''Deserialize Hole from json.'''
        raw_data = json.loads(blob)

        return Hole(type=raw_data.get('type'),
                    body=raw_data.get('body'),
                    diameter=raw_data.get('diameter'),
                    length=raw_data.get('length'),
                    origin=Point3D.deserialize(
                        json.dumps(raw_data.get('origin'))),
                    direction=Vector3D.deserialize(
                        json.dumps(raw_data.get('direction'))),
                    faces=[
                        EntityOne.deserialize(json.dumps(x))
                        for x in raw_data.get('faces', [])
                    ],
                    edges=[
                        EntityOne.deserialize(json.dumps(x))
                        for x in raw_data.get('edges', [])
                    ])


@dataclasses.dataclass
class JointSet:
    '''Joint paramter information.

    https://github.com/AutodeskAILab/Fusion360GalleryDataset/blob/master/docs/assembly_joint.md#joint-set-json
    '''
    body_one: str
    body_two: str
    joints: Sequence[Joint]
    contacts: Sequence[Contact]
    holes: Sequence[Hole]

    @staticmethod
    def deserialize(blob: Text) -> 'JointSet':
        '''Deserialize JointSet from json.'''
        raw_data = json.loads(blob)

        body_one = raw_data.get('body_one')
        body_two = raw_data.get('body_two')
        joints = [
            Joint.deserialize(json.dumps(x)) for x in raw_data.get('joints')
        ]
        contacts = [
            Contact.deserialize(json.dumps(x))
            for x in raw_data.get('contacts', [])
        ]
        holes = [
            Hole.deserialize(json.dumps(x)) for x in raw_data.get('holes', [])
        ]

        return JointSet(body_one=body_one,
                        body_two=body_two,
                        joints=joints,
                        contacts=contacts,
                        holes=holes)
