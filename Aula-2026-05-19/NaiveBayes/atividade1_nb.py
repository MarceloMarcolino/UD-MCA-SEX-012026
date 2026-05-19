"""
PYTHON para Inteligência Artificial - Aula 09
Naive Bayes - Atividade 1

Objetivo: Aplicar Naive Bayes ao dataset simples criado na Atividade 1
do KNN (clima x temperatura -> brincar), comparando os resultados com
o KNN.

Requisitos: pip install scikit-learn
"""

from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

print("=" * 60)
print("ATIVIDADE 1 - NAIVE BAYES")
print("Comparação Naive Bayes (Gaussian) x KNN")
print("=" * 60)

# --- Dataset ---
clima = ['Ensolarado', 'Ensolarado', 'Nublado', 'Chuvoso', 'Chuvoso',
         'Chuvoso', 'Nublado', 'Ensolarado', 'Ensolarado', 'Chuvoso',
         'Ensolarado', 'Nublado', 'Nublado', 'Chuvoso']

temp = ['Quente', 'Quente', 'Quente', 'Ameno', 'Frio', 'Frio', 'Frio',
        'Ameno', 'Frio', 'Ameno', 'Ameno', 'Ameno', 'Quente', 'Ameno']

brincar = ['Não', 'Não', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim',
           'Sim', 'Sim', 'Sim', 'Sim', 'Não']

# --- Pré-processamento ---
le = preprocessing.LabelEncoder()
clima_encoded = le.fit_transform(clima)
temp_encoded = le.fit_transform(temp)
alvo = le.fit_transform(brincar)

carac = list(zip(clima_encoded, temp_encoded))
print("\nCaracterísticas (clima, temp):", carac)
print("Alvo:", alvo)

casos = [
    ((2, 0), "Nublado e Ameno"),
    ((1, 2), "Ensolarado e Quente"),
    ((0, 1), "Chuvoso e Frio"),
    ((1, 1), "Ensolarado e Frio"),
    ((2, 2), "Nublado e Quente"),
    ((0, 0), "Chuvoso e Ameno"),
]

# --- Modelo Naive Bayes (Gaussian) ---
modelo_nb = GaussianNB()
modelo_nb.fit(carac, alvo)

# --- Modelo KNN ---
modelo_knn = KNeighborsClassifier(n_neighbors=3)
modelo_knn.fit(carac, alvo)

# --- Comparação caso a caso ---
print("\n" + "-" * 60)
print(f"{'Caso':<25}{'KNN':<12}{'Naive Bayes'}")
print("-" * 60)
for entrada, descricao in casos:
    pred_knn = modelo_knn.predict([list(entrada)])[0]
    pred_nb = modelo_nb.predict([list(entrada)])[0]

    r_knn = "Sim" if pred_knn == 1 else "Não"
    r_nb = "Sim" if pred_nb == 1 else "Não"

    print(f"{descricao:<25}{r_knn:<12}{r_nb}")

# --- Probabilidades estimadas pelo NB ---
print("\nProbabilidades a posteriori (Naive Bayes):")
print(f"{'Caso':<25}{'P(Não)':<10}{'P(Sim)'}")
print("-" * 50)
for entrada, descricao in casos:
    proba = modelo_nb.predict_proba([list(entrada)])[0]
    print(f"{descricao:<25}{proba[0]:.4f}    {proba[1]:.4f}")

# --- Acurácia nas amostras de treino ---
acc_nb = modelo_nb.score(carac, alvo) * 100
acc_knn = modelo_knn.score(carac, alvo) * 100
print("\nAcurácia (nos próprios dados de treino, apenas referência):")
print(f"  Naive Bayes: {acc_nb:.2f}%")
print(f"  KNN (k=3):   {acc_knn:.2f}%")

print("\n" + "=" * 60)
print("COMENTÁRIOS / CONCLUSÕES")
print("=" * 60)
print("""
1. Em datasets pequenos como esse, KNN e Naive Bayes costumam concordar
   na maioria das previsões — em particular, ambos acertam que jogar
   com tempo nublado é sempre "Sim" e que ensolarado-quente é "Não".

2. O Naive Bayes calcula probabilidades reais (P(Não), P(Sim)). Isso é
   uma vantagem sobre o KNN porque permite avaliar a confiança da
   previsão, não só a classe vencedora.

3. O KNN olha para os k vizinhos mais próximos; em um espaço com poucos
   pontos e categorias codificadas como inteiros, isso pode dar
   resultados sensíveis ao valor de k. Já o Naive Bayes estima
   distribuições e tende a ser mais estável.

4. Naive Bayes assume independência entre as features — aqui clima e
   temperatura não são totalmente independentes (dias ensolarados
   tendem a ser mais quentes), mas mesmo com essa hipótese violada
   o modelo ainda generaliza bem.

5. Em ambos os modelos a base de 14 amostras é insuficiente para uma
   avaliação rigorosa (não há separação treino/teste). Para um juízo
   confiável, ver a Atividade 3 que usa bootstrap com milhares de
   treinamentos.
""")
