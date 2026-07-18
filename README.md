# AI Sports Quiz Generator

A Streamlit app that generates sports quizzes using:
- local ChromaDB historical facts
- live DuckDuckGo search snippets
- OpenAI chat completions for quiz creation

## Quick start

1. Clone the repo.
2. Copy `.env.example` to `.env` and add your OpenAI API key.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Environment variables

Create a `.env` file with:
```ini
OPENAI_API_KEY=your_openai_api_key_here
```

## Deployment

### Streamlit Community Cloud
1. Push this repo to GitHub.
2. Go to https://share.streamlit.io and connect your GitHub account.
3. Create a new app using this repo.
4. Set the app file to `app.py`.
5. Add your secret in Streamlit dashboard:
   - `OPENAI_API_KEY`

### Notes
- Do not commit `.env` or `chroma_db/`.
- The app will rebuild the local ChromaDB from `data/sports_facts.json` on startup.

## App behavior

- Select a sport and difficulty.
- Click **Generate Quiz**.
- The app combines historical facts with live news snippets and requests quiz content from OpenAI.
