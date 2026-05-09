🚀 Nexus Backend
This repository contains the core microservices for the Nexus platform, including the Nucleus orchestrator, Nexus-AI worker, and the Realtime transport layer.

🛠 Prerequisites
Docker & Docker Compose (Ensure Docker Desktop is running)

Git

Environment File: Create a .env file in the root directory based on .env.example.

📥 Setup Instructions
1. Clone & Branching

First, pull the latest code and switch to the development branch where active features are integrated.

Bash
# Clone the repository
git clone git@github.com:NeuralOPS-Nexus/nexus-backend.git
cd nexus-backend

# Switch to the dev branch
git checkout dev
2. Configuration

Ensure your .env file is populated with the necessary API keys and database credentials.

Bash
cp .env.example .env
# Edit .env with your specific keys (OpenAI, Anthropic, Centrifugo secrets)
🏗 Building & Running
For M4 Mac (ARM64)

If you are developing on an M4 Mac, use the dedicated architecture builds:

Bash
# Build the transport module and other services for ARM64
ARCH=arm64 docker compose build --no-cache

# Spin up the infrastructure
docker compose up -d
For standard x86/AMD64

Bash
docker compose build
docker compose up -d
🛰 Service Map
Service	Internal Port	External Port	Description
Nucleus	8000	8003	Main Orchestrator (FastAPI)
Nexus-AI	8000	8000	AI Worker (LLM integration)
Realtime	8000	8002	Centrifugo-based Transport
Postgres	5432	5433	Primary Relational DB
ChromaDB	8000	N/A	Vector Database
🔄 Development Workflow
To contribute changes or fix build issues (like the transport module internal/ folder mapping):

Create a feature branch: git checkout -b feature/my-new-feature

Commit changes: Ensure critical Go internal/ folders are tracked (not ignored).

Push and Compare: Push your branch and create a Pull Request (PR) targeting the dev branch.

Test: Verify the build passes in Docker using docker compose build.

📝 Important Notes

Nucleus Debugging: By default, the Nucleus service is set to tail -f /dev/null. To start the server manually for debugging, use docker exec -it nexus-nucleus python3 -m uvicorn apps.main:app --host 0.0.0.0.

Database Volumes: Data is persisted locally in ./data/postgres_data and ./data/chroma_data.

> ⚠️ **Important Notice Regarding Branches**
> 
> * **`dev` (Default):** This is the active, stable development branch. **Clients and users should clone from this branch.**
> * **`master`:** This branch is currently legacy/outdated and is pending deprecation. Do not deploy from `master`.
