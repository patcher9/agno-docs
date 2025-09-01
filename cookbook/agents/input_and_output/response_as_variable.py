from typing import Iterator  # noqa
from rich.pretty import pprint
from agno.agent import Agent, RunOutput
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=["Use tables where possible"],
    markdown=True,
)

run_response: RunOutput = agent.run("What is the latest news about NVDA")
pprint(run_response)

# run_response_strem: Iterator[RunOutputEvent] = agent.run("What is the latest news about NVDA", stream=True)
# for response in run_response_strem:
#     pprint(response)
