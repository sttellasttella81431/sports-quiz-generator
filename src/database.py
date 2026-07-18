import json
import chromadb
from chromadb.utils import embedding_functions

# Create SentenceTransformer embedding function
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Create persistent ChromaDB client
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="sports_facts",
    embedding_function=embedding_function
)


def setup_and_populate_db():
    """Load sports facts from JSON into ChromaDB."""

    with open("data/sports_facts.json", "r", encoding="utf-8") as file:
        facts = json.load(file)

    existing = collection.count()

    if existing > 0:
        return

    for index, item in enumerate(facts):
        collection.add(
            ids=[str(index)],
            documents=[item["fact"]],
            metadatas=[{"sport": item["sport"]}]
        )


def query_historic_facts(sport, query_text, n_results=2):
    """Retrieve historical facts."""

    results = collection.query(
        query_texts=[query_text],
        n_results=n_results,
        where={"sport": sport}
    )

    if results["documents"]:
        return results["documents"][0]

    return []