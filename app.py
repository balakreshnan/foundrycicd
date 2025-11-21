import asyncio
from datetime import datetime
import time
from azure.identity import DefaultAzureCredential
from agenticai import eval, agent_eval
from redteam import redteamagent
from dotenv import load_dotenv

load_dotenv()

def main() -> None:
    start_time = time.time()
    print(f"Starting evaluations at {datetime.now().isoformat()}\n")
    rs = eval()
    print("Agent Evaluation Results:")
    for r in rs:
        print(r)

    # Run Agent Evaluations
    print("Starting Agent Evaluations...\n")
    evalrs = agent_eval()
    print("Agent Evaluation Results:" , evalrs)

    # Run Red Team Evaluation
    print("\nStarting Red Team Evaluation...\n")
    asyncio.run(redteamagent())

    end_time = time.time()
    duration = end_time - start_time
    print(f"\nAll evaluations completed in {duration:.2f} seconds.")

if __name__ == "__main__":
    main()