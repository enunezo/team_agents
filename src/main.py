from agents.scrum_master import scrum_master
from agents.qa_engineer import qa_engineer
from agents.product_owner import product_owner
from agents.developer import developer

# Available agents
agents = {
    "scrum": scrum_master,
    "qa": qa_engineer,
    "po": product_owner,
    "dev": developer
}

# Available actions for each agent
actions = {
    "scrum": ["fetch_sprint_status", "fetch_impediments", "facilitate_daily_meeting"],
    "qa": ["fetch_test_status", "fetch_bug_status"],
    "po": ["fetch_backlog", "fetch_user_stories"],
    "dev": ["fetch_task_status"]
}

def main():
    print("\n🚀 **INTERACTIVE SCRUM ASSISTANT** 🚀")
    print("Type 'exit' anytime to quit.")

    while True:
        print("\n👥 Choose an agent: (scrum, qa, po, dev)")
        agent_choice = input("> ").strip().lower()

        if agent_choice == "exit":
            print("👋 Exiting...")
            break

        if agent_choice not in agents:
            print("⚠️ Invalid agent. Try again.")
            continue

        print(f"\n✅ {agent_choice.upper()} selected. Available actions:")
        for func in agents[agent_choice].functions:
            print(f"  - {func.__name__}")  # Print available functions

        print("\n📌 Type an action:")
        action_choice = input("> ").strip()

        if action_choice == "exit":
            print("👋 Exiting...")
            break

        # ✅ Find the correct function in the agent’s list
        func = next((f for f in agents[agent_choice].functions if f.__name__ == action_choice), None)

        if func:
            if action_choice == "redirect_query":
                query_type = input("📌 Enter query type (technical_requirements, product, tests): ").strip()
                response = func(query_type)  # ✅ Pass the required argument
            else:
                response = func()  # Keep other functions as they are
                print("\n📝 Response:\n", response)
        else:
            print(f"⚠️ Action '{action_choice}' not found in {agent_choice}. Try again.")

if __name__ == "__main__":
    main()
