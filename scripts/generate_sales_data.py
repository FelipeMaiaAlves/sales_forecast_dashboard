import pandas as pd
import numpy as np
import random
import os
from datetime import datetime

# Parâmetros do dataset
n_lojas = 5
n_produtos = 10
semanas = pd.date_range(start="2023-01-01", end="2024-12-31", freq='W')

# IDs simulados
lojas = [f"L{str(i).zfill(3)}" for i in range(1, n_lojas + 1)]
produtos = [f"P{str(i).zfill(3)}" for i in range(1, n_produtos + 1)]
categorias = ['Eletrônicos', 'Vestuário', 'Alimentos', 'Higiene', 'Brinquedos']

# Simulação dos dados
dados = []

for data in semanas:
    for loja in lojas:
        for produto in produtos:
            categoria = random.choice(categorias)
            preco = round(np.random.uniform(10, 200), 2)
            promocao = np.random.choice([0, 1], p=[0.8, 0.2])
            feriado = np.random.choice([0, 1], p=[0.9, 0.1])

            base_venda = np.random.randint(20, 200)

            if promocao:
                base_venda *= 1.4
            if categoria == 'Alimentos':
                base_venda *= 1.2
            if feriado:
                base_venda *= 1.1

            vendas = int(base_venda * np.random.uniform(0.7, 1.3))

            dados.append([
                data, loja, produto, categoria, vendas,
                preco, promocao, feriado
            ])

# Criar DataFrame
df = pd.DataFrame(dados, columns=[
    'data', 'loja_id', 'produto_id', 'categoria', 'vendas',
    'preco_unitario', 'promocao', 'feriado'
])

# Garantir que a pasta existe
os.makedirs("data/raw", exist_ok=True)

# Salvar CSV
df.to_csv("data/raw/vendas_simuladas.csv", index=False)

print("✅ Dataset gerado com sucesso e salvo em data/raw/vendas_simuladas.csv")
