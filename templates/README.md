# CD4ML Project Template

Este repositório fornece uma estrutura base para projetos de Machine Learning com foco em Continuous Delivery (CD4ML). Ele inclui:

- Estrutura modular de código (`src/`, `tests/`)
- Pipeline CI/CD com GitHub Actions
- Script de treino de modelo
- Testes automatizados
- Upload de artefatos treinados

## 📂 Estrutura

```
.
├── .github/workflows/         # CI/CD Pipeline
├── src/                       # Código fonte do modelo
├── tests/                     # Testes com pytest
├── requirements.txt           # Dependências
└── README.md                  # Este arquivo
```

## 🚀 Como usar

1. Clone o repositório
2. Instale os requisitos com `pip install -r requirements.txt`
3. Execute os testes com `pytest`
4. Treine o modelo com `python src/train.py`

## 📦 CI/CD

O pipeline está localizado em `.github/workflows/cd4ml_ci.yml` e será executado a cada `push` na branch `main`.

## 📁 Artefatos

Após o treino, o modelo será salvo como `iris_model.joblib` e armazenado como artefato do pipeline.

---

Criado como parte de capacitação profissional em CD4ML.
