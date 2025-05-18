# 📊 Diagramas C4 – Arquitetura CD4ML

Este diretório contém diagramas em PlantUML que representam os principais níveis da arquitetura da solução CD4ML.

---

## 🧭 Diagrama de Contexto – `c4_context_cd4ml.puml`

Representa as interações entre os principais atores e sistemas externos da plataforma CD4ML.

### Principais Elementos:

- **Cientista de Dados / Engenheiro de ML**: Desenvolve e entrega modelos.
- **Engenheiro DevOps**: Automatiza a infraestrutura e monitora os pipelines.
- **GitHub**: Repositório de código, dados, modelos e CI/CD.
- **Google Cloud (GCP)**: Execução dos pipelines e deploy (Vertex AI, Cloud Run).
- **Usuários Finais**: Consumidores das APIs de inferência.

---

## 🧱 Diagrama de Containers – `c4_container_cd4ml.puml`

Detalha os componentes internos da plataforma CD4ML com foco em entrega contínua.

### Componentes:

- **Repositório Git**: Versão única da verdade (código + contrato + modelo).
- **CI/CD Pipeline**: Automatização com GitHub Actions.
- **Script de Treinamento**: Pipeline de modelagem em Python (scikit-learn).
- **Testes Automatizados**: Validadores unitários e de integração.
- **Model Serving**: API REST usando FastAPI + Docker (pode rodar no Cloud Run).
- **Monitoramento**: Prometheus, Grafana e Evidently AI para drift e performance.

---

## ▶️ Como Renderizar

Utilize uma das opções:

- [PlantUML Live Editor](https://www.planttext.com/)
- Extensões do VSCode como "PlantUML"
- GitLab/GitHub + CI com PlantUML Docker