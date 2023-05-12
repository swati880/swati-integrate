import openai

openai.api_key = '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'
content = input("User: ")
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{
    "role":
    "user",
    "content":content
  }])

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')
