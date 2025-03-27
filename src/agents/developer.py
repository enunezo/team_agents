from swarm import Agent
from functions.data_mock import get_dev_task_info, get_technical_requirements

def fetch_dev_task():
    task_info = get_dev_task_info()
    return f"Task: {task_info['ticket']}\nStatus: {task_info['status']}\nImpediments: {', '.join(task_info['impediments'])}"

def fetch_release_info():
    task_info = get_dev_task_info()
    return "Release History:\n" + "\n".join(task_info["release_history"])

def fetch_technical_requirements():
    technical_requirements = get_technical_requirements()
    return technical_requirements


developer = Agent(
    name="Developer",
    instructions="You track task progress, releases, and technical blockers.",
    functions=[fetch_dev_task, fetch_release_info, fetch_technical_requirements]
)
