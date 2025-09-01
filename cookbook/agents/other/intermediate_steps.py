from typing import Iterator

from agno.agent import Agent, RunOutputEvent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from rich.pretty import pprint

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

run_stream: Iterator[RunOutputEvent] = agent.run(
    "What is the latest news about NVDA", stream=True, stream_intermediate_steps=True
)
for chunk in run_stream:
    pprint(chunk.to_dict())
    print("---" * 20)
