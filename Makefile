.PHONY: render clean install-pre-commit

# Arquivos PlantUML
PUML_FILES := $(shell find . -name '*.puml')

# Comando PlantUML com Docker
PLANTUML_DOCKER := docker run --rm -v $(PWD):/workspace plantuml/plantuml

render:
	@echo "Renderizando diagramas .puml para .png via Docker..."
	@for file in $(PUML_FILES); do \
		echo "Renderizando $$file..."; \
		$(PLANTUML_DOCKER) -tpng /workspace/$$file; \
	done
	@echo "Diagramas renderizados com sucesso."

clean:
	@echo "Removendo arquivos .png..."
	@find . -name '*.png' -type f -delete
	@echo "Arquivos removidos."