from agents import (
    Agent,
    RunContextWrapper,
    function_tool,
    ToolsToFinalOutputResult,
    FunctionToolResult,
)
from configs.config import model_config


@function_tool
def bank(query: str) -> str:
    """Handles banking-related queries."""
    if "balance" in query.lower():
        return "Your balance is $2,350"
    elif "transfer" in query.lower():
        return "Transfer of $500 completed"
    else:
        return "I'm sorry, I can't assist with that."


@function_tool
def weather(location: str) -> str:
    """Handles weather queries."""
    if "paris" in location.lower():
        return "Sunny, 23°C"
    elif "london" in location.lower():
        return "Rainy, 16°C"
    else:
        return "No weather data."


def tools_to_final_output(
    ctx: RunContextWrapper, results: list[FunctionToolResult]
) -> ToolsToFinalOutputResult:
    """Decide whether to stop or let LLM continue."""
    if not results:
        return ToolsToFinalOutputResult(is_final_output=False)

    # If banking → return directly (sensitive info)
    if results[0].tool.name == "bank":
        return ToolsToFinalOutputResult(
            is_final_output=True,
            final_output=results[0].output,
        )

    # If weather → let LLM continue to rephrase nicely
    if results[0].tool.name == "weather":
        # Don't finalize yet, let LLM generate response
        return ToolsToFinalOutputResult(is_final_output=False)

    return ToolsToFinalOutputResult(is_final_output=False)


General_Agent = Agent(
    name="General_Agent",
    instructions=(
        "You are General_Agent. Always reply concisely. "
    ),
    model=model_config,
    tools=[bank, weather],
    tool_use_behavior=tools_to_final_output,
)
