from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
       
        {
            "role": "user",
            "content": f'''
            Dime qué es PHP
            '''
        }
    ],
    temperature=0.7,
    max_tokens=1024,
    top_p=1
)
message_content = response.choices[0].message.content
print(message_content)
