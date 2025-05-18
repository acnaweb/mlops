# 🗃️ Feature Store - Feast (`feature_repo`)

Esta pasta define o repositório de features para o projeto CD4ML, utilizando o [Feast](https://docs.feast.dev/).

---

## 📁 Estrutura

| Arquivo                 | Descrição                                  |
|-------------------------|--------------------------------------------|
| `feature_store.yaml`    | Configuração geral do Feast                |
| `entities.py`           | Entidades registradas (ex: customer_id)    |
| `data_sources.py`       | Fontes de dados para as features           |
| `feature_views.py`      | Feature Views (schemas, TTL, entidades)    |

---

## 📦 Gerando dados de exemplo (`features.parquet`)

> Instale o pacote necessário:

```bash
pip install pyarrow
```

> Rode o script abaixo:

```python
import pandas as pd
from datetime import datetime

df = pd.DataFrame({
    "customer_id": [1001, 1002, 1003, 1004],
    "feature1": [0.85, 0.76, 0.92, 0.67],
    "feature2": [1.2, 1.0, 0.9, 1.3],
    "target": [1, 0, 1, 0],
    "event_timestamp": pd.to_datetime(["2023-05-01 12:00", "2023-05-01 13:00", "2023-05-01 14:00", "2023-05-01 15:00"]),
    "created": pd.to_datetime(["2023-05-01 16:00"] * 4)
})

df.to_parquet("data/features.parquet", index=False)
```

---

## 🚀 Comandos úteis do Feast

```bash
# Inicializar o repo
feast init feature_repo

# Listar entidades e features
feast apply

# Validar objetos
feast validate

# Iniciar UI local (opcional)
feast ui
```