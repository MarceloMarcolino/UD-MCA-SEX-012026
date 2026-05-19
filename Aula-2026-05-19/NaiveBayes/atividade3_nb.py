"""
PYTHON para Inteligência Artificial - Aula 09
Naive Bayes - Atividade 3

Objetivo: Comparar KNN e Naive Bayes (GaussianNB) com 5000 treinamentos
nos datasets de câncer de mama e Iris, reportando média, desvio padrão
e histogramas de acurácia.

Requisitos:
    pip install scikit-learn numpy matplotlib seaborn
"""

import os
import warnings

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import Normalizer

warnings.filterwarnings("ignore")
sns.set()

OUTDIR = os.path.dirname(os.path.abspath(__file__))
N_ITER = 5000


def avaliar(dataset_name, X, y):
    print("\n" + "=" * 60)
    print(f"DATASET: {dataset_name}")
    print("=" * 60)

    # --- Treino único para o relatório base ---
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, random_state=42)

    knn = KNeighborsClassifier()
    knn.fit(X_tr, y_tr)
    print(f"\n[Treino único] KNN: {knn.score(X_te, y_te) * 100:.2f}%")
    print(classification_report(y_te, knn.predict(X_te)))

    nb = GaussianNB()
    nb.fit(X_tr, y_tr)
    print(f"[Treino único] Naive Bayes (Gaussian): {nb.score(X_te, y_te) * 100:.2f}%")
    print(classification_report(y_te, nb.predict(X_te)))

    # --- Normalização + 5000 treinamentos ---
    scaler = Normalizer()
    scaler.fit(X)
    X_norm = scaler.transform(X)

    scores_knn = []
    scores_nb = []

    print(f"Executando {N_ITER} treinamentos com normalização L2...")
    for _ in range(N_ITER):
        X_tr, X_te, y_tr, y_te = train_test_split(X_norm, y)

        knn = KNeighborsClassifier()
        knn.fit(X_tr, y_tr)
        scores_knn.append(knn.score(X_te, y_te))

        nb = GaussianNB()
        nb.fit(X_tr, y_tr)
        scores_nb.append(nb.score(X_te, y_te))

    print(f"  KNN          | média {np.mean(scores_knn) * 100:6.2f}%  | "
          f"desvio padrão {np.std(scores_knn) * 100:.2f}%")
    print(f"  Naive Bayes  | média {np.mean(scores_nb) * 100:6.2f}%  | "
          f"desvio padrão {np.std(scores_nb) * 100:.2f}%")

    # --- Histogramas ---
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    sns.histplot(scores_knn, kde=True, ax=axes[0], color="#4C72B0")
    axes[0].set_title(f"KNN — {dataset_name}")
    axes[0].set_xlabel("Acurácia")

    sns.histplot(scores_nb, kde=True, ax=axes[1], color="#DD8452")
    axes[1].set_title(f"Naive Bayes — {dataset_name}")
    axes[1].set_xlabel("Acurácia")

    fig.suptitle(f"Distribuição da acurácia em {N_ITER} treinamentos — {dataset_name}")
    nome_arquivo = f"atividade3_hist_{dataset_name.lower().replace(' ', '_')}.png"
    caminho = os.path.join(OUTDIR, nome_arquivo)
    fig.savefig(caminho, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  Histogramas salvos em: {caminho}")

    return scores_knn, scores_nb


# ------------------------------------------------------------------
# 1. Câncer de mama
# ------------------------------------------------------------------
cancer = load_breast_cancer()
scores_knn_cancer, scores_nb_cancer = avaliar("Cancer de Mama", cancer.data, cancer.target)

# ------------------------------------------------------------------
# 2. Iris
# ------------------------------------------------------------------
iris = load_iris()
scores_knn_iris, scores_nb_iris = avaliar("Iris", iris.data, iris.target)

# ------------------------------------------------------------------
# Resumo comparativo
# ------------------------------------------------------------------
print("\n" + "=" * 60)
print("RESUMO COMPARATIVO")
print("=" * 60)
print(f"{'Dataset':<18}{'Modelo':<15}{'Média':<12}{'Desvio padrão'}")
print("-" * 60)
for nome, knn, nb in [
    ("Cancer de Mama", scores_knn_cancer, scores_nb_cancer),
    ("Iris", scores_knn_iris, scores_nb_iris),
]:
    print(f"{nome:<18}{'KNN':<15}{np.mean(knn) * 100:>6.2f}%     {np.std(knn) * 100:.2f}%")
    print(f"{nome:<18}{'Naive Bayes':<15}{np.mean(nb) * 100:>6.2f}%     {np.std(nb) * 100:.2f}%")

print("\n" + "=" * 60)
print("COMENTÁRIOS / CONCLUSÕES")
print("=" * 60)
print("""
1. NO IRIS as duas técnicas se equivalem (~97% após normalização L2),
   com desvios padrão parecidos (~2,5%). Isso é coerente com a aula 08:
   as três espécies são bem separáveis e a setosa fica geometricamente
   isolada, então qualquer classificador simples se sai bem.

2. NO CÂNCER DE MAMA com normalização L2 o resultado se inverte em
   relação ao treino único do PDF (sem normalização):
       - SEM normalizar (treino único): NB ~96%, KNN ~76%
       - COM normalização L2 (5000 treinos): KNN ~92%, NB ~82%
   A normalização L2 ajuda muito o KNN (escalas equilibradas) e ao
   mesmo tempo prejudica o NB Gaussian — projetar todos os vetores
   para o mesmo módulo destrói parte da informação que as features
   originais carregam (área média, compactness etc.).

3. PORTANTO: a normalização L2 não é sempre benéfica. Para o KNN,
   que depende de distâncias, ela é quase obrigatória. Para o NB
   Gaussian, que estima média/variância por feature, pode até atrapalhar
   se o conjunto original já tiver boa estrutura.

4. O Naive Bayes Gaussian em sklearn é extremamente rápido — 5000
   treinamentos demoram poucos segundos. Para problemas com muitos
   atributos contínuos ele é uma excelente linha de base.

5. Conclusão geral: a melhor técnica depende do pré-processamento
   E do dataset. Em geral, treinar ambas e comparar (como esta
   atividade faz) é uma prática saudável antes de escolher um modelo.
""")
