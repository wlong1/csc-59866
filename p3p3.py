import pandas as pd
import os
import time




filename = "/tmp/tlcdata/yellow_tripdata_2009-01.parquet"

start = time.time()
df = pd.read_parquet(filename)
end = time.time()
print("Time to load parquet:", (end - start) * 1000)
size = os.path.getsize(filename)
print(f"Size of parquet: {size}")

filename = "data.csv"
if not os.path.exists(filename):
    df.to_csv(filename)

start = time.time()
df = pd.read_csv(filename)
end = time.time()
print("Time to load csv:", (end - start) * 1000)
size = os.path.getsize(filename)
print(f"Size of csv: {size}")