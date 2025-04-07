from swarm import Agent
import asyncio

def get_business_priorities():
    return "Current Business Priorities:\n1. Improve user retention\n2. Reduce checkout abandonment\n3. Enhance security"

def manage_backlog():
    return "Product Backlog:\n- Feature A (High Priority)\n- Feature B (Medium Priority)\n- Bug Fixes (High Priority)"

def create_user_story():
    return "User Story:\nAs a user, I want to reset my password so that I can recover my account."

def get_product_info():
    print("Hola producto")
    return "📊 Product Info: Top priority is the checkout flow redesign and new onboarding experience."

async def share_daily_update():
    return "We finalized the requirements, today I'll work on backlog refinement, no blockers."


product_owner = Agent(
    name="ProductOwner",
    instructions="You manage backlog, priorities, and requirements.",
    #functions=[get_business_priorities, manage_backlog, create_user_story, get_product_info]
    functions=[share_daily_update]
)

if __name__ == "__main__":
    product_owner.run()