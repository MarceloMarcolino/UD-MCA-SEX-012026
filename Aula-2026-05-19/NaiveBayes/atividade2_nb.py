"""
PYTHON para Inteligência Artificial - Aula 09
Naive Bayes - Atividade 2

Objetivo: Aplicar Naive Bayes ao dataset simples (clima/temperatura ->
brincar) com os três classificadores disponíveis no scikit-learn:
GaussianNB, MultinomialNB e BernoulliNB. Comparar e comentar.

Requisitos: pip install scikit-learn
"""

import numpy as np
from sklearn import preprocessing
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB

print("=" * 60)
print("ATIVIDADE 2 - NAIVE BAYES")
print("Comparação Gaussian x Multinomial x Bernoulli")
print("=" * 60)

# --- Dataset ---
clima = ['Ensolarado', 'Ensolarado', 'Nublado', 'Chuvoso', 'Chuvoso',
         'Chuvoso', 'Nublado', 'Ensolarado', 'Ensolarado', 'Chuvoso',
         'Ensolarado', 'Nublado', 'Nublado', 'Chuvoso']

temp = ['Quente', 'Quente', 'Quente', 'Ameno', 'Frio', 'Frio', 'Frio',
        'Ameno', 'Frio', 'Ameno', 'Ameno', 'Ameno', 'Quente', 'Ameno']

brincar = ['Não', 'Não', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim',
           'Sim', 'Sim', 'Sim', 'Sim', 'Não']

le = preprocessing.LabelEncoder()
clima_encoded = le.fit_transform(clima)
temp_encoded = le.fit_transform(temp)
alvo = le.fit_transform(brincar)

carac = np.array(list(zip(clima_encoded, temp_encoded)))

print("\nDados codificados:")
print("Características:", carac.tolist())
print("Alvo:", alvo.tolist())

# --- Criar e treinar os três modelos ---
modelos = {
    "GaussianNB":    GaussianNB(),
    "MultinomialNB": MultinomialNB(),
    "BernoulliNB":   BernoulliNB(),
}

for nome, modelo in modelos.items():
    modelo.fit(carac, alvo)

# --- Casos de teste ---
casos = [
    ((2, 0), "Nublado e Ameno"),
    ((1, 2), "Ensolarado e Quente"),
    ((0, 1), "Chuvoso e Frio"),
    ((1, 1), "Ensolarado e Frio"),
    ((2, 2), "Nublado e Quente"),
    ((0, 0), "Chuvoso e Ameno"),
]

print("\n" + "-" * 60)
print(f"{'Caso':<25}{'Gaussian':<12}{'Multinomial':<14}{'Bernoulli'}")
print("-" * 60)
for entrada, descricao in casos:
    linha = f"{descricao:<25}"
    for nome, modelo in modelos.items():
        pred = modelo.predict([list(entrada)])[0]
        r = "Sim" if pred == 1 else "Não"
        col_w = 12 if nome == "GaussianNB" else 14 if nome == "MultinomialNB" else 0
        if nome == "BernoulliNB":
            linha += f"{r}"
        else:
            linha += f"{r:<{col_w}}"
    print(linha)

# --- Acurácia nas próprias amostras ---
print("\nAcurácia (treino, referência apenas):")
for nome, modelo in modelos.items():
    acc = modelo.score(carac, alvo) * 100
    print(f"  {nome}: {acc:.2f}%")

# --- Probabilidades por modelo ---
print("\nProbabilidades a posteriori P(Sim) por modelo:")
print(f"{'Caso':<25}{'Gaussian':<12}{'Multinomial':<14}{'Bernoulli'}")
print("-" * 60)
for entrada, descricao in casos:
    linha = f"{descricao:<25}"
    for nome, modelo in modelos.items():
        proba = modelo.predict_proba([list(entrada)])[0][1]
        col_w = 12 if nome == "GaussianNB" else 14 if nome == "MultinomialNB" else 0
        valor = f"{proba:.4f}"
        if nome == "BernoulliNB":
            linha += valor
        else:
            linha += f"{valor:<{col_w}}"
    print(linha)

print("\n" + "=" * 60)
print("COMENTÁRIOS / CONCLUSÕES")
print("=" * 60)
print("""
1. GAUSSIAN: assume que as features seguem distribuição normal. Aqui as
   features são categorias codificadas como 0/1/2, então a suposição é
   uma aproximação grosseira — ainda assim, tende a separar bem o
   "Sim" do "Não".

2. MULTINOMIAL: pensado para contagens (ex.: número de vezes que uma
   palavra aparece). Trata os códigos 0/1/2 como se fossem contagens.
   Funciona, mas a interpretação não combina com o significado
   semântico das categorias (Ensolarado, Nublado, Chuvoso não são
   contagens).

3. BERNOULLI: trabalha melhor com features binárias (0/1). Aqui ele
   binariza qualquer valor > 0, então perde a distinção entre
   Ensolarado (1) e Nublado (2). Resultado: tende a empatar as
   previsões e dá acurácia mais baixa.

4. CONCLUSÃO PRÁTICA: para este dataset categórico pequeno o GaussianNB
   teve o melhor desempenho. Em problemas reais, a melhor variante
   depende da natureza das features:
       - Numéricas contínuas ........ Gaussian
       - Contagens (texto, eventos) . Multinomial
       - Binárias (presença/ausência) .. Bernoulli
""")
