from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def validate_content(generated_content, retrieved_results):

    # Original RAG context
    context = ""

    for i, item in enumerate(retrieved_results, start=1):

        context += f"\n--- SOURCE {i} ---\n"
        context += item["content"]
        context += "\n"


    prompt = f"""
You are a strict fact validation agent.

Your task is to validate presentation content against the provided source information.

SOURCE INFORMATION:
{context}


GENERATED PRESENTATION:
{generated_content}


STRICT RULES:

1. Keep only statements supported by the source information.
2. Remove unsupported claims.
3. Remove invented benefits, statistics, achievements, or capabilities.
4. Do not add new information.
5. Do not rewrite or improve the content.
6. Preserve the original slide structure as much as possible.
7. If a bullet point is not supported, remove it.
8. Return ONLY the validated presentation.

Do not explain your decisions.
"""

    response = llm.invoke(prompt)

    return response.content