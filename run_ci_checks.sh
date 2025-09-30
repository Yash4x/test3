#!/bin/bash
# CI Check Script - Run the same checks that run in GitHub Actions

set -e  # Exit on any error

echo "🔍 Running CI checks locally (exactly as GitHub Actions)..."
echo "========================================================="

echo "📦 Installing dependencies..."
pip install --upgrade pip >/dev/null 2>&1
pip install -r requirements.txt >/dev/null 2>&1
pip install black >/dev/null 2>&1

echo ""
echo "🔤 Checking import sorting with isort..."
isort --check-only --diff src/ tests/

echo ""
echo "🎨 Checking code formatting with black..."
black --check --diff src/ tests/

echo ""
echo "🔍 Running pylint (must score >= 8.0)..."
pylint src/ tests/ --fail-under=8.0

echo ""
echo "🧪 Running pytest with coverage (must be 100%)..."
pytest --cov=src --cov-report=term-missing --cov-report=xml --cov-fail-under=100

echo ""
echo "✅ All CI checks passed! Your code is ready for GitHub Actions."
echo "💡 You can also run 'make ci-check' for the same result."