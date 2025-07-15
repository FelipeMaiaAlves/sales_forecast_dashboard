import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações visuais
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Carregar dataset
df = pd.read_csv(r"C:\Users\felip\Desktop\sales_forecast_dashboard\data\raw\vendas_simuladas.csv", parse_dates=["data"])

print("Dados carregados:")
print(df.head())
print("\nInformações gerais:")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe())

# 1. Vendas totais por semana (linha do tempo)
vendas_por_semana = df.groupby("data")["vendas"].sum().reset_index()

plt.figure()
sns.lineplot(data=vendas_por_semana, x="data", y="vendas")
plt.title("Vendas Totais por Semana")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.tight_layout()
plt.show()

# 2. Top 10 produtos por vendas totais
top_produtos = df.groupby("produto_id")["vendas"].sum().sort_values(ascending=False).head(10)

plt.figure()
sns.barplot(x=top_produtos.values, y=top_produtos.index, palette="viridis")
plt.title("Top 10 Produtos por Vendas Totais")
plt.xlabel("Vendas")
plt.ylabel("Produto")
plt.tight_layout()
plt.show()

# 3. Impacto de promoções nas vendas
plt.figure()
sns.boxplot(x="promocao", y="vendas", data=df)
plt.title("Impacto da Promoção nas Vendas")
plt.xlabel("Promoção (0=Não, 1=Sim)")
plt.ylabel("Vendas")
plt.tight_layout()
plt.show()

# 4. Vendas por categoria
vendas_por_categoria = df.groupby("categoria")["vendas"].sum().sort_values(ascending=False)

plt.figure()
sns.barplot(x=vendas_por_categoria.values, y=vendas_por_categoria.index, palette="magma")
plt.title("Vendas Totais por Categoria")
plt.xlabel("Vendas")
plt.ylabel("Categoria")
plt.tight_layout()
plt.show()
