#!/usr/bin/env python
"""
Example of a simple chatbot that just passes current conversation
state back and forth between server and client.
"""
from typing import List, Union

from mangum import Mangum
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langserve import add_routes
from langserve.pydantic_v1 import BaseModel, Field

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Spin up a simple api server using Langchain's Runnable interfaces",
)

# Declare a chain
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful, professional assistant named Cob."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | ChatOpenAI(model="gpt-3.5-turbo")


class InputChat(BaseModel):
    """Input for the chat endpoint."""

    messages: List[Union[HumanMessage, AIMessage, SystemMessage]] = Field(
        ...,
        description="The chat messages representing the current conversation.",
    )


add_routes(
    app,
    chain.with_types(input_type=InputChat),
    # enable_feedback_endpoint=True,
    # enable_public_trace_link_endpoint=True,
    playground_type="chat",
    path="/openai"
)

handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    print("hello from app.server")
