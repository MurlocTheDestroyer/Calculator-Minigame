# Calculator Minigame
 
A Python terminal game that tests your mental math skills across five difficulty levels. Answer arithmetic questions correctly to rack up points — but one wrong answer resets your score to zero. Think you can handle it?
 
---
 
## Features
 
- Five difficulty levels with escalating number ranges and point rewards
- Four operations: addition, subtraction, multiplication, and division
- Local high score leaderboard saved to `History Saved Scores.txt`, sorted by score
- Auto-generated starter scores for new players so the leaderboard isn't empty on first launch
- Cross-platform terminal clearing (Windows and Unix/macOS)
---
 
## Requirements
 
- Python 3.10+ (uses `match`/`case` syntax)
- No external libraries — only Python standard library modules: `random`, `time`, `os`
---
 
## Getting Started
 
1. Clone or download the repository
2. Run the game from your terminal:
```bash
python MiniGame.py
```
 
3. Enter your name and choose a difficulty level to begin
---
 
## How to Play
 
Each round you are shown an arithmetic problem. Type your answer and press Enter.
 
- **Correct answer** → you earn points based on the difficulty level, then choose to keep going or cash out
- **Wrong answer** → your score resets to zero and you get another chance (unless BeastMode is Activated then you lose)
- **Cashing out** → your score is saved to the leaderboard and the top 10 scores are displayed
- **Quitting mid-game** (`q` or `quit`) → you exit without saving your score
---
 
## Difficulty Levels
 
| # | Name | Number Range | Points per Correct Answer |
|---|------|-------------|--------------------------|
| 1 | I'm too young to be losing! | 1 – 25 | +3 |
| 2 | Be Gentle! | 26 – 99 | +5 |
| 3 | Hey, not too rough! | 100 – 249 | +8 |
| 4 | Watch me lose! | 250 – 499 | +13 |
| 5 | I Own This Game! | 500 – 1000 | +21 |
 
> **Note:** For difficulty 1, multiplication and division use smaller numbers (1–12) to keep results manageable. Division answers are rounded to the nearest tenth
 
---
 
## Project Structure
 
```
Calculator-Minigame/
├── MiniGame.py              # Main game logic
├── Slayer History.txt       #Created automatically when a player earns B3AST SL4Y3R
├── History Saved Scores.txt # Created automatically on first run
└── README.md
```
 
### `MiniGame.py`
 
Contains the `Main` class with three core methods:
 
- `Calculator(Name, Score)` — presents a difficulty menu, generates a random problem, checks the answer, and updates the score
- `Replay(Name, Score)` — asks whether to continue or cash out, handles saving the score and displaying the leaderboard
- `quit(Name, Score, BeastMode, BeastCounter)` — confirms before exiting without saving
- `ActivatedBeastMode(Name, Score, BeastMode, BeastCounter)` — runs the Beast Mode question loop with scaled difficulty tiers and 4× point multipliers
- `BeastReplay(Name, Score, BeastMode, BeastCounter)` — handles win/loss/continue outcomes during Beast Mode
- `WinnerZone(Name)` — awards the B3AST SL4Y3R title and writes to `Slayer History.txt`
- `generate_scores()` — creates `History Saved Scores.txt` and populates it with five random starter scores on first run
- `OperatingCommand(command)` — clears the terminal on both Windows and Unix/macOS
 
---
 
## Scores File
 
Scores are stored locally in `History Saved Scores.txt` in the format:
 
```
PlayerName : Score
```
 
The file is kept sorted in descending order by score. A score of 0 is not saved. The top 5 scores are shown at the end of each session.
 
---
 
## Planned Upgrades
 
- Global leaderboard
- Correct answer streak multiplier for continuous hard difficulty selections
- Show your current score and questions answered during a round, not just at the end
- Accuracy summary shown at cash-out (questions answered, questions wrong, accuracy %)
- A win streak counter displayed during play so you can see how long your current run is
- Possible introductions to newer modes of gameplay (Highscores scored will be separated from normal game modes highscores):
- WIP: A sudden death variant where one wrong answer ends the game entirely with no second chance
- MAYBE: Mixed difficulty mode that randomly cycles through all five levels each question

---
 
## Beast Mode

Beast Mode is a hidden escalating challenge triggered by a specific in-game sequence. Once active:

- Difficulty is chosen automatically based on your current score — the higher your score, the harder the tier
- Number ranges are significantly larger than normal mode at every tier
- Correct answers earn **4× the normal point reward** for that tier
- You cannot quit during Beast Mode
- Reach 500 points to defeat the Beast and earn the title of **B3AST SL4Y3R**; your name is saved to `Slayer History.txt`
- A wrong answer resets your score to 0 and ends the program in a game loss

---

## Notes

`time.sleep()` calls are intentional — they add brief pauses to improve readability during gameplay and prevent output from flashing past too quickly. The only files this program reads from or writes to is `History Saved Scores.txt` and `Slayer History.txt`.
