def sprint_review(completed_tasks: list) -> str:
    return f"Sprint Review:\nCompleted tasks:\n" + "\n".join(f"- {task}" for task in completed_tasks)
