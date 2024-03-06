# Mistral LLM Discord Bot Prototype

This project represents an early prototype of a Discord bot powered by a local Large Language Model (LLM), specifically "TheBloke/Mistral-7B-Instruct-v0.1-GGUF". It listens to messages starting with `/talk` and generates responses using the deployed LLM, bringing advanced conversational capabilities directly into your Discord server.

## Features

- Integration with Discord through a custom bot.
- Utilization of a local LLM for generating responses, providing privacy and full control over the data processing.
- Streamed response generation to handle long responses and minimize wait times.
- Customizable prompts for tailored interactions based on server or conversation context.

## Prerequisites

To run this bot, you will need:
- Python 3.8 or newer.
- The Discord bot token (obtainable by creating a bot on the Discord Developer Portal).

## Installation

Follow these steps to set up the bot:

1. **Clone the repository:**
   ```
   git clone https://github.com/WilleDCrazy/LocalDiscordLLM
   ```

2. **Install required Python packages:**
   - Install Discord.py:
     ```
     pip install discord.py
     ```
   - Install the necessary model and transformers library:
     ```
     pip install ctransformers
     ```

3. **Configuration:**
   - Open the provided Python script with your preferred text editor.
   - Replace `'Discord bot token here'` with your actual Discord bot token.
   - (Optional) Adjust the model parameters or `input_text` system prompt within the script as needed for your application.

4. **Run the bot:**
   Execute the script to start your bot:
   ```
   python LocalLLM.py
   ```

## Usage

With the bot running and added to your Discord server:
- Users can initiate interactions with the bot by typing `/talk` followed by their message.
- The bot processes this input using the local LLM and generates a response, which is then sent back in the chat.

## Customization

You can customize the system prompt or model parameters to better suit your needs or to experiment with different settings for response generation.

## Contributing

Contributions to improve the prototype or extend its functionality are highly welcomed. Feel free to fork the project, make your changes, and submit a pull request.

## License

MIT License

## Acknowledgments

- Thanks to the creators of the "TheBloke/Mistral-7B-Instruct-v0.1-GGUF" model for their contribution to the community.
- Discord.py library for making Discord bot development accessible.
