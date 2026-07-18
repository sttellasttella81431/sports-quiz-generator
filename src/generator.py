from openai import OpenAI
from src.config import OPENAI_API_KEY
from src.database import query_historic_facts
from src.search import get_live_news_context


def compile_quiz_data(sport, difficulty):

    db_query = f"{sport} history cup championships rules records"

    db_results = query_historic_facts(
        sport=sport,
        query_text=db_query,
        n_results=2
    )

    db_context = "\n".join(db_results) if db_results else "No offline historic data recorded."

    web_context = get_live_news_context(sport)

    unified_context = (
        "=== HISTORICAL FACTS ===\n"
        f"{db_context}\n\n"
        "=== LIVE INTERNET NEWS ===\n"
        f"{web_context}"
    )

    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is required to generate quizzes.")

    client = OpenAI(api_key=OPENAI_API_KEY)

    system_instruction = (
        "You are an expert sports quiz creator. Your job is to write multiple-choice quizzes "
        "relying strictly on the provided Context. Avoid hallucinations. Do not use facts not "
        "found in the Context below. If facts are scarce, make do with what you have, "
        "but keep details completely accurate to the text context.\n\n"
        f"CONTEXT DETAILS:\n{unified_context}"
    )

    user_prompt = (
        f"Generate exactly 3 unique multiple-choice questions for the sport: {sport}.\n"
        f"Difficulty target: {difficulty}.\n\n"
        "Format each question exactly as follows so my program can parse it:\n"
        "Question: [Question text here]\n"
        "A) [Option A]\n"
        "B) [Option B]\n"
        "C) [Option C]\n"
        "D) [Option D]\n"
        "Correct Answer: [Single Letter, e.g., A]\n"
        "Explanation: [Detailed background reasoning quoting from the context details]\n"
        "---"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content, unified_context