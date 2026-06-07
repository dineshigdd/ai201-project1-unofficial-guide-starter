"""
app.py — Milestone 5: Gradio user interface
=============================================

Thin web front-end over query.answer_question(). Lets a user type a question,
runs the grounded RAG pipeline, and shows the answer alongside the programmatic
list of source files the answer was drawn from.

Run `python app.py` and open http://localhost:7860
"""

from __future__ import annotations

import gradio as gr

from query import answer_question


def ask(question: str) -> tuple[str, str]:
    """Bridge the UI to the pipeline. Returns (answer, sources-as-bullets)."""
    question = (question or "").strip()
    if not question:
        return "Please enter a question.", ""

    result = answer_question(question)
    answer = result["answer"]
    sources = "\n".join(f"• {s}" for s in result["sources"]) or "• (none)"
    return answer, sources


def build_demo() -> gr.Blocks:
    with gr.Blocks(title="The Unofficial Guide") as demo:
        gr.Markdown(
            "# The Unofficial Guide\n"
            "Ask about Cal Poly Pomona CS professors, courses, study spots, and "
            "nearby food — answered **only** from student reviews."
        )

        inp = gr.Textbox(
            label="Your question",
            placeholder="e.g. What do students say about Professor Fuh Sang?",
            lines=2,
        )
        ask_btn = gr.Button("Ask", variant="primary")

        answer_out = gr.Textbox(label="Answer", lines=8)
        sources_out = gr.Textbox(label="Retrieved from", lines=6)

        # Trigger on both button click and Enter-key submission.
        ask_btn.click(ask, inputs=inp, outputs=[answer_out, sources_out])
        inp.submit(ask, inputs=inp, outputs=[answer_out, sources_out])

    return demo


if __name__ == "__main__":
    demo = build_demo()
    demo.launch(server_name="localhost", server_port=7860)
