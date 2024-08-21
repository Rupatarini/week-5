import matplotlib.pyplot as plt
import numpy as np
overs = np.array([1, 20, 27, 35, 40, 45, 50])
sri_lanka_wickets = np.array([0, 10, 40, 65, 89, 160, 200]) 
india_wickets = np.array([1, 1, 6, 160, 161, 162, 206]) 
n = len(overs)
bar_width = 0.35
index = np.arange(n)
plt.figure(figsize=(6, 6))
plt.bar(index - bar_width/2, sri_lanka_wickets, bar_width, color='purple', label='Sri Lanka')
plt.bar(index + bar_width/2, india_wickets, bar_width, color='orange', label='India')
plt.xlabel('Overs')
plt.ylabel('Fall of Wickets')
plt.title('Fall of Wickets for India and Sri Lanka Over 50 Overs')
plt.xticks(index, overs)
plt.legend()
plt.grid(axis='y')
plt.show
