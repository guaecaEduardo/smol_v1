from phoenix.otel import register
from openinference.instrumentation.smolagents import SmolagentsInstrumentor

register()
SmolagentsInstrumentor().instrument()


import os
import subprocess

from agentsTools.toolCodeNavigator import navigate_code
from agentsTools.toolRunMainErrorAnalyzer import toolRunMainErrorAnalyzer
from agentsTools.toolRunMainFixApplier import toolRunMainFixApplier
from agentsTools.toolReadFile import get_file_source
from agentsTools.toolApplyCodeFix import toolApplyCodeFix
from agentsTools.toolGetProjectContext import toolGetProjectContext
from agentsTools.toolUpdateFile import update_file


from models.openai_model import get_openai_model
from models.gemini_model import get_gemini_model

from smolagents import ToolCallingAgent

# model = get_openai_model()
model = get_gemini_model()

async def run_agent():
    # Create the agent with the tools
    agent = ToolCallingAgent(
        tools=[
            navigate_code,
            get_file_source,
            # toolApplyCodeFix,
            toolGetProjectContext,
            update_file,
            # toolRunMainErrorAnalyzer,
            # toolRunMainFixApplier
        ],
        max_steps=7,
        model=model,
        planning_interval=3 
    )

    # Run the project and capture any errors
    print("💡 Running main.py...")
    result = subprocess.run(
        ["python", "realproject/main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print("\n✅ STDOUT:\n", result.stdout)
    print("\n❌ STDERR:\n", result.stderr)

    if result.returncode != 0:
        error = result.stderr

        # code = await navigate_code(project_root=".")
        # if asyncio.iscoroutine(code):
        #     code = await code

        # Let the agent handle the task and the error
        task = f"""
        You are an experienced Python developer.
        Your task is to analyze the following error produced by running main.py:
        ```
        {error}
        ```
       If there are multiple possible solutions, you shall chose the best and fix the error
        """
        # The following is the code context:
        # ```
        # {code["code"]}
        # ```
        # Fix the error if possible and apply the fix.
        
        print("\n🤖 Starting agent task...")

        # Let the agent drive the task execution (ReAct loop)
        result = agent.run(task=task)

        print("\n✅ Agent result:\n", result)

    else:
        print("\n✅ Execution successful — no errors.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_agent())
