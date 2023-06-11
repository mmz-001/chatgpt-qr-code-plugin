# ChatGPT Plugin

A simple ChatGPT plugin for creating QR codes. Check out my ChatGPT Plugin Development Tutorial to learn how to build this.

## Local setup

Dependencies are managed with [Poetry](https://python-poetry.org/), so install it if you already haven't:

```bash
pip install poetry
```

Clone the starter template and navigate to the project directory:

```bash
git clone https://github.com/mmz-001/chatgpt-qr-code-plugin
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

## Testing in ChatGPT

To test a localhost plugin in ChatGPT, follow these steps:

1. Run the API backend locally with `poetry run start`.
2. Visit [ChatGPT](https://chat.openai.com).
3. In the Model drop-down, select "Plugins," click on the plugins picker, and click "Plugin Store" at the bottom of the list. (If you don't see this you may not have access to plugins yet.)
4. Choose "Develop your own plugin".
5. Enter in `localhost:8000` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed for your Chat session! You can generate a QR code by asking "Generate a QR for https://chat.openai.com".
