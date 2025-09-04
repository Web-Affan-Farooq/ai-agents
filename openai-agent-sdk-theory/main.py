from config import config
from agents import Agent, Runner
from pydantic import BaseModel

my_agent = Agent(
    name="hello agent",
    instructions="Please answer the questions of user"   
)
result = Runner.run_sync(
    starting_agent=my_agent,
    input="Where is quaid-e-azam born",
    run_config=config)
    
print(result.final_output)


# class ExampleResponse(BaseModel):
#     message:str
#     success:bool

# agent= Agent(
#     name="maths agent",
#     instructions="You're an intellegent agent that is genius in maths",
#     output_type=ExampleResponse
# )
# async def main():
#     streams = Runner.run_streamed(starting_agent=agent,input="2+3 = ?", run_config=config)
#     async for event in streams.stream_events():
#         print(f"\n[EVENT] : ${event} \n")

# asyncio.run(main())

# Stream event can contains the following clases :
#  $AgentUpdatedStreamEvent(new_agent=Agent(), type='agent_updated_stream_event')
# $RawResponsesStreamEvent()   this class reports us each an every task llm do while creating a response for us  this also calls folliwing classes :
#      ResponseCreatedEvent() -> tells us that starting response creation
#      ResponseOutputItemAddedEvent() -> The system has created an output item in the response, of type "message". Think of this as the message slot where the assistant will start filling in tokens.
#      ResponseContentPartAddedEvent() -> Inside that message, the model begins adding a content part .This will hold your streamed text.
#      ResponseTextDeltaEvent() -> generates and returns tokens as they are created
#      ResponseContentPartDoneEvent() -> this returns the final output as text property
#      ResponseOutputItemDoneEvent() ->  tells us that it had completed content generation
#      ResponseCompletedEvent() -> tells us that response is delivered

# RunItemStreamEvent() -> this is called when delivering response

# 

#  Agent(name='maths agent', handoff_description=None, tools=[], mcp_servers=[], mcp_config={}, instructions="You're an intellegent agent that is genius in maths", prompt=None, handoffs=[], model=None, model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=None, truncation=None, max_tokens=None, reasoning=None, metadata=None, store=None, include_usage=None, response_include=None, extra_query=None, extra_body=None, extra_headers=None, extra_args=None), input_guardrails=[], output_guardrails=[], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True)