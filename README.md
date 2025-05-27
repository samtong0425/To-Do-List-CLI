# To-Do-List-CLI
A  command-line to-do list application built as a CS50P final project.
![Screenshot From 2025-05-27 21-26-42](https://github.com/user-attachments/assets/f185d99e-6de8-4b98-a3f1-e4d97b34016d)

# How to use
- When adding tasks, type the task description and due datea. Then, press Enter
- When marking as complete or deleting, enter the task number ID
- Type 'q' to return to the main menu

# Available Commands:
- a, add    - Add a new task to your list
- m, mark   - Mark a task as complete or incomplete
- d, delete - Remove a task from your list
- h, help   - Display this help information
- q, quit   - Exit the application

# Technical difficulty
- Choosing wrong data structure and format. Originally, the dictionary in the list is used but the order is not numbered. Then, the structure changed to a dictionary in dictionary. However, I setted the key as integer ‘1’. I don’t know json to store everything in string. The value is set as items and status.
- Displaying in a table format. Because of my data structure, I have to restructure the database to properly display the list in this third-party library. 
Testing is hard for my program because most functions need user input. I don’t know how to test user input.
- I understand what technical debt is. Because of my data structure choice, I invented a creative way to add new features to my program. It makes me not want to add new features. However, I have to rewrite the program if I want to change the data structure.
- The structure of the program will affect the growth of the features. I don't know how to refactor in a more effective way so  everything will become a mess if I add more and more features. 
- It is important to choose a proper data structure and program structure that allow the growth of the program. 
- I know it is harder to add features in a fixed structure than rewrite everything.
- The Git command is scary. I screwed up my repo a few times because of a VS code freeze after committing. Codespace is refreshing all the time and shows error when using FireFox.

# Reflection
- I used AI to explain the documentation and provide code examples for me to understand the syntax. It is also useful in naming variables. It is hard to come up with good naming. AI is also useful in suggesting good user interfaces and prompting.
- I found AI makes things unnecessarily complex and difficult when I can accomplish the same task with less code.
- I write all the code myself because it is the best way to learn. Programming is like driving. You cannot learn through watching YouTube. You have to drive it yourself.
