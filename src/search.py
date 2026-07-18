from duckduckgo_search import DDGS


def get_live_news_context(sport_name):
    """
    Search DuckDuckGo for recent sports news.
    Returns the top 3 snippets as a single string.
    """

    query = f"{sport_name} latest tournament results championship winners news"

    snippets = []

    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=3)

            for i, result in enumerate(results, start=1):
                title = result.get("title", "")
                body = result.get("body", "")

                snippets.append(
                    f"Web Source {i}\n"
                    f"Title: {title}\n"
                    f"Snippet: {body}"
                )

    except Exception as e:
        return f"Web search unavailable: {e}"

    return "\n\n".join(snippets)