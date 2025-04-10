# File Manager App (Beginner Edition) - April 2025

> "This is not a production-level app.  
> This is me practicing, learning, and building from scratch."  
> — Sid.py

---

## About This Project
A beginner's attempt at a file manager simulation using Python basics:

- Lists for data and recycle bin storage
- Loops for continuous operation
- Conditionals for decision-making
- Try-Except for error handling
- User input management

---

## Why I Built This
- Wanted to create a practical app without tutorials, focusing on data management.
- Practiced list operations, conditional logic, and basic error handling.
- Aimed to simulate file storage, deletion, and recovery with a recycle bin—still learning advanced features.

---

## How to Run
1. Save as `file_manager_app.py`.
2. Run with `python file_manager_app.py` in your terminal.

---

## Features
|Feature|What It Does|
|-------|------------|
|Open App|Displays stored data if any|
|Enter Data|Adds user input to storage (any format)|
|Delete Data|Removes data with recycle bin option and clear all|
|Recycle Bin|Shows deleted data, allows restore (all or specific) with sub-menu|
|Exit|Closes the app|

## What can program do:
1. Open App
2. Enter Data
3. Delete Data
4. Recycle Bin
5. Exit

## Sample Flow
- Choose 2 → Enter "Note1" → "Note1 is added successfully..."
- Choose 3 → Enter "Note1" → "Note1 got deleted..." → "yes" → Stored in recycle
- Choose 4 → Choose 1 → "Done! all data is restored"
- Choose 5 → "Thank You for using our app..."

---

## Known Issues
- No validation for empty strings or special characters.
- No handling for large data sets.

---

## Author
- [Sid.py] ([https://github.com/BscCanCode](https://github.com/BscCanCode))

## Development Notes
- Built via self-learning from YouTube.
- Uses basic Python (lists, loops, conditionals, try-except).
- Highlights: Added recycle bin sub-menu with range check attempt (`0 < m <= 2`) to improve restore options. (This the update)
- Current skill level: Beginner

---

## NOTE
- README crafted with AI chatbot assistance.
- Kept raw to document my learning journey; plan to refine later.

---

## Fun Fact
- Took one hour to write and 30 minutes to analyze and rectify the errors
