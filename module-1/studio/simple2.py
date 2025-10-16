from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


def node_1(state):
    return {"graph_state": state['graph_state']}

def node_2(state):
    return {"graph_state": state['graph_state'] +" entered browser"}

def node_3(state):
    return {"graph_state": state['graph_state'] +" doing math"}

def node_4(state):
    return {"graph_state": state['graph_state'] + " general llm query"}
def decide_mood(state) -> Literal["node_2", "node_3", "node_4"]:
    
    user_input = state['graph_state'] 
    if "calculate" in user_input:
        return "node_3"
    elif "search" in user_input:
        return "node_2"
    else:
        return "node_4"
    
    
    

builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_node("node_4", node_4)


builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)
builder.add_edge("node_4", END)

graph = builder.compile()

