# Alexandria Beta — Discord Bot

Alexandria Beta is a multipurpose Discord bot built using **Python** and **discord.py** with slash commands.  
It includes **utility tools, moderation features, leveling, games, polls, and IP lookup**.

---

## 🚀 Features

### 🛠 Utility Commands
- `/ping` — Bot latency  
- `/coin` — Coin flip  
- `/userinfo` — View user info  
- `/serverinfo` — Server details  
- `/avatar` — Get a user’s profile picture  

---

## 🛡 Moderation  
Only admins or approved roles can use these:
- `/kick` — Kick a user  
- `/ban` — Ban a user  
- `/clear` — Bulk delete messages  

Role verification and permission checks are built into the moderation cog.

---

## 📈 Leveling System
Users gain XP automatically when sending messages.  
Evolution stages are assigned based on level ranges:

- **Stage 1:** Levels 1–10  
- **Stage 2:** Levels 11–20  
- **Stage 3:** Levels 21+  

Stage names are customizable inside the leveling cog.

---

## 🎮 Games
Three interactive slash-command games:
- `/guess` — Number guessing game  
- `/rps` — Rock–Paper–Scissors  
- `/dice` — Roll a random dice  

---

## 🗳 Poll System
- `/poll` — Create reaction-based polls  
- Supports multiple voting options  

---

## 🌐 IP Lookup
- `/iplookup` — Retrieves basic public IP information using a free lookup service  
- No paid API or authentication required  

---

## 🏗 Project Structure

```
Alexandria-Beta/
│── cogs/
│   ├── utility.py
│   ├── moderation.py
│   ├── leveling.py
│   ├── games.py
│   ├── polls.py
│   ├── iplookup.py
│── main.py
│── README.md
│── requirements.txt
│── .gitignore
```

---

## 📌 Notes
- This project is **not licensed**.  
- Copying, redistributing, or reusing any part of this project is **not permitted**.  
- Intended strictly for private use.

