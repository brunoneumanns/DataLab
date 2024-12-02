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
        
        # Auxiliar indexes to control the design and manupulation of the model
        self.lst_indx_nodes = []
        self.lst_indx_customers = []
        self.lst_indx_vehicles = []
        self.lst_indx_vehicles_with_dummy = []
        self.lst_indx_scenarios = []
        self.indx_depot_start = None
        self.indx_depot_end = None
        self.indx_vehicle_dummy = None

