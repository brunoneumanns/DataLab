import copy
import json
from typing import Dict, List

from src.node import Node


def read_experiment_setting(file_path: str) -> Dict:
    """
    Read the experiment setting from a JSON file.
    
    Attributes:
    	file_path (str): Path to the file containing the JSON file.
        
    Returns:
    	dict_setting (Dict): A experimental setting as a dictionary.
    """
    with open(file_path, 'r') as f:
        dict_setting = json.load(f)
    return dict_setting


def get_distance(
    x1: float, 
    y1: float, 
    x2: float, 
    y2: float, 
    geography: str
) -> float:
  """
  Calculate the distance between two coordinates.

  Attributes:
    x1 (float): The x-coordinate of the first point.
    y1 (float): The y-coordinate of the first point.
    x2 (float): The x-coordinate of the second point.
    y2 (float): The y-coordinate of the second point.  
    geography (str): The type of distance calculation ('MANHATTAN' or 'EUCLIDEAN').

  Returns:
    float: The distance between the two points.

  Raises:
    ValueError: If geography is not 'MANHATTAN' or 'EUCLIDEAN'.
  """
  if geography == 'MANHATTAN':
    return abs(x1 - x2) + abs(y1 - y2)
  if geography == 'EUCLIDEAN':
    return math.hypot(x1 - x2, y1 - y2)
  raise ValueError("Invalid geography value. Must be 'MANHATTAN' or 'EUCLIDEAN'")


def read_nodes(file_path: str) -> List[Node]:
    """
    Read node data from a file. Return a list with the node objects.
    
    Attributes:
        file_path (str): Path to the file containing the node data.
    
    Returns:
        List[Node]: A list with Node objects.
    """
    SERVICE_TIME = 30
    COORD_SCALE_FACTOR = 100
    
    lst_nodes = []
    print(f"File path: {file_path}")
    with open(file_path) as fp:
        # Skip the header line
        next(fp)  
        
        for node_no, line in enumerate(fp):
            customer_no, xcoord, ycoord, *_ = map(float, line.split())
            
            # Apply a scale factor to the original coordinates
            xcoord *= COORD_SCALE_FACTOR
            ycoord *= COORD_SCALE_FACTOR
            
            # Create node object
            node = Node(
                node_no=node_no, 
                customer_no=int(customer_no), 
                xcoord=xcoord, 
                ycoord=ycoord, 
                service_time=SERVICE_TIME,
            )
            
            # Add node object to the list
            lst_nodes.append(node)
    
    # Make a copy of the node depot with node index set as n+1
    # Assume no service time in the depot
    lst_nodes[0].service_time = 0
    node_depot = copy.deepcopy(lst_nodes[0])
    node_depot.node_no = len(lst_nodes)
    lst_nodes.append(node_depot)
    
    return lst_nodes
