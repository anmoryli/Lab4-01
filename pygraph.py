from typing import Tuple, Union, Iterable

Node = Union[str, int]
Edge = Tuple[Node, Node]


class Graph(object):
    """Graph data structure, undirected by default."""

    def __init__(self, edges: Iterable[Edge] = [], directed: bool = False):
        """Initialize graph with optional edges and directionality."""
        self.nodes = set()
        self.edges = set()
        self.directed = directed
        for edge in edges:
            self.add_edge(edge)

    def has_node(self, node: Node) -> bool:
        """Whether a node is in graph."""
        return node in self.nodes

    def has_edge(self, edge: Edge) -> bool:
        """Whether an edge is in graph."""
        node1, node2 = edge
        if not (self.has_node(node1) and self.has_node(node2)):
            return False
        if self.directed:
            return edge in self.edges
        return edge in self.edges or (node2, node1) in self.edges

    def add_node(self, node: Node):
        """Add a node."""
        self.nodes.add(node)

    def add_edge(self, edge: Edge):
        """Add an edge (node1, node2). For directed graph, node1 -> node2."""
        node1, node2 = edge
        self.add_node(node1)
        self.add_node(node2)
        self.edges.add(edge)
        if not self.directed:
            self.edges.add((node2, node1))

    def remove_node(self, node: Node):
        """Remove all references to node."""
        if node in self.nodes:
            self.nodes.remove(node)
            # Remove all edges involving the node
            edges_to_remove = {
                (n1, n2) for n1, n2 in self.edges if n1 == node or n2 == node
            }
            self.edges.difference_update(edges_to_remove)

    def remove_edge(self, edge: Edge):
        """Remove an edge from graph."""
        if edge in self.edges:
            self.edges.remove(edge)
            if not self.directed:
                reverse_edge = (edge[1], edge[0])
                if reverse_edge in self.edges:
                    self.edges.remove(reverse_edge)

    def indegree(self, node: Node) -> int:
        """Compute indegree for a node (number of incoming edges)."""
        if not self.has_node(node):
            return 0
        return sum(1 for _, n2 in self.edges if n2 == node)

    def outdegree(self, node: Node) -> int:
        """Compute outdegree for a node (number of outgoing edges)."""
        if not self.has_node(node):
            return 0
        return sum(1 for n1, _ in self.edges if n1 == node)

    def __str__(self) -> str:
        """String representation of the graph."""
        return (
            f"Graph(nodes={self.nodes}, edges={self.edges}, directed={self.directed})"
        )

    def __repr__(self) -> str:
        """Detailed string representation of the graph."""
        return self.__str__()
