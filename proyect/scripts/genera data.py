import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuración
NUM_ROWS = 300
PRODUCTS = {
    'Laptop': {'Category': 'Electronics', 'PriceRange': (800, 1500)},
    'Mouse': {'Category': 'Accessories', 'PriceRange': (20, 50)},
    'Monitor': {'Category': 'Electronics', 'PriceRange': (200, 400)},
    'Desk': {'Category': 'Furniture', 'PriceRange': (150, 300)},
    'Chair': {'Category': 'Furniture', 'PriceRange': (100, 250)},
    'Headphones': {'Category': 'Accessories', 'PriceRange': (50, 150)}
}
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 12, 31)

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

data = []
for i in range(NUM_ROWS):
    prod_name = random.choice(list(PRODUCTS.keys()))
    prod_info = PRODUCTS[prod_name]
    
    # Error Intencional: Formatos de Fecha Mixtos (10% de probabilidad de DD-MM-YYYY)
    date_obj = random_date(START_DATE, END_DATE)
    if random.random() < 0.1:
        date_str = date_obj.strftime('%d-%m-%Y')
    else:
        date_str = date_obj.strftime('%Y/%m/%d')
        
    # Error Intencional: Precio Nulo (5% de probabilidad)
    if random.random() < 0.05:
        price = np.nan
    else:
        price = round(random.uniform(*prod_info['PriceRange']), 2)
        
    row = {
        'OrderID': 1000 + i,
        'Date': date_str,
        'Product': prod_name,
        'Category': prod_info['Category'],
        'Price': price,
        'Quantity': random.randint(1, 5),
        'CustomerID': f'CUST-{random.randint(1, 50):03d}'
    }
    data.append(row)

df = pd.DataFrame(data)

# Error Intencional: Filas Duplicadas (Duplicar 5 filas aleatorias)
duplicates = df.sample(n=5)
df = pd.concat([df, duplicates], ignore_index=True)

# Save to CSV
# Guardar en CSV
# Obtener el directorio raíz del proyecto (un nivel arriba de este script)
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_dir = os.path.join(project_root, 'data')

# Asegurar que el directorio data exista
os.makedirs(data_dir, exist_ok=True)

output_file = os.path.join(data_dir, 'raw data.csv')
df.to_csv(output_file, index=False)
print(f"Generated {output_file} with {len(df)} rows.")
