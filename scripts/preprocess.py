import pandas as pd

# Carregar e preparar dados
df = pd.read_csv("data/raw/vendas_simuladas.csv", parse_dates=["data"])

# Ordenar
df = df.sort_values(['loja_id', 'produto_id', 'data'])

# Variáveis temporais
df['ano'] = df['data'].dt.year
df['semana'] = df['data'].dt.isocalendar().week

# Média móvel de 3 semanas por produto e loja
df['media_movel_3s'] = df.groupby(['loja_id', 'produto_id'])['vendas'].transform(
    lambda x: x.rolling(window=3, min_periods=1).mean()
)

# Lag: vendas da semana anterior
df['venda_anterior'] = df.groupby(['loja_id', 'produto_id'])['vendas'].shift(1)

# Remove linhas com NaN criadas pelo shift()
df = df.dropna()

# Agrupar por semana e loja/produto/categoria
df_agg = df.groupby(
    ['ano', 'semana', 'loja_id', 'categoria', 'promocao', 'feriado', 'produto_id']
).agg({
    'vendas': 'sum',
    'preco_unitario': 'mean',
    'media_movel_3s': 'mean',
    'venda_anterior': 'mean'
}).reset_index()

# One-hot encoding
df_encoded = pd.get_dummies(df_agg, columns=['categoria', 'loja_id', 'produto_id'], drop_first=True, dtype=int)

# Salvar
df_encoded.to_csv("data/processed/vendas_preprocessadas.csv", index=False)
print("✅ Pré-processamento com média móvel e lag salvo com sucesso!")
