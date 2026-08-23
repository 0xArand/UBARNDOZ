UBARNDOZ

<p align="center">
  <strong>BUSSID Utility & Database Toolkit</strong>
  <br>
  <sub>Automate. Process. Inject. Repeat.</sub>
</p><p align="center">
  <a href="https://github.com/0xArand/UBARNDOZ">
    <img src="https://img.shields.io/github/stars/0xArand/UBARNDOZ?style=flat-square" alt="Stars">
  </a>
  <a href="https://github.com/0xArand/UBARNDOZ">
    <img src="https://img.shields.io/github/forks/0xArand/UBARNDOZ?style=flat-square" alt="Forks">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Status-Experimental-orange?style=flat-square" alt="Status">
</p>---

⚡ Overview

UBARNDOZ is a Python-based utility built around the Bus Simulator Indonesia (BUSSID) ecosystem.

The project provides a lightweight command-line interface for interacting with account-related data, processing career data, handling reward operations, and working with structured game data.

It is intentionally kept simple:

INPUT
  ↓
AUTHENTICATION
  ↓
PROCESSING
  ↓
DATABASE / BACKEND OPERATION
  ↓
RESULT

No bloated framework. No unnecessary abstraction. Just Python doing Python things while pretending the terminal is still cool.

---

✦ Features

🔐 Authentication

- Token-based authentication
- Session authorization handling
- Backend request headers
- Authentication state management

💰 Account Operations

- Account-related reward processing
- Automated reward calculation workflows
- Backend response parsing
- Result display directly in the terminal

🗺️ Career Processing

Supports predefined career routes using city identifiers such as:

BKL
SBY
SMG
CBN
JKT
P_Merak
P_Bakauheni
LPG
PLB
JMB
PBR
BKT
PDG

Career data is represented as structured records containing:

sourceCity
destinationCity
routePassed
activityRewards
Value

This allows route/reward data to be processed programmatically instead of manually handling every entry.

🗄️ Maleo Database Integration

UBARNDOZ includes a planned/experimental workflow for injecting or importing structured database data originating from Maleo.

The integration is designed around a controlled data pipeline:

Maleo Database
      │
      ▼
  Data Export
      │
      ▼
 Validation / Parsing
      │
      ▼
 UBARNDOZ Database Layer
      │
      ▼
 Target Dataset

Database workflow

- Import structured Maleo database data
- Parse database records
- Validate supported fields
- Transform records into UBARNDOZ-compatible structures
- Apply database changes
- Preserve the original dataset where possible
- Provide clear operation results

«Experimental: Maleo database compatibility may change between versions. Always keep a backup of your original data before performing database operations.»

---

🧩 Architecture

                    ┌─────────────────┐
                    │    UBARNDOZ     │
                    │   CLI Utility   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        Authentication    Career       Database
                          Processing   Integration
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Backend / Data  │
                    │    Processing   │
                    └─────────────────┘

---

🛠 Requirements

- Python 3.x
- Internet connection
- Valid authentication token where required

Python dependencies

Current dependencies include:

pyfiglet
requests
colorama
pytz

See ""require.txt"" (./require.txt) for the repository's dependency list.

---

🚀 Installation

Clone the repository:

git clone https://github.com/0xArand/UBARNDOZ.git
cd UBARNDOZ

Install dependencies:

pip install -r require.txt

Run:

python main.py

The application will initialize the CLI and request the required authentication input.

---

🗃️ Database Import

For the Maleo database workflow, the recommended process is:

1. Backup original database
          ↓
2. Export / obtain Maleo database
          ↓
3. Validate database format
          ↓
4. Import into UBARNDOZ
          ↓
5. Transform compatible records
          ↓
6. Verify resulting dataset

Important

Database formats can change between application versions.

Do not assume that a database from one Maleo version is compatible with another version without validation.

Always keep:

original.db
backup.db
modified.db

separate during development.

---

📁 Project Structure

UBARNDOZ/
│
├── main.py
├── require.txt
└── README.md

As the database integration evolves, the project can be separated into:

UBARNDOZ/
│
├── main.py
│
├── database/
│   ├── importer.py
│   ├── parser.py
│   ├── validator.py
│   └── transformer.py
│
├── data/
│   └── schemas/
│
├── require.txt
└── README.md

---

🔬 Development Status

Component| Status
CLI| 🟢 Working
Authentication| 🟢 Working
Career processing| 🟢 Working
Reward processing| 🟢 Working
Maleo database integration| 🟡 Experimental
Database validation| 🟡 Experimental
Automated testing| 🔴 Planned
Versioned database schemas| 🔴 Planned

---

🧪 Roadmap

- [x] Initial Python CLI
- [x] Token authentication
- [x] Career route processing
- [x] Backend request handling
- [x] Reward processing
- [ ] Maleo database importer
- [ ] Database schema detection
- [ ] Automatic backup before modification
- [ ] Database validation
- [ ] Version compatibility checks
- [ ] Import/export commands
- [ ] Better error handling
- [ ] Configuration file support
- [ ] Automated tests
- [ ] Modular database architecture

---

⚠️ Disclaimer

UBARNDOZ is an independent community project and is not affiliated with, endorsed by, or officially connected to the developers or publishers of BUSSID or Maleo.

Use the software responsibly.

Database modification can result in corrupted data or unexpected behavior. Always create a backup before modifying any database.

The repository is intended for educational, research, development, and personal experimentation purposes.

---

🤝 Contributing

Contributions are welcome.

Before opening a pull request:

git checkout -b feature/your-feature

Make your changes, test them locally, then submit a pull request with a clear description of what changed.

Bug reports should include:

- Python version
- Operating system
- Application/database version
- Error message
- Relevant logs
- Steps to reproduce

Never upload authentication tokens, account credentials, or private database contents to an issue.

---

📜 License

See the repository for the applicable license information.

---

<p align="center">
  <strong>UBARNDOZ</strong>
  <br>
  <sub>Built by <a href="https://github.com/0xArand">0xArand</a></sub>
  <br><br>
  <code>0xARND // DATA // SYSTEMS // EXPERIMENTAL</code>
</p>
