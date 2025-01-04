from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    monitoring=True,
    markdown=True,
)
finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)
