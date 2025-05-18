import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Carregar dados
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

# Treinar modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avaliar
acc = model.score(X_test, y_test)
print(f"Acurácia: {acc:.2f}")

# Salvar modelo
joblib.dump(model, "iris_model.joblib")
