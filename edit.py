import pandas as pd

# 1. Încărcarea fișierului CSV existent
df = pd.read_csv('samp.csv')

# 2. Eliminarea cuvântului 'DISINFO:' din coloana 'title'
df['title'] = df['title'].str.replace('DISINFO:', '', regex=False).str.strip()

# 3. Ștergerea coloanelor 'summary', 'link' și 'links_in_text'
df = df.drop(columns=['summary', 'link', 'links_in_text'])

# 4. Salvarea modificărilor într-un nou fișier CSV (sau suprascrierea fișierului original)
df.to_csv('sss.csv', index=False)

print("Modificările au fost efectuate și salvate în 'sampm.csv'.")
