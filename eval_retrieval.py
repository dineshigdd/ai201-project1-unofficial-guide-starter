"""Quick harness: run the 5 evaluation-plan questions through retrieve()."""
from embed import retrieve

QUESTIONS = [
    "What is considered the hardest core Computer Science course to pass at Cal Poly Pomona?",
    "Which Computer Science professors do students recommend avoiding at Cal Poly Pomona?",
    "Who are considered the best Computer Science professors at Cal Poly Pomona to take algorithm and data structures?",
    "What is the best place to study on campus at Cal Poly Pomona according to students?",
    "What are the best three off-campus dining places near Cal Poly Pomona based on top student reviews?",
]

for i, q in enumerate(QUESTIONS, 1):
    print(f"\n=== Q{i}: {q}")
    for r in retrieve(q):
        print(f"  score={r['score']:.3f}  {r['source']:<22} subject={r['subject']}")
        print(f"     {r['text'][:110]}")
