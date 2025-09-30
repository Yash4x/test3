.PHONY: install test lint format check-format check-imports ci-check clean

# Use the project's virtualenv python for tooling to avoid relying on PATH
VENV_PY=/home/yash1x/test/python_calculator/venv/bin/python

# Install dependencies
install:
	$(VENV_PY) -m pip install --upgrade pip
	$(VENV_PY) -m pip install -r requirements.txt
	$(VENV_PY) -m pip install black isort

# Run tests with coverage
test:
	# Run pytest via python -m and override pytest.ini addopts to avoid
	# duplicate/unrecognized argument issues when plugins add options.
	PYTHONPATH=src $(VENV_PY) -m pytest --cov=src --cov-report=term-missing --cov-fail-under=100 -q -o addopts=""

# Run pylint
lint:
	PYTHONPATH=src $(VENV_PY) -m pylint src/ tests/ --fail-under=8.0

# Format code with black and isort
format:
	$(VENV_PY) -m black src/ tests/
	$(VENV_PY) -m isort src/ tests/

# Check code formatting (dry run)
check-format:
	$(VENV_PY) -m black --check --diff src/ tests/

# Check import sorting (dry run)
check-imports:
	$(VENV_PY) -m isort --check-only --diff src/ tests/

# Run all CI checks locally (same as GitHub Actions)
ci-check: check-imports check-format lint test
	@echo "✅ All CI checks passed!"

# Clean up generated files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -name "*.egg-info" -exec rm -rf {} +
	rm -rf .coverage coverage.xml .pytest_cache