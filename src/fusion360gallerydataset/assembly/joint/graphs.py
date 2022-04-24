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
'''Represents example of the dataset as graphs.'''

from typing import Mapping, MutableMapping
import numpy as np
from scipy import sparse


def create_joint_set_graph(
        body_one_graph: Mapping[str, np.ndarray],
        body_two_graph: Mapping[str, np.ndarray]) -> Mapping[str, np.ndarray]:
    '''Create joint set graph (fully connected graph of the vertices of the body_one_graph and body_two_graph)
    Here we use only face/edge entity vertices and assume that vertices enumerated as first faces then edges.
    The structure of the format has to be similar to:
    https://github.com/d61h6k4/brep2graph2/blob/main/src/brep2graph/configurations.py#L88

    Here we are not going to copy the nodes, because we are not going to use them directly,
    but derivatives (learned ones) of them, so we create here only the strucutre (edges).
    '''
    _check_graph(body_one_graph)
    _check_graph(body_two_graph)

    body_one_nodes = (body_one_graph['face_features'].shape[0] +
                      body_one_graph['edge_features'].shape[0])
    body_two_nodes = (body_two_graph['face_features'].shape[0] +
                      body_two_graph['edge_features'].shape[0])

    xx, yy = np.mgrid[0:body_one_nodes, 0:body_two_nodes]
    one_to_two_senders = np.ravel(xx)
    one_to_two_receivers = np.ravel(yy)
    two_to_one_senders = np.ravel(yy)
    two_to_one_receivers = np.ravel(xx)

    senders = np.concatenate((one_to_two_senders, two_to_one_senders))
    receivers = np.concatenate((one_to_two_receivers, two_to_one_receivers))

    return {
        'n_node': np.array([body_one_nodes + body_two_nodes]),
        'senders': senders,
        'receivers': receivers,
    }


def add_positional_encoding(pos_enc_dim: int,
                            graph: MutableMapping[str, np.ndarray]):
    '''Add positional encoding features to the `nodes`.'''
    _check_graph(graph)

    n_node = (graph['face_features'].shape[0] +
              graph['edge_features'].shape[0] +
              graph['coedge_features'].shape[0])
    n_edge = graph['senders'].shape[0]
    senders = graph['senders']
    receivers = graph['receivers']

    pos_enc = positional_encoding(pos_enc_dim=pos_enc_dim,
                                  n_node=n_node,
                                  n_edge=n_edge,
                                  senders=senders,
                                  receivers=receivers)
    # When number of nodes in graph less than pos_enc_dim
    # we pad with zeros
    if pos_enc.shape[1] < pos_enc_dim:
        pos_enc = np.pad(
            pos_enc, np.array([(0, 0), (0, pos_enc_dim - pos_enc.shape[1])]))

    graph['pos_enc'] = pos_enc


def positional_encoding(
    pos_enc_dim: int,
    n_node: int,
    n_edge: int,
    senders: np.ndarray,
    receivers: np.ndarray,
) -> np.ndarray:
    """Graph positional encoding v/ Laplacian eigenvectors."""
    a = sparse.coo_matrix((np.ones((n_edge, )), (senders, receivers)),
                          shape=(n_node, n_node))
    l = sparse.csgraph.laplacian(a)

    # Eigenvectors with numpy
    eig_val, eig_vec = np.linalg.eig(l.toarray())
    idx = eig_val.argsort()  # increasing order
    eig_val, eig_vec = eig_val[idx], np.real(eig_vec[:, idx])
    return eig_vec[:, 1:pos_enc_dim + 1]


def _check_graph(graph):
    keys = [
        'face_features', 'edge_features', 'coedge_features', 'senders',
        'receivers'
    ]
    for k in keys:
        if k not in graph:
            msg = f'Expected graph as a mapping has keys {keys}'
            raise ValueError(msg)
