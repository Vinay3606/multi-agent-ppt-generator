import streamlit as st
from pathlib import Path

from agents.document_agent import document_agent
from agents.vector_store import create_vector_store, search_vector_store
from agents.content_generator import generate_ppt_content
from agents.validation_agent import validate_content
from agents.ppt_generator import generate_ppt


st.set_page_config(
    page_title="Document AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Document AI")

st.subheader("Multi-Agent AI System for Document-Based PPT Generation")

st.divider()


col1, col2 = st.columns(2)

with col1:
    pdf_file = st.file_uploader(
        "📄 Upload Company Document",
        type="pdf"
    )

with col2:
    ppt_file = st.file_uploader(
        "📊 Upload PPT Template",
        type="pptx"
    )


query = st.text_area(
    "💬 What presentation do you want to create?",
    placeholder="Create a 10-slide presentation about AI services"
)


if st.button("🚀 Generate Presentation"):

    if not pdf_file or not ppt_file or not query:
        st.warning("Please upload both files and enter your requirement.")
        st.stop()

    Path("uploads").mkdir(exist_ok=True)
    Path("output").mkdir(exist_ok=True)

    pdf_path = f"uploads/{pdf_file.name}"
    ppt_path = f"uploads/{ppt_file.name}"

    with open(pdf_path, "wb") as f:
        f.write(pdf_file.getbuffer())

    with open(ppt_path, "wb") as f:
        f.write(ppt_file.getbuffer())

    with st.spinner("🤖 AI Agents are working..."):

        document = document_agent(pdf_path)

        index, chunks = create_vector_store(document["content"])

        results = search_vector_store(query, index, chunks, top_k=5)

        content = generate_ppt_content(query, results)

        validated_content = validate_content(content, results)

        output_path = "output/Generated_Presentation.pptx"

        generate_ppt(
            ppt_path,
            validated_content,
            output_path
        )

    st.success("🎉 Presentation generated successfully!")

    with open(output_path, "rb") as f:
        st.download_button(
            "⬇️ Download Generated PPT",
            f,
            file_name="Generated_Presentation.pptx"
        )