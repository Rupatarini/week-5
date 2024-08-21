import matplotlib.pyplot as plt
import numpy as np
overs = np.array([1, 20, 27, 35, 40, 45, 50])
sri_lanka_wickets = np.array([0, 10, 40, 65, 89, 160, 200])  
india_wickets = np.array([1, 1, 6, 160, 161, 162, 206])  
plt.figure(figsize=(6, 6))
plt.scatter(overs, sri_lanka_wickets, marker='*', color='blue', label='Sri Lanka')
plt.scatter(overs, india_wickets, marker='o', color='orange', label='India')
plt.xlabel('Overs')
plt.ylabel('Fall of Wickets')
plt.title('Fall of Wickets for India and Sri Lanka Over 50 Overs')
plt.legend()
plt.grid(True)
plt.show()
