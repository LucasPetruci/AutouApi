# AutouApi

API REST para classificação de emails usando Google Gemini. Desenvolvida com FastAPI.

## Pré-requisitos

- Docker e Docker Compose
- Git

## Como Executar

### 1. Clonar os Repositórios

Os dois repositórios precisam estar no mesmo diretório:

```bash
mkdir AutoU
cd AutoU

git clone https://github.com/LucasPetruci/AutouApi.git
git clone https://github.com/LucasPetruci/AutouWeb.git
```

Estrutura esperada:

```
AutoU/
├── AutouApi/
└── AutouWeb/
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` no diretório `AutouApi`:

```env
GOOGLE_API_KEY=sua_chave_api_aqui
AI_MODEL=gemini-1.5-flash
DEBUG=true
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
MAX_FILE_SIZE_MB=10
NEXT_PUBLIC_API_URL=http://localhost:8000
NODE_ENV=development
```

Obtenha a chave da API do Google Gemini em [Google AI Studio](https://makersuite.google.com/app/apikey).

### 3. Executar

No diretório `AutouApi`:

```bash
docker-compose up --build
```

A API ficará em `http://localhost:8000` e a interface web em `http://localhost:3000`.

## Documentação da API

Importe o arquivo `AutouApiDocs.yaml` no Insomnia para testar os endpoints da API.

## Tecnologias

- FastAPI
- Google Gemini
- Uvicorn
- Pydantic
- PyPDF

## Links

- [Interface Web](https://github.com/LucasPetruci/AutouWeb)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Google Gemini API](https://ai.google.dev/)
