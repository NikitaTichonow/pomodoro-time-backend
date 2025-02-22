.DEFAULT_GOAL := help

HOST ?= 127.0.0.1
PORT ?= 8000

run: ## Run the application using uvicorn with provided arguments or defaults --host $(HOST) --port $(PORT) --env-file .local.env --env-file ${ENV_FILE}
	poetry run uvicorn main:app --reload 

install:  ## Install a dependency using poetry
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall: ## Uninstall a dependency using poetry
	@echo "Uninstalling dependency $(LIBRARY)"
	poetry remove $(LIBRARY)

migrate-create: # Create migrations alembic
	alembic revision --autogenerate -m $(MIGRATION)

migrate-upgrade: # Applying migrations alembic
	alembic upgrade head

alembic-history:
	alembic history --verbose
   
help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands: "
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $1, $2}'