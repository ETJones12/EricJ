import networkx as nx  #import routing algorithm from the package 
import time


G = nx.Graph() # creates graph with nodes and weighted edges
G.add_edges_from([(1, 2, {'weight': 6}), (2, 3, {'weight': 9}), (1, 7, {'weight': 12}), (4, 5, {'weight': 13}), (3, 4, {'weight': 7}), (3, 7, {'weight': 2}),(2, 4, {'weight': 16}),(5, 6, {'weight': 11}),(3, 6, {'weight': 12}),(3, 2, {'weight': 19})])
start = 2 #starting node
destination = 5 #Destination node 

# Dijkstra routing algorithm
start_time = time.time() #starts timer
dijkstra_routing_algorithm = nx.dijkstra_path(G, start, destination) # go through each node to finds shortest pathway
end_time = time.time() - start_time # calulates time 
print("Dijkstra Time", end_time) 


def dijkstra_hop_count(G, start, destination):
        dhops = nx.dijkstra_path(G, start, destination)
        return len(dhops) - 1  # calculate Dijkstra hop count visted
 

hop_count = dijkstra_hop_count(G, start, destination)
print(" dikjkstra Hop Count:", hop_count)   # prints hop count

def bellman_ford_hop_count(G, start, destination):
        bhops = nx.bellman_ford_path(G, start, destination)
        return len(bhops) - 1  # Calculate Bellman-Ford hop count
  

bhop_count = bellman_ford_hop_count(G, start, destination)
print("bellman-Ford Hop Count:", bhop_count) # Prints Bellman-Ford hop count 

# Bellman-Ford Routing algorithm
bstart_time = time.time() # starts timer
bellman_ford_routing_algorithm = nx.bellman_ford_path(G, start, destination) # go through each node to finds shortest pathway 
bellman_ford_end_time = time.time() - bstart_time # calulate time 
print("Bellman-Ford Time", bellman_ford_end_time) # prints Bellman-Ford time


   

