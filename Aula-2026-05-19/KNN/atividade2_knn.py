"""
PYTHON para Inteligência Artificial - Aula 08
KNN (K - Nearest Neighbors) - Atividade 2

Objetivo: Aplicar KNN ao dataset de câncer de mama (sklearn) usando duas
características ('mean area' e 'mean compactness'), obter a matriz de
confusão e visualizar os resultados com scatterplots.

Requisitos: pip install scikit-learn pandas matplotlib seaborn
"""

import os

import numpy as np
import pandas as pd
import matplotlib

# Backend não-interativo para gerar PNG mesmo sem display
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

sns.set()

OUTDIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("ATIVIDADE 2 - KNN no dataset de câncer de mama")
print("=" * 60)

# --- Carregar dataset ---
cancer_mama = load_breast_cancer()
X = pd.DataFrame(cancer_mama.data, columns=cancer_mama.feature_names)
X = X[['mean area', 'mean compactness']]
print("\nPrimeiras linhas das features selecionadas:")
print(X.head())

y = pd.Categorical.from_codes(cancer_mama.target, cancer_mama.target_names)
print("\nTarget (primeiras 5 amostras):", y[:5].tolist())

# drop_first economiza colunas quando só duas opções
y = pd.get_dummies(y, drop_first=True)
print("\nTarget binarizado (1 = benigno, 0 = maligno):")
print(y.head())

# --- Treinamento ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=1, test_size=0.25
)
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_train, y_train.values.ravel())

y_pred = knn.predict(X_test)
print("\nPredições no conjunto de teste:")
print(y_pred)

# --- Avaliação ---
acuracia = knn.score(X_test, y_test) * 100
print(f"\nAcurácia: {acuracia:.2f}%")

cm = confusion_matrix(y_test, y_pred)
print("\nMatriz de confusão (linhas: real, colunas: predito):")
print(cm)
print("  [VN FP]")
print("  [FN VP]   (0 = maligno, 1 = benigno)")

print("\nRelatório de classificação:")
print(classification_report(y_test, y_pred, target_names=['maligno', 'benigno']))

# --- Visualização 1: dispersão dos rótulos reais ---
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(
    x='mean area',
    y='mean compactness',
    hue='benign',
    data=X_test.join(y_test, how='outer'),
    ax=ax,
)
ax.set_title("Rótulos reais (0 = maligno, 1 = benigno)")
plot1 = os.path.join(OUTDIR, "atividade2_real.png")
fig.savefig(plot1, dpi=120, bbox_inches="tight")
plt.close(fig)
print(f"\nGráfico salvo: {plot1}")

# --- Visualização 2: predição do KNN ---
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(
    X_test['mean area'],
    X_test['mean compactness'],
    c=y_pred,
    cmap='coolwarm',
    alpha=0.7,
)
ax.set_xlabel('mean area')
ax.set_ylabel('mean compactness')
ax.set_title("Predições do KNN (azul = maligno, vermelho = benigno)")
plot2 = os.path.join(OUTDIR, "atividade2_predito.png")
fig.savefig(plot2, dpi=120, bbox_inches="tight")
plt.close(fig)
print(f"Gráfico salvo: {plot2}")

print("\n" + "=" * 60)
print("COMENTÁRIOS")
print("=" * 60)
print("""
1. Mesmo usando apenas duas características das 30 disponíveis,
   o KNN classifica corretamente a maior parte das amostras.

2. A matriz de confusão mostra alguns falsos positivos e falsos negativos.
   Em diagnóstico médico, falsos negativos (predito benigno quando é
   maligno) são especialmente graves — é uma situação onde valeria
   ajustar o threshold ou usar mais features.

3. Comparando os dois scatterplots, a fronteira de decisão do KNN
   acompanha bem a separação visual entre tumores grandes/compactos
   (malignos) e pequenos/menos compactos (benignos).

4. Adicionar mais variáveis e normalizar a escala provavelmente
   melhoraria a acurácia (o KNN é muito sensível à escala).
""")
