#Author: William Bukowski

import openai


prompt = input("Please enter a query >")

openai.Completion.create(
  engine="davinci",
  prompt="prompt"
)



