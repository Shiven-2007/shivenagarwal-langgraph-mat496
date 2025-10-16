initial setup

## Video 2 (simple graph)
> In this video we learned how to add nodes and edges to the graph. 
  conditional edges can be used that decide which node to point to based on the user input, here we just used a randomiser function 
  I went ahead and made an example that in the end of this file, in this dummy scenario we do a web search or open a calculator or pass input to a general llm query 

## Video 3 (langsmith studio)
> In this video we just use the pre existing files from the course to verify that the langsmith studio works, 
Not much to do here, but I went ahead and added the example I made earlier to this

## Video 4 (chains)
> In this video we learned how to make tools that use predefined functions to give an accurate output. This is helpful for doing math since llm's generate text based on probability and do not always give the mathematically correct output.
I just added a few more tools for subtraction, multiplication, division etc at the end of this file. Interesting observation: it seems when I try to prompt it to divide 5 by 0, it doesn't call the tool, whereas it does call the tools when a non zero division takes place