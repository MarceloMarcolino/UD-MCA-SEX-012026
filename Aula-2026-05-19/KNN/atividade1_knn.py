"""
PYTHON para Inteligência Artificial - Aula 08
KNN (K - Nearest Neighbors) - Atividade 1

Objetivo: Criar um dataset simples (clima/temperatura/brincar) e
comentar os resultados obtidos com a técnica de KNN.

Requisitos: pip install scikit-learn
"""

from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

print("=" * 60)
print("ATIVIDADE 1 - KNN")
print("Dataset simples: clima x temperatura -> brincar")
print("=" * 60)

# --- Criar dataset ---
clima = ['Ensolarado', 'Ensolarado', 'Nublado', 'Chuvoso', 'Chuvoso',
         'Chuvoso', 'Nublado', 'Ensolarado', 'Ensolarado', 'Chuvoso',
         'Ensolarado', 'Nublado', 'Nublado', 'Chuvoso']
print("\nClima:", clima)

temp = ['Quente', 'Quente', 'Quente', 'Ameno', 'Frio', 'Frio', 'Frio',
        'Ameno', 'Frio', 'Ameno', 'Ameno', 'Ameno', 'Quente', 'Ameno']
print("\nTemperatura:", temp)

brincar = ['Não', 'Não', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim',
           'Sim', 'Sim', 'Sim', 'Sim', 'Não']
print("\nBrincar:", brincar)

base = list(zip(clima, temp, brincar))
print("\nBase agrupada:")
for linha in base:
    print(" ", linha)

# --- Pré-processamento (LabelEncoder) ---
le = preprocessing.LabelEncoder()
clima_encoded = le.fit_transform(clima)
print("\nClima codificado:    ", clima_encoded)
# 0=Chuvoso, 1=Ensolarado, 2=Nublado

temp_encoded = le.fit_transform(temp)
print("Temperatura codificada:", temp_encoded)
# 0=Ameno, 1=Frio, 2=Quente

alvo = le.fit_transform(brincar)
print("Alvo codificado:     ", alvo)
# 0=Não, 1=Sim

carac = list(zip(clima_encoded, temp_encoded))
print("\nCaracterísticas combinadas (clima, temp):")
print(carac)

# --- Treinando o modelo KNN ---
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(carac, alvo)

# --- Predições de teste ---
print("\n" + "-" * 60)
print("Predições")
print("-" * 60)

casos = [
    ((2, 0), "Nublado e Ameno"),
    ((1, 2), "Ensolarado e Quente"),
    ((0, 1), "Chuvoso e Frio"),
    ((1, 1), "Ensolarado e Frio"),
    ((2, 2), "Nublado e Quente"),
]

for entrada, descricao in casos:
    pred = modelo.predict([list(entrada)])[0]
    resultado = "Sim (brinca)" if pred == 1 else "Não (não brinca)"
    print(f"  {descricao:<30} -> {resultado}")

# --- Comentários sobre os resultados ---
print("\n" + "=" * 60)
print("COMENTÁRIOS / CONCLUSÕES")
print("=" * 60)
print("""
1. Para (Nublado, Ameno) -> Sim: o KNN encontra 3 vizinhos próximos com
   o clima nublado e a maioria deles tem como alvo "Sim". Isso reflete
   o padrão do dataset, onde sempre que está nublado os jogadores brincam.

2. Para (Ensolarado, Quente) -> Não: existem duas amostras com essa exata
   combinação no treinamento e ambas tem alvo "Não". A previsão é coerente.

3. O KNN funciona bem mesmo em dataset pequeno e categórico, mas é
   sensível à codificação numérica das categorias. O LabelEncoder
   atribui valores ordinais (0, 1, 2) que sugerem distância, embora
   as categorias sejam nominais. Para datasets maiores e categóricos,
   o OneHotEncoder costuma trazer resultados mais consistentes.

4. Para datasets desbalanceados o KNN pode favorecer a classe majoritária.
   Aqui temos 9 "Sim" e 5 "Não", então há leve viés a favor de "Sim".
""")
