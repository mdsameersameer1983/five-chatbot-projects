# Five Chatbot Projects

Five self-contained Flask + Gemini starter apps. Each folder includes its own source, requirements, Render configuration, and setup guide. No API keys are included.

- `ai-study-assistant`
- `smart-shopping-assistant`
- `ai-coding-helper`
- `health-information-chatbot`
- `ai-resume-career-assistant`

Read each app’s README for local and Render setup. Set `GEMINI_API_KEY` as an environment secret. `GEMINI_MODEL` optionally overrides the default `gemini-2.5-flash`. Flask serves each app locally; Gunicorn is used on Render.
