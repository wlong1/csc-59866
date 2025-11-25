import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import haversine_distances
from sklearn.cluster import AgglomerativeClustering
from math import radians


filename = 'world_cities.csv'
df = pd.read_csv(filename)

df = df[df['population'] > 1_000_000]

coords = df[['lat', 'lng']].map(radians).to_numpy()
dist_km = haversine_distances(coords) * 6371

model = AgglomerativeClustering(n_clusters=10, metric='precomputed', linkage='average')
df['cluster'] = model.fit_predict(dist_km)

plt.scatter(df['lng'], df['lat'], c=df['cluster'], cmap='tab10')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Clusters')
plt.show()