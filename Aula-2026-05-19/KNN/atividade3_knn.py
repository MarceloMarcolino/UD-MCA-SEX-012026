"""
PYTHON para Inteligência Artificial - Aula 08
KNN (K - Nearest Neighbors) - Atividade 3

Objetivo: Comprovar a confiabilidade do KNN no dataset Iris. Treinar
2000 vezes, calcular média / desvio padrão e gerar o histograma da
acurácia. Também produz a matriz de confusão, pairplot e gráfico 3D.

Requisitos:
    pip install scikit-learn numpy pandas matplotlib seaborn plotly
"""

import os
import warnings

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import Normalizer

warnings.filterwarnings("ignore")
sns.set()

OUTDIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("ATIVIDADE 3 - KNN no dataset Iris")
print("=" * 60)

# --- Treino único para checagem inicial ---
iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
modelo = KNeighborsClassifier()
modelo.fit(X_train, y_train)
acuracia_unico = modelo.score(X_test, y_test) * 100
print(f"\nAcurácia em um único split: {acuracia_unico:.2f}%")

y_pred = modelo.predict(X_test)
print("\nRelatório de classificação:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("Matriz de confusão:")
print(confusion_matrix(y_test, y_pred))
print("(linhas: real, colunas: predito; ordem = setosa, versicolor, virginica)")

# --- Pairplot ---
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Species'] = iris.target

fig = sns.pairplot(df, hue='Species', vars=iris.feature_names)
fig.fig.suptitle("Pairplot do dataset Iris", y=1.02)
plot_pair = os.path.join(OUTDIR, "atividade3_pairplot.png")
fig.savefig(plot_pair, dpi=100, bbox_inches="tight")
plt.close(fig.fig)
print(f"\nPairplot salvo em: {plot_pair}")

# --- Gráfico 3D estático com matplotlib (alternativa ao plotly) ---
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')
cores = ['#a78a91', '#c45a4f', '#6e3a44']
for classe, nome in enumerate(iris.target_names):
    mask = iris.target == classe
    ax.scatter(
        iris.data[mask, 0], iris.data[mask, 1], iris.data[mask, 3],
        label=nome, c=cores[classe], s=30, alpha=0.7,
    )
ax.set_xlabel('sepal length')
ax.set_ylabel('sepal width')
ax.set_zlabel('petal width')
ax.set_title("Iris em 3D")
ax.legend()
plot_3d = os.path.join(OUTDIR, "atividade3_3d.png")
fig.savefig(plot_3d, dpi=120, bbox_inches="tight")
plt.close(fig)
print(f"Gráfico 3D salvo em: {plot_3d}")

# --- 2000 treinamentos com normalização ---
print("\n" + "-" * 60)
print("Treinando o KNN 2000 vezes com normalização (L2)")
print("-" * 60)

scaler = Normalizer()
scaler.fit(X)
X_norm = scaler.transform(X)

scores = []
for _ in range(2000):
    X_tr, X_te, y_tr, y_te = train_test_split(X_norm, y)
    knn = KNeighborsClassifier()
    knn.fit(X_tr, y_tr)
    scores.append(knn.score(X_te, y_te))

print(f"Média:        {np.mean(scores) * 100:.2f}%")
print(f"Desvio padrão: {np.std(scores) * 100:.2f}%")

# --- Histograma ---
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(scores, kde=True, ax=ax)
ax.set_title("Acurácias do KNN (2000 treinamentos, Iris normalizado)")
ax.set_xlabel("Acurácia")
plot_hist = os.path.join(OUTDIR, "atividade3_histograma.png")
fig.savefig(plot_hist, dpi=120, bbox_inches="tight")
plt.close(fig)
print(f"Histograma salvo em: {plot_hist}")

print("\n" + "=" * 60)
print("COMENTÁRIOS")
print("=" * 60)
print("""
1. A acurácia média do KNN no Iris fica próxima de 96%-97%, com desvio
   padrão pequeno (~2-3%). Isso indica um classificador estável neste
   dataset.

2. No relatório de classificação a classe setosa costuma ter precisão
   e recall = 1.00. Olhando o pairplot e o gráfico 3D, a setosa fica
   geometricamente isolada, enquanto versicolor e virginica se sobrepõem.
   Por isso os erros do KNN concentram-se entre essas duas.

3. A normalização L2 (Normalizer) ajusta cada vetor para ter módulo
   unitário; isso elimina o efeito de escala (sepal length tem ordem
   de 4-8 cm enquanto petal width vai de 0-2,5 cm).

4. O histograma mostra a distribuição da acurácia em milhares de
   amostragens — um teste estatístico mais confiável do que um único
   train_test_split, que pode dar resultados muito otimistas ou
   pessimistas por acaso.
""")
