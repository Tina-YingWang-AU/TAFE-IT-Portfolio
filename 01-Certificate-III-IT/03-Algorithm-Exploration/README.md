# 🧮 Algorithm Exploration: Manual Bubble Sort

While Python provides built-in sorting methods, this project demonstrates my understanding of fundamental computer science algorithms by implementing a **Bubble Sort** from scratch.

## 🎯 Project Objective
The goal was to read a list of usernames from an external `accounts.txt` file and sort them alphabetically (A-Z) using manual swap logic rather than automated library functions.

---

## 🛠️ Technical Implementation
* **File I/O**: Utilizes the `csv` module to parse external data and clean it using `.strip().lower()`.
* **Nested Loop Logic**: Implements a `while` loop structure to compare adjacent elements.
* **In-place Swapping**: Uses a "transit" variable to swap elements without losing data, a core concept in algorithm design.



## 🧠 Why this matters
Manual algorithm implementation proves:
1. **Computational Thinking**: Understanding the $O(n^2)$ complexity and the logic of element comparison.
2. **Data Integrity**: Ensuring that data read from a file remains consistent throughout the sorting process.
3. **Problem Solving**: Breaking down a complex sorting task into simple "compare and swap" steps.

---
**Key Concepts**: `CSV Parsing`, `Algorithm Logic`, `In-place Swapping`, `Control Flow`.
