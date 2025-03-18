# FIX APPLIED:
# from .src.projectAgentsTools.toolClassifier import RequirementClassifierTool

# This is the main file for the project. It will be the entry point for the project.
# It will import the necessary tools and agents and run the main function.

#system imports
import json

#import tools
from projectAgentsTools.toolClassifier import RequirementClassifierTool
from projectAgentsTools.toolUpdateFeature import FeatureUpdateTool

#import agents
from projectAgents import RequirementClassifierAgent

from smolagents import ToolCallingAgent, run_agent


async def main():
    with open("spec/C1specification.json", "r", encoding="utf-8") as f:
        requirements = json.load(f)

    initial_state = {
        "requirements": requirements,
        "current_index": 0,
        "done": False
    }

    agent = RequirementClassifierAgent(
        tools=[
            RequirementClassifierTool("C1features.json", "C1context.json"),
            FeatureUpdateTool("C1features.json", "C1spec.json")
        ],
        model=model
    )

    result = await run_agent(agent, initial_state)
    print(json.dumps(result["requirements"], indent=2))

if __name__ == "__main__":
    print("Hello, World!")
    import asyncio
    asyncio.run(main())
