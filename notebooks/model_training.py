import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

# Caminho do arquivo preprocessado
data_path = r"C:\Users\felip\Desktop\sales_forecast_dashboard\data\processed\vendas_preprocessadas.csv"

# Carregar os dados
df = pd.read_csv(data_path)

# Separar target
y = df["vendas"]

# Selecionar features
X = df.drop(columns=["vendas"])

# Transformar categóricas em dummies, se houver
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True, dtype=int)

# Dividir treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Treinar modelo
model = RandomForestRegressor(
    n_estimators=300,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=3,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Avaliar
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))

# Criar pasta model se não existir
os.makedirs(r"C:\Users\felip\Desktop\sales_forecast_dashboard\model", exist_ok=True)

# Salvar o modelo treinado
model_save_path = r"C:\Users\felip\Desktop\sales_forecast_dashboard\model\sales_forecast_model.pkl"
joblib.dump(model, model_save_path)
print(f"✅ Modelo salvo em {model_save_path}")
