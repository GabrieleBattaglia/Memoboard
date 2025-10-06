# Memoboard
An helper to play faster chess without touching or watching the board. Exercises with diagonals, knight's jump and square colours.
## Memoboard by Gabriele Battaglia (IZ4APU) - october 2025

## Se esegui lo script Python, assicurati di avere GBUtils.py nella stessa cartella. Puoi scaricarlo dall'omonimo progetto su GitHub.

## If you're running the python script, be sure to have GBUtils.py on the same folder. You can grab it from the GBUtils project here on GitHub.

## This small utility helps to familiarize yourself with the chessboard. The goal is to train the chess player to quickly visualize the 64 squares during analysis, now with personalized progress tracking and leaderboards to challenge your friends.

With daily practice, repeated over time with consistency, these exercises will allow you to gain a lot of speed in studying positions and finding candidate moves.

**IMPORTANT**: you can get benefits from these exercises only if you play them without looking at the chessboard.

This software is designed and written in Python by the undersigned and is distributed without any warranty. Distribution is permitted through any channel but not the disassembly and/or modification of the source code.

For requests and bug reports, please write to iz4apu@libero.it

---
## **Application Description**

The application does not require installation. It can be copied to a folder of your choice and executed.

This software is a CLI (Command Line Interface) type, i.e. without a graphical interface. In the terminal, a blinking cursor is located on the last line waiting for a command. The command can be a pressed key or a word typed on the keyboard followed by the enter key.

If a command consists of several letters, for example in the case of "quit" useful to exit the application, it is also sufficient to press only the "q", since "quit" is the only command that starts with this letter, to obtain the desired effect.

To learn how to read the output in the terminal with your screen reader, refer to the manual of the latter.

---
## **Launching Memoboard**

When you launch Memoboard, it will first ask for your **username**. This name will be used to save your personal records and display your results on the leaderboard.

After entering your name, a screen will appear where Memoboard introduces itself. The last line at the bottom will show the commands that can be given to the program. Let's see them together.

* `quit`: Closes the program.
* `help`: Shows this document.
* `menu`: Displays the list of all available commands.
* `knights`, `bishops`, `colors`: These commands access the individual exercises. You can choose how many attempts to make.
    * In `knights`, you must determine if two squares are a knight's move apart (`y` for yes, `n` for no).
    * In `bishops`, you must determine if two squares are on the same diagonal (`y` for yes, `n` for no).
    * In `colors`, you must identify a square's color (`w` for white, `b` for black).
* `chart`: This new command shows the leaderboard. You can select an exercise to see a detailed ranking of all users.
* `test`: The final test, consisting of a predefined number of attempts across all exercise types.

---
## **New Features: User Profiles and Leaderboards**

Memoboard now saves your performance to track your progress and compete with others.

### **User Profiles and Data File**
Your results are saved under the username you provide at startup. All data is stored in a file named `memoboard_scores.json` in the application's folder. This file acts as the database for your personal bests and the leaderboard.

### **Performance Comparison Report**
At the end of each exercise, if you have a previously saved score, Memoboard will show you a detailed comparison table. This table compares your **Current** performance against your **Previous** record, showing the difference in both absolute numbers and percentage. This helps you immediately see where you've improved.

### **The Leaderboard (`chart`)**
The `chart` command opens a detailed leaderboard. You can choose which exercise to view, and the app will display a ranked list of all users. The ranking is based on **Points per Minute**, a metric that measures your scoring efficiency, ensuring a fair comparison regardless of the number of attempts. The leaderboard includes details like attempts, win percentage, time, and the date of the record.

---
## **How the Scores Work**

To make the exercises more fun, Memoboard assigns a score at the end of each session.

### **Scoring Mechanism**
After the square(s) for an exercise are announced, a hidden timer starts from 15,000 points (one point per millisecond for 15 seconds). For every millisecond you take to answer, points are subtracted from this initial amount. A correct answer adds the remaining points to your total score. A wrong answer scores zero.

### **The Main Ranking Metric: Points per Minute**
While the `Total Score` is fun, the main metric for ranking is **Points per Minute**. This value represents your **efficiency**—how quickly you score points. It's calculated by dividing your total score by the total time of the exercise. This ensures that a short, fast, and accurate session is ranked higher than a long session where more points were accumulated but at a slower pace.

---
## **Log and Data Files**

Memoboard now uses two files:

1.  **memoboard.txt (Log File)**: This file is a simple log. It records the results of every exercise you complete, with new data appended to the end. You can safely delete this file at any time; Memoboard will create a new one if it's missing.
2.  **memoboard_scores.json (Data File)**: **This is an important file.** It stores all user profiles, personal bests, and leaderboard data. If you delete this file, **all saved records will be permanently lost**.

---
## **Conclusion**

Thank you for reading this manual. I wish you have fun with Memoboard and, above all, learn to play blind chess, a very important skill for any successful chess player.

Gabriele Battaglia.