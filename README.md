<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-3.0.0-lightgrey.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.50-red.svg" alt="SQLAlchemy Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  
  <h1>TechFlow Solutions - Task API</h1>
  <p>Uma API RESTful elegante e eficiente para gerenciamento de tarefas (To-Do), desenvolvida em Python com Flask.</p>
</div>

---

## 📖 Sobre o Projeto

Este projeto é uma **API de Gerenciamento de Tarefas** desenvolvida como parte de um trabalho acadêmico. O objetivo principal é demonstrar a construção de uma arquitetura RESTful limpa, robusta e escalável, utilizando as melhores práticas de desenvolvimento backend em Python.

A aplicação permite que os usuários realizem operações completas de CRUD (Create, Read, Update, Delete) em tarefas, oferecendo suporte a atributos como status da tarefa e prioridade.

## ✨ Funcionalidades

- **Criação de Tarefas**: Adicione novas tarefas com título, status e nível de prioridade.
- **Listagem**: Recupere todas as tarefas cadastradas de forma estruturada.
- **Atualização**: Edite os dados de uma tarefa existente (título, status ou prioridade).
- **Remoção**: Exclua tarefas de forma segura.
- **Tratamento de Erros**: Respostas padronizadas para erros do cliente (404) e do servidor (500).

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)** - Linguagem de programação principal.
- **[Flask](https://flask.palletsprojects.com/)** - Microframework web para a construção da API.
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)** - ORM para interação com o banco de dados.
- **[SQLite](https://www.sqlite.org/index.html)** - Banco de dados relacional leve (ideal para ambientes de desenvolvimento e trabalhos acadêmicos).
- **[Pytest](https://docs.pytest.org/)** - Framework para execução dos testes automatizados.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto localmente na sua máquina. A aplicação é multiplataforma e pode ser executada em Windows, Linux ou macOS.

### 📋 Pré-requisitos

Certifique-se de ter o seguinte instalado em seu sistema:
- Python 3.8 ou superior
- Git

### 🔧 Instalação Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/Trabalho-TechFlow-Solutions.git
   cd Trabalho-TechFlow-Solutions
   ```

2. **Crie um Ambiente Virtual (Recomendado)**
   O ambiente virtual isola as dependências do projeto para evitar conflitos.
   
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
   Com o ambiente virtual ativado, instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie a Aplicação**
   Execute o servidor de desenvolvimento do Flask:
   ```bash
   python src/app.py
   ```
   A API estará rodando em `http://127.0.0.1:5000/`. O banco de dados (`tasks.db`) será criado automaticamente na pasta `instance/` ao iniciar o servidor pela primeira vez.

---

## 📚 Documentação da API

Todas as requisições e respostas seguem o padrão JSON. A URL base padrão para testes locais é `http://localhost:5000`.

### 1. Criar Tarefa (`POST /tasks`)
Cria uma nova tarefa no sistema.

**Corpo da Requisição (JSON):**
```json
{
  "title": "Finalizar documentação do projeto",
  "status": "Em Progresso",
  "priority": true
}
```
*(Nota: O campo `title` é obrigatório. `status` e `priority` são opcionais. Status padrão: "A Fazer", Prioridade padrão: false).*

**Resposta de Sucesso (201 Created):**
```json
{
  "id": 1,
  "title": "Finalizar documentação do projeto",
  "status": "Em Progresso",
  "priority": true
}
```

### 2. Listar Tarefas (`GET /tasks`)
Retorna todas as tarefas cadastradas.

**Resposta de Sucesso (200 OK):**
```json
[
  {
    "id": 1,
    "title": "Finalizar documentação do projeto",
    "status": "Em Progresso",
    "priority": true
  },
  {
    "id": 2,
    "title": "Revisar código fonte",
    "status": "A Fazer",
    "priority": false
  }
]
```

### 3. Atualizar Tarefa (`PUT /tasks/<id>`)
Atualiza uma tarefa existente pelo seu ID. Você pode enviar apenas os campos que deseja alterar.

**Corpo da Requisição (JSON):**
```json
{
  "status": "Concluído"
}
```

**Resposta de Sucesso (200 OK):**
```json
{
  "id": 1,
  "title": "Finalizar documentação do projeto",
  "status": "Concluído",
  "priority": true
}
```

### 4. Deletar Tarefa (`DELETE /tasks/<id>`)
Remove uma tarefa existente.

**Resposta de Sucesso (204 No Content):**
*(Nenhum conteúdo é retornado em caso de sucesso).*

---

## 🧪 Testes Automatizados

O projeto inclui uma suíte de testes para garantir a integridade das rotas da API. Utilizamos o `pytest` para a execução dos testes.

Para rodar os testes, certifique-se de que o ambiente virtual está ativado e execute o comando na raiz do projeto:

```bash
pytest tests/
```

---

## 📁 Estrutura do Projeto

```text
Trabalho-TechFlow-Solutions/
├── instance/               # Armazena o banco de dados SQLite (gerado automaticamente)
├── src/                    # Código fonte principal
│   └── app.py              # Arquivo principal da aplicação, modelos e rotas
├── tests/                  # Testes automatizados da API
│   └── test_api.py         # Arquivo de testes unitários (pytest)
├── .gitignore              # Arquivos a serem ignorados pelo git
├── LICENSE                 # Licença do projeto (MIT)
├── README.md               # Documentação que você está lendo
└── requirements.txt        # Dependências do projeto para o pip
```

---

<div align="center">
  <i>Desenvolvido com dedicação para fins acadêmicos. ✨</i>
</div>
