from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List


class AgentState(TypedDict):
    user_query: str
    files: List[str]
    next_agent: str


def supervisor(state: AgentState):
    query = state["user_query"].lower()

    # Simple routing logic for now
    if "research" in query or "latest" in query or "trend" in query:
        next_agent = "research_agent"

    elif "ppt" in query or "presentation" in query:
        next_agent = "ppt_agent"

    elif "document" in query or "report" in query or "proposal" in query:
        next_agent = "document_agent"

    else:
        next_agent = "research_agent"

    return {"next_agent": next_agent}


def create_supervisor_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node("supervisor", supervisor)

    workflow.add_edge(START, "supervisor")
    workflow.add_edge("supervisor", END)

    return workflow.compile()