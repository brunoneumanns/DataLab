import copy
import itertools
import json

from math import factorial, pow
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


def read_nodes(
    file_path: str,
	number_of_nodes: int,
) -> List[Node]:
    """
    Read node data from a file. Return a list with the node objects.
    
    Attributes:
        file_path (str): Path to the file containing the node data.
        number_of_nodes (int): Number of customer nodes from the instance to consider.
    
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
            
            # Check if the desired number of nodes has been already loaded
            if node_no == number_of_nodes:
                break
    
    # Make a copy of the node depot with node index set as n+1
    # Assume no service time in the depot
    lst_nodes[0].service_time = 0
    node_depot = copy.deepcopy(lst_nodes[0])
    node_depot.node_no = len(lst_nodes)
    lst_nodes.append(node_depot)
    
    return lst_nodes


def get_vehicle_data(
    number_of_vehicles: int,
    absence_prob: float = 0.07,
    time_horizon: float = 240.0,
    cost_km: float = 0.00,
    geography: str = "MANHATTAN",
    vehicle_speed: float = 0.002,
    balance: int = 2,
    max_number_of_absences: int = 2,
) -> Dict:
    """
    Read the experiment setting from a JSON file.
    
    Attributes:
    	number_of_vehicles (int): Number of vehicles.
        absence_prob (float): Probability that the caregiver operating the vehicle is absence.
        time_horizon (float): Time in minutes that a vehicle can operate.
        cost_km (float): The cost for each driven kilometer.
        geography (str): Geography metric to consider.
        vehicle_speed (float): Metric depicting vehicle speed.
        balance (int): Parameter to balance assignments among caregivers.
        max_number_of_absences: Maximal number of absences to consider.
        
    Returns:
    	vehicle_data (Dict): A dictionary with the data related to the vehicle.
    """
    v = number_of_vehicles
    p = absence_prob
	
    # Compute accumulated probabilities for absences
    accumulated_prob = 0.0
    for k in range(0, v + 1):
        out = (
            factorial(v) / (factorial(k) * factorial(v-k))
        ) * pow(1-p, v-k) * pow(p, k)
        accumulated_prob += out
        print(f'Accumulated probability after {k} absences: {accumulated_prob}')
        
    # Compute probability for 'k' absences
    for k in range(0, v + 1):
        out = pow(1 - p, v - k) * pow(p, k)
        print(f'Probability of {k} absences: {round(out, 8)}')
    
    # Create dictionary
    vehicle_data = {
        'time_horizon': time_horizon,
        'cost_km': cost_km,
        'geography': geography,
        'vehicle_speed': vehicle_speed,
        'balance': balance,
        'number_of_vehicles': v,
    }
	
    # List with the index for the vehicles
    index_vehicles = [x for x in range(0, v)]
   
	# Scenario counter
    s = 0
    
    # List with scenario data
    scenarios = []

    for k in range(max_number_of_absences+1):
        print(f"Scenarios with {k} absences.")
        # Probability of a scenario if there are k absenses
        probability = pow(1-p, v-k) * pow(p, k)
        
        # Create possible combinations given the available vehicles
        for av in set(itertools.combinations(index_vehicles, v-k)):
            available_vehicles = list(av)
            print(available_vehicles)
            
            # Create dictionary with scenario-dependent data
            scenario = {
                'scenario': s, 
                'probability': probability, 
                'available_vehicles': available_vehicles
            }
            
            # Add scenario to the list
            scenarios.append(scenario)
            
            # Update scenario counter
            s += 1

    vehicle_data['scenarios'] = scenarios
        
    return vehicle_data

