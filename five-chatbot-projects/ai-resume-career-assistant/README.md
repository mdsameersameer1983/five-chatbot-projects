# AI Resume & Career Assistant

A responsive Flask chatbot powered by Google Gemini. The API key is read only from the `GEMINI_API_KEY` environment variable.

## Run locally

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Set your API key in the environment: PowerShell `$env:GEMINI_API_KEY="your-key"`; macOS/Linux `export GEMINI_API_KEY="your-key"`.
5. Optional: set `GEMINI_MODEL` (default `gemini-2.5-flash`).
6. Run `python app.py` and open http://localhost:5000.

## Deploy on Render

1. Push this app folder to a Git repository (or use the full extracted ZIP and set the service root directory to `ai-resume-career-assistant`).
2. Create a Render Web Service with Python runtime, build command `pip install -r requirements.txt`, and start command `gunicorn app:app`. `render.yaml` records these settings.
3. Add `GEMINI_API_KEY` as a secret environment variable in Render. Optionally set `GEMINI_MODEL`. Never commit the key.
4. Deploy and visit the service URL.

## Notes

Messages are sent to Google Gemini for responses. Avoid submitting sensitive personal information.  Before public use, add appropriate authentication, rate limiting, and a privacy policy.
