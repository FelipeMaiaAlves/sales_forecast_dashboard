import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Carregar dataset (ajuste o caminho do arquivo)
df = pd.read_csv("data/raw/vendas_simuladas.csv", parse_dates=["data"])

# Vendas totais por categoria
vendas_por_categoria = df.groupby("categoria")["vendas"].sum().sort_values(ascending=False)
print("Vendas por categoria:")
print(vendas_por_categoria)

# Plotar gráfico
plt.figure()
vendas_por_categoria.plot(kind='bar', color='skyblue')
plt.title("Vendas Totais por Categoria")
plt.ylabel("Vendas")
plt.xlabel("Categoria")
plt.show()

# Vendas totais por loja
vendas_por_loja = df.groupby("loja_id")["vendas"].sum().sort_values(ascending=False)
print("\nVendas por loja:")
print(vendas_por_loja)

# Plotar gráfico
plt.figure()
vendas_por_loja.plot(kind='bar', color='salmon')
plt.title("Vendas Totais por Loja")
plt.ylabel("Vendas")
plt.xlabel("Loja")
plt.show()

# Agrupar por mês
df['mes'] = df['data'].dt.to_period('M')
vendas_por_mes = df.groupby('mes')['vendas'].sum()

print("\nVendas por mês:")
print(vendas_por_mes)

# Plotar gráfico
plt.figure()
vendas_por_mes.plot(marker='o')
plt.title("Vendas Totais por Mês")
plt.ylabel("Vendas")
plt.xlabel("Mês")
plt.xticks(rotation=45)
plt.show()

# Vendas totais por categoria
vendas_por_categoria = df.groupby("categoria")["vendas"].sum().sort_values(ascending=False)

print("\nVendas por categoria:")
print(vendas_por_categoria)

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x=vendas_por_categoria.index, y=vendas_por_categoria.values, palette="viridis")
plt.title("Vendas Totais por Categoria")
plt.ylabel("Vendas")
plt.xlabel("Categoria")
plt.xticks(rotation=45)
plt.show()
