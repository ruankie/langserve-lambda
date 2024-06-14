#!/usr/bin/env python
"""
Example of a simple chatbot that just passes current conversation
state back and forth between server and client.
"""
# from mangum import Mangum
from fastapi import FastAPI
from langchain.schema.runnable import RunnableLambda

from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)

def func(x: str) -> str:
    """Repeats what was passed."""
    return f"You said: {x}"


add_routes(
    app,
    RunnableLambda(func).with_types(input_type=str),
    # enable_feedback_endpoint=True,
    # enable_public_trace_link_endpoint=True,
    # playground_type="chat",
    path="/dummy"
)

# handler = Mangum(app, lifespan="off")
