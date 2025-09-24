from agents import Runner, set_tracing_export_api_key, trace
from agents.run import AgentRunner, set_default_agent_runner
from openai.types.responses import ResponseTextDeltaEvent
from mockup_agents.aagents import General_Agent
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

class MockAgent(AgentRunner):
    async def run(self, starting_agent, input, **kwargs):
        return await super().run(starting_agent, input, **kwargs)
        return "that’s my taste and nothing else feels right"
set_default_agent_runner(MockAgent())

Tracing_key = os.getenv("Tracing_key")
async def main():
    set_tracing_export_api_key(Tracing_key)
    with trace(workflow_name="mockup", disabled=False):
        try:
            while True:
                output = await Runner.run(starting_agent=General_Agent, input=input())
                print(output)
        except KeyboardInterrupt:
            print("\nExiting...")
if __name__ == "__main__":
    asyncio.run(main())
