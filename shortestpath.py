'''
Created on Dec 8, 2017

@author: mahathir.ahamed
'''
from compiler.ast import Node
from pipes import SOURCE


class ShortestPath():
    """
    This class will give the shortest path among the given nodes
    """
    def __init__(self,cities,source,destination):
        self.path = []
        self.cost = 0
        self.traverse = {'path':[],'cost':0}
        self.cities = cities
        self.source = source
        self.destination = destination
    def get_shortest_path(self):
        """
        Get the Shortest Path
        """
        
        source = self.source
        while source:
             source = self.get_neibhours(self.cities[source])
        return self.traverse
    def get_neibhours(self,node):
        """
        Here we will get the neibhour and their cost
        """
        #import pdb;pdb.set_trace()
        self.traverse['path'].append(node.node)
        neb_weight={}
        for neibhour in node.get_neighbours():
            neb_weight[neibhour.weight] = neibhour.node
        min_neg= min(neb_weight.items())
        self.traverse['cost']+=neibhour.weight
        if node.node ==  self.destination:
           return False
        return min_neg[1]


class Graph():
    """
    Creates the Heap graph with the weight
    """
    def __init__(self,node,weight,root=False):
        self.root = root
        self.node = node
        self.weight = weight
        self._neighbours = []
    def compute_weight(self):
        """
        Compute the Weight of Traveling distance
        """
        pass
    def cost_of_destination(self,):
        """
        Compute the Cost of the Destination
        """
        pass 
    def set_neighbours(self,neighbour):
        """
        Set the neighbour for the given sets
        """
        self._neighbours.append(neighbour)
        return True
    def get_neighbours(self,):
        """
        Get the neighbours from the list
        """
        return self._neighbours

if __name__ == "__main__":
    import pdb;pdb.set_trace()
    globvar = 0
    def set_globvar_to_one():
       #global globvar    # Needed to modify global copy of globvar
       globvar = 1
    def print_globvar():
       print globvar     # No need for global declaration to read value of globvar
    set_globvar_to_one()
    print_globvar()  
    root = True 
    cities_map= {}    
    cities = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]
    for citi in cities:
        #import pdb;pdb.set_trace()
        if not cities_map.get(citi[0]):
            root_node= Graph(citi[0],0,root)
            root = False
            root_node.set_neighbours(Graph(citi[1],citi[2],root))
            cities_map[citi[0]] = root_node
        else:
            citi_obj = cities_map[citi[0]]
            citi_obj.set_neighbours(Graph(citi[1],citi[2]))
    path= ShortestPath(cities_map,"A","C")
    print path.get_shortest_path()
