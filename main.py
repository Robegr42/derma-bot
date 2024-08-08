import pyrogram
from openai import OpenAI

bot_client = pyrogram.Client('matcom-bot', bot_token=open('token').read())
llm_client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

START_PROMPT = """
You are an asistant bot who helps people to identify skin injuries.
"""

@bot_client.on_message(pyrogram.filters.command("\start"))
def start_message(client: pyrogram.Client, message: pyrogram.types.Message):
    completion = llm_client.chat.completions.create(
        model="model-identifier",
        messages=[
            {"role": "system", "content": START_PROMPT},
            {"role": "user", "content": "Introduce yourself."}
        ],
        temperature=0.7,
    )

    client.send_message(
            message.chat.id,
            completion.choices[0].message.content,
            disable_web_page_preview=True
        )

def main():
    bot_client.start()
    pyrogram.idle()
    bot_client.stop()


