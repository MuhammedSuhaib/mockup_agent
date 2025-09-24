from agents import Agent, ModelSettings, RunContextWrapper, StopAtTools , function_tool
from configs.config import model_config
@function_tool
def bank(query: str) -> str:
    '''Handles banking-related queries.'''
    if "balance" in query.lower():
        return "Checking balance..."
    elif "transfer" in query.lower():
        return "Transferring funds..."
    else:
        return "I'm sorry, I can't assist with that."
    
# General Agent — decides who should handle the query
General_Agent = Agent(
    name="General_Agent",
    instructions=(
        "You are General_Agent, an intelligent and helpful assistant. "
        "Reply in the shortest way"
        " Reply to all kinds of queries. no matter what the query is, you must answer it. but dont halucinate or make up information. if you dont know the answer, just say 'i dont know'."
    ),
    model=model_config,
    tools=[bank],
    # tool_use_behavior="stop_on_first_tool",
    # model_settings=ModelSettings(tool_choice="none")
)
