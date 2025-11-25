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

export = "data.csv"
if not os.path.exists(export):
    df.to_csv(export)

start = time.time()
df = pd.read_csv(filename)
end = time.time()
print("Time to load csv:", (end - start) * 1000)
size = os.path.getsize(filename)
print(f"Size of csv: {size}")