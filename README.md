# AlexandriaAlexandria Beta — Discord Bot

Alexandria Beta is a multipurpose Discord bot built using Python and discord.py with slash commands.
It includes utility tools, moderation features, games, leveling, polls, and more.

🚀 Features
🛠 Utility

/ping — Check bot latency

/coin — Flip a coin

/userinfo — View user info

/serverinfo — Basic server info

🛡 Moderation

(Admin-only commands)

/kick — Kick a user

/ban — Ban a user

/clear — Bulk delete messages

Role-based protection (only admin or approved roles)

📈 Leveling System

XP gained per message

Evolution stages (custom names) based on level brackets

Stage 1 → Level 1–10

Stage 2 → Level 11–20

Stage 3 → Level 21+

🎮 Games

Includes 3 interactive slash-command games:

/guess — Number guessing

/rps — Rock–Paper–Scissors

/dice — Roll a random dice

🗳 Poll System

/poll — Create interactive reactions-based polls

Supports multi-option polls

🌐 Extra Tools

/iplookup — Basic IP information lookup (public API)

/avatar — Show someone's profile picture

🏗 Project Structure
Alexandria-Beta/
│── cogs/
│   ├── utility.py
│   ├── moderation.py
│   ├── leveling.py
│   ├── games.py
│   ├── polls.py
│── main.py
│── README.md
│── requirements.txt
│── .gitignore

🔐 Environment Variables (IMPORTANT)

Create a .env file locally containing:

TOKEN=your_discord_bot_token_here


This file is never uploaded because .gitignore protects it.

When deploying on Render or other cloud platforms, add:

TOKEN as an environment variable

▶️ Running Locally
1. Create virtual environment
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows

2. Install dependencies
pip install -r requirements.txt

3. Run the bot
python main.py

☁️ Deploying on Render

Push your code to GitHub

Create a new Web Service on Render

Set Start Command:

python main.py


Add Environment Variables:

TOKEN = <your_token>


Deploy 🎉

📜 License

This project is free to use, modify, and improve.