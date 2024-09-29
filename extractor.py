import pandas as pd

# 1. Încărcați fișierul CSV original
df = pd.read_csv('euvsdisinfo_part_0.csv')

# 2. Extragerea a 50 de rânduri aleatorii
df_sample = df.sample(n=50, random_state=42)

# 3. Salvarea rândurilor extrase într-un nou fișier CSV
df_sample.to_csv('ramf.csv', index=False)

print("Cele 50 de rânduri au fost extrase și salvate în 'ramf.csv'.")
