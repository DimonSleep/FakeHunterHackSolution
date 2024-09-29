import pandas as pd
from googletrans import Translator

# Încărcarea fișierului CSV original
df = pd.read_csv('fisier_original.csv')

# Inițializarea traducătorului
translator = Translator()

# Funcția de traducere
def traduce_text(text):
    try:
        traducere = translator.translate(text, src='ro', dest='en')
        return traducere.text
    except Exception as e:
        print(f"Eroare la traducerea textului: {e}")
        return text

# Aplicarea traducerii pe coloanele dorite
df['titlu_tradus'] = df['titlu'].apply(traduce_text)
df['continut_tradus'] = df['continut'].apply(traduce_text)

# Salvarea noului fișier CSV
df.to_csv('fisier_tradus.csv', index=False)
