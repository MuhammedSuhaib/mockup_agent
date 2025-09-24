from agents import Runner,set_tracing_export_api_key,trace
from openai.types.responses import ResponseTextDeltaEvent
from mockup_agents.aagents import General_Agent
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
Tracing_key = os.getenv('Tracing_key')
 
async def main():
    set_tracing_export_api_key(Tracing_key)

    with trace(workflow_name="mockup",disabled=False): 
        try:
            while True:
                output = Runner.run_streamed(starting_agent=General_Agent, input=input())
                async for event in output.stream_events():
                    if event.type == "raw_response_event" and isinstance(event.item, ResponseTextDeltaEvent):
                        print(event.item, end="", flush=True)
        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    asyncio.run(main())