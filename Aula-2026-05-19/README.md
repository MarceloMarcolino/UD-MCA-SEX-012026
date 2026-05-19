# Aula 08 (KNN) e Aula 09 (Naive Bayes) — 2026-05-19

Implementação das atividades das aulas práticas de KNN e Naive Bayes em Python.

## Requisitos

```bash
pip install scikit-learn numpy pandas matplotlib seaborn
```

## KNN — [KNN/](KNN/)

| Arquivo | Descrição | Artefatos |
| --- | --- | --- |
| [atividade1_knn.py](KNN/atividade1_knn.py) | Dataset simples clima × temperatura → brincar. Codificação por `LabelEncoder` e predições com KNN (k=3). | console |
| [atividade2_knn.py](KNN/atividade2_knn.py) | KNN sobre o dataset breast cancer usando `mean area` e `mean compactness`. Matriz de confusão e scatterplots. | [real](KNN/atividade2_real.png), [predito](KNN/atividade2_predito.png) |
| [atividade3_knn.py](KNN/atividade3_knn.py) | KNN no Iris com pairplot, gráfico 3D e histograma de 2 000 treinamentos com normalização L2. | [pairplot](KNN/atividade3_pairplot.png), [3D](KNN/atividade3_3d.png), [histograma](KNN/atividade3_histograma.png) |

### Resultados principais

- **Atividade 2:** acurácia ≈ 84,6 % (com apenas 2 features). Matriz de confusão `[[42 13][9 79]]` — bate com o PDF.
- **Atividade 3:** média 96,9 % / desvio 2,6 % em 2 000 treinos — bate com o PDF (96,92 % / 2,57 %).

## Naive Bayes — [NaiveBayes/](NaiveBayes/)

| Arquivo | Descrição | Artefatos |
| --- | --- | --- |
| [atividade1_nb.py](NaiveBayes/atividade1_nb.py) | Naive Bayes (Gaussian) sobre o mesmo dataset clima × temperatura, comparado com KNN. Inclui probabilidades a posteriori. | console |
| [atividade2_nb.py](NaiveBayes/atividade2_nb.py) | Comparação `GaussianNB` × `MultinomialNB` × `BernoulliNB` no dataset simples. | console |
| [atividade3_nb.py](NaiveBayes/atividade3_nb.py) | KNN × NB em **breast cancer** e **Iris**: 5 000 treinamentos com normalização L2, média, desvio padrão e histogramas. | [hist. cancer](NaiveBayes/atividade3_hist_cancer_de_mama.png), [hist. iris](NaiveBayes/atividade3_hist_iris.png) |

### Resultados principais (Atividade 3, 5 000 iterações com normalização L2)

| Dataset | KNN | Naive Bayes |
| --- | --- | --- |
| Cancer de mama | **92,2 %** ± 2,0 % | 81,6 % ± 3,0 % |
| Iris           | 96,9 % ± 2,6 % | **97,0 %** ± 2,5 % |

Curiosidade: sem normalização (treino único do PDF), o NB ganha do KNN no breast cancer (≈ 97 % × 76 %). Com normalização L2, o KNN passa na frente — a normalização L2 ajuda muito o KNN porque ele depende de distância, mas o NB Gaussian perde informação de escala ao ter os vetores forçados ao módulo unitário.

## Como executar

```bash
# KNN
cd "Aula-2026-05-19/KNN"
python atividade1_knn.py
python atividade2_knn.py
python atividade3_knn.py

# Naive Bayes
cd "../NaiveBayes"
python atividade1_nb.py
python atividade2_nb.py
python atividade3_nb.py   # demora alguns segundos (5000 iterações × 2 datasets)
```

Os scripts usam o backend `Agg` do matplotlib, então rodam sem display gráfico — as figuras são salvas em PNG ao lado de cada `.py`.
