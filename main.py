from src.discordbot import IpoBot
from keep_alive import keep_alive
keep_alive()

if __name__ == "__main__":
    bot = IpoBot(command_prefix="$")
    bot.run_bot()


