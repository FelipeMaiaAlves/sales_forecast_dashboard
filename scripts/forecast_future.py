import pandas as pd
import numpy as np
import joblib
from datetime import timedelta

# Quantas semanas à frente prever
N_WEEKS = 8

# Caminhos ajustados conforme seu projeto
data_processed_path = r"C:\Users\felip\Desktop\sales_forecast_dashboard\data\processed\vendas_preprocessadas.csv"
data_raw_path = r"C:\Users\felip\Desktop\sales_forecast_dashboard\data\raw\vendas_simuladas.csv"
model_path = r"C:\Users\felip\Desktop\sales_forecast_dashboard\model\sales_forecast_model.pkl"

# Carregar dados pré-processados
df = pd.read_csv(data_processed_path)

# Carregar modelo treinado
model = joblib.load(model_path)

# Carregar dados brutos para cálculo de features futuras
df_raw = pd.read_csv(data_raw_path, parse_dates=["data"])

# Última data conhecida no histórico
last_date = df_raw["data"].max()

# Gerar datas futuras semana a semana
future_dates = [last_date + timedelta(weeks=i) for i in range(1, N_WEEKS + 1)]

# Identificar todas as combinações loja/produto/categoria existentes
combos = df_raw[["loja_id", "produto_id", "categoria"]].drop_duplicates()

# Criar DataFrame futuro com todas combinações para cada data futura
future_df = pd.DataFrame([
    {"data": d, "loja_id": loja, "produto_id": prod, "categoria": cat}
    for d in future_dates
    for loja, prod, cat in combos.values
])

# Variáveis temporais
future_df["ano"] = future_df["data"].dt.year
future_df["semana"] = future_df["data"].dt.isocalendar().week

# Agrupar vendas históricas para facilitar cálculos
hist_grouped = df_raw.groupby(
    ["loja_id", "produto_id", "categoria", "data"]
)["vendas"].sum().reset_index()

# Concatenar histórico com futuro (vendas futuras ainda desconhecidas)
hist_plus_future = pd.concat([hist_grouped, future_df.assign(vendas=np.nan)], ignore_index=True)

# Ordenar para cálculo de rolling e lag
hist_plus_future = hist_plus_future.sort_values(
    ["loja_id", "produto_id", "categoria", "data"]
).reset_index(drop=True)

# Função para calcular média móvel 3 semanas e lag
def calc_features(group):
    group = group.sort_values("data").copy()
    group["media_movel_3s"] = group["vendas"].rolling(window=3, min_periods=1).mean()
    group["venda_anterior"] = group["vendas"].shift(1)
    return group

hist_plus_future = hist_plus_future.groupby(
    ["loja_id", "produto_id", "categoria"]
).apply(calc_features).reset_index(drop=True)

# Filtrar só as datas futuras
future_features = hist_plus_future[hist_plus_future["data"].isin(future_dates)].copy()

# Preencher NA nas features com médias gerais (para primeiros registros)
future_features["media_movel_3s"].fillna(future_features["media_movel_3s"].mean(), inplace=True)
future_features["venda_anterior"].fillna(future_features["venda_anterior"].mean(), inplace=True)

# Calcular médias históricas das variáveis categóricas usadas no modelo
features_mean = df_raw.groupby(["loja_id", "produto_id", "categoria"])[
    ["promocao", "feriado", "preco_unitario"]
].mean().reset_index()

# Juntar médias no futuro_features
future_features = future_features.merge(features_mean, on=["loja_id", "produto_id", "categoria"], how="left")

# Garantir variáveis temporais
future_features["ano"] = future_features["data"].dt.year
future_features["semana"] = future_features["data"].dt.isocalendar().week

# Criar dummies para categorias, lojas e produtos (mesmo esquema do preprocess)
df_train = pd.read_csv(data_processed_path)
dummy_cols = [col for col in df_train.columns if ("categoria_" in col or "loja_id_" in col or "produto_id_" in col)]

future_dummies = pd.get_dummies(future_features[["categoria", "loja_id", "produto_id"]],
                                drop_first=True, dtype=int)

# Montar dataframe final com todas as features
X_future = pd.concat([
    future_features[
        ["ano", "semana", "promocao", "feriado", "preco_unitario", "media_movel_3s", "venda_anterior"]
    ],
    future_dummies
], axis=1)

# Garantir que todas as colunas do treino estejam no futuro (colunas faltantes zeradas)
for col in dummy_cols:
    if col not in X_future.columns:
        X_future[col] = 0

# Ordenar colunas igual ao treino
X_future = X_future[df_train.drop(columns=["vendas"]).columns]

# Fazer a previsão
preds = model.predict(X_future)

# Preparar output
output_df = future_features[["data", "loja_id", "produto_id", "categoria"]].copy()
output_df["vendas_previstas"] = preds

# Salvar para Power BI
# Forçar tipo float
output_df["vendas_previstas"] = output_df["vendas_previstas"].astype(float)

# Salvar com separador decimal como vírgula
output_df.to_csv(
    r"C:\Users\felip\Desktop\sales_forecast_dashboard\data\future_sales_forecast.csv",
    index=False,
    sep=";",
    decimal=","
)

print("✅ Previsões futuras salvas com separador decimal correto")
