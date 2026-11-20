########################################################################
# LangGraph Autonomous Agent

from typing import TypedDict
from langgraph.graph import StateGraph
from agents.tools import *

class AgentState(TypedDict):
    record: dict
    allowed_channels: list
    selected_channel: str
    decision: dict

########################################################################
# check_consent()

def check_consent(state):
    allowed = consent_check(state["record"])

    state["allowed_channels"] = allowed
    return state

########################################################################
# choose_channel()

def choose_channel(state):

    state["selected_channel"] = preferred_channel(
        state["record"],
        state["allowed_channels"]
    )

    return state

########################################################################
# reason()

def reason(state):

    decision = agent.decide(
        state["record"],
        state["examples"]
    )

    state["decision"] = decision
    return state

########################################################################
# Build Graph

builder = StateGraph(AgentState)

builder.add_node(
    "consent",
    check_consent
)

builder.add_node(
    "channel",
    choose_channel
)

builder.add_node(
    "reason",
    reason
)

builder.add_edge(
    "consent",
    "channel"
)

builder.add_edge(
    "channel",
    "reason"
)

builder.set_entry_point("consent")

graph = builder.compile()

########################################################################