from pptx import Presentation
from pathlib import Path
import re


def parse_ppt_content(content):

    slides = []

    # SLIDE 1, SLIDE 2 etc ke basis par split
    slide_blocks = re.split(r"SLIDE\s+\d+", content)

    for block in slide_blocks:

        block = block.strip()

        if not block:
            continue

        title = ""
        subtitle = ""
        bullets = []

        lines = block.split("\n")

        mode = None

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if line.startswith("TITLE:"):

                title = line.replace("TITLE:", "").strip()
                mode = "title"

            elif line.startswith("SUBTITLE:"):

                subtitle = line.replace("SUBTITLE:", "").strip()
                mode = "subtitle"

            elif line.startswith("CONTENT:"):

                mode = "content"

            elif line.startswith("-"):

                bullet = line.replace("-", "", 1).strip()
                bullets.append(bullet)

        slides.append({
            "title": title,
            "subtitle": subtitle,
            "bullets": bullets
        })

    return slides


def replace_slide_text(slide, new_data):

    title_added = False
    subtitle_added = False
    bullet_index = 0

    for shape in slide.shapes:

        if not shape.has_text_frame:
            continue

        current_text = shape.text.strip()

        if not current_text:
            continue

        # First suitable text box → Title
        if not title_added and new_data["title"]:

            shape.text = new_data["title"]
            title_added = True
            continue

        # Second suitable text box → Subtitle
        if (
            title_added
            and not subtitle_added
            and new_data["subtitle"]
        ):

            shape.text = new_data["subtitle"]
            subtitle_added = True
            continue

        # Remaining text boxes → Bullet points
        if bullet_index < len(new_data["bullets"]):

            shape.text = new_data["bullets"][bullet_index]

            bullet_index += 1


def generate_ppt(template_path, validated_content, output_path):

    template_path = Path(template_path)
    output_path = Path(output_path)

    # Generated content parse karo
    slides_data = parse_ppt_content(validated_content)

    # Original template load karo
    presentation = Presentation(template_path)

    # Existing slides me content replace karo
    for index, slide in enumerate(presentation.slides):

        if index < len(slides_data):

            replace_slide_text(
                slide,
                slides_data[index]
            )

    # New PPT save karo
    presentation.save(output_path)

    return {
        "status": "success",
        "file": str(output_path),
        "total_slides": len(presentation.slides)
    }