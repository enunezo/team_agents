from functions.data_mock import manage_backlog

def sprint_planning():
    backlog = manage_backlog()
    return f"Sprint Planning:\n{backlog}\nPlease estimate the tasks."
