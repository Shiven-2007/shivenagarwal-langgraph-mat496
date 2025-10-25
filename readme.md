initial setup

## Video 2 (simple graph)

> In this video we learned how to add nodes and edges to the graph.
> conditional edges can be used that decide which node to point to based on the user input, here we just used a randomiser function
> I went ahead and made an example that in the end of this file, in this dummy scenario we do a web search or open a calculator or pass input to a general llm query

## Video 3 (langsmith studio)

> In this video we just use the pre existing files from the course to verify that the langsmith studio works,
> Not much to do here, but I went ahead and added the example I made earlier to this

## Video 4 (chains)

> In this video we learned how to make tools that use predefined functions to give an accurate output. This is helpful for doing math since llm's generate text based on probability and do not always give the mathematically correct output.
> I just added a few more tools for subtraction, multiplication, division etc at the end of this file. Interesting observation: it seems when I try to prompt it to divide 5 by 0, it doesn't call the tool, whereas it does call the tools when a non zero division takes place

## Video 5 (router)

> In this video we routed to the tools node in case a tool was being called by the llm on user input.
> I added a node, in the middle of the file itself after tools that just prints the tool output. In more practical examples I think this can be used to further process the result after we get a result from the tool.

## Video 6 (agent)

> In this video we learned how to make a recursive loop, this allows for sequential tool calling. A tools output can be fed back into the tool with this. For my modification I added a tool that sorts a list of numbers. My intended behaviour was to have the llm then recursively subtract this list, but I was unable to get this to work. Perhaps a more refined prompt or another tool for this could help.

## Video 7 (agent with memory)

> In this video we learned how to persist memory so that we can continue prompting in pieces.
> I made a very simple modification and multiplied this final new result by 10.

# Module 2

## Lesson 1: State Schema

> In this lesson we learned about the various different methods in which we can define the state schema. For my modification at the end of the file I make another graph using pydantic state.

## Lesson 2: State reducers

> In this lesson we learned about an issue where while branching 2 steps simultaneously attempt to update one value. This is resolved by using reducers. Instead of modifying the value itself, we append values in a list. We also learn about a custom reducer that can help handle the values when they are potentially unsupported by the operator. This is then used to illustrate how messages can be modified and deleted using the add_messages reducer. For my modification I made a reducer for merging dictionaries. This example is in the last cell of this python notebook.

## Lesson 3: Multiple Schemas

> In this lesson we learned about defining different schemas for the input and output states. This is useful if for example we want to internally communicate some data between nodes but not show it in the final result to the user. For my modification I created a different output and input state in a simple graph.

## Lesson 4: Trimming and filtering messages

> In this lesson we learned about trimming and filtering messages, in order to reduce latency and more efficiently use our tokens, since this is a limited and expensive resource. There are various strategies like using the reducer used in lesson 2, or filtering the list of messages we use, or using the trim messages utility that allows us to limit the number of tokens of messages passed to the server. Since this is a very simple example I haven't made any modifications of my own.

## Lesson 5: Chatbot with Summarising messages and Memory

> In this lesson we made a chatbot with a function that summarises the chat if there are more than 6 messages. We also used the memory persistence so that state of the graph is saved and we can have multi turn conversations with the chatbot.

## Lesson 6: Chatbot with External memory

> This lesson is similar to the last one, except here the memory is saved to a local sqlite3 database. This means that even if we restart the environment, our in memory state is lost but we still have the state in the database and can refer back to it. This is especially useful for saving conversations.

# Module 2

## Lesson 1: Streaming
> I learned about the different streaming modes: values mode, which streams the full graph state after each node runs; updates mode, which streams only the parts of the state that changed; messages mode, used for message-based workflows; and astream_events, which provides real-time token streaming. For my modification, I added a turn_count field to the state.