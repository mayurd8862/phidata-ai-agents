from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="gemma2-9b-it"),
    # model=Ollama(id="mistral"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    monitoring=True,
    markdown=True,
)
web_agent.print_response("who is the current president of india", stream=True)
