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
'''Fixtures to hold a test data.'''

import pytest


@pytest.fixture
def joint_set_17549():
    return '''{
        "body_one":
        "22666_bdaa1303_0035_2",
        "body_two":
        "22666_bdaa1303_0008_2",
        "joints": [{
            "name": "Rigid9",
            "type": "Joint",
            "joint_motion": {
                "joint_type": "RigidJointType"
            },
            "geometry_or_origin_one": {
                "type":
                "JointGeometry",
                "geometry_type":
                "JointBRepEdgeGeometry",
                "key_point_type":
                "CenterKeyPoint",
                "origin": {
                    "type": "Point3D",
                    "x": 0.0,
                    "y": 0.0,
                    "z": -4.60502
                },
                "primary_axis_vector": {
                    "type": "Vector3D",
                    "x": 0.0,
                    "y": 0.0,
                    "z": 1.0,
                    "length": 1.0
                },
                "secondary_axis_vector": {
                    "type": "Vector3D",
                    "x": 1.0,
                    "y": 0.0,
                    "z": 0.0,
                    "length": 1.0
                },
                "tertiary_axis_vector": {
                    "type": "Vector3D",
                    "x": 0.0,
                    "y": 1.0,
                    "z": 0.0,
                    "length": 1.0
                },
                "entity_one": {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.9105899999999999,
                        "y": 0.0,
                        "z": -0.9550400000000001
                    },
                    "index": 7,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.9105899999999999,
                            "y": 0.9105899999999999,
                            "z": -0.9550400000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.9105899999999999,
                            "y": -0.9105899999999999,
                            "z": -0.9550400000000001
                        }
                    },
                    "id": 0
                },
                "transform": {
                    "origin": {
                        "type": "Point3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": -5.56006
                    },
                    "x_axis": {
                        "type": "Vector3D",
                        "x": -1.0,
                        "y": 1.2246467991473532e-16,
                        "z": 0.0,
                        "length": 1.0
                    },
                    "y_axis": {
                        "type": "Vector3D",
                        "x": 1.2246467991473532e-16,
                        "y": 1.0,
                        "z": 0.0,
                        "length": 1.0
                    },
                    "z_axis": {
                        "type": "Vector3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": -1.0,
                        "length": 1.0
                    }
                },
                "axis_line": {
                    "origin": {
                        "type": "Point3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": -4.60502
                    },
                    "direction": {
                        "type": "Vector3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": -1.0,
                        "length": 1.0
                    }
                },
                "entity_one_equivalents": [{
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "CylinderSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 2.9161901904696347e-17,
                        "y": -0.47625,
                        "z": -0.7556500000000002
                    },
                    "index": 0,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.47625,
                            "y": 0.47625,
                            "z": 0.0
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.47625,
                            "y": -0.47625,
                            "z": -1.5113000000000003
                        }
                    },
                    "id": 1
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "PlaneSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.8324849999999999,
                        "y": 0.0,
                        "z": -1.2725400000000002
                    },
                    "index": 1,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.9105899999999999,
                            "y": 0.9105899999999999,
                            "z": -1.2725400000000002
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.9105899999999999,
                            "y": -0.9105899999999999,
                            "z": -1.2725400000000002
                        }
                    },
                    "id": 2
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "CylinderSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -5.575755644177941e-17,
                        "y": 0.9105899999999999,
                        "z": -1.3919200000000003
                    },
                    "index": 2,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.9105899999999999,
                            "y": 0.9105899999999999,
                            "z": -1.2725400000000002
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.9105899999999999,
                            "y": -0.9105899999999999,
                            "z": -1.5113000000000003
                        }
                    },
                    "id": 3
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "PlaneSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 0.6934199999999999,
                        "y": 0.0,
                        "z": -1.5113000000000003
                    },
                    "index": 3,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.9105899999999999,
                            "y": 0.9105899999999999,
                            "z": -1.5113000000000003
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.9105899999999999,
                            "y": -0.9105899999999999,
                            "z": -1.5113000000000003
                        }
                    },
                    "id": 4
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "CylinderSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -4.619245261703901e-17,
                        "y": 0.7543799999999999,
                        "z": -1.1531600000000002
                    },
                    "index": 4,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.7543799999999999,
                            "y": 0.7543799999999999,
                            "z": -1.0337800000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.7543799999999999,
                            "y": -0.7543799999999999,
                            "z": -1.2725400000000002
                        }
                    },
                    "id": 5
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "CylinderSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -5.575755644177941e-17,
                        "y": 0.9105899999999999,
                        "z": -0.9944100000000001
                    },
                    "index": 5,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.9105899999999999,
                            "y": 0.9105899999999999,
                            "z": -0.9550400000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.9105899999999999,
                            "y": -0.9105899999999999,
                            "z": -1.0337800000000001
                        }
                    },
                    "id": 6
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "PlaneSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.8324849999999999,
                        "y": 0.0,
                        "z": -1.0337800000000001
                    },
                    "index": 6,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.9105899999999999,
                            "y": 0.9105899999999999,
                            "z": -1.0337800000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.9105899999999999,
                            "y": -0.9105899999999999,
                            "z": -1.0337800000000001
                        }
                    },
                    "id": 7
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "PlaneSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 0.91313,
                        "y": 0.0,
                        "z": -0.7950200000000001
                    },
                    "index": 7,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 1.19126,
                            "y": 1.19126,
                            "z": -0.7950200000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -1.19126,
                            "y": -1.19126,
                            "z": -0.7950200000000001
                        }
                    },
                    "id": 8
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "CylinderSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -7.29436372976138e-17,
                        "y": 1.19126,
                        "z": -0.8750300000000001
                    },
                    "index": 14,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 1.19126,
                            "y": 1.19126,
                            "z": -0.7950200000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -1.19126,
                            "y": -1.19126,
                            "z": -0.9550400000000001
                        }
                    },
                    "id": 15
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "PlaneSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.9410700000000001,
                        "y": 0.0,
                        "z": -0.9550400000000001
                    },
                    "index": 15,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 1.19126,
                            "y": 1.19126,
                            "z": -0.9550400000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -1.19126,
                            "y": -1.19126,
                            "z": -0.9550400000000001
                        }
                    },
                    "id": 16
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "CylinderSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 3.8882535872928465e-17,
                        "y": -0.635,
                        "z": -0.39751000000000003
                    },
                    "index": 16,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.635,
                            "y": 0.635,
                            "z": 0.0
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.635,
                            "y": -0.635,
                            "z": -0.7950200000000001
                        }
                    },
                    "id": 17
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0035_2",
                    "surface_type": "PlaneSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 0.555625,
                        "y": 0.0,
                        "z": 0.0
                    },
                    "index": 17,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.635,
                            "y": 0.635,
                            "z": 0.0
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.635,
                            "y": -0.635,
                            "z": 0.0
                        }
                    },
                    "id": 18
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 0.47625,
                        "y": 0.0,
                        "z": -1.5113000000000003
                    },
                    "index": 0,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.47625,
                            "y": 0.47625,
                            "z": -1.5113000000000003
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.47625,
                            "y": -0.47625,
                            "z": -1.5113000000000003
                        }
                    },
                    "id": 22
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 0.47625,
                        "y": 0.0,
                        "z": 0.0
                    },
                    "index": 1,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.47625,
                            "y": 0.47625,
                            "z": 0.0
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.47625,
                            "y": -0.47625,
                            "z": 0.0
                        }
                    },
                    "id": 23
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.9105899999999999,
                        "y": 0.0,
                        "z": -1.2725400000000002
                    },
                    "index": 2,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.9105899999999999,
                            "y": 0.9105899999999999,
                            "z": -1.2725400000000002
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.9105899999999999,
                            "y": -0.9105899999999999,
                            "z": -1.2725400000000002
                        }
                    },
                    "id": 24
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.7543799999999999,
                        "y": 0.0,
                        "z": -1.2725400000000002
                    },
                    "index": 3,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.7543799999999999,
                            "y": 0.7543799999999999,
                            "z": -1.2725400000000002
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.7543799999999999,
                            "y": -0.7543799999999999,
                            "z": -1.2725400000000002
                        }
                    },
                    "id": 19
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.9105899999999999,
                        "y": 0.0,
                        "z": -1.5113000000000003
                    },
                    "index": 4,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.9105899999999999,
                            "y": 0.9105899999999999,
                            "z": -1.5113000000000003
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.9105899999999999,
                            "y": -0.9105899999999999,
                            "z": -1.5113000000000003
                        }
                    },
                    "id": 25
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.7543799999999999,
                        "y": 0.0,
                        "z": -1.0337800000000001
                    },
                    "index": 5,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.7543799999999999,
                            "y": 0.7543799999999999,
                            "z": -1.0337800000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.7543799999999999,
                            "y": -0.7543799999999999,
                            "z": -1.0337800000000001
                        }
                    },
                    "id": 20
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.9105899999999999,
                        "y": 0.0,
                        "z": -1.0337800000000001
                    },
                    "index": 6,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.9105899999999999,
                            "y": 0.9105899999999999,
                            "z": -1.0337800000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.9105899999999999,
                            "y": -0.9105899999999999,
                            "z": -1.0337800000000001
                        }
                    },
                    "id": 26
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -1.19126,
                        "y": 0.0,
                        "z": -0.7950200000000001
                    },
                    "index": 8,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 1.19126,
                            "y": 1.19126,
                            "z": -0.7950200000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -1.19126,
                            "y": -1.19126,
                            "z": -0.7950200000000001
                        }
                    },
                    "id": 27
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 0.635,
                        "y": 0.0,
                        "z": -0.7950200000000001
                    },
                    "index": 15,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.635,
                            "y": 0.635,
                            "z": -0.7950200000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.635,
                            "y": -0.635,
                            "z": -0.7950200000000001
                        }
                    },
                    "id": 21
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -1.19126,
                        "y": 0.0,
                        "z": -0.9550400000000001
                    },
                    "index": 22,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 1.19126,
                            "y": 1.19126,
                            "z": -0.9550400000000001
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -1.19126,
                            "y": -1.19126,
                            "z": -0.9550400000000001
                        }
                    },
                    "id": 40
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0035_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 0.635,
                        "y": 0.0,
                        "z": 0.0
                    },
                    "index": 23,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.635,
                            "y": 0.635,
                            "z": 0.0
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.635,
                            "y": -0.635,
                            "z": 0.0
                        }
                    },
                    "id": 41
                }]
            },
            "geometry_or_origin_two": {
                "type":
                "JointGeometry",
                "geometry_type":
                "JointBRepEdgeGeometry",
                "key_point_type":
                "CenterKeyPoint",
                "origin": {
                    "type": "Point3D",
                    "x": 0.0,
                    "y": 0.0,
                    "z": -4.60502
                },
                "primary_axis_vector": {
                    "type": "Vector3D",
                    "x": 0.0,
                    "y": 0.0,
                    "z": 1.0,
                    "length": 1.0
                },
                "secondary_axis_vector": {
                    "type": "Vector3D",
                    "x": 1.0,
                    "y": 0.0,
                    "z": 0.0,
                    "length": 1.0
                },
                "tertiary_axis_vector": {
                    "type": "Vector3D",
                    "x": 0.0,
                    "y": 1.0,
                    "z": 0.0,
                    "length": 1.0
                },
                "entity_one": {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0008_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 0.91313,
                        "y": 0.0,
                        "z": -4.60502
                    },
                    "index": 142,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.91313,
                            "y": 0.91313,
                            "z": -4.60502
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.91313,
                            "y": -0.91313,
                            "z": -4.60502
                        }
                    },
                    "id": 0
                },
                "transform": {
                    "origin": {
                        "type": "Point3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": 0.0
                    },
                    "x_axis": {
                        "type": "Vector3D",
                        "x": 1.0,
                        "y": 0.0,
                        "z": 0.0,
                        "length": 1.0
                    },
                    "y_axis": {
                        "type": "Vector3D",
                        "x": 0.0,
                        "y": 1.0,
                        "z": 0.0,
                        "length": 1.0
                    },
                    "z_axis": {
                        "type": "Vector3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": 1.0,
                        "length": 1.0
                    }
                },
                "axis_line": {
                    "origin": {
                        "type": "Point3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": -4.60502
                    },
                    "direction": {
                        "type": "Vector3D",
                        "x": 0.0,
                        "y": 0.0,
                        "z": 1.0,
                        "length": 1.0
                    }
                },
                "entity_one_equivalents": [{
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0008_2",
                    "surface_type": "CylinderSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.142849658282152,
                        "y": -0.9018871171209135,
                        "z": -2.30251
                    },
                    "index": 78,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.91313,
                            "y": 0.91313,
                            "z": 0.0
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.91313,
                            "y": -0.91313,
                            "z": -4.60502
                        }
                    },
                    "id": 79
                }, {
                    "type": "BRepFace",
                    "body": "22666_bdaa1303_0008_2",
                    "surface_type": "CylinderSurfaceType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -0.7216894358845934,
                        "y": -0.9477682974928935,
                        "z": -2.30251
                    },
                    "index": 88,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 1.1912600000000002,
                            "y": 0.0,
                            "z": 0.0
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -1.1912600000000002,
                            "y": -1.1912599664331394,
                            "z": -4.60502
                        }
                    },
                    "id": 89
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0008_2",
                    "curve_type": "Circle3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": 0.91313,
                        "y": 0.0,
                        "z": 0.0
                    },
                    "index": 143,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 0.91313,
                            "y": 0.91313,
                            "z": 0.0
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -0.91313,
                            "y": -0.91313,
                            "z": 0.0
                        }
                    },
                    "id": 237
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0008_2",
                    "curve_type": "Arc3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -7.294363729761381e-17,
                        "y": -1.1912600000000002,
                        "z": 0.0
                    },
                    "index": 168,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 1.1912600000000002,
                            "y": 0.0,
                            "z": 0.0
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -1.1912600000000002,
                            "y": -1.1912600000000002,
                            "z": 0.0
                        }
                    },
                    "id": 259
                }, {
                    "type": "BRepEdge",
                    "body": "22666_bdaa1303_0008_2",
                    "curve_type": "Arc3DCurveType",
                    "point_on_entity": {
                        "type": "Point3D",
                        "x": -7.294363729761381e-17,
                        "y": -1.1912600000000002,
                        "z": -4.60502
                    },
                    "index": 169,
                    "bounding_box": {
                        "type": "BoundingBox3D",
                        "max_point": {
                            "type": "Point3D",
                            "x": 1.1912600000000002,
                            "y": 0.0,
                            "z": -4.60502
                        },
                        "min_point": {
                            "type": "Point3D",
                            "x": -1.1912600000000002,
                            "y": -1.1912600000000002,
                            "z": -4.60502
                        }
                    },
                    "id": 260
                }]
            },
            "offset": {
                "type": "ModelParameter",
                "value": 0.0,
                "name": "offset",
                "role": "alignOffsetZ"
            },
            "angle": {
                "type": "ModelParameter",
                "value": 3.141592653589793,
                "name": "angle",
                "role": "alignAngle"
            },
            "is_flipped": true
        }],
        "contacts": [{
            "entity_one": {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.9410700000000001,
                    "y": 0.0,
                    "z": -0.9550400000000001
                },
                "index": 15,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.19126,
                        "y": 1.19126,
                        "z": -0.9550400000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.19126,
                        "y": -1.19126,
                        "z": -0.9550400000000001
                    }
                },
                "id": 16
            },
            "entity_two": {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 8.515275356171335e-18,
                    "y": 1.0521950000000002,
                    "z": -4.60502
                },
                "index": 90,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.905,
                        "y": 2.540000081062317,
                        "z": -4.60502
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.905,
                        "y": -1.1912600000000002,
                        "z": -4.60502
                    }
                },
                "id": 91
            },
            "joint_index": 0
        }, {
            "entity_one": {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -5.575755644177941e-17,
                    "y": 0.9105899999999999,
                    "z": -0.9944100000000001
                },
                "index": 5,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.9105899999999999,
                        "y": 0.9105899999999999,
                        "z": -0.9550400000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.9105899999999999,
                        "y": -0.9105899999999999,
                        "z": -1.0337800000000001
                    }
                },
                "id": 6
            },
            "entity_two": {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.142849658282152,
                    "y": -0.9018871171209135,
                    "z": -2.30251
                },
                "index": 78,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.91313,
                        "y": 0.91313,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.91313,
                        "y": -0.91313,
                        "z": -4.60502
                    }
                },
                "id": 79
            },
            "joint_index": 0
        }, {
            "entity_one": {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -5.575755644177941e-17,
                    "y": 0.9105899999999999,
                    "z": -1.3919200000000003
                },
                "index": 2,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.9105899999999999,
                        "y": 0.9105899999999999,
                        "z": -1.2725400000000002
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.9105899999999999,
                        "y": -0.9105899999999999,
                        "z": -1.5113000000000003
                    }
                },
                "id": 3
            },
            "entity_two": {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.142849658282152,
                    "y": -0.9018871171209135,
                    "z": -2.30251
                },
                "index": 78,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.91313,
                        "y": 0.91313,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.91313,
                        "y": -0.91313,
                        "z": -4.60502
                    }
                },
                "id": 79
            },
            "joint_index": 0
        }],
        "holes": [{
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0035_2",
            "diameter":
            0.9525,
            "length":
            1.5113000000000003,
            "origin": {
                "type": "Point3D",
                "x": 0.0,
                "y": 0.0,
                "z": 0.0
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 2.9161901904696347e-17,
                    "y": -0.47625,
                    "z": -0.7556500000000002
                },
                "index": 0,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.47625,
                        "y": 0.47625,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.47625,
                        "y": -0.47625,
                        "z": -1.5113000000000003
                    }
                },
                "id": 1
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.47625,
                    "y": 0.0,
                    "z": 0.0
                },
                "index": 1,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.47625,
                        "y": 0.47625,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.47625,
                        "y": -0.47625,
                        "z": 0.0
                    }
                },
                "id": 23
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.47625,
                    "y": 0.0,
                    "z": -1.5113000000000003
                },
                "index": 0,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.47625,
                        "y": 0.47625,
                        "z": -1.5113000000000003
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.47625,
                        "y": -0.47625,
                        "z": -1.5113000000000003
                    }
                },
                "id": 22
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0035_2",
            "diameter":
            0.16001999999999983,
            "length":
            0.16002000000000005,
            "origin": {
                "type": "Point3D",
                "x": -0.52578,
                "y": -0.9106776736035643,
                "z": -0.7950200000000001
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": -0.8306676736035643,
                    "z": -0.8750300000000001
                },
                "index": 13,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.44577,
                        "y": -0.8306676736035643,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.60579,
                        "y": -0.9906876736035644,
                        "z": -0.9550400000000001
                    }
                },
                "id": 14
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.60579,
                    "y": -0.9106776736035643,
                    "z": -0.7950200000000001
                },
                "index": 14,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.44577,
                        "y": -0.8306676736035643,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.60579,
                        "y": -0.9906876736035644,
                        "z": -0.7950200000000001
                    }
                },
                "id": 33
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.60579,
                    "y": -0.9106776736035643,
                    "z": -0.9550400000000001
                },
                "index": 21,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.44577,
                        "y": -0.8306676736035643,
                        "z": -0.9550400000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.60579,
                        "y": -0.9906876736035644,
                        "z": -0.9550400000000001
                    }
                },
                "id": 39
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0035_2",
            "diameter":
            0.16002000000000005,
            "length":
            0.16002000000000005,
            "origin": {
                "type": "Point3D",
                "x": 0.52578,
                "y": 0.9106776736035642,
                "z": -0.7950200000000001
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": 0.9906876736035641,
                    "z": -0.8750300000000001
                },
                "index": 12,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.60579,
                        "y": 0.9906876736035641,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.44577000000000006,
                        "y": 0.8306676736035643,
                        "z": -0.9550400000000001
                    }
                },
                "id": 13
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.44577000000000006,
                    "y": 0.9106776736035642,
                    "z": -0.7950200000000001
                },
                "index": 13,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.60579,
                        "y": 0.9906876736035641,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.44577000000000006,
                        "y": 0.8306676736035643,
                        "z": -0.7950200000000001
                    }
                },
                "id": 32
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.44577000000000006,
                    "y": 0.9106776736035642,
                    "z": -0.9550400000000001
                },
                "index": 20,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.60579,
                        "y": 0.9906876736035641,
                        "z": -0.9550400000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.44577000000000006,
                        "y": 0.8306676736035643,
                        "z": -0.9550400000000001
                    }
                },
                "id": 38
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0035_2",
            "diameter":
            0.16002000000000027,
            "length":
            0.16002000000000005,
            "origin": {
                "type": "Point3D",
                "x": -0.52578,
                "y": 0.9106776736035643,
                "z": -0.7950200000000001
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": 0.9906876736035644,
                    "z": -0.8750300000000001
                },
                "index": 11,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.44577,
                        "y": 0.9906876736035644,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.60579,
                        "y": 0.8306676736035643,
                        "z": -0.9550400000000001
                    }
                },
                "id": 12
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.60579,
                    "y": 0.9106776736035643,
                    "z": -0.7950200000000001
                },
                "index": 12,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.44577,
                        "y": 0.9906876736035644,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.60579,
                        "y": 0.8306676736035643,
                        "z": -0.7950200000000001
                    }
                },
                "id": 31
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.60579,
                    "y": 0.9106776736035643,
                    "z": -0.9550400000000001
                },
                "index": 19,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.44577,
                        "y": 0.9906876736035644,
                        "z": -0.9550400000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.60579,
                        "y": 0.8306676736035643,
                        "z": -0.9550400000000001
                    }
                },
                "id": 37
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0035_2",
            "diameter":
            0.16001999999999983,
            "length":
            0.16002000000000005,
            "origin": {
                "type": "Point3D",
                "x": -1.05156,
                "y": 0.0,
                "z": -0.7950200000000001
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.05156,
                    "y": 0.08000999999999991,
                    "z": -0.8750300000000001
                },
                "index": 10,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.9715500000000001,
                        "y": 0.08000999999999991,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.13157,
                        "y": -0.08000999999999991,
                        "z": -0.9550400000000001
                    }
                },
                "id": 11
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.13157,
                    "y": 0.0,
                    "z": -0.7950200000000001
                },
                "index": 11,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.9715500000000001,
                        "y": 0.08000999999999991,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.13157,
                        "y": -0.08000999999999991,
                        "z": -0.7950200000000001
                    }
                },
                "id": 30
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.13157,
                    "y": 0.0,
                    "z": -0.9550400000000001
                },
                "index": 18,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.9715500000000001,
                        "y": 0.08000999999999991,
                        "z": -0.9550400000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.13157,
                        "y": -0.08000999999999991,
                        "z": -0.9550400000000001
                    }
                },
                "id": 36
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0035_2",
            "diameter":
            0.16001999999999983,
            "length":
            0.16002000000000005,
            "origin": {
                "type": "Point3D",
                "x": 0.52578,
                "y": -0.9106776736035643,
                "z": -0.7950200000000001
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": -0.8306676736035643,
                    "z": -0.8750300000000001
                },
                "index": 9,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.60579,
                        "y": -0.8306676736035643,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.44577,
                        "y": -0.9906876736035644,
                        "z": -0.9550400000000001
                    }
                },
                "id": 10
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.44577,
                    "y": -0.9106776736035643,
                    "z": -0.7950200000000001
                },
                "index": 10,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.60579,
                        "y": -0.8306676736035643,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.44577,
                        "y": -0.9906876736035644,
                        "z": -0.7950200000000001
                    }
                },
                "id": 29
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.44577,
                    "y": -0.9106776736035643,
                    "z": -0.9550400000000001
                },
                "index": 17,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.60579,
                        "y": -0.8306676736035643,
                        "z": -0.9550400000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.44577,
                        "y": -0.9906876736035644,
                        "z": -0.9550400000000001
                    }
                },
                "id": 35
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0035_2",
            "diameter":
            0.16001999999999983,
            "length":
            0.16002000000000005,
            "origin": {
                "type": "Point3D",
                "x": 1.05156,
                "y": 0.0,
                "z": -0.7950200000000001
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0035_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.05156,
                    "y": 0.08001000000000003,
                    "z": -0.8750300000000001
                },
                "index": 8,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.13157,
                        "y": 0.08001000000000003,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.97155,
                        "y": -0.08001000000000003,
                        "z": -0.9550400000000001
                    }
                },
                "id": 9
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.97155,
                    "y": 0.0,
                    "z": -0.7950200000000001
                },
                "index": 9,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.13157,
                        "y": 0.08001000000000003,
                        "z": -0.7950200000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.97155,
                        "y": -0.08001000000000003,
                        "z": -0.7950200000000001
                    }
                },
                "id": 28
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0035_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.97155,
                    "y": 0.0,
                    "z": -0.9550400000000001
                },
                "index": 16,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.13157,
                        "y": 0.08001000000000003,
                        "z": -0.9550400000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.97155,
                        "y": -0.08001000000000003,
                        "z": -0.9550400000000001
                    }
                },
                "id": 34
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            1.82626,
            "length":
            4.60502,
            "origin": {
                "type": "Point3D",
                "x": 0.0,
                "y": 0.0,
                "z": 0.0
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.142849658282152,
                    "y": -0.9018871171209135,
                    "z": -2.30251
                },
                "index": 78,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.91313,
                        "y": 0.91313,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.91313,
                        "y": -0.91313,
                        "z": -4.60502
                    }
                },
                "id": 79
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.91313,
                    "y": 0.0,
                    "z": 0.0
                },
                "index": 143,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.91313,
                        "y": 0.91313,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.91313,
                        "y": -0.91313,
                        "z": 0.0
                    }
                },
                "id": 237
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.91313,
                    "y": 0.0,
                    "z": -4.60502
                },
                "index": 142,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.91313,
                        "y": 0.91313,
                        "z": -4.60502
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.91313,
                        "y": -0.91313,
                        "z": -4.60502
                    }
                },
                "id": 0
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.635,
                    "y": 0.6561870136630258,
                    "z": -3.571240000000001
                },
                "index": 81,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.635,
                        "y": 0.9131299999999999,
                        "z": -2.9362400000000006
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.635,
                        "y": 0.6561870136630258,
                        "z": -4.206240000000001
                    }
                },
                "id": 179
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.6350000000000001,
                    "y": 0.6561870136630257,
                    "z": -1.0312400000000002
                },
                "index": 79,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6350000000000001,
                        "y": 0.9131299999999999,
                        "z": -0.39624000000000015
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.6350000000000001,
                        "y": 0.6561870136630256,
                        "z": -1.6662400000000002
                    }
                },
                "id": 177
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.14284965828215196,
                    "y": -0.9018871171209135,
                    "z": -2.3025099999999994
                },
                "index": 4,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1416303040859808,
                        "y": -0.9018871171209135,
                        "z": -2.1602699999999997
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.142849658282152,
                        "y": -0.91313,
                        "z": -2.44475
                    }
                },
                "id": 123
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.25146000000000024,
            "length":
            0.31750008106231664,
            "origin": {
                "type": "Point3D",
                "x": -1.5875,
                "y": 0.31750008106231664,
                "z": -3.8887400000000008
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": -0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.5875,
                    "y": 0.15875004053115832,
                    "z": -4.014470000000001
                },
                "index": 71,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -1.4617699999999998,
                        "y": 0.3175000810623178,
                        "z": -3.7630100000000004
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.71323,
                        "y": 0.0,
                        "z": -4.014470000000001
                    }
                },
                "id": 72
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.71323,
                    "y": 0.31750008106231664,
                    "z": -3.8887400000000008
                },
                "index": 121,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -1.4617699999999998,
                        "y": 0.3175000810623178,
                        "z": -3.7630100000000004
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.71323,
                        "y": 0.3175000810623178,
                        "z": -4.014470000000001
                    }
                },
                "id": 219
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.71323,
                    "y": 0.0,
                    "z": -3.8887400000000008
                },
                "index": 120,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -1.4617699999999998,
                        "y": 0.0,
                        "z": -3.7630100000000004
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.71323,
                        "y": 0.0,
                        "z": -4.014470000000001
                    }
                },
                "id": 218
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.25146000000000024,
            "length":
            0.317500081062317,
            "origin": {
                "type": "Point3D",
                "x": 1.5875,
                "y": 0.317500081062317,
                "z": -3.8887400000000008
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": -0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.5875,
                    "y": 0.1587500405311585,
                    "z": -4.014470000000001
                },
                "index": 70,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.71323,
                        "y": 0.3175000810623168,
                        "z": -3.7630100000000004
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 1.4617699999999998,
                        "y": 0.0,
                        "z": -4.014470000000001
                    }
                },
                "id": 71
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.4617699999999998,
                    "y": 0.317500081062317,
                    "z": -3.8887400000000008
                },
                "index": 119,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.71323,
                        "y": 0.3175000810623168,
                        "z": -3.7630100000000004
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 1.4617699999999998,
                        "y": 0.3175000810623168,
                        "z": -4.014470000000001
                    }
                },
                "id": 217
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.4617699999999998,
                    "y": 0.0,
                    "z": -3.8887400000000008
                },
                "index": 118,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.71323,
                        "y": 0.0,
                        "z": -3.7630100000000004
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 1.4617699999999998,
                        "y": 0.0,
                        "z": -4.014470000000001
                    }
                },
                "id": 216
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.25146000000000024,
            "length":
            0.317500081062317,
            "origin": {
                "type": "Point3D",
                "x": 1.5875,
                "y": 0.317500081062317,
                "z": -0.7137399999999698
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": -0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.5875,
                    "y": 0.1587500405311585,
                    "z": -0.83946999999997
                },
                "index": 69,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.71323,
                        "y": 0.3175000810623168,
                        "z": -0.5880099999999697
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 1.4617699999999998,
                        "y": 0.0,
                        "z": -0.83946999999997
                    }
                },
                "id": 70
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.4617699999999998,
                    "y": 0.317500081062317,
                    "z": -0.7137399999999698
                },
                "index": 117,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.71323,
                        "y": 0.3175000810623168,
                        "z": -0.5880099999999697
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 1.4617699999999998,
                        "y": 0.3175000810623168,
                        "z": -0.83946999999997
                    }
                },
                "id": 215
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.4617699999999998,
                    "y": 0.0,
                    "z": -0.7137399999999698
                },
                "index": 116,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.71323,
                        "y": 0.0,
                        "z": -0.5880099999999697
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 1.4617699999999998,
                        "y": 0.0,
                        "z": -0.83946999999997
                    }
                },
                "id": 214
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.25146000000000024,
            "length":
            0.31750008106231664,
            "origin": {
                "type": "Point3D",
                "x": -1.5875,
                "y": 0.31750008106231664,
                "z": -0.71374
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": -0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.5875,
                    "y": 0.15875004053115832,
                    "z": -0.8394700000000002
                },
                "index": 58,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -1.4617699999999998,
                        "y": 0.3175000810623178,
                        "z": -0.5880099999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.71323,
                        "y": 0.0,
                        "z": -0.8394700000000002
                    }
                },
                "id": 59
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.71323,
                    "y": 0.31750008106231664,
                    "z": -0.71374
                },
                "index": 83,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -1.4617699999999998,
                        "y": 0.3175000810623178,
                        "z": -0.5880099999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.71323,
                        "y": 0.3175000810623178,
                        "z": -0.8394700000000002
                    }
                },
                "id": 181
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.71323,
                    "y": 0.0,
                    "z": -0.71374
                },
                "index": 82,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -1.4617699999999998,
                        "y": 0.0,
                        "z": -0.5880099999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.71323,
                        "y": 0.0,
                        "z": -0.8394700000000002
                    }
                },
                "id": 180
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            1.27,
            "length":
            1.883813067399291,
            "origin": {
                "type": "Point3D",
                "x": 0.0,
                "y": 2.540000081062317,
                "z": -3.5712400000000004
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": -1.0,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -3.8882535872928465e-17,
                    "y": 1.5980935473626714,
                    "z": -4.20624
                },
                "index": 57,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.635,
                        "y": 2.540000081062317,
                        "z": -2.93624
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.635,
                        "y": 0.6561870136630258,
                        "z": -4.20624
                    }
                },
                "id": 58
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Arc3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.6349987098844316,
                    "y": 2.0802600810623173,
                    "z": -3.5725200176199885
                },
                "index": 41,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.635,
                        "y": 2.080260081062717,
                        "z": -3.492499642438721
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.6297765979008524,
                        "y": 2.0802600810623173,
                        "z": -3.652519989766413
                    }
                },
                "id": 148
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.635,
                    "y": 2.540000081062317,
                    "z": -3.5712400000000004
                },
                "index": 80,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.635,
                        "y": 2.540000081062317,
                        "z": -2.9362400000000006
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.635,
                        "y": 2.540000081062317,
                        "z": -4.20624
                    }
                },
                "id": 178
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5873664230603662,
                    "y": 2.2402800756862264,
                    "z": -3.812539989766413
                },
                "index": 45,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6297765979008524,
                        "y": 2.4003000810623165,
                        "z": -3.652519989766413
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5873664230603662,
                        "y": 2.0802600810623173,
                        "z": -3.812539989766413
                    }
                },
                "id": 152
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5884034860536163,
                    "y": 2.2402802612335164,
                    "z": -3.332480000000101
                },
                "index": 51,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6300992083791249,
                        "y": 2.400300081062317,
                        "z": -3.33248
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5884034860535751,
                        "y": 2.080260081062717,
                        "z": -3.4924999999999997
                    }
                },
                "id": 158
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999988,
                    "y": 1.8643600810623169,
                    "z": -2.9679378654107054
                },
                "index": 58,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1981200000000001,
                        "y": 2.062480081062317,
                        "z": -2.93624
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.666240081062317,
                        "z": -2.9679378654107054
                    }
                },
                "id": 165
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Arc3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.6349987095103828,
                    "y": 2.400300081062317,
                    "z": -3.5725202031668695
                },
                "index": 48,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.635,
                        "y": 2.400300081062317,
                        "z": -3.4924999999999997
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.6297765965245732,
                        "y": 2.4003000810623165,
                        "z": -3.652520000430149
                    }
                },
                "id": 155
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.635,
                    "y": 0.6561870136630258,
                    "z": -3.571240000000001
                },
                "index": 81,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.635,
                        "y": 0.9131299999999999,
                        "z": -2.9362400000000006
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.635,
                        "y": 0.6561870136630258,
                        "z": -4.206240000000001
                    }
                },
                "id": 179
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            1.2700000000000002,
            "length":
            1.8838130673992908,
            "origin": {
                "type": "Point3D",
                "x": 0.0,
                "y": 2.540000081062317,
                "z": -1.0312400000000002
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": -0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -3.888253587292847e-17,
                    "y": 1.5980935473626712,
                    "z": -1.6662400000000002
                },
                "index": 56,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6350000000000001,
                        "y": 2.540000081062317,
                        "z": -0.3962399999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.6350000000000001,
                        "y": 0.6561870136630256,
                        "z": -1.6662400000000004
                    }
                },
                "id": 57
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.6350000000000001,
                    "y": 2.540000081062317,
                    "z": -1.0312400000000002
                },
                "index": 78,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6350000000000001,
                        "y": 2.540000081062317,
                        "z": -0.39624000000000015
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.6350000000000001,
                        "y": 2.540000081062317,
                        "z": -1.6662400000000002
                    }
                },
                "id": 176
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Arc3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.6349987093054127,
                    "y": 2.3709588887876576,
                    "z": -1.0325203048309266
                },
                "index": 29,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6350000000000001,
                        "y": 2.370958888787657,
                        "z": -0.9525002021896539
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.629776596580089,
                        "y": 2.370958888787657,
                        "z": -1.1125200000000004
                    }
                },
                "id": 136
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999988,
                    "y": 1.8643600810623169,
                    "z": -0.42793786541070483
                },
                "index": 54,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.19812000000000005,
                        "y": 2.062480081062317,
                        "z": -0.39624000000000004
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.666240081062317,
                        "z": -0.4279378654107049
                    }
                },
                "id": 161
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5884034860544582,
                    "y": 2.210938029935183,
                    "z": -0.7924800000021759
                },
                "index": 33,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6300992336456107,
                        "y": 2.370958888787657,
                        "z": -0.7924799999998711
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.588403486053523,
                        "y": 2.05091888878753,
                        "z": -0.9525002021896539
                    }
                },
                "id": 140
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.587366418856237,
                    "y": 2.2109388887876573,
                    "z": -1.2725399999999993
                },
                "index": 39,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6297765965800892,
                        "y": 2.370958888787657,
                        "z": -1.1125199999999986
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.587366418856237,
                        "y": 2.0509188887876575,
                        "z": -1.2725399999999993
                    }
                },
                "id": 146
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999985,
                    "y": 1.8643600810623167,
                    "z": -1.6345421345892954
                },
                "index": 57,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1981200000000001,
                        "y": 2.062480081062317,
                        "z": -1.6345421345892954
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.666240081062317,
                        "z": -1.6662400000000004
                    }
                },
                "id": 164
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Arc3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.634998709510806,
                    "y": 2.0509188887876575,
                    "z": -1.0325202029570697
                },
                "index": 36,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6350000000000001,
                        "y": 2.0509188887876575,
                        "z": -0.9525000000140083
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.6297765965800892,
                        "y": 2.05091888878753,
                        "z": -1.1125199999999986
                    }
                },
                "id": 143
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.6350000000000001,
                    "y": 0.6561870136630257,
                    "z": -1.0312400000000002
                },
                "index": 79,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.6350000000000001,
                        "y": 0.9131299999999999,
                        "z": -0.39624000000000015
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.6350000000000001,
                        "y": 0.6561870136630256,
                        "z": -1.6662400000000002
                    }
                },
                "id": 177
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.17830800000000013,
            "length":
            0.635,
            "origin": {
                "type": "Point3D",
                "x": -0.58928,
                "y": 2.540000081062317,
                "z": -2.9819600000000004
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58928,
                    "y": 1.9050000810623169,
                    "z": -2.9819600000000004
                },
                "index": 55,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -2.892806
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -3.0711140000000006
                    }
                },
                "id": 56
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58928,
                    "y": 2.222500081062317,
                    "z": -3.0711140000000006
                },
                "index": 54,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -2.892806
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -3.0711140000000006
                    }
                },
                "id": 55
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.678434,
                    "y": 1.9050000810623169,
                    "z": -2.9819600000000004
                },
                "index": 76,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -2.892806
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -3.0711140000000006
                    }
                },
                "id": 113
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.678434,
                    "y": 2.540000081062317,
                    "z": -2.9819600000000004
                },
                "index": 77,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -2.892806
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 2.540000081062317,
                        "z": -3.0711140000000006
                    }
                },
                "id": 175
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.1783079999999999,
            "length":
            0.635,
            "origin": {
                "type": "Point3D",
                "x": 0.58928,
                "y": 2.540000081062317,
                "z": -0.44196000000000013
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58928,
                    "y": 1.9050000810623169,
                    "z": -0.44196000000000013
                },
                "index": 53,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 1.9050000810623169,
                        "z": -0.3528060000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -0.5311140000000001
                    }
                },
                "id": 54
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58928,
                    "y": 2.222500081062317,
                    "z": -0.5311140000000001
                },
                "index": 52,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 2.540000081062317,
                        "z": -0.3528060000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -0.5311140000000001
                    }
                },
                "id": 53
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5001260000000001,
                    "y": 1.9050000810623169,
                    "z": -0.44196000000000013
                },
                "index": 74,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 1.9050000810623169,
                        "z": -0.3528060000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -0.5311140000000001
                    }
                },
                "id": 112
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5001260000000001,
                    "y": 2.540000081062317,
                    "z": -0.44196000000000013
                },
                "index": 75,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 2.540000081062317,
                        "z": -0.3528060000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -0.5311140000000001
                    }
                },
                "id": 174
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.1783079999999999,
            "length":
            0.635,
            "origin": {
                "type": "Point3D",
                "x": -0.58928,
                "y": 2.540000081062317,
                "z": -0.44196000000000013
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58928,
                    "y": 1.9050000810623169,
                    "z": -0.44196000000000013
                },
                "index": 51,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -0.3528060000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -0.5311140000000001
                    }
                },
                "id": 52
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58928,
                    "y": 2.222500081062317,
                    "z": -0.5311140000000001
                },
                "index": 50,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -0.3528060000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -0.5311140000000001
                    }
                },
                "id": 51
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.678434,
                    "y": 1.9050000810623169,
                    "z": -0.44196000000000013
                },
                "index": 72,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -0.3528060000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -0.5311140000000001
                    }
                },
                "id": 111
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.678434,
                    "y": 2.540000081062317,
                    "z": -0.44196000000000013
                },
                "index": 73,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -0.3528060000000001
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 2.540000081062317,
                        "z": -0.5311140000000001
                    }
                },
                "id": 173
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.17830800000000013,
            "length":
            0.635,
            "origin": {
                "type": "Point3D",
                "x": 0.58928,
                "y": 2.540000081062317,
                "z": -2.9819600000000004
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58928,
                    "y": 1.9050000810623169,
                    "z": -2.9819600000000004
                },
                "index": 49,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 1.9050000810623169,
                        "z": -2.892806
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -3.0711140000000006
                    }
                },
                "id": 50
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58928,
                    "y": 2.222500081062317,
                    "z": -3.0711140000000006
                },
                "index": 48,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 2.540000081062317,
                        "z": -2.892806
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -3.0711140000000006
                    }
                },
                "id": 49
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5001260000000001,
                    "y": 1.9050000810623169,
                    "z": -2.9819600000000004
                },
                "index": 70,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 1.9050000810623169,
                        "z": -2.892806
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -3.0711140000000006
                    }
                },
                "id": 110
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5001260000000001,
                    "y": 2.540000081062317,
                    "z": -2.9819600000000004
                },
                "index": 71,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 2.540000081062317,
                        "z": -2.892806
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -3.0711140000000006
                    }
                },
                "id": 172
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.1783079999999997,
            "length":
            0.635,
            "origin": {
                "type": "Point3D",
                "x": -0.58928,
                "y": 2.540000081062317,
                "z": -4.16052
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58928,
                    "y": 1.9050000810623169,
                    "z": -4.16052
                },
                "index": 47,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -4.071366
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -4.249674
                    }
                },
                "id": 48
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58928,
                    "y": 2.222500081062317,
                    "z": -4.249674
                },
                "index": 46,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -4.071366
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -4.249674
                    }
                },
                "id": 47
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.678434,
                    "y": 1.9050000810623169,
                    "z": -4.16052
                },
                "index": 68,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -4.071366
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -4.249674
                    }
                },
                "id": 109
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.678434,
                    "y": 2.540000081062317,
                    "z": -4.16052
                },
                "index": 69,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -4.071366
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 2.540000081062317,
                        "z": -4.249674
                    }
                },
                "id": 171
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.1783079999999999,
            "length":
            0.635,
            "origin": {
                "type": "Point3D",
                "x": 0.58928,
                "y": 2.540000081062317,
                "z": -1.6205200000000002
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58928,
                    "y": 1.9050000810623169,
                    "z": -1.6205200000000002
                },
                "index": 45,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 1.9050000810623169,
                        "z": -1.5313660000000002
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -1.7096740000000001
                    }
                },
                "id": 46
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58928,
                    "y": 2.222500081062317,
                    "z": -1.7096740000000001
                },
                "index": 44,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 2.540000081062317,
                        "z": -1.5313660000000002
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -1.7096740000000001
                    }
                },
                "id": 45
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5001260000000001,
                    "y": 1.9050000810623169,
                    "z": -1.6205200000000002
                },
                "index": 66,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 1.9050000810623169,
                        "z": -1.5313660000000002
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -1.7096740000000001
                    }
                },
                "id": 108
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5001260000000001,
                    "y": 2.540000081062317,
                    "z": -1.6205200000000002
                },
                "index": 67,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 2.540000081062317,
                        "z": -1.5313660000000002
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -1.7096740000000001
                    }
                },
                "id": 170
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.1783079999999999,
            "length":
            0.635,
            "origin": {
                "type": "Point3D",
                "x": -0.58928,
                "y": 2.540000081062317,
                "z": -1.6205200000000002
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58928,
                    "y": 1.9050000810623169,
                    "z": -1.6205200000000002
                },
                "index": 43,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -1.5313660000000002
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -1.7096740000000001
                    }
                },
                "id": 44
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58928,
                    "y": 2.222500081062317,
                    "z": -1.7096740000000001
                },
                "index": 42,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -1.5313660000000002
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -1.7096740000000001
                    }
                },
                "id": 43
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.678434,
                    "y": 1.9050000810623169,
                    "z": -1.6205200000000002
                },
                "index": 64,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -1.5313660000000002
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 1.9050000810623169,
                        "z": -1.7096740000000001
                    }
                },
                "id": 107
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.678434,
                    "y": 2.540000081062317,
                    "z": -1.6205200000000002
                },
                "index": 65,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -1.5313660000000002
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.678434,
                        "y": 2.540000081062317,
                        "z": -1.7096740000000001
                    }
                },
                "id": 169
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.1783079999999997,
            "length":
            0.635,
            "origin": {
                "type": "Point3D",
                "x": 0.58928,
                "y": 2.540000081062317,
                "z": -4.16052
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": -1.0,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58928,
                    "y": 1.9050000810623169,
                    "z": -4.16052
                },
                "index": 41,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 1.9050000810623169,
                        "z": -4.071366
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -4.249674
                    }
                },
                "id": 42
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58928,
                    "y": 2.222500081062317,
                    "z": -4.249674
                },
                "index": 40,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 2.540000081062317,
                        "z": -4.071366
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -4.249674
                    }
                },
                "id": 41
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5001260000000001,
                    "y": 1.9050000810623169,
                    "z": -4.16052
                },
                "index": 62,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 1.9050000810623169,
                        "z": -4.071366
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 1.9050000810623169,
                        "z": -4.249674
                    }
                },
                "id": 106
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.5001260000000001,
                    "y": 2.540000081062317,
                    "z": -4.16052
                },
                "index": 63,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.678434,
                        "y": 2.540000081062317,
                        "z": -4.071366
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.5001260000000001,
                        "y": 2.540000081062317,
                        "z": -4.249674
                    }
                },
                "id": 168
            }]
        }, {
            "type":
            "CounterboreThroughHole",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.5740399999999992,
            "length":
            0.8331200000000003,
            "origin": {
                "type": "Point3D",
                "x": -0.8331200000000001,
                "y": 1.8643600810623169,
                "z": -2.30124
            },
            "direction": {
                "type": "Vector3D",
                "x": 1.0,
                "y": -6.818965350800032e-17,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.65532,
                    "y": 1.8643600810623169,
                    "z": -2.58826
                },
                "index": 38,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.47751999999999994,
                        "y": 2.151380081062317,
                        "z": -2.01422
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.8331200000000001,
                        "y": 1.5773400810623168,
                        "z": -2.58826
                    }
                },
                "id": 39
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.47751999999999994,
                    "y": 1.6217900810623167,
                    "z": -2.30124
                },
                "index": 37,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.47751999999999994,
                        "y": 2.151380081062317,
                        "z": -2.01422
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.47751999999999994,
                        "y": 1.5773400810623168,
                        "z": -2.58826
                    }
                },
                "id": 38
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.2387599999999999,
                    "y": 1.8643600810623169,
                    "z": -2.49936
                },
                "index": 39,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.1102230246251565e-16,
                        "y": 2.0624800810623167,
                        "z": -2.10312
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.47751999999999994,
                        "y": 1.6662400810623168,
                        "z": -2.49936
                    }
                },
                "id": 40
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.47751999999999994,
                    "y": 1.6662400810623168,
                    "z": -2.30124
                },
                "index": 60,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.47751999999999994,
                        "y": 2.0624800810623167,
                        "z": -2.10312
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.47751999999999994,
                        "y": 1.6662400810623168,
                        "z": -2.49936
                    }
                },
                "id": 166
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Ellipse3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999988,
                    "y": 1.8643600810623169,
                    "z": -2.49936
                },
                "index": 56,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.1102230246251565e-16,
                        "y": 2.0624800810623167,
                        "z": -2.30124
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.6662400810623168,
                        "z": -2.49936
                    }
                },
                "id": 163
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.47751999999999994,
                    "y": 1.5773400810623168,
                    "z": -2.30124
                },
                "index": 59,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.47751999999999994,
                        "y": 2.151380081062317,
                        "z": -2.01422
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.47751999999999994,
                        "y": 1.5773400810623168,
                        "z": -2.58826
                    }
                },
                "id": 105
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Ellipse3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999988,
                    "y": 1.8643600810623169,
                    "z": -2.10312
                },
                "index": 55,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.1102230246251565e-16,
                        "y": 2.0624800810623167,
                        "z": -2.10312
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.6662400810623168,
                        "z": -2.30124
                    }
                },
                "id": 162
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.8331200000000001,
                    "y": 1.5773400810623168,
                    "z": -2.30124
                },
                "index": 61,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.8331200000000001,
                        "y": 2.151380081062317,
                        "z": -2.01422
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.8331200000000001,
                        "y": 1.5773400810623168,
                        "z": -2.58826
                    }
                },
                "id": 167
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.39624,
            "length":
            0.42793786541070494,
            "origin": {
                "type": "Point3D",
                "x": 1.1102230246251568e-16,
                "y": 1.8643600810623169,
                "z": 0.0
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.2315365365486936e-16,
                    "y": 1.6662400810623168,
                    "z": -0.21396893270535247
                },
                "index": 35,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1981200000000001,
                        "y": 2.0624800810623167,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.6662400810623168,
                        "z": -0.4279378654107049
                    }
                },
                "id": 36
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999988,
                    "y": 1.8643600810623169,
                    "z": -0.42793786541070483
                },
                "index": 54,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.19812000000000005,
                        "y": 2.062480081062317,
                        "z": -0.39624000000000004
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.666240081062317,
                        "z": -0.4279378654107049
                    }
                },
                "id": 161
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.1981200000000001,
                    "y": 1.8643600810623169,
                    "z": 0.0
                },
                "index": 53,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1981200000000001,
                        "y": 2.0624800810623167,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.6662400810623168,
                        "z": 0.0
                    }
                },
                "id": 160
            }]
        }, {
            "type":
            "RoundHoleWithThroughBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.3962399999999997,
            "length":
            1.3333957308214097,
            "origin": {
                "type": "Point3D",
                "x": 1.1102230246251568e-16,
                "y": 1.8643600810623169,
                "z": -1.6345421345892954
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.2990852073137187e-16,
                    "y": 2.0624800810623167,
                    "z": -2.30124
                },
                "index": 36,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1981200000000001,
                        "y": 2.0624800810623167,
                        "z": -1.6345421345892954
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.6662400810623168,
                        "z": -2.9679378654107054
                    }
                },
                "id": 37
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Ellipse3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999988,
                    "y": 1.8643600810623169,
                    "z": -2.49936
                },
                "index": 56,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.1102230246251565e-16,
                        "y": 2.0624800810623167,
                        "z": -2.30124
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.6662400810623168,
                        "z": -2.49936
                    }
                },
                "id": 163
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Ellipse3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999988,
                    "y": 1.8643600810623169,
                    "z": -2.10312
                },
                "index": 55,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.1102230246251565e-16,
                        "y": 2.0624800810623167,
                        "z": -2.10312
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.6662400810623168,
                        "z": -2.30124
                    }
                },
                "id": 162
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999988,
                    "y": 1.8643600810623169,
                    "z": -2.9679378654107054
                },
                "index": 58,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1981200000000001,
                        "y": 2.062480081062317,
                        "z": -2.93624
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.666240081062317,
                        "z": -2.9679378654107054
                    }
                },
                "id": 165
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.19811999999999985,
                    "y": 1.8643600810623167,
                    "z": -1.6345421345892954
                },
                "index": 57,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1981200000000001,
                        "y": 2.062480081062317,
                        "z": -1.6345421345892954
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.19811999999999988,
                        "y": 1.666240081062317,
                        "z": -1.6662400000000004
                    }
                },
                "id": 164
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12446000000000002,
            "length":
            0.3810000000000002,
            "origin": {
                "type": "Point3D",
                "x": -1.05156,
                "y": 2.636779683484747e-16,
                "z": -4.60502
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": -0.0,
                "z": 1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.05156,
                    "y": 2.636779683484747e-16,
                    "z": -4.224019999999999
                },
                "index": 10,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.98933,
                        "y": 0.062230000000000264,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.11379,
                        "y": -0.06222999999999974,
                        "z": -4.224019999999999
                    }
                },
                "id": 11
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.05156,
                    "y": -0.06222999999999974,
                    "z": -4.4145199999999996
                },
                "index": 9,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.98933,
                        "y": 0.062230000000000264,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.11379,
                        "y": -0.06222999999999974,
                        "z": -4.60502
                    }
                },
                "id": 10
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.11379,
                    "y": 2.636779683484747e-16,
                    "z": -4.60502
                },
                "index": 12,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.98933,
                        "y": 0.062230000000000264,
                        "z": -4.60502
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.11379,
                        "y": -0.06222999999999974,
                        "z": -4.60502
                    }
                },
                "id": 127
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.11379,
                    "y": 2.636779683484747e-16,
                    "z": -4.224019999999999
                },
                "index": 11,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.98933,
                        "y": 0.062230000000000264,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.11379,
                        "y": -0.06222999999999974,
                        "z": -4.224019999999999
                    }
                },
                "id": 96
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12446000000000002,
            "length":
            0.381,
            "origin": {
                "type": "Point3D",
                "x": -1.05156,
                "y": 2.636779683484747e-16,
                "z": 0.0
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.05156,
                    "y": 2.636779683484747e-16,
                    "z": -0.381
                },
                "index": 26,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.98933,
                        "y": 0.062230000000000264,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.11379,
                        "y": -0.06222999999999974,
                        "z": -0.381
                    }
                },
                "id": 27
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -1.05156,
                    "y": -0.06222999999999974,
                    "z": -0.1905
                },
                "index": 25,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.98933,
                        "y": 0.062230000000000264,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.11379,
                        "y": -0.06222999999999974,
                        "z": -0.381
                    }
                },
                "id": 26
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.98933,
                    "y": 2.636779683484747e-16,
                    "z": -0.381
                },
                "index": 27,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.98933,
                        "y": 0.062230000000000264,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.11379,
                        "y": -0.06222999999999974,
                        "z": -0.381
                    }
                },
                "id": 104
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.98933,
                    "y": 2.636779683484747e-16,
                    "z": 0.0
                },
                "index": 28,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.98933,
                        "y": 0.062230000000000264,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -1.11379,
                        "y": -0.06222999999999974,
                        "z": 0.0
                    }
                },
                "id": 135
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12446000000000024,
            "length":
            0.3810000000000002,
            "origin": {
                "type": "Point3D",
                "x": 0.52578,
                "y": 0.91186,
                "z": -4.60502
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": -0.0,
                "z": 1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": 0.91186,
                    "z": -4.224019999999999
                },
                "index": 6,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": 0.97409,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": 0.84963,
                        "z": -4.224019999999999
                    }
                },
                "id": 7
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": 0.84963,
                    "z": -4.4145199999999996
                },
                "index": 5,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": 0.97409,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": 0.84963,
                        "z": -4.60502
                    }
                },
                "id": 6
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.46355,
                    "y": 0.91186,
                    "z": -4.60502
                },
                "index": 8,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": 0.97409,
                        "z": -4.60502
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": 0.84963,
                        "z": -4.60502
                    }
                },
                "id": 125
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.46355,
                    "y": 0.91186,
                    "z": -4.224019999999999
                },
                "index": 7,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": 0.97409,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": 0.84963,
                        "z": -4.224019999999999
                    }
                },
                "id": 94
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12445999999999979,
            "length":
            0.381,
            "origin": {
                "type": "Point3D",
                "x": 0.52578,
                "y": 0.91186,
                "z": 0.0
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": 0.91186,
                    "z": -0.381
                },
                "index": 24,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": 0.97409,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": 0.84963,
                        "z": -0.381
                    }
                },
                "id": 25
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": 0.84963,
                    "z": -0.1905
                },
                "index": 23,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": 0.97409,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": 0.84963,
                        "z": -0.381
                    }
                },
                "id": 24
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58801,
                    "y": 0.91186,
                    "z": -0.381
                },
                "index": 25,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": 0.97409,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": 0.84963,
                        "z": -0.381
                    }
                },
                "id": 103
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58801,
                    "y": 0.91186,
                    "z": 0.0
                },
                "index": 26,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": 0.97409,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": 0.84963,
                        "z": 0.0
                    }
                },
                "id": 134
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12446000000000002,
            "length":
            0.3810000000000002,
            "origin": {
                "type": "Point3D",
                "x": 1.05156,
                "y": -8.326672684688674e-17,
                "z": -4.60502
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": -0.0,
                "z": 1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.05156,
                    "y": -8.326672684688674e-17,
                    "z": -4.224019999999999
                },
                "index": 14,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.11379,
                        "y": 0.06222999999999992,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.98933,
                        "y": -0.062230000000000084,
                        "z": -4.224019999999999
                    }
                },
                "id": 15
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.05156,
                    "y": -0.062230000000000084,
                    "z": -4.4145199999999996
                },
                "index": 13,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.11379,
                        "y": 0.06222999999999992,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.98933,
                        "y": -0.062230000000000084,
                        "z": -4.60502
                    }
                },
                "id": 14
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.98933,
                    "y": -8.326672684688674e-17,
                    "z": -4.224019999999999
                },
                "index": 15,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.11379,
                        "y": 0.06222999999999992,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.98933,
                        "y": -0.062230000000000084,
                        "z": -4.224019999999999
                    }
                },
                "id": 98
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.98933,
                    "y": -8.326672684688674e-17,
                    "z": -4.60502
                },
                "index": 16,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.11379,
                        "y": 0.06222999999999992,
                        "z": -4.60502
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.98933,
                        "y": -0.062230000000000084,
                        "z": -4.60502
                    }
                },
                "id": 129
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12446000000000002,
            "length":
            0.381,
            "origin": {
                "type": "Point3D",
                "x": 1.05156,
                "y": -8.326672684688674e-17,
                "z": 0.0
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.05156,
                    "y": -8.326672684688674e-17,
                    "z": -0.381
                },
                "index": 22,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.11379,
                        "y": 0.06222999999999992,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.98933,
                        "y": -0.062230000000000084,
                        "z": -0.381
                    }
                },
                "id": 23
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.05156,
                    "y": -0.062230000000000084,
                    "z": -0.1905
                },
                "index": 21,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.11379,
                        "y": 0.06222999999999992,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.98933,
                        "y": -0.062230000000000084,
                        "z": -0.381
                    }
                },
                "id": 22
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.11379,
                    "y": -8.326672684688674e-17,
                    "z": -0.381
                },
                "index": 23,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.11379,
                        "y": 0.06222999999999992,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.98933,
                        "y": -0.062230000000000084,
                        "z": -0.381
                    }
                },
                "id": 102
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 1.11379,
                    "y": -8.326672684688674e-17,
                    "z": 0.0
                },
                "index": 24,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 1.11379,
                        "y": 0.06222999999999992,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.98933,
                        "y": -0.062230000000000084,
                        "z": 0.0
                    }
                },
                "id": 133
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12445999999999979,
            "length":
            0.3810000000000002,
            "origin": {
                "type": "Point3D",
                "x": -0.52578,
                "y": -0.9118599999999998,
                "z": -4.60502
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": -0.0,
                "z": 1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": -0.9118599999999998,
                    "z": -4.224019999999999
                },
                "index": 4,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": -0.8496299999999998,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": -0.9740899999999998,
                        "z": -4.224019999999999
                    }
                },
                "id": 5
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": -0.9740899999999998,
                    "z": -4.4145199999999996
                },
                "index": 3,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": -0.8496299999999998,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": -0.9740899999999998,
                        "z": -4.60502
                    }
                },
                "id": 4
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58801,
                    "y": -0.9118599999999998,
                    "z": -4.60502
                },
                "index": 6,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": -0.8496299999999998,
                        "z": -4.60502
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": -0.9740899999999998,
                        "z": -4.60502
                    }
                },
                "id": 124
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58801,
                    "y": -0.9118599999999998,
                    "z": -4.224019999999999
                },
                "index": 5,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": -0.8496299999999998,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": -0.9740899999999998,
                        "z": -4.224019999999999
                    }
                },
                "id": 93
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12446000000000024,
            "length":
            0.381,
            "origin": {
                "type": "Point3D",
                "x": -0.52578,
                "y": -0.9118599999999998,
                "z": 0.0
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": -0.9118599999999998,
                    "z": -0.381
                },
                "index": 20,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": -0.8496299999999998,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": -0.9740899999999998,
                        "z": -0.381
                    }
                },
                "id": 21
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": -0.9740899999999998,
                    "z": -0.1905
                },
                "index": 19,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": -0.8496299999999998,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": -0.9740899999999998,
                        "z": -0.381
                    }
                },
                "id": 20
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.46355,
                    "y": -0.9118599999999998,
                    "z": -0.381
                },
                "index": 21,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": -0.8496299999999998,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": -0.9740899999999998,
                        "z": -0.381
                    }
                },
                "id": 101
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.46355,
                    "y": -0.9118599999999998,
                    "z": 0.0
                },
                "index": 22,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": -0.8496299999999998,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": -0.9740899999999998,
                        "z": 0.0
                    }
                },
                "id": 132
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12446000000000024,
            "length":
            0.3810000000000002,
            "origin": {
                "type": "Point3D",
                "x": -0.52578,
                "y": 0.91186,
                "z": -4.60502
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": -0.0,
                "z": 1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": 0.91186,
                    "z": -4.224019999999999
                },
                "index": 12,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": 0.97409,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": 0.84963,
                        "z": -4.224019999999999
                    }
                },
                "id": 13
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": 0.84963,
                    "z": -4.4145199999999996
                },
                "index": 11,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": 0.97409,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": 0.84963,
                        "z": -4.60502
                    }
                },
                "id": 12
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58801,
                    "y": 0.91186,
                    "z": -4.60502
                },
                "index": 14,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": 0.97409,
                        "z": -4.60502
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": 0.84963,
                        "z": -4.60502
                    }
                },
                "id": 128
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.58801,
                    "y": 0.91186,
                    "z": -4.224019999999999
                },
                "index": 13,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": 0.97409,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": 0.84963,
                        "z": -4.224019999999999
                    }
                },
                "id": 97
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12445999999999979,
            "length":
            0.381,
            "origin": {
                "type": "Point3D",
                "x": -0.52578,
                "y": 0.91186,
                "z": 0.0
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": 0.91186,
                    "z": -0.381
                },
                "index": 18,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": 0.97409,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": 0.84963,
                        "z": -0.381
                    }
                },
                "id": 19
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.52578,
                    "y": 0.84963,
                    "z": -0.1905
                },
                "index": 17,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": 0.97409,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": 0.84963,
                        "z": -0.381
                    }
                },
                "id": 18
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.46355,
                    "y": 0.91186,
                    "z": -0.381
                },
                "index": 19,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": 0.97409,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": 0.84963,
                        "z": -0.381
                    }
                },
                "id": 100
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.46355,
                    "y": 0.91186,
                    "z": 0.0
                },
                "index": 20,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.46355,
                        "y": 0.97409,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.58801,
                        "y": 0.84963,
                        "z": 0.0
                    }
                },
                "id": 131
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12445999999999979,
            "length":
            0.3810000000000002,
            "origin": {
                "type": "Point3D",
                "x": 0.52578,
                "y": -0.91186,
                "z": -4.60502
            },
            "direction": {
                "type": "Vector3D",
                "x": -0.0,
                "y": -0.0,
                "z": 1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": -0.91186,
                    "z": -4.224019999999999
                },
                "index": 8,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": -0.84963,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": -0.97409,
                        "z": -4.224019999999999
                    }
                },
                "id": 9
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": -0.97409,
                    "z": -4.4145199999999996
                },
                "index": 7,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": -0.84963,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": -0.97409,
                        "z": -4.60502
                    }
                },
                "id": 8
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.46355,
                    "y": -0.91186,
                    "z": -4.60502
                },
                "index": 10,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": -0.84963,
                        "z": -4.60502
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": -0.97409,
                        "z": -4.60502
                    }
                },
                "id": 126
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.46355,
                    "y": -0.91186,
                    "z": -4.224019999999999
                },
                "index": 9,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": -0.84963,
                        "z": -4.224019999999999
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": -0.97409,
                        "z": -4.224019999999999
                    }
                },
                "id": 95
            }]
        }, {
            "type":
            "RoundHoleWithBlindBottom",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.12446000000000024,
            "length":
            0.381,
            "origin": {
                "type": "Point3D",
                "x": 0.52578,
                "y": -0.91186,
                "z": 0.0
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.0,
                "y": 0.0,
                "z": -1.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": -0.91186,
                    "z": -0.381
                },
                "index": 16,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": -0.84963,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": -0.97409,
                        "z": -0.381
                    }
                },
                "id": 17
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.52578,
                    "y": -0.97409,
                    "z": -0.1905
                },
                "index": 15,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": -0.84963,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": -0.97409,
                        "z": -0.381
                    }
                },
                "id": 16
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58801,
                    "y": -0.91186,
                    "z": -0.381
                },
                "index": 17,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": -0.84963,
                        "z": -0.381
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": -0.97409,
                        "z": -0.381
                    }
                },
                "id": 99
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.58801,
                    "y": -0.91186,
                    "z": 0.0
                },
                "index": 18,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.58801,
                        "y": -0.84963,
                        "z": 0.0
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": 0.46355,
                        "y": -0.97409,
                        "z": 0.0
                    }
                },
                "id": 130
            }]
        }, {
            "type":
            "CounterboreThroughHole",
            "body":
            "22666_bdaa1303_0008_2",
            "diameter":
            0.6349999999999998,
            "length":
            0.2893389968478713,
            "origin": {
                "type": "Point3D",
                "x": -0.0006783492115878135,
                "y": -1.1912598725318104,
                "z": -2.30251
            },
            "direction": {
                "type": "Vector3D",
                "x": 0.00023739254715313043,
                "y": 0.9999999718223889,
                "z": 0.0
            },
            "faces": [{
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.000672922417959878,
                    "y": -1.1683998731759506,
                    "z": -2.6200099999999997
                },
                "index": 0,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.31683184515987717,
                        "y": -1.1454645016863698,
                        "z": -1.9850102463971937
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.31816808501482796,
                        "y": -1.1912599664331394,
                        "z": -2.6200097536028055
                    }
                },
                "id": 1
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "PlaneSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.22920249789848063,
                    "y": -1.1455944432449052,
                    "z": -2.30251
                },
                "index": 1,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.31683249542927666,
                        "y": -1.1454645016863698,
                        "z": -1.9850099999999997
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.31816748667794065,
                        "y": -1.1456152459538123,
                        "z": -2.62001
                    }
                },
                "id": 2
            }, {
                "type": "BRepFace",
                "body": "22666_bdaa1303_0008_2",
                "surface_type": "CylinderSurfaceType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.0006385789572336605,
                    "y": -1.0237303788284557,
                    "z": -2.44475
                },
                "index": 2,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.14163030408598082,
                        "y": -0.9018871171209135,
                        "z": -2.1602699999999997
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.14290749161634858,
                        "y": -1.1455736405359982,
                        "z": -2.44475
                    }
                },
                "id": 3
            }],
            "edges": [{
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.14284965828215196,
                    "y": -0.9018871171209135,
                    "z": -2.3025099999999994
                },
                "index": 4,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1416303040859808,
                        "y": -0.9018871171209135,
                        "z": -2.1602699999999997
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.142849658282152,
                        "y": -0.91313,
                        "z": -2.44475
                    }
                },
                "id": 123
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.31683184515987717,
                    "y": -1.14835446160695,
                    "z": -2.3025099999999994
                },
                "index": 1,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.31683184515987717,
                        "y": -1.14835446160695,
                        "z": -1.9850102463971937
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.0002827962457216395,
                        "y": -1.1912599664331394,
                        "z": -2.6200097536028055
                    }
                },
                "id": 121
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.31683249542927666,
                    "y": -1.1456152459538123,
                    "z": -2.30251
                },
                "index": 2,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.31683249542927666,
                        "y": -1.1454645016863698,
                        "z": -1.9850099999999997
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.31816748667794065,
                        "y": -1.1456152459538123,
                        "z": -2.62001
                    }
                },
                "id": 92
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "Circle3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": 0.14157250036768465,
                    "y": -1.1455736405359982,
                    "z": -2.30251
                },
                "index": 3,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": 0.1415725003676847,
                        "y": -1.1455061071041839,
                        "z": -2.1602699999999997
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.14290749161634858,
                        "y": -1.1455736405359982,
                        "z": -2.44475
                    }
                },
                "id": 122
            }, {
                "type": "BRepEdge",
                "body": "22666_bdaa1303_0008_2",
                "curve_type": "NurbsCurve3DCurveType",
                "point_on_entity": {
                    "type": "Point3D",
                    "x": -0.31816808501482796,
                    "y": -1.1479849551618686,
                    "z": -2.30251
                },
                "index": 0,
                "bounding_box": {
                    "type": "BoundingBox3D",
                    "max_point": {
                        "type": "Point3D",
                        "x": -0.0002827962457216393,
                        "y": -1.1479849551618686,
                        "z": -1.9850102463971937
                    },
                    "min_point": {
                        "type": "Point3D",
                        "x": -0.31816808501482796,
                        "y": -1.1912599664331394,
                        "z": -2.6200097536028055
                    }
                },
                "id": 120
            }]
        }]
    }'''
