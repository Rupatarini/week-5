import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Overs': [5, 10, 15, 20, 30, 40, 50],
    'India Wickets': [1, 12, 20, 27, 34, 46, 49],
    'Sri Lanka Wickets': [3, 9, 29, 33, 35, 47, 50]
}
df = pd.DataFrame(data)
df.set_index('Overs', inplace=True)
fig, axs = plt.subplots(4, 2, figsize=(9, 9))
df.plot(ax=axs[0, 0], marker='o')
axs[0, 0].set_title('Line Plot')
axs[0, 0].set_ylabel('Wickets')
df.plot(kind='bar', ax=axs[0, 1], width=0.8)
axs[0, 1].set_title('Bar Plot')
axs[0, 1].set_ylabel('Wickets')
df.plot(kind='hist', bins=10, alpha=0.5, ax=axs[1, 0])
axs[1, 0].set_title('Histogram')
axs[1, 0].set_ylabel('Frequency')
df.plot(kind='box', ax=axs[1, 1])
axs[1, 1].set_title('Box Plot')
df.plot(kind='area', alpha=0.4, ax=axs[2, 0])
axs[2, 0].set_title('Area Plot')
df.plot(kind='scatter', x='India Wickets', y='Sri Lanka Wickets', ax=axs[2, 1], color='purple', alpha=0.7)
axs[2, 1].set_title('Scatter Plot')
pie_data = df.sum()
pie_data.plot(kind='pie', autopct='%1.1f%%', ax=axs[3, 0], colors=['blue', 'orange'])
axs[3, 0].set_title('Pie Chart')
axs[3, 1].axis('off')
plt.tight_layout()
plt.show()
