# 📦 Capacitação Profissional em CD4ML (Continuous Delivery for Machine Learning)

Este repositório contém o material completo para capacitação prática e profissional em CD4ML: Continuous Delivery for Machine Learning.

---

## 📚 Módulos Didáticos

- [01 – Fundamentos de CD4ML](notebooks/01_fundamentos_cd4ml.ipynb)
- [02 – Arquitetura de Referência](notebooks/02_arquitetura_referencia.ipynb)
- [03 – Versionamento e Data Contracts](notebooks/03_versionamento_contracts.ipynb)
- [04 – Testes em ML](notebooks/04_testes_ml.ipynb)
- [05 – Orquestração e Pipelines](notebooks/05_orquestracao_pipelines.ipynb)
- [06 – Deploy Contínuo de Modelos](notebooks/06_deploy_modelos.ipynb)
- [07 – Monitoramento e Observabilidade](notebooks/07_monitoramento_observabilidade.ipynb)
- [08 – Gerenciamento de Experimentos](notebooks/08_experimentos_rastreabilidade.ipynb)
- [09 – Padrões de Projeto](notebooks/09_padroes_projeto.ipynb)
- [10 – Projeto Final](notebooks/10_projeto_final.ipynb)

---

## 🧪 Desafios Práticos

- [01 – Fundamentos de CD4ML](desafios/01_fundamentos.md)

---

## 🏗️ Templates

- [Estrutura de Projeto com CI/CD, testes e treino](templates/)
 [train.py](templates/src/train.py)
 [test_basic.py](templates/tests/test_basic.py)
 [.github/workflows/cd4ml_ci.yml](templates/.github/workflows/cd4ml_ci.yml)
 [requirements.txt](templates/requirements.txt)
 [README.md](templates/README.md)

---

## 🗂️ Diagramas C4

- [Diagrama de Contexto (C4)](docs/diagrams/c4_context_cd4ml.puml)
- [Diagrama de Containers (C4)](docs/diagrams/c4_container_cd4ml.puml)
- [Descrição dos Diagramas](docs/diagrams/README.md)

---

## 🚀 Requisitos

- Python 3.10+
- Git, DVC (opcional)
- VSCode + Extensão PlantUML (opcional)
- Docker, FastAPI (para serving)
- Prometheus, Grafana, Evidently (para monitoramento)

---

Capacitação estruturada com foco em aplicação no mercado e validação por meio de desafios práticos.

---

## 🧪 Testes Adicionais

- `test_input_validation.py`: Garante que os arquivos CSV de entrada têm colunas e dados válidos.

## ⏰ Monitoramento Agendado

- **Interno (cron):** Container `cron` executa o monitoramento continuamente.
- **Externo (GitHub Actions):** Workflow `scheduled_monitor.yml` roda a cada 15 minutos automaticamente.

## ☁️ Armazenamento

- Relatórios de drift são salvos como JSON e enviados para S3.
 Bucket padrão: `cd4ml-monitoring`
 Caminho: `drift_reports/drift_report.json`

## 📦 Comandos Úteis

```bash
make install       # Instala dependências
make train         # Treina modelo
make test          # Executa testes
make monitor       # Gera relatório Evidently + envia para S3
```