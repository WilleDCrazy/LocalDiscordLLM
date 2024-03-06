import discord
from ctransformers import AutoModelForCausalLM
import asyncio
import time


llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file="mistral-7b-instruct-v0.1.Q4_0.gguf", model_type="mistral", gpu_layers=800, max_new_tokens=1024)


intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.voice_states = True
intents.messages = True
intents.message_content = True



client = discord.Client(intents=intents)


is_generating_response = False

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global is_generating_response

    if message.author == client.user:
        return

    if message.content.startswith('/talk'):
        if is_generating_response:
            await message.reply("I'm already talking!")
            return

        is_generating_response = True  

        # Format the input for the GPT model
        input_text = f"<s>[INST]{Place your system prompt here}: Prompt {message.content[len('/talk '):]} [/INST]"
        response_message = await message.channel.send("⠀")  # Initial minimal content

        full_response = ""  

        async def collect_and_update():
            nonlocal full_response
            global is_generating_response
            generator = llm(input_text, stream=True)
            last_update_time = time.time()

            try:
                while True:
                    batch_text = ""
                    start_time = time.time()
                    while time.time() - start_time < 0.5:
                        try:
                            token = next(generator)
                            batch_text += token
                            last_update_time = time.time()
                        except StopIteration:
                            break

                    full_response += batch_text

                    if batch_text:
                        await response_message.edit(content=full_response)

                    if time.time() - last_update_time > 4:
                        break

                    await asyncio.sleep(0.5)

            finally:
                is_generating_response = False 

        client.loop.create_task(collect_and_update())

client.run('Discord bot token here')
