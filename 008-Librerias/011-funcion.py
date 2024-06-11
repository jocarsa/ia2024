from openai import OpenAI

client = OpenAI()
def mi_openai(entrada):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
           
            {
                "role": "user",
                "content": entrada
            }
        ],
        temperature=0.7,
        max_tokens=1024,
        top_p=1
    )
    message_content = response.choices[0].message.content
    return message_content

print(mi_openai("quiero saber que es HTML"))
