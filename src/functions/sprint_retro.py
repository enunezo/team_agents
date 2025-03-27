def sprint_retro(feedback: list) -> str:
    return "Sprint Retrospective:\n" + "\n".join(f"- {item}" for item in feedback)
