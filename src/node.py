class Node:
    """
    Class defining a node of the network.
    
    Attributes:
    	node_no (int): Node identifier number. 
        customer_no (int): Customer identifier number.
        xcoord (float): x-coordinate.
        ycoord (float): y-coordinate
        service time (int): service time in minutes.
    """
    def __init__(
        self, 
        node_no: int, 
        customer_no: int, 
        xcoord: float, 
        ycoord: float,  
        service_time: int,
    ):
        self.node_no = node_no
        self.customer_no = customer_no
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.service_time = service_time
