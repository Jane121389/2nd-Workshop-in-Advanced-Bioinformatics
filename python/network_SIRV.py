import networkx as nx
import EoN
import matplotlib.pyplot as plt
from collections import defaultdict

G = nx.grid_2d_graph(100,100) #each node is (u,v) where 0<=u,v<=99
#we'll initially infect those near the middle
initial_infections = [(u,v) for (u,v) in G if 45<u<55 and 45<v<55]

H = nx.DiGraph()  #transisiones espontaneas
H.add_edge('Sus', 'Vac', rate = 0.01)
H.add_edge('Inf', 'Rec', rate = 1.0)


J = nx.DiGraph()  #transisiones inducidas
J.add_edge(('Inf', 'Sus'), ('Inf', 'Inf'), rate = 2.0)

IC = defaultdict(lambda:'Sus') #Creamos un mapa vacio

for node in initial_infections:#Agregamos los nodos infectados al mapa
    IC[node] = 'Inf'

return_statuses = ['Sus', 'Inf', 'Rec', 'Vac']

color_dict = {'Sus': '#009a80','Inf':'#ff2000', 'Rec':'gray','Vac': '#5AB3E6'}
pos = {node:node for node in G}
tex = False
sim_kwargs = {'color_dict':color_dict, 'pos':pos, 'tex':tex}

sim = EoN.Gillespie_simple_contagion(G, H, J, IC, return_statuses, tmax=30, return_full_data=True, sim_kwargs=sim_kwargs)
#Esto no maneja contagios complejos. Se asume que cuando un individuo cambia de estado, ha recibido una “transmisión” de un solo vecino o está cambiando de estado independientemente de los vecinos. Entonces esto es como SIS o SIR. 
#EoN.Gillespie_simple_contagion(G, spontaneous_transition_graph, nbr_induced_transition_graph, IC, return_statuses, tmin=0, tmax=100, spont_kwargs=None, nbr_kwargs=None, return_full_data=False, sim_kwargs=None)
#spontaneous_transition_graph:contagios espontaneos, nbr_induced_transition_graph: transiciones inducidas por vecinos,  IC:establece el estado inicial de cada nodo en la red. 

times, D = sim.summary()
#
#imes is a numpy array of times.  D is a dict, whose keys are the entries in
#return_statuses.  The values are numpy arrays giving the number in that
#status at the corresponding time.

newD = {'Sus+Vac':D['Sus']+D['Vac'], 'Inf+Rec' : D['Inf'] + D['Rec']}# Creamos un mapa con los usuarios susceptibles+vacunados y los usuarios infectados +recuperados
#
#newD  indica el número que aún no está infectado o el número que alguna vez se infectó
#Let's add this timeseries to the simulation.
#
new_timeseries = (times, newD)
sim.add_timeseries(new_timeseries, label = 'Simulation', color_dict={'Sus+Vac':'#E69A00', 'Inf+Rec':'#CD9AB3'})

sim.display(6, node_size = 4, ts_plots=[['Inf'], ['Sus+Vac', 'Inf+Rec']])
plt.savefig('SIRV_display.png')

ani=sim.animate(ts_plots=[['Inf'], ['Sus+Vac', 'Inf+Rec']], node_size = 4)
plt.show()
