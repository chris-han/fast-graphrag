from fast_graphrag import GraphRAG, DefaultEmbeddingService,DefaultLLMService
# from fast_graphrag import OllamaAILLMService
# from fast_graphrag import OpenAIEmbeddingService, OpenAILLMService


DOMAIN = "Analyze this story and identify the characters. Focus on how they interact with each other, the locations they explore, and their relationships."

EXAMPLE_QUERIES = [
    "What is the significance of Christmas Eve in A Christmas Carol?",
    "How does the setting of Victorian London contribute to the story's themes?",
    "Describe the chain of events that leads to Scrooge's transformation.",
    "How does Dickens use the different spirits (Past, Present, and Future) to guide Scrooge?",
    "Why does Dickens choose to divide the story into \"staves\" rather than chapters?"
]

ENTITY_TYPES = ["Character", "Animal", "Place", "Object", "Activity", "Event"]

# Assuming OllamaAILLMService is defined and is a valid implementation similar to how DefaultLLMService is implemented
llm_service = DefaultLLMService(
    model="llama3.2",
    base_url="http://localhost:11434/v1"  # This URL should be the endpoint for Ollama AI's service
)

# Define other services similarly if you want to customize those as well, 
# otherwise the defaults will be used.
embedding_service = DefaultEmbeddingService(
    model="nomic-embed-text",
    base_url="http://localhost:11434/api" 
    )

config = GraphRAG.Config(
    llm_service = llm_service,
    embedding_service = embedding_service    # Add other necessary configurations here if required
)

grag = GraphRAG(
    working_dir="./book_example",
    domain=DOMAIN,
    example_queries="\n".join(EXAMPLE_QUERIES),
    entity_types=ENTITY_TYPES,
    config=config
)

with open("./book.txt") as f:
    grag.insert(f.read())

re = grag.query("Who is Scrooge?").response
print(re)
