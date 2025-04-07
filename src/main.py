import os
from dotenv import load_dotenv
import time
import openai
from openai import OpenAIError

from agents.scrum_master import scrum_master
from agents.qa_engineer import qa_engineer
from agents.product_owner import product_owner
from agents.developer import developer

from swarm.repl import run_demo_loop

all_agents = [scrum_master, developer, qa_engineer, product_owner]


# Load API key from .env file
load_dotenv()

#if __name__ == "__main__":
#    main()


if __name__ == "__main__":
    for agent in all_agents:
        print(f"Starting loop for {agent.name}...")  
        try:
            run_demo_loop(agent)  
        except OpenAIError as e:
            print(f"⚠️ OpenAI API Error: {e}. Retrying in 10 seconds...")
            time.sleep(10)
            run_demo_loop(agent)  # Retry once

