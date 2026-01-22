# simple-text-rpg
Text RPG

# 🧙‍♂️ Text RPG (Python)

A **terminal-based Text RPG written in Python**.  
Fight random enemies, level up, collect potions, and try to survive as many routes as possible.

This is a simple project, great for **learning programming logic**, **game loops**, and **basic RPG systems**.

---

## 🎮 How the Game Works

- The game is divided into infinite **routes**
- In each route:
  - A random enemy appears (`goblin`, `bandit`, or `orc`)
  - Difficulty scales with the route number
- You can:
  - Attack
  - Check your stats
  - Use potions
  - Run away
- When you defeat enemies:
  - You gain XP
  - You can level up
  - You earn potions every 3 routes

If your HP reaches **0**, the game ends ☠️

---

## 📊 Progression System

### Player Stats
- **HP / Max HP**
- **Damage**
- **Level**
- **Experience (XP)**
- **Potions**

### Level Up
When your XP reaches `level × 10`:
- +1 Level
- +3 Damage
- +5 Max HP
- HP is fully restored

---

## 👹 Enemies

Enemies are randomly selected from:

- Goblin
- Bandit
- Orc

Enemy stats scale with the current route:
- **HP:** `5 × route`
- **Damage:** `2 × route`

---

## 🧪 Potions

- Restore HP to maximum
- You gain **2 potions every 3 routes**
- Limited resource — use wisely

---

## ▶️ How to Run

### Requirements
- Python 3.8 or higher

### Run the Game
```bash
python main.py
