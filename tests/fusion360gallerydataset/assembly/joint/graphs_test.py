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
'''Tests suite of the fusion360gallerydataset.assembly.joint.graphs'''
import numpy as np

from fusion360gallerydataset.assembly.joint import graphs


def test_position_enc_nnode_less_posdim():
    '''Test position enc when number of nodes of the graph is less the position encoding dimesntion.'''
    n_node = 5
    pos_enc_dim = 3
    pos_enc = graphs.positional_encoding(pos_enc_dim=pos_enc_dim,
                                         n_node=n_node,
                                         n_edge=5,
                                         senders=np.array([0, 1, 2, 3, 2]),
                                         receivers=np.array([1, 2, 0, 4, 3]))

    assert pos_enc.shape == (n_node, pos_enc_dim)


def test_add_positional_encoding():
    '''Test positional_encoding adds pos enc features.'''
    graph = {
        'face_features': np.zeros((2, 1)),
        'edge_features': np.zeros((1, 1)),
        'coedge_features': np.zeros((2, 1)),
        'senders': np.array([0, 1, 2, 2]),
        'receivers': np.array([3, 4, 3, 4])
    }
    pos_enc_dim = 10
    graphs.add_positional_encoding(pos_enc_dim, graph)

    assert 'pos_enc' in graph
    pos_enc = graph['pos_enc']
    assert pos_enc.shape == (5, pos_enc_dim)
