from langchain_ollama import ChatOllama
import re


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def validate_content(generated_content, retrieved_results):

    context = ""

    for i, item in enumerate(retrieved_results, start=1):

        context += f"\n--- SOURCE {i} ---\n"
        context += item["content"]
        context += "\n"


    prompt = f"""
You are a fact validation agent.

Validate the presentation against the source information.

SOURCE INFORMATION:
{context}

PRESENTATION:
{generated_content}

RULES:

1. Remove or correct unsupported factual claims only.
2. Do not add new information.
3. Preserve the EXACT output structure.
4. Never remove SLIDE markers.
5. Never remove TITLE:, SUBTITLE:, DESCRIPTION: labels.
6. Never remove POINT X TITLE: labels.
7. Never remove POINT X DESCRIPTION: labels.
8. Return ONLY the presentation content.
9. Do not add explanations before or after the presentation.

The output must remain machine-readable in the same format.
"""


    response = llm.invoke(prompt)

    validated = response.content.strip()


    # --------------------------------------------------
    # SAFETY CHECK
    # If validator destroys presentation structure,
    # use original generated content instead.
    # --------------------------------------------------

    original_slides = len(
        re.findall(
            r"SLIDE\s+\d+",
            generated_content,
            re.IGNORECASE
        )
    )

    validated_slides = len(
        re.findall(
            r"SLIDE\s+\d+",
            validated,
            re.IGNORECASE
        )
    )


    # Structure damaged → fallback to original content
    if (
        validated_slides != original_slides
        or "TITLE:" not in validated.upper()
    ):

        print(
            "Validation changed structure. "
            "Using original generated content."
        )

        return generated_content


    return validated