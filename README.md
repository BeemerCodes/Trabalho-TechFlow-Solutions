<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-3.0.0-lightgrey.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.50-red.svg" alt="SQLAlchemy Version">
  <img src="https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue.svg" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  
  <h1>TechFlow Solutions - Task Manager API</h1>
  <p>Uma API RESTful elegante e ágil para gerenciamento de fluxo de trabalho.</p>
</div>

---

## 📖 Sobre o Projeto

Este projeto, idealizado pela **TechFlow Solutions**, é um **Sistema de Gerenciamento de Tarefas** construído sob medida para atender as necessidades de uma startup de logística. O objetivo principal do software é permitir que a empresa cliente acompanhe seu fluxo de trabalho em tempo real, priorize tarefas críticas de transporte/estoque e monitore a eficiência de sua equipe.

Através deste sistema, buscamos mitigar os problemas mais comuns em operações de rápido crescimento, como falhas de comunicação e perda de rastreabilidade das atividades.

_Nota: Este repositório foi construído como parte da disciplina de Engenharia de Software, aplicando na prática o ciclo de vida de desenvolvimento, desde a governança até o controle de qualidade automatizado._

---

## 🔄 Metodologias Ágeis e Engenharia de Software

A estrutura do projeto foi concebida sob os pilares das metodologias ágeis e melhores práticas da Engenharia de Software:

- **Quadro Kanban (GitHub Projects):** Todo o fluxo de desenvolvimento foi guiado por um painel Kanban, organizado nas raias **A Fazer**, **Em Progresso** e **Concluído**. Isso permitiu clareza na atribuição de tarefas e no ritmo de desenvolvimento.
- **Commits Estruturados:** O histórico de evolução do código foi mantido limpo e rastreável, com mensagens descritivas detalhando a motivação de cada alteração.
- **Pipeline de Qualidade (CI/CD):** Utilizamos **GitHub Actions** para garantir a confiabilidade contínua. Cada alteração passa por uma suíte de testes automatizados (`pytest`), o que previne regressões e garante entregas seguras de software para o cliente.

### ⚠️ Gestão de Mudanças (Alteração de Escopo)

**Contexto e Justificativa:** Durante as avaliações de usabilidade da primeira versão, a startup de logística identificou que não era possível distinguir demandas operacionais normais de entregas urgentes (expressas). Em cenários logísticos, uma falha de priorização pode gerar multas e atrasos graves.
**Adequação:** O escopo inicial foi modificado para introduzir um sistema de **Sinalização de Prioridade**. Adicionamos o campo `priority` na API e no banco de dados. O quadro Kanban foi adaptado com novos cards para modelar a alteração no banco, adequar os endpoints e atualizar os testes automatizados para cobrir essa nova regra de negócios.

---

## ✨ Funcionalidades (Core CRUD)

- **Criação de Tarefas**: Registre novas demandas operacionais definindo título, status atual e definindo se é uma prioridade alta (`priority: true`).
- **Acompanhamento (Leitura)**: Consulte a lista integral de atividades ativas.
- **Transição de Status (Atualização)**: Atualize tarefas, movendo o status de "A Fazer" para "Em Progresso" ou "Concluído" à medida que a equipe logística trabalha.
- **Exclusão**: Remova registros duplicados ou cancelados.

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** - Base da aplicação.
- **[Flask](https://flask.palletsprojects.com/)** - Framework web para construção da API.
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)** - ORM para a comunicação com o banco de dados.
- **[SQLite](https://www.sqlite.org/index.html)** - Banco de dados embutido.
- **[Pytest](https://docs.pytest.org/) & [GitHub Actions](https://github.com/features/actions)** - Qualidade de código e testes automatizados.

---

## 🚀 Como Executar o Projeto

A aplicação é multiplataforma. Siga as instruções abaixo para rodar a API localmente:

### 📋 Pré-requisitos

- Python 3.8 ou superior
- Git

### 🔧 Instalação Passo a Passo

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/Trabalho-TechFlow-Solutions.git
   cd Trabalho-TechFlow-Solutions
   ```

2. **Crie e Ative um Ambiente Virtual**
   - No **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - No **Linux/macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as Dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie a Aplicação**
   ```bash
   python src/app.py
   ```
   A API estará operando em `http://127.0.0.1:5000/`. O banco de dados (`tasks.db`) será auto-gerado no primeiro acesso na pasta `instance/`.

---

## 📚 Documentação da API

Base URL local: `http://localhost:5000`

### 1. Criar Tarefa (`POST /tasks`)

**Corpo da Requisição (JSON):**

```json
{
  "title": "Despachar lote logístico B-402",
  "status": "A Fazer",
  "priority": true
}
```

**Resposta (201 Created):**

```json
{
  "id": 1,
  "title": "Despachar lote logístico B-402",
  "status": "A Fazer",
  "priority": true
}
```

### 2. Listar Tarefas (`GET /tasks`)

**Resposta (200 OK):**

```json
[
  {
    "id": 1,
    "title": "Despachar lote logístico B-402",
    "status": "A Fazer",
    "priority": true
  }
]
```

### 3. Atualizar Status ou Prioridade (`PUT /tasks/<id>`)

**Corpo da Requisição (JSON):**

```json
{
  "status": "Concluído"
}
```

**Resposta (200 OK):**

```json
{
  "id": 1,
  "title": "Despachar lote logístico B-402",
  "status": "Concluído",
  "priority": true
}
```

### 4. Remover Tarefa (`DELETE /tasks/<id>`)

**Resposta de Sucesso:** `204 No Content`

---

## 🧪 Controle de Qualidade e Testes

O projeto contém testes automatizados configurados sob a suíte do `pytest`.

Para executar a validação localmente:

```bash
pytest tests/
```

_Esses testes também rodam automaticamente a cada push via GitHub Actions._

---

## 📁 Estrutura do Repositório

```text
Trabalho-TechFlow-Solutions/
├── .github/workflows/      # Pipelines de CI/CD (GitHub Actions)
├── instance/               # Banco de Dados SQLite (auto-gerado)
├── src/                    # Código fonte da API
│   └── app.py              # Lógica central e roteamento
├── tests/                  # Diretório de testes automatizados
│   └── test_api.py         # Validações dos endpoints
├── .gitignore              # Ignora arquivos desnecessários no versionamento
├── README.md               # Documentação técnica do projeto
└── requirements.txt        # Especificação das bibliotecas e frameworks
```

---

<div align="center">
  <i>BeemerCodes© 2026 - Menos boilerplate, mais impacto.</i>
</div>
