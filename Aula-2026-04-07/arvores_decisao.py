"""
PYTHON para Inteligência Artificial – Aula 05
Árvores de Decisão

Requisitos: pip install scikit-learn pandas
"""

# ============================================================
# PARTE 1 - Conteúdo da Aula: Base Iris
# ============================================================

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
import pandas as pd

# --- Carregar e explorar os dados ---
iris = load_iris()
print(iris['DESCR'])

# --- Dividir em treino (75%) e teste (25%) ---
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42
)

# --- Treinar a Árvore de Decisão ---
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
clf = clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

# --- Avaliar o modelo ---
print("\nMatriz de confusão detalhada:\n",
      pd.crosstab(y_test, predictions, rownames=['Real'], colnames=['Predito'],
                  margins=True, margins_name='Todos'))

print("\nRelatório sobre a qualidade:\n")
print(metrics.classification_report(y_test, predictions,
      target_names=['Setosa', 'Versicolor', 'Virgínica']))

# --- Visualizar a árvore (descomente se tiver graphviz instalado) ---
# import graphviz
# dot_data = tree.export_graphviz(clf, out_file=None,
#                                 feature_names=iris.feature_names,
#                                 class_names=iris.target_names,
#                                 filled=True, rounded=True,
#                                 special_characters=True)
# graph = graphviz.Source(dot_data, format="png")
# graph.render("iris_tree", view=True)

# Alternativa sem graphviz: visualização em texto
print("\nÁrvore em formato texto:")
print(tree.export_text(clf, feature_names=iris.feature_names))


# ============================================================
# EXERCÍCIO 1a) Variando a proporção teste/treinamento
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 1a) Variando a proporção teste/treinamento")
print("=" * 60)

for ts in [0.10, 0.25, 0.50, 0.75, 0.90]:
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=ts, random_state=42
    )
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = metrics.accuracy_score(y_test, preds)

    print(f"\ntest_size={ts:.2f} | Treino: {len(X_train)} | Teste: {len(X_test)} | Acurácia: {acc:.4f}")
    print(metrics.classification_report(y_test, preds,
          target_names=['Setosa', 'Versicolor', 'Virgínica'], zero_division=0))

# Comentário:
# Com poucos dados de treino (test_size alto), a acurácia tende a cair.
# Com poucos dados de teste (test_size baixo), a avaliação fica pouco confiável.
# O equilíbrio usual fica entre 0.20 e 0.30.


# ============================================================
# EXERCÍCIO 1b) Variando a profundidade da árvore
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 1b) Variando a profundidade da árvore")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42
)

for depth in [1, 2, 3, 4, None]:
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=depth, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = metrics.accuracy_score(y_test, preds)
    label = str(depth) if depth else "ilimitado"

    print(f"\nmax_depth={label} | Acurácia: {acc:.4f}")
    print(pd.crosstab(y_test, preds, rownames=['Real'], colnames=['Predito'],
                      margins=True, margins_name='Todos'))
    print(metrics.classification_report(y_test, preds,
          target_names=['Setosa', 'Versicolor', 'Virgínica'], zero_division=0))

# Comentário:
# Profundidade 1: só separa Setosa, mistura as outras duas espécies.
# A partir de profundidade 2, a acurácia já sobe bastante.
# Profundidade ilimitada pode causar overfitting (ajuste excessivo ao ruído).


# ============================================================
# EXERCÍCIO 2) Base Breast Cancer
# ============================================================
print("\n" + "=" * 60)
print("EXERCÍCIO 2) Base Breast Cancer")
print("=" * 60)

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print(cancer['DESCR'])

X = cancer['data']
y = cancer['target']
print(f"\nAmostras: {X.shape[0]} | Atributos: {X.shape[1]}")
print(f"Classes: {cancer.target_names}")

# --- Modelo base ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
clf.fit(X_train, y_train)
preds = clf.predict(X_test)

print(f"\n--- Modelo base (test_size=0.25, max_depth=3) ---")
print(f"Acurácia: {metrics.accuracy_score(y_test, preds):.4f}")
print("\nMatriz de confusão:")
print(pd.crosstab(y_test, preds, rownames=['Real'], colnames=['Predito'],
                  margins=True, margins_name='Todos'))
print("\nRelatório:")
print(metrics.classification_report(y_test, preds, target_names=['Maligno', 'Benigno']))

# Árvore em texto
print("\nÁrvore em formato texto:")
print(tree.export_text(clf, feature_names=list(cancer.feature_names)))

# --- 2a) Variando proporção ---
print("\n" + "-" * 40)
print("2a) Variando proporção teste/treinamento")
print("-" * 40)

for ts in [0.10, 0.25, 0.50, 0.75, 0.90]:
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=ts, random_state=42)
    c = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
    c.fit(Xtr, ytr)
    p = c.predict(Xte)
    print(f"test_size={ts:.2f} | Treino:{len(Xtr):4d} | Teste:{len(Xte):4d} | Acurácia: {metrics.accuracy_score(yte, p):.4f}")

# --- 2b) Variando profundidade ---
print("\n" + "-" * 40)
print("2b) Variando profundidade da árvore")
print("-" * 40)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

for depth in [1, 2, 3, 4, None]:
    c = tree.DecisionTreeClassifier(criterion='entropy', max_depth=depth, random_state=42)
    c.fit(X_train, y_train)
    p = c.predict(X_test)
    label = str(depth) if depth else "ilimitado"
    print(f"\nmax_depth={label:>9s} | Acurácia: {metrics.accuracy_score(y_test, p):.4f}")
    print(metrics.classification_report(y_test, p, target_names=['Maligno', 'Benigno']))