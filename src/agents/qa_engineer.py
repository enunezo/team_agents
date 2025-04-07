from swarm import Agent
from functions.data_mock import get_test_status, get_bug_report
import asyncio

def fetch_test_status():
    test_data = get_test_status()
    return f"Test Summary:\nTotal: {test_data['total_tests']}, Passed: {test_data['passed']}, Failed: {test_data['failed']}, Blocked: {test_data['blocked']}"

def fetch_bug_report():
    bugs = get_bug_report()
    return "Bug Report:\n" + "\n".join([f"- {bug['bug']} (Status: {bug['status']}, Assigned to: {bug['assigned_to']})" for bug in bugs])

async def share_daily_update():
    print("Hola QA")
    await asyncio.sleep(1)  # Simulate a delay
    return "I completed test cases for the new feature, today I'll run regression tests, no blockers."


qa_engineer = Agent(
    name="QAEngineer",
    instructions="You manage test execution and report bugs.",
    #functions=[fetch_test_status, fetch_bug_report]
    functions=[share_daily_update]
)
