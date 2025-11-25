import cudf

"""
For a table with the following three columns and four rows, write a few lines of python code to build a Pandas dataframe, and output the minimum and maximum height for each of the “kind” groups, i.e., ‘cat’ and ‘dog’, respectively.  
Note: 5 bonus point if you also solve the problem using cuDF (optional).   
"""

data = {'kind': ['cat', 'dog', 'cat', 'dog'],
        'height': [9.1, 6.0, 9.5, 34.0],
        'weight': [7.9, 7.5, 9.9, 198.0]
        }

df = cudf.DataFrame(data)
res = df.groupby('kind').agg({'height':['min','max']})
print(res)