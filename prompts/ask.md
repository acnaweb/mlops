# 📘 Prompt Consolidado – Repositório Profissional CD4ML

> **Crie um repositório profissional e completo para capacitação em CD4ML (Continuous Delivery for Machine Learning)** com as seguintes características:

---

## 🎯 Objetivo

Capacitar profissionais em práticas de entrega contínua de modelos de machine learning, com integração de versionamento, testes, monitoramento, automação e orquestração de pipelines, alinhado às arquiteturas utilizadas no mercado.

---

## 📁 Estrutura do Repositório

- `README.md`: Guia completo com índice de módulos, comandos, e instruções de uso.
- `notebooks/`: 10 módulos temáticos de CD4ML, com código e explicações didáticas.
- `desafios/`: Desafios práticos por módulo.
- `docs/diagrams/`: Diagramas C4 em PlantUML (`Context` e `Containers`) com explicações.
- `templates/`:
  - `src/`: Código Python (`train.py`, `monitor_drift.py`, etc.)
  - `tests/`: Testes unitários e de validação de dados (`pytest`)
  - `scripts/`: Automação de comandos (`feast_apply_validate.py`)
  - `data/`: Arquivos `.csv` e `features.parquet` (com instruções para geração)
  - `monitoring/`: Configuração Prometheus + scripts de monitoramento
  - `feature_repo/`: Projeto de Feature Store com Feast
  - `airflow_dags/`: DAG para ingestão de features com Airflow
  - `.github/workflows/`: CI/CD com GitHub Actions (`scheduled_monitor.yml`, `cd4ml_ci.yml`)
  - `Dockerfile`: Imagem com Python + Feast + Airflow + Evidently + Prometheus client
  - `docker-compose.yml`: Infraestrutura com containers para: app, cron, postgres, prometheus e grafana

---

## 🛠️ Funcionalidades Integradas

| Componente        | Descrição                                                                 |
|-------------------|---------------------------------------------------------------------------|
| **CI/CD**         | GitHub Actions com testes, treino e upload de artefatos                  |
| **Serving**       | FastAPI em Docker com previsão de modelos                                 |
| **Monitoramento** | Evidently + Prometheus + Grafana para geração e visualização de métricas  |
| **Agendamento**   | `cron` via Docker ou agendado via GitHub Actions                         |
| **Feature Store** | Feast com entidades, fontes de dados e Feature Views                     |
| **Orquestração**  | Airflow com DAG de ingestão de features + treino                         |
| **S3 Integration**| Upload automático de relatórios JSON para S3 com `boto3`                 |

---

## 📦 Requisitos

- Python 3.10+
- Docker + Docker Compose
- `pip install -r requirements.txt` (inclui: `scikit-learn`, `joblib`, `evidently`, `feast`, `boto3`, etc)

---

## 🧪 Exemplos de Uso

```bash
make install            # Instala dependências
make train              # Treina modelo
make test               # Roda testes
make monitor            # Gera relatório de drift e envia ao S3
docker-compose up       # Sobe stack com app, cron, prometheus, grafana
```

---

## 📊 Monitoramento

- Evidently salva `drift_report.json` localmente e envia para bucket S3 (`cd4ml-monitoring`)
- Prometheus scrapea métricas via `/metrics`
- Grafana acessível em `localhost:3000`

---

## 🧠 Módulos de Capacitação (Notebooks)

1. Fundamentos de CD4ML  
2. Arquitetura de Referência (C4)  
3. Versionamento e Data Contracts  
4. Testes em ML  
5. Orquestração e Pipelines  
6. Deploy Contínuo  
7. Monitoramento e Observabilidade  
8. Experimentos e Tracking  
9. Padrões de Projeto  
10. Projeto Final: pipeline completo