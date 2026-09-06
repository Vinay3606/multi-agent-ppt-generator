from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def generate_ppt_content(user_query, retrieved_results):

    context = ""

    for i, item in enumerate(retrieved_results, start=1):

        context += f"\n--- SOURCE {i} ---\n"
        context += item["content"]
        context += "\n"

    prompt = f"""
You are a strict presentation content generator.

Your job is to create presentation content ONLY from the provided company knowledge.

STRICT RULES:

1. Use ONLY facts explicitly present in the provided context.
2. Do NOT use outside knowledge.
3. Do NOT add assumptions or interpretations.
4. Do NOT create new benefits, achievements, statistics, clients, or capabilities.
5. Do NOT add marketing phrases unless they are explicitly present in the context.
6. Do NOT expand a sentence with new information.
7. If information is missing, simply skip that point.
8. Every bullet point must be directly supported by the provided context.
9. Do not invent company details.
10. Do not add contact information unless provided in the context.

USER REQUEST:
{user_query}

PROVIDED COMPANY KNOWLEDGE:
{context}

Create the requested presentation.

Return ONLY the presentation structure in the following format:

SLIDE 1
TITLE: ...
SUBTITLE: ...

SLIDE 2
TITLE: ...
CONTENT:
- ...
- ...
- ...

SLIDE 3
TITLE: ...
CONTENT:
- ...
- ...
- ...

Continue according to the user's requested number of slides.

Do not write any explanation before or after the slides.
"""

    response = llm.invoke(prompt)

    return response.content