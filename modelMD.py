import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pickle

# 1. Încarcă setul de date
data = pd.read_csv('datele_mele.csv')

# 2. Concatenăm titlul și textul
# Asigură-te că există coloane numite 'titlu' și 'text' în setul de date
data['titlu_text'] = data['titlu'].fillna('') + ' ' + data['text'].fillna('')

# 3. Reprezentarea textului folosind TF-IDF pe combinația titlu + text
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=10000)
X = vectorizer.fit_transform(data['titlu_text'])

# Convertim etichetele într-un format numeric
y = data['label']

# 4. Împărțirea setului de date
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Antrenarea modelului SVM
model_svm = SVC(C=1.0, kernel='linear', probability=True)
model_svm.fit(X_train, y_train)

# 6. Antrenarea modelului RandomForest
model_rf = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=42)
model_rf.fit(X_train, y_train)

# 7. Evaluarea modelului SVM
y_pred_svm = model_svm.predict(X_test)
print("Performanța modelului SVM:")
print(classification_report(y_test, y_pred_svm))
print(confusion_matrix(y_test, y_pred_svm))

# 8. Evaluarea modelului RandomForest
y_pred_rf = model_rf.predict(X_test)
print("Performanța modelului RandomForest:")
print(classification_report(y_test, y_pred_rf))
print(confusion_matrix(y_test, y_pred_rf))

# 9. Salvarea modelelor și a vectorizatorului
with open('model_stiri_false_svm.pkl', 'wb') as f:
    pickle.dump(model_svm, f)

with open('model_stiri_false_rf.pkl', 'wb') as f:
    pickle.dump(model_rf, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Modelele și vectorizatorul au fost salvate cu succes.")
