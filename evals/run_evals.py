import json
from pathlib import Path

from app.llm_service import generate_response

THRESHOLD = 0.66
CASES = json.loads((Path(__file__).parent / "test_cases.json").read_text())


def run_evals() -> float:
    passed = 0
    for case in CASES:
        answer = generate_response(case["input"]).lower()
        ok = case["expected_keyword"].lower() in answer
        print(f"[{'PASS' if ok else 'FAIL'}] {case['input']}")
        passed += ok
    score = passed / len(CASES)
    print(f"Eval score: {score:.2f}")
    return score


if __name__ == "__main__":
    if run_evals() < THRESHOLD:
        raise SystemExit("LLM evaluation failed")
