import ollama


def generate_ppt_content(query, results, slide_count):

    context = "\n\n".join(
        result["content"]
        for result in results
    )

    prompt = f"""
You are generating content for a professional business PowerPoint presentation.

User Request:
{query}

Company Information:
{context}

Create EXACTLY {slide_count} slides.

Use ONLY the company information provided above.
Do not invent unsupported facts, statistics, achievements, or claims.

IMPORTANT: FOLLOW THIS EXACT SLIDE ORDER.

SLIDE 1
TITLE: Hyperion Cloud Defense
SUBTITLE: Short professional company or solution subtitle
DESCRIPTION: A concise executive overview of Hyperion Cloud Defense.

SLIDE 2
TITLE: Current Cybersecurity Challenges
DESCRIPTION: Explain the major enterprise cybersecurity or cloud security challenges from the document.

POINT 1 TITLE: Challenge heading
POINT 1 DESCRIPTION: Explanation based on company information.

POINT 2 TITLE: Challenge heading
POINT 2 DESCRIPTION: Explanation based on company information.

POINT 3 TITLE: Challenge heading
POINT 3 DESCRIPTION: Explanation based on company information.


SLIDE 3
TITLE: Hyperion Security Strategy
DESCRIPTION: Explain Hyperion's overall approach to solving enterprise security challenges.

POINT 1 TITLE: Strategy heading
POINT 1 DESCRIPTION: Explanation.

POINT 2 TITLE: Strategy heading
POINT 2 DESCRIPTION: Explanation.

POINT 3 TITLE: Strategy heading
POINT 3 DESCRIPTION: Explanation.


SLIDE 4
TITLE: Key Capabilities
DESCRIPTION: Introduce the major technical capabilities of Hyperion Cloud Defense.

POINT 1 TITLE: Capability heading
POINT 1 DESCRIPTION: Explanation.

POINT 2 TITLE: Capability heading
POINT 2 DESCRIPTION: Explanation.

POINT 3 TITLE: Capability heading
POINT 3 DESCRIPTION: Explanation.


SLIDE 5
TITLE: Implementation Approach
DESCRIPTION: Explain deployment, assessment, roadmap, or implementation information from the document.

POINT 1 TITLE: Implementation step
POINT 1 DESCRIPTION: Explanation.

POINT 2 TITLE: Implementation step
POINT 2 DESCRIPTION: Explanation.

POINT 3 TITLE: Implementation step
POINT 3 DESCRIPTION: Explanation.


SLIDE 6
TITLE: Business Benefits
DESCRIPTION: Explain the operational, security, or business benefits supported by the document.

POINT 1 TITLE: Benefit heading
POINT 1 DESCRIPTION: Explanation.

POINT 2 TITLE: Benefit heading
POINT 2 DESCRIPTION: Explanation.

POINT 3 TITLE: Benefit heading
POINT 3 DESCRIPTION: Explanation.


SLIDE 7
TITLE: Future Direction
DESCRIPTION: Summarize future capabilities, strategic direction, or next steps mentioned in the document.

POINT 1 TITLE: Future focus
POINT 1 DESCRIPTION: Explanation.

POINT 2 TITLE: Future focus
POINT 2 DESCRIPTION: Explanation.

POINT 3 TITLE: Future focus
POINT 3 DESCRIPTION: Explanation.


STRICT OUTPUT RULES:

- Return exactly {slide_count} slides.
- Start directly with SLIDE 1.
- Do not write anything before SLIDE 1.
- Follow the slide order above exactly.
- Do not move Slide 1 content to another slide.
- Do not repeat the same information across multiple slides.
- Do not use markdown symbols.
- Do not use *, **, #, bullets, or extra formatting.
- Every POINT TITLE must have a POINT DESCRIPTION.
- Keep titles under 8 words when possible.
- Keep descriptions concise and professional.
- Keep point descriptions under 25 words.
- Use meaningful explanations, not keywords only.
- Use only information supported by the company document.
"""

    response = ollama.generate(
        model="llama3.2:3b",
        prompt=prompt
    )

    return response["response"]