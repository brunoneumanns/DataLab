from typing import Dict, List

from src.node import Node

class ArcFormulation:
    
    def __init__(
        self,
        lst_nodes: List[Node],
        vehicle_data: Dict,
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
        
        # Get values from vehicle_data
        self.number_of_vehicles = vehicle_data["number_of_vehicles"]
        self.number_of_scenarios = vehicle_data["number_of_scenarios"]
        
        # Auxiliar indexes to control the design and manupulation of the model
        self.lst_indx_nodes = None
        self.lst_indx_customers = None
        self.lst_indx_vehicles = None
        self.lst_indx_vehicles_with_dummy = None
        self.lst_indx_scenarios = None
        self.indx_depot_start = None
        self.indx_depot_end = None
        self.indx_vehicle_dummy = None
        
        self.set_indx_lists()
        
    def set_indx_lists(self):
        """
        Set lists that are used to iterate when building the model.

        Attributes:
            This method has no attributes.

        Returns:
            This method does not return values.
        """
        self.lst_indx_nodes = [node.node_no for node in self.lst_nodes]
        self.lst_indx_customers = [node.node_no for node in self.lst_customers]
        self.lst_indx_vehicles = [k for k in range(self.number_of_vehicles)]
        self.lst_indx_vehicles_with_dummy = [k for k in range(self.number_of_vehicles+1)]
        self.lst_indx_scenarios = [s for s in range(self.number_of_scenarios)]
        
        self.indx_depot_start = self.depot_start.node_no
        self.indx_depot_end = self.depot_end.node_no
        self.indx_vehicle_dummy = self.number_of_vehicles
