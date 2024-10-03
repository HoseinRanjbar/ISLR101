import numpy as np
from . import tools

# Edge format: (origin, neighbor)
num_node = 67
self_link = [(i, i) for i in range(num_node)]
inward = [
    # Body connections (OpenPose 25)
    (1, 0), (2, 1), (3, 2), (4, 3), (5, 1), (6, 5), (7, 6), (8, 1), (9, 8),
    (10, 9), (11, 10), (12, 8), (13, 12), (14, 13), (15, 0), (16, 0),
    (17, 15), (18, 16), (19, 14), (20, 19), (21, 14), (22, 11), (23, 22), (24, 11),
    
    # Left hand connections
    (26, 25), (27, 26), (28, 27), (30, 29), (31, 30), (32, 31), (34, 33),
    (35, 34), (36, 35), (38, 37), (39, 38), (40, 39), (42, 41), (43, 42), (44, 43),
    
    # Right hand connections
    (47, 46), (48, 47), (49, 48), (51, 50), (52, 51), (53, 52), (55, 54),
    (56, 55), (57, 56), (59, 58), (60, 59), (61, 60), (63, 62), (64, 63), (65, 64)
]

outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward


class Graph():
    """ The Graph to model the skeletons extracted by the openpose
    Arguments:
        labeling_mode: must be one of the follow candidates
            uniform: Uniform Labeling
            dastance*: Distance Partitioning*
            dastance: Distance Partitioning
            spatial: Spatial Configuration
            DAD: normalized graph adjacency matrix
            DLD: normalized graph laplacian matrix
    For more information, please refer to the section 'Partition Strategies' in our paper.
    """

    def __init__(self, labeling_mode='uniform'):
        self.A = self.get_adjacency_matrix(labeling_mode)
        self.num_node = num_node
        self.self_link = self_link
        self.inward = inward
        self.outward = outward
        self.neighbor = neighbor

    def get_adjacency_matrix(self, labeling_mode=None):
        if labeling_mode is None:
            return self.A
        if labeling_mode == 'uniform':
            A = tools.get_uniform_graph(num_node, self_link, neighbor)
        elif labeling_mode == 'distance*':
            A = tools.get_uniform_distance_graph(num_node, self_link, neighbor)
        elif labeling_mode == 'distance':
            A = tools.get_distance_graph(num_node, self_link, neighbor)
        elif labeling_mode == 'spatial':
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)
        elif labeling_mode == 'DAD':
            A = tools.get_DAD_graph(num_node, self_link, neighbor)
        elif labeling_mode == 'DLD':
            A = tools.get_DLD_graph(num_node, self_link, neighbor)
        # elif labeling_mode == 'customer_mode':
        #     pass
        else:
            raise ValueError()
        return A


def main():
    mode = ['uniform', 'distance*', 'distance', 'spatial', 'DAD', 'DLD']
    np.set_printoptions(threshold=np.nan)
    for m in mode:
        print('=' * 10 + m + '=' * 10)
        print(Graph(m).get_adjacency_matrix())


if __name__ == '__main__':
    main()