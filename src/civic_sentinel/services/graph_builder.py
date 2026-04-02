"""Knowledge graph builder using NetworkX."""
import logging
import networkx as nx
from typing import List, Dict, Any

logger = logging.getLogger("civic_sentinel.graph")

class GraphBuilder:
    def __init__(self):
        self.G = nx.Graph()

    def build(self, entities: List[Dict[str, Any]]) -> nx.Graph:
        """Build a graph from list of entities (with at least 'text' and 'label')."""
        self.G.clear()
        # Add entity nodes
        for ent in entities:
            name = ent.get("text", "Unknown")
            label = ent.get("label", "ENTITY")
            self.G.add_node(name, label=label)
        # Connect co-occurring entities (simple heuristic)
        # In a real app, you'd have relations from NLP (subject-predicate-object)
        return self.G

    def to_cytoscape(self) -> Dict[str, List]:
        """Export graph as Cytoscape JSON (useful for frontend)."""
        elements = {"nodes": [], "edges": []}
        for n, data in self.G.nodes(data=True):
            elements["nodes"].append({"data": {"id": n, "label": n, "type": data.get("label")}})
        for u, v in self.G.edges():
            elements["edges"].append({"data": {"source": u, "target": v}})
        return elements
