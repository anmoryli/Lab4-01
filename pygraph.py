from typing import Tuple, Union, Iterable, Set, Dict

Node = Union[str, int]
Edge = Tuple[Node, Node]


class Graph(object):
    """Graph data structure, undirected by default."""

    def __init__(self, edges: Iterable[Edge] = [], directed: bool = False):
        self.directed = directed
        self.adj: Dict[Node, Set[Node]] = {}
        for edge in edges:
            self.add_edge(edge)

    def has_node(self, node: Node) -> bool:
        """Whether a node is in graph"""
        return node in self.adj

    def has_edge(self, edge: Edge) -> bool:
        """Whether an edge is in graph"""
        u, v = edge
        if not self.has_node(u) or not self.has_node(v):
            return False
        return v in self.adj[u]

    def add_node(self, node: Node) -> None:
        """Add a node"""
        if node not in self.adj:
            self.adj[node] = set()

    def add_edge(self, edge: Edge) -> None:
        """Add an edge (node1, node2). For directed graph, node1 -> node2"""
        u, v = edge
        self.add_node(u)
        self.add_node(v)
        self.adj[u].add(v)
        if not self.directed:
            self.adj[v].add(u)

    def remove_node(self, node: Node) -> None:
        """Remove all references to node"""
        if node in self.adj:
            # Remove all incoming edges
            for neighbor in self.adj[node].copy():
                self.remove_edge((neighbor, node))
            # Remove the node itself
            del self.adj[node]

    def remove_edge(self, edge: Edge) -> None:
        """Remove an edge from graph"""
        u, v = edge
        if u in self.adj and v in self.adj[u]:
            self.adj[u].remove(v)
            if not self.directed and u in self.adj[v]:
                self.adj[v].remove(u)

    def indegree(self, node: Node) -> int:
        """Compute indegree for a node"""
        if not self.directed:
            return len(self.adj.get(node, set()))
        count = 0
        for neighbor in self.adj:
            if node in self.adj[neighbor]:
                count += 1
        return count

    def outdegree(self, node: Node) -> int:
        """Compute outdegree for a node"""
        if not self.directed:
            return len(self.adj.get(node, set()))
        return len(self.adj.get(node, set()))

    def __str__(self) -> str:
        """String representation of the graph"""
        return f"Graph(directed={self.directed}, nodes={list(self.adj.keys())}, edges={self._get_edges()})"

    def __repr__(self) -> str:
        """Official string representation"""
        return f"Graph(edges={self._get_edges()}, directed={self.directed})"

    def _get_edges(self) -> Set[Edge]:
        """Helper method to get all edges as a set of tuples"""
        edges = set()
        for u in self.adj:
            for v in self.adj[u]:
                if self.directed or (u, v) not in edges:
                    edges.add((u, v))
        return edges
