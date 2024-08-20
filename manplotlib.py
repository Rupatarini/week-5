import matplotlib.pyplot as plt
import numpy as np
overs = np.array([1, 20, 27, 35, 40, 45, 50])
sri_lanka_wickets = np.array([0, 10, 40, 65, 89, 160, 200]) 
india_wickets= np.array([1, 1, 6, 160, 161, 162, 206]) 
plt.figure(figsize=(6, 6))
plt.plot(overs,sri_lanka_wickets,marker='*',color='purple',linestyle='dashed',label='Sri Lanka')
plt.plot(overs,india_wickets,marker='o',color='orange',linestyle='-',label='India')
plt.xlabel('Overs')
plt.ylabel('Fall of Wickets')
plt.title('Fall of Wickets for India and Sri Lanka Over 50 Overs')
plt.legend()
plt.grid(True)
plt.show()
