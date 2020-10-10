"""
Given a graph G = (V, E) find a Minimum Spanning Tree in the graph (it may not be unique).
Minimum Spanning Tree: Subset of edges which connect all vertices in the graph with the minimal total edge cost.
    - Also no cycles
- Three steps:
    1. Sort edges by ascending edge weight
    2. Walk through sorted edges and look at the two nodes the edge belongs to.
        If the nodes are already unified, don't include this edge, otherwise unify.
    3. Terminate when all the edges has been processed, or all the vertices have been unified.
"""

    #TODO
