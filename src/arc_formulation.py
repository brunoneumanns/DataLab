from typing import List

from src.node import Node

class ArcFormulation:
    
    def __init__(
        self,
        lst_nodes: List[Node],
    ):
        print("Starting constructor arc formulation")
        # List with nodes, including customers and two replications of the depot
        self.lst_nodes = lst_nodes 
        
        # List with customers
        self.lst_customers = self.lst_nodes[1:-1]
        
        # Depot replication in which vehicles start tours
        self.depot_start = self.lst_nodes[0]  
        
        # Depot replication in which vehicles end tours
        self.depot_end = self.lst_nodes[-1]  
