import pandas as pd



data = {'kind': ['cat', 'dog', 'cat', 'dog'],
        'height': [9.1, 6.0, 9.5, 34.0],
        'weight': [7.9, 7.5, 9.9, 198.0]
        }

df = pd.DataFrame(data)
res = df.groupby('kind').agg({'height':['min','max']})
print(res)