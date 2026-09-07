from document_agent import document_agent
from vector_store import create_vector_store, search_vector_store
from content_generator import generate_ppt_content
from validation_agent import validate_content
from ppt_generator import generate_ppt


# -----------------------------------------
# Read Updated PDF
# -----------------------------------------

document = document_agent(
    "Hyperion_Cloud_Defense_Updated_Test_Document.pdf"
)

text = document["content"]


# -----------------------------------------
# Create Vector Store
# -----------------------------------------

print("Creating vector store...")

index, chunks = create_vector_store(text)


# -----------------------------------------
# User Request
# -----------------------------------------

query = """
Create a professional 7-slide presentation about Hyperion Cloud Defense
using the uploaded company document. Use only the provided information
and include meaningful explanations.
"""


# -----------------------------------------
# Search Relevant Information
# -----------------------------------------

print("Retrieving information...")

results = search_vector_store(
    query,
    index,
    chunks,
    top_k=len(chunks)
)


# -----------------------------------------
# Generate Content
# -----------------------------------------

print("Generating content...")

content = generate_ppt_content(
    query,
    results,
    slide_count=7
)


print("\n" + "=" * 60)
print("GENERATED CONTENT")
print("=" * 60)

print(content)


# -----------------------------------------
# Validate Content
# -----------------------------------------

print("\nValidating content...")

validated_content = validate_content(
    content,
    results
)


print("\n" + "=" * 60)
print("VALIDATED CONTENT")
print("=" * 60)

print(validated_content)


# -----------------------------------------
# Generate PPT
# -----------------------------------------

print("\nGenerating PPT...")

result = generate_ppt(
    "Hyperion Cloud Defense Presentation.pptx",
    validated_content,
    "Generated_Hyperion_Presentation.pptx"
)


print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)

print(result)