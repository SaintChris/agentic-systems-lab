# Agentic Systems Lab

[![Portfolio](https://img.shields.io/badge/Portfolio-saintlex.sbs-blue)](https://saintlex.sbs/)
[![CI](https://github.com/SaintChris/agentic-systems-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/SaintChris/agentic-systems-lab/actions)

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> Portfolio lab exploring six agent roles, a shared task queue, and a lightweight Python/HTML monitoring dashboard. This is a learning project, not a production deployment.

---

## What This Is

A portfolio experiment that models six specialized agent roles coordinating through a shared task queue.

**Key Highlights:**
- **Local-first experiment** — Designed around local and free-tier tooling; actual operating cost depends on the selected providers and environment
- **Architecture experiment** — Delegation, tests, and monitoring concepts
- **Built for learning and demonstration** — Not enterprise production experience
- **Dashboard experiment** — Python HTTP server with a repo-local HTML UI, demo data, and optional Paperclip integration

---

## Quick Start

The safest reproducible entry point is the dashboard's mock-data mode:

```bash
git clone https://github.com/SaintChris/agentic-systems-lab.git
cd agentic-systems-lab

python3 dashboard/app.py --demo
```

Open `http://127.0.0.1:9120`.

Live Paperclip mode is environment-dependent. Configure `PAPERCLIP_API_BASE` and `COMPANY_ID` before running `python3 dashboard/app.py`. Local file browsing/search is disabled by default; set `DASHBOARD_DATA_ROOT` only when you explicitly want to expose a specific local directory to the dashboard process.

---

## 🏗️ Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────┐
│  CEO Agent  │────▶│  Task Queue       │◀────│  Research   │
│  (orchestr.)│     │  (delegation)     │     │  Agent      │
└─────────────┘     └──────────────────┘     └─────────────┘
                           │    │    │
              ┌────────────┘    │    └────────────┐
              ▼                 ▼                  ▼
     ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
     │ Market       │  │ Content      │  │ Finance      │
     │ Analyst      │  │ Growth       │  │ Agent        │
     └──────────────┘  └──────────────┘  └──────────────┘
```

---

## 🤖 Agents

| Agent | Role | Key Capability |
|-------|------|----------------|
| **CEO** | Orchestrator | Monitors system health, delegates tasks, resolves conflicts |
| **Market Analyst** | Analysis | Macro insights, market data, trend identification |
| **Content Growth** | Content | LinkedIn posts, blog content, outreach automation |
| **Finance** | Financial | P&L tracking, budget monitoring, KPI reporting |
| **Ops** | Infrastructure | Deployment, health checks, system monitoring |
| **Research** | Intelligence | External data gathering, specialized analysis |

---

## ✨ Features

- **Agent Delegation Bridge** — Seamless handoff between agents via shared task queue
- **Dashboard UI** — Repo-local HTML served by a lightweight Python HTTP server with mock-data and optional live integration modes
- **Cost-conscious design** — Supports local and free-tier components; no universal monthly-cost claim is made
- **Demo Mode** — Run with mock data for instant demos (no backend dependencies)
- **Test suite included** — Current GitHub Actions CI is green; use the latest workflow result as the verification record
- **Docker Compose integration** — Service wiring is checked in, but the complete multi-service stack is not claimed as end-to-end CI verified

---

## 🧪 Testing

```bash
# Run all integration tests
python3 -m pytest tests/ -v

# Run eval framework
python3 tests/evals.py
```

The repaired baseline passed [CI](https://github.com/SaintChris/agentic-systems-lab/actions/runs/35483437571). The executable example tests passed 52 assertions during rename verification. Use the CI workflow and its latest result as the current verification record.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.11+ |
| Dashboard | Python stdlib HTTP server + HTML/CSS/JS |
| Orchestration integration | Paperclip |
| Vector DB service | Qdrant |
| LLM service | Ollama |
| Storage service | PostgreSQL |
| Deployment/integration config | Docker Compose |

---

## 📁 Repository Structure

```
agentic-systems-lab/
├── dashboard/          # Python/HTML monitoring UI — optional live integration + demo mode
├── docs/               # Architecture docs and diagrams
├── examples/           # Example agent workflow implementations
├── scripts/            # Utility and setup scripts
├── tests/              # Integration tests + eval framework
├── docker-compose.yml  # Full stack deployment
├── requirements.txt
├── .env.example
├── CONTRIBUTING.md
└── LICENSE (MIT)
```

---

## 💡 Why This Exists

Built to practice and demonstrate AI-agent engineering concepts:

1. **Multi-agent orchestration** — Real delegation patterns, not just prompts
2. **Architecture fundamentals** — Tests, monitoring, containerization, documentation
3. **Cost awareness** — Designed to support local and free-tier components where available
4. **Real-world patterns** — Task queues, health checks, eval frameworks, human-in-the-loop

---

## 📄 License

MIT — Free to adapt and reuse.

---

## 👤 Author

**Alex Bogle** — IoT & AI Technician based in Jamaica. This repository is a personal learning lab and is not presented as production employment experience.

- 🌐 [saintlex.sbs](https://saintlex.sbs/)
- 💼 [linkedin.com/in/alex-bogle](https://linkedin.com/in/alex-bogle)
- 📧 [alex@alexbogle.com](mailto:alex@alexbogle.com)

---

> ⭐ If this project is useful or interesting, a star is appreciated — it helps others discover this work.
