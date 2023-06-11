# ChatGPT Plugin

This branch contains the starter code for my [ChatGPT Plugin Development Tutorial](https://dev.to/mmz001/chatgpt-plugin-development-tutorial-4p4d).

## Local setup

Dependencies are managed with [Poetry](https://python-poetry.org/), so install it if you already haven't:

```bash
pip install poetry
```

Clone the starter template and navigate to the project directory:

```bash
git clone -b starter-template --single-branch https://github.com/mmz-001/chatgpt-qr-code-plugin
cd chatgpt-qr-code-plugin
```

Create and activate a virtual environment and install the dependencies:

```bash
poetry shell
poetry install
```

Run the API backend locally:

```bash
poetry run start
```

Access the interactive API docs at http://localhost:8000/docs and test out the endpoints.
