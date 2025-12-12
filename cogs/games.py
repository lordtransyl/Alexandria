import discord
from discord import app_commands
from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Rock Paper Scissors
    @app_commands.command(name="rps", description="Play Rock-Paper-Scissors")
    async def rps(self, interaction: discord.Interaction, choice: str):
        bot_choice = random.choice(["rock", "paper", "scissors"])
        choice = choice.lower()

        outcomes = {
            ("rock", "scissors"): "You win!",
            ("paper", "rock"): "You win!",
            ("scissors", "paper"): "You win!"
        }
        if choice == bot_choice:
            result = "It's a tie!"
        elif (choice, bot_choice) in outcomes:
            result = outcomes[(choice, bot_choice)]
        else:
            result = "You lose!"

        await interaction.response.send_message(
            f"🪨 **Rock-Paper-Scissors**\nYou chose: `{choice}`\nBot chose: `{bot_choice}`\n**{result}**"
        )

    # Guess Number
    @app_commands.command(name="guess", description="Guess a number between 1-10")
    async def guess(self, interaction: discord.Interaction, number: int):
        bot_number = random.randint(1, 10)
        if number == bot_number:
            msg = "🎉 Correct!"
        else:
            msg = f"❌ Wrong! I chose `{bot_number}`."

        await interaction.response.send_message(msg)

    # TicTacToe (simple)
    @app_commands.command(name="tictactoe", description="Play tic tac toe vs bot")
    async def tictactoe(self, interaction: discord.Interaction):
        board = ["⬜"] * 9
        bot_pos = random.randint(0, 8)
        board[bot_pos] = "❌"

        display = (
            f"{board[0]} {board[1]} {board[2]}\n"
            f"{board[3]} {board[4]} {board[5]}\n"
            f"{board[6]} {board[7]} {board[8]}"
        )

        await interaction.response.send_message(f"🎮 **Tic Tac Toe (Bot Move)**\n\n{display}")

async def setup(bot):
    await bot.add_cog(Games(bot))
