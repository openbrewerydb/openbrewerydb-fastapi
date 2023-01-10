# 🍻 Official Open Brewery DB FastAPI REST API Server

![Open Brewery DB Logo](OpenBreweryDBLogo.png)

## 🛑 NOTE: WORK IN PROGRESS

The Open Brewery DB API server is a FastAPI REST-based API server connected to a PostgreSQL DB server.

[Documentation](https://www.openbrewerydb.org/)

## 📦 Dependencies

- Python 3.10.6

## 🚀 Getting Started

- Create a virtual environment
  - `python3 -m venv venv`
- Activate environment
  - `source ./venv/bin/activate`
- Install dependencies
  - `pip3 install -r requirements.txt`
- Run the tests
  - `pytest`
- Run the server
  - `uvicorn main:app`
  - Change the host to any connection
    - `--host=0.0.0.0`
  - Change the port (8001 used as example)
    - `--port=8001`

### Endpoints

- `https://localhost:8000/` (HTML)
- `https://localhost:8000/v1/healthcheck` (JSON)

## 🚛 Roadmap

| Task                       | Complete? |
| -------------------------- | --------- |
| Setup repo                 | ✅        |
| README                     | ✅        |
| Initial Unit/Request tests | ✅        |
| Endpoint placeholders      |           |
| Pydantic models            |           |
| Update tests               |           |
| DB Mocks                   |           |
| Query validation           |           |
| Path validation            |           |
| Sentry integration         |           |
| Authentication             |           |
| Rate-limiting              |           |

## 🤝 Contributing

For information on contributing to this project, please see the [contributing guide](CONTRIBUTING.md) and our [code of conduct](CODE_OF_CONDUCT.md).

## 🔗 Related

- [Open Brewery DB Website & Documentation](https://github.com/openbrewerydb/openbrewerydb-sveltekit)
- [Open Brewery DB Dataset](https://github.com/openbrewerydb/openbrewerydb)

## 👾 Community

- [Join the Newsletter](http://eepurl.com/dBjS0j)
- [Join the Discord](https://discord.gg/SHtpdEN)

## 📫 Feedback

Any feedback, please [email me](mailto:chris@openbrewerydb.org).

Cheers! 🍻
