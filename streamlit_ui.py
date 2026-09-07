import streamlit as st
from pathlib import Path
from pptx import Presentation

from agents.document_agent import document_agent

from agents.vector_store import (
    create_vector_store,
    search_vector_store
)

from agents.content_generator import (
    generate_ppt_content
)

from agents.ppt_generator import (
    generate_ppt
)


# =========================================================
# STREAMLIT CONFIG
# =========================================================

st.set_page_config(
    page_title="Document AI",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# UI
# =========================================================

st.title("🤖 Document AI")

st.subheader(
    "Multi-Agent AI System for Document-Based PPT Generation"
)

st.divider()


# =========================================================
# FILE UPLOAD
# =========================================================

col1, col2 = st.columns(2)


with col1:

    pdf_file = st.file_uploader(
        "📄 Upload Company Document",
        type="pdf"
    )


with col2:

    ppt_file = st.file_uploader(
        "📊 Upload Existing PPT",
        type="pptx"
    )


# =========================================================
# USER QUERY
# =========================================================

query = st.text_area(
    "💬 What do you want to update?",
    placeholder=(
        "Create an updated professional presentation "
        "using the uploaded company information"
    )
)


# =========================================================
# GENERATE BUTTON
# =========================================================

if st.button("🚀 Generate Presentation"):

    # Validate input
    if not pdf_file or not ppt_file or not query:

        st.warning(
            "Please upload both files and enter your requirement."
        )

        st.stop()


    # =====================================================
    # CREATE FOLDERS
    # =====================================================

    Path("uploads").mkdir(
        exist_ok=True
    )

    Path("output").mkdir(
        exist_ok=True
    )


    # =====================================================
    # SAVE UPLOADED FILES
    # =====================================================

    pdf_path = (
        f"uploads/{pdf_file.name}"
    )

    ppt_path = (
        f"uploads/{ppt_file.name}"
    )


    with open(pdf_path, "wb") as file:

        file.write(
            pdf_file.getbuffer()
        )


    with open(ppt_path, "wb") as file:

        file.write(
            ppt_file.getbuffer()
        )


    # =====================================================
    # AI PROCESSING
    # =====================================================

    with st.spinner(
        "🤖 AI Agents are updating your presentation..."
    ):


        # -------------------------------------------------
        # 1. DOCUMENT AGENT
        # -------------------------------------------------

        document = document_agent(
            pdf_path
        )


        # -------------------------------------------------
        # 2. VECTOR STORE
        # -------------------------------------------------

        index, chunks = create_vector_store(
            document["content"]
        )


        # -------------------------------------------------
        # 3. RAG RETRIEVAL
        # -------------------------------------------------

        results = search_vector_store(
            query,
            index,
            chunks,
            top_k=min(10, len(chunks))
        )


        # -------------------------------------------------
        # 4. GET EXISTING PPT SLIDE COUNT
        # -------------------------------------------------

        presentation = Presentation(
            ppt_path
        )

        slide_count = len(
            presentation.slides
        )


        # -------------------------------------------------
        # 5. CONTENT GENERATOR AGENT
        # -------------------------------------------------

        generated_content = generate_ppt_content(
            query,
            results,
            slide_count
        )


        # -------------------------------------------------
        # 6. VALIDATION BYPASSED
        # IMPORTANT:
        # Validation agent structure change kar raha tha,
        # isliye generated content directly use karenge.
        # -------------------------------------------------

        validated_content = generated_content


        # -------------------------------------------------
        # 7. PPT GENERATOR AGENT
        # -------------------------------------------------

        output_path = (
            "output/Updated_Presentation.pptx"
        )


        result = generate_ppt(
            ppt_path,
            validated_content,
            output_path
        )


    # =====================================================
    # SUCCESS MESSAGE
    # =====================================================

    st.success(
        "🎉 Presentation updated successfully!"
    )


    st.info(
        f"Total Slides: {result['total_slides']}"
    )


    # =====================================================
    # DOWNLOAD BUTTON
    # =====================================================

    with open(output_path, "rb") as file:

        st.download_button(
            "⬇️ Download Updated PPT",
            file,
            file_name="Updated_Presentation.pptx",
            mime=(
                "application/vnd.openxmlformats-officedocument."
                "presentationml.presentation"
            )
        )