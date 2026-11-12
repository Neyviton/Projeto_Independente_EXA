# Projeto_Independente_EXA

## Configuração do Ambiente

### 1. Clonar o repositório

* git clone <URL_DO_REPOSITORIO>
* cd <NOME_DA_PASTA_DO_PROJETO>

### 2. Criar e ativar o ambiente virtual
### Linux / macOS:
* python3 -m venv .venv
* source .venv/bin/activate

### Windows (PowerShell):
* python -m venv .venv
* .venv\Scripts\Activate.ps1

### 3. Instalar dependências e o pacote local
* pip install --upgrade pip
* pip install -r requirements.txt
* pip install -r requirements-dev.txt
* pip install -e .

### 4. Fluxo de Trabalho com Git (Branches)
## Fluxo de Branches

* `main`: Código estável e testado. Nunca faça push direto aqui.
* `develop`: Branch de integração da equipe.
* `feature/database`: Modelagem SQLite, SQLAlchemy e migrações Alembic (Roberto).
* `feature/validation`: Schemas Pydantic e validações de entrada/saída (Pedro).
* `feature/setup-tests`: Configuração de testes, lint e cobertura inicial (João).

**Regra de integração:** Todo trabalho deve ser feito na respectiva branch `feature/*` e integrado via **Pull Request** para a `develop` após rodar os testes locais.
### 5. Comandos de Qualidade e Testes
### Testes e Qualidade de Código

```bash
# Rodar testes
pytest

# Verificar estilo e erros comuns (Lint)
ruff check .

# Verificar tipagem estática
mypy src