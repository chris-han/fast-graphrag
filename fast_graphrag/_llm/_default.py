__all__ = ['DefaultLLMService', 'DefaultEmbeddingService']

# from ._llm_openai import OpenAIEmbeddingService, OpenAILLMService
from ._llm_ollama import OllamaAIEmbeddingService, OllamaAILLMService

# class DefaultLLMService(OpenAILLMService):
#     pass
# class DefaultEmbeddingService(OpenAIEmbeddingService):
#     pass

class DefaultLLMService(OllamaAILLMService):
    pass
class DefaultEmbeddingService(OllamaAIEmbeddingService):
    pass
