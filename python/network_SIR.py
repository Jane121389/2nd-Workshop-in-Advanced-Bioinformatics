import networkx as nx
import EoN
import matplotlib.pyplot as plt

G = nx.grid_2d_graph(100,100) #creamos una malla de nodos
#colocamos infecciones iniciales 
initial_infections = [(u,v) for (u,v) in G if 45<u<55 and 45<v<55]
print(initial_infections)
#realizamos un diccionario de nuestra red
pos = {node:node for node in G}
#nx.draw(G)
#plt.show() #si queremos visualizar el grafos
#print(pos)

sim_kwargs = {'pos': pos}
tau=2.0 #tasa de transmision
gamma=1.0 # tasa de recuperacion
sim = EoN.fast_SIR(G, tau, gamma, initial_infecteds = initial_infections,
               tmax = 40, return_full_data=True, sim_kwargs = sim_kwargs)

#EoN.fast_SIR(G, tau, gamma, initial_infecteds=None, initial_recovereds=None, rho=None, tmin=0, tmax=inf, transmission_weight=None, recovery_weight=None, return_full_data=False, sim_kwargs=None)
#Simulación SIR rápida para tiempos de recuperación e infección distribuidos exponencialmente
#Gráfo G networkx, tau: tasa de transmisión por arista, gamma: tasa de recuperación por nodo initial_infecteds:nodo inicialmente infectado, initial_recovereds,initial_recovereds: Entendido que todos los que no están infectados o no se recuperan inicialmente son susceptibles, rho: fracción inicial infectada. el número es int (round (G.order () * rho)), tmin (predeterminado 0): tiempo inicial, tmax (infinito predeterminado): tiempo máximo después del cual se detendrá la simulación, transmission_weight:peso en las aristas. la velocidad de transmisión es G.adj [i] [j] [Transmission_weight] * tau, recovery_weight string (predeterminado Ninguno)) peso dado a los nodos para escalar sus tasas de recuperación gamma_i = G.nodes [i] [recovery_weight] * gamma, return_full_data boolean (predeterminado False):Indica si se debe devolver un objeto Simulation_Investigation, sim_kwargs:argumentos enviados al objeto Simulation_Investigation

ani=sim.animate(ts_plots=['I', 'SIR'], node_size = 4) 
plt.show()

tau=90.0 #tasa de transmision
gamma=1.0 # tasa de recuperacion
sim = EoN.fast_SIR(G, tau, gamma, initial_infecteds = initial_infections,
               tmax = 40, return_full_data=True, sim_kwargs = sim_kwargs)

ani=sim.animate(ts_plots=['I', 'SIR'], node_size = 4) 
plt.show()

tau=2.0 #tasa de transmision
gamma=50.0 # tasa de recuperacion
sim = EoN.fast_SIR(G, tau, gamma, initial_infecteds = initial_infections,
               tmax = 40, return_full_data=True, sim_kwargs = sim_kwargs)

ani=sim.animate(ts_plots=['I', 'SIR'], node_size = 4) 
plt.show()

