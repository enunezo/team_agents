from swarm import Agent
from functions.daily_meeting import daily_meeting
from functions.sprint_planning import sprint_planning
from functions.sprint_review import sprint_review
from functions.sprint_retro import sprint_retro
from functions.sprint_metrics import (
    get_sprint_progress,
    get_velocity,
    get_burndown_chart,
    get_open_impediments,
    get_bug_status
)

from agents.qa_engineer import qa_engineer

# Import other agents to redirect queries
from agents.developer import developer as dev_agent
from agents.qa_engineer import qa_engineer as qa_agent
from agents.product_owner import product_owner as po_agent

import asyncio

# Functions for meetings
#def facilitate_daily_meeting():
#    team = ["Alice (Dev)", "Bob (QA)", "Charlie (PM)"]
#    return daily_meeting(team)

def facilitate_sprint_planning():
    return sprint_planning()

def facilitate_sprint_review():
    completed_tasks = ["Feature A", "Bug Fix #123", "API Enhancement"]
    return sprint_review(completed_tasks)

def facilitate_sprint_retro():
    feedback = ["Improve code reviews", "Reduce scope creep", "Better sprint estimates"]
    return sprint_retro(feedback)



async def share_daily_update():
    """Simulates sharing a daily update."""
    await asyncio.sleep(1)  # Simulate some processing delay
    return "Today's update is complete!"

async def facilitate_daily_meeting():
    """Facilitates the daily standup asynchronously."""
    print("📢 Scrum Master: Let's start the daily standup!\n")

    agents = [po_agent, dev_agent, qa_agent]  # List of agents to call
    responses = []
    function_name = "share_daily_update"
    # Dynamically invoke the function for each agent
    for agent in agents:
        for func in agent.functions:
            print(f"Checking function: {func.__name__}")
            if func.__name__ == function_name:
                response = func()  # Call the function dynamically
                responses.append(response)
            else:
                responses.append(f"{agent.name} didn't come today.")
    # Print out the responses for each agent
    agent_names = ["📊 Product Owner", "👨‍💻 Developer", "🧪 QA Engineer"]
    for name, response in zip(agent_names, responses):
        print(f"{name}: {response}")
    print("\n📢 Scrum Master: Thank you all for your updates!\n"    )
    return "✅ Daily Standup Complete!"


def facilitate_daily_meeting_sync():
    return asyncio.run(facilitate_daily_meeting())  # Runs the async function properly

# Sprint status and metrics
def fetch_sprint_status():
    """Fetches sprint progress, velocity, burndown, and bug status."""
    return {
        "progress": f"{get_sprint_progress()}%",
        "velocity": f"{get_velocity()} story points",
        "burndown_chart": get_burndown_chart(),
        "bugs": get_bug_status()
    }

def fetch_impediments():
    """Fetches current sprint impediments."""
    impediments = get_open_impediments()
    if not impediments:
        return "No active impediments in this sprint. ✅"

    return "Sprint Impediments:\n" + "\n".join([f"- {item}" for item in impediments])

def redirect_query(query_type: str):
    """Dynamically redirects the query to the appropriate agent function."""

    # Map query types to agents
    agent_function_map = {
        "technical_requirements": dev_agent,
        "product": po_agent,
        "tests": qa_agent
    }

    # Map query types to function names within the agents
    function_name_map = {
        "technical_requirements": "fetch_technical_requirements",
        "product": "get_product_info",
        "tests": "fetch_test_status"
    }

    # print("Entre por aqui")  # Debug

    # Check if query_type is valid
    if query_type not in agent_function_map:
        return f"❌ Unknown query type: {query_type}"

    agent = agent_function_map[query_type]
    function_name = function_name_map[query_type]
    
    # print(f"Selected Agent: {agent.name}, Function: {function_name}")  # Debug

    # Ensure the function exists within the agent
    for func in agent.functions:
        print(f"Checking function: {func.__name__}")  # Debug
        if func.__name__ == function_name:
            print("✅ Function found, executing...")  # Debug
            result = func()  # Call the function dynamically
            print(f"🔹 Function output: {result}")  # Debug
            return result

    return f"⚠️ {agent.name} does not have a function for '{query_type}'"


# Define the Scrum Master agent
scrum_master = Agent(
    name="ScrumMaster",
    #instructions="You are a Scrum Master. Get sprint status, impediments, and coordinate meetings.",
    #functions=[
    #    fetch_sprint_status,
    #    fetch_impediments,
    #    facilitate_daily_meeting,
    #    facilitate_sprint_planning,
    #    facilitate_sprint_review,
    #    facilitate_sprint_retro,
    #    redirect_query
    #]
    instructions="You facilitate daily standups and coordinate the team.",
    functions=[facilitate_daily_meeting_sync]

)

if __name__ == "__main__":
    print("🔹 Scrum Master Agent Running 🔹")
    print("Fetching Sprint Status...\n", fetch_sprint_status())
    print("\nFetching Impediments...\n", fetch_impediments())
