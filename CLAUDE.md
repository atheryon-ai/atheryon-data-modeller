# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

The Atheryon Data Modeller is an MXML to ISDA CDM (Common Domain Model) transformation platform that consists of multiple integrated components:

### Core Architecture
- **Python Transformation Engine** (`/transform/mxml_to_cdm.py`): Converts legacy MXML trade files to standardized ISDA CDM format
- **Azure Functions** (`/azure-functions/`): Serverless compute with AI-powered trade search agents
- **Flask Web Interface** (`/webapp/`): User-friendly web application for data exploration  
- **Spring Boot CDM Service** (`/cdm-service/`): Enterprise Java REST API for CDM data access
- **Rosetta DSL Code Generators** (`/rosetta-dsl/`): Multi-language code generation (DAML, Python, Java, Scala, TypeScript, JSON Schema)

### Data Flow
1. MXML files are processed by the Python transformation engine
2. Transformed CDM JSON is stored in the canonical store (`/canonical_store/trades/`)
3. AI agent provides natural language querying capabilities
4. Multiple interfaces (web, API, functions) provide access to the data

## Development Commands

### Python Development
```bash
# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Code formatting and linting
black .                 # Format code
isort .                 # Sort imports  
flake8                  # Lint code
mypy .                  # Type checking

# Testing
pytest                  # Run tests
coverage run -m pytest  # Run tests with coverage
coverage report         # Show coverage report
```

### Java Development (CDM Service)
```bash
cd cdm-service/
mvn spring-boot:run     # Run the Spring Boot service
mvn clean package      # Build the JAR
mvn test               # Run tests
```

### Azure Functions
```bash
cd azure-functions/
# Install dependencies from requirements 2.txt
pip install -r "requirements 2.txt"
```

## Key File Locations

### Configuration Files
- `pyproject.toml`: Python project configuration with Black and isort settings
- `requirements.txt`: Core Python dependencies (Flask, python-dotenv)
- `requirements-dev.txt`: Development dependencies (testing, linting tools)
- `cdm-service/pom.xml`: Maven configuration for Spring Boot service

### Core Components
- `transform/mxml_to_cdm.py`: Main MXML to CDM transformation logic
- `azure-functions/search_trades_by_field/`: AI-powered trade search agent
- `canonical_store/trades/`: CDM JSON storage location
- `sample_data/`: Test MXML files for development

### Architecture Documentation
- `# Atheryon Data Modeller Architecture.md`: Comprehensive system architecture diagram
- `# Atheryon Data Modeller HL Requirements.md`: High-level requirements and AI agent concepts

## Code Standards

- Python code follows Black formatting (88 character line length)
- Import sorting handled by isort with Black profile
- Type hints enforced via mypy
- All code should pass flake8 linting
- Java code follows Spring Boot conventions

## Testing Strategy

- Python tests located in `/tests/` directory
- Agent functionality tests in `/azure-functions/search_trades_by_field/agent/tools/`
- Use pytest for Python testing with coverage reporting

## ISDA CDM Integration

This project implements ISDA Common Domain Model standards:
- CDM objects represent standardized financial instruments
- Transformation ensures regulatory compliance
- Multi-language code generation supports various platforms
- Full lifecycle event management from trade execution to termination