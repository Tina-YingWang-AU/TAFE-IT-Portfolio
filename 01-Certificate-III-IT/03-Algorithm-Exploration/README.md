# 🧮 Algorithm Exploration: Manual Bubble Sort

While Python provides built-in sorting methods, this project demonstrates my understanding of fundamental computer science algorithms by implementing a **Bubble Sort** from scratch.

## 🎯 Project Objective
The goal was to read a list of usernames from an external text file and sort them alphabetically (A-Z) using manual swap logic rather than automated library functions.

---

## 🛠️ Technical Implementation
* **File I/O**: Utilizes the `csv` module to parse external data and clean it using `.strip().lower()`.
* **Nested Loop Logic**: Implements a `while` loop structure to compare adjacent elements.
* **In-place Swapping**: Uses a "transit" variable to swap elements without losing data, a core concept in algorithm design.



---

## 📋 Environment Setup & Requirements
To run this script locally, ensure you have a file named `accounts.txt` in the same directory as the script. The file should follow this structure (one entry per line, or comma-separated):

**Example `accounts.txt` content:**
```text
Zebra2023,Password123
Alpha_User,SecurePass!
Beta_Tester,MyPassword
