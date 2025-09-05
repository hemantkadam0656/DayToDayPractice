import pandas as pd 

file_path = 'path+ file.csv'

chunk_size = 10000

total_sales = 0

for chunk in pd.read_csv(file_path):
    total_sales += chunk['sales'].sum()






