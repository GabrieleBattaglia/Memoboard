# Memoboard
An helper to play faster chess without touching or watching the board. Exercises with diagonals, knight's jump and square colours.
## Memoboard by Gabriele Battaglia (IZ4APU) - May 2024

This small utility helps to familiarize yourself with the chessboard. The goal is to train the chess player to quickly visualize the 64 squares during analysis.

With daily practice, repeated over time with consistency, these exercises will allow you to gain a lot of speed in studying positions and finding candidate moves.

IMPORTANT: you can get benefits from these exercise only if you play them without llooking the chessboard.

This software is designed and written in Python by the undersigned and is distributed without any warranty. Distribution is permitted through any channel but not the disassembly and/or modification of the source code.

For requests and bug reports, please write to iz4apu@libero.it

**Application Description**

The application does not require installation. It can be copied to a folder of your choice and executed.

This software is a CLI (Command Line Interface) type, i.e. without a graphical interface. Unlike programs with a GUI (Graphic User Interface), Memoboard is executed in a terminal window, also known as a command prompt or Windows terminal. This also means that there are no menus, windows, buttons, checkboxes, combo boxes, edit fields; you do not move with tab or shift+tab and typically do not close with alt+f4.

In the terminal, a blinking cursor is located on the last line waiting for a command. The command can be a pressed key or a word typed on the keyboard followed by the enter key. When Memoboard receives a command, it produces an output, i.e. a written response that appears immediately above the line where commands are entered and scrolls upwards during use of the application.

If a command consists of several letters, for example in the case of "quit" useful to exit the application, it is also sufficient to press only the "q", since "quit" is the only command that starts with this letter, to obtain the desired effect.

To learn how to read the output in the terminal with your screen reader, refer to the manual of the latter.

**Launching Memoboard**

So let's launch our virtual instructor. A screen will appear where Memoboard introduces itself. The last line at the bottom will show the commands that can be given to the program. Let's see them together.

The first is "quit" or "q" which is used to close the program.
We then have "help" which will show this same document.
Then we find "menu" which will cause the display of a list with all available commands and a brief explanation for each item.
There are then "knights", "bishops" and "colors" which allow access to the individual exercises, in their respective specialties. In each of these exercises we could decide how many attempts we want to make, after which we will be brought back to this menu.
"knights" will give us access to the exercise in which we will have to tell the computer if 2 squares that are read to us are located at knight's move from each other and we will have to answer "y" for yes, yes, or "n" for no.
"bishops" instead will ask us if the 2 squares reported belong to the same diagonal, i.e. they are at bishop's move and here too we will let the app know our choice with the keys "y" for yes and "n" for no.
"colors" instead will present us with only one square at a time and we will have to say if it is a white square by pressing the "w" of white, or black by pressing the "b" of black.
At the end of each exercise, Memoboard saves a report to the memoboard.txt file which you will find in the same folder where the main application resides.
Then we have the beating heart of Memoboard, the super mega final test.
In this mode, we cannot decide how many attempts to make but, both the type of exercise and its duration are predefined and established by that nasty programmer.
The super mega final test consists of 4 parts: 25 attempts in the square color exercise, 25 for the knight's move, another 25 for the bishop's move and, more difficult than all of them, another 25 attempts randomly chosen from the first 3 types.
Here too, at the end, a detailed report is added to the usual memoboard.txt that you can comfortably read whenever you want, with your favorite text editor, the Windows Notepad will be just fine.

**How the scores work**

To make the exercises more fun, Memoboard assigns a score at the end of each exercise. You can have fun challenging yourself and your friends trying to surpass each other in increasingly close challenges.
Here's how the app assigns scores.
After reading the, or the, squares of the exercise, a hidden timer starts counting from 15 seconds to 0.
## Scoring System in Memoboard

**Scoring Mechanism**

Each millisecond counts as one point. Therefore, for every millisecond you think, the sneaky application will subtract one point from your initial score of 15,000 points.

If your answer is correct, the points you have earned will be added to your total, while in case of a wrong answer, you will naturally not earn any points.

The scoring system works the same way for the 3 color, knight, and bishop exercises, while, given the difficulty, you are awarded a bonus in the mixed exercise.

As always, everything is reported in memoboard.txt.

**Log File**

And finally, I remind you that every time you use the app, this log, memoboard.txt, is written, the new data is added to the bottom of the file; after a certain period of time, therefore, especially if you use the application often, the log could tend to grow a bit. Therefore, you can delete it without problems whenever you want: if Memoboard does not find it, it will create a new one.

**Conclusion**

Thank you for reading this manual, I wish you have fun with Memoboard and, above all, learn to play blind chess, a very important skill for any successful chess player.

Gabriele Battaglia.
