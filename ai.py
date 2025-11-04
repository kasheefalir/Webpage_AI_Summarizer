import os
def ai_chat(reply):
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    completion=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"system","content":f"Summarize this text from wikipedia in 3 paragraphs or less and include references at the end: {reply}"}]

    )

    reply=completion.choices[0].message.content
    print(reply)
