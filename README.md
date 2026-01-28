# CRM Satisfaction Engine

Pipeline ETL containerizado para processamento e análise de dados de interações de clientes, com carga em banco MySQL.

## 📌 Visão Geral

Este projeto implementa um **ETL completo (Extract, Transform, Load)** que:

- Extrai dados de interações de clientes a partir de arquivos Excel
- Realiza transformações e cálculos de métricas
- Carrega os dados tratados em um banco MySQL
- Executa de forma automatizada e reprodutível via Docker

O objetivo é simular um fluxo real de engenharia de dados, com foco em organização, confiabilidade e boas práticas.

---

## 🏗️ Arquitetura

Excel (Input)
↓
Extract (Pandas)
↓
Transform (Regras de Negócio / Métricas)
↓
Load (SQLAlchemy)
↓
MySQL

Todos os serviços são executados em containers Docker orquestrados com Docker Compose.

---

## 📂 Estrutura do Projeto

crm-satisfaction-engine/
│
├── data/
│ └── input/
│ └── crm_interactions.xlsx
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py
│
├── sql/
│ ├── schema.sql
│ └── queries.sql
│
├── docker/
│ ├── Dockerfile
│ ├── docker-compose.yml
│ ├── .env
│ └── .env.example
│
├── requirements.txt
└── README.md

---

## ⚙️ Tecnologias Utilizadas

- Python 3.11
- Pandas
- SQLAlchemy
- MySQL 8
- Docker
- Docker Compose

---

## 🚀 Como Executar o Projeto (Deploy Local)

### Pré-requisitos

- Docker
- Docker Compose

---

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/gustavoyoshizawa/crm-satisfaction-engine.git
cd crm-satisfaction-engine/docker

2️⃣ Configurar variáveis de ambiente

Crie o arquivo .env baseado no exemplo:

cp .env.example .env

Exemplo de .env:

DB_HOST=mysql
DB_PORT=3306
DB_NAME=crm_db
DB_USER=crm_user
DB_PASSWORD=senha_aqui

3️⃣ Subir os containers

docker compose up --build

4️⃣ Resultado esperado

    O MySQL será inicializado automaticamente

    O pipeline ETL será executado

    A tabela customer_profile será criada no banco crm_db

    O container ETL finaliza após a carga dos dados
```
