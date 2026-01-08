# 🧩 Logic Comparison: Country-Capital Quiz Engine

This folder showcases two distinct programmatic approaches to solving a common algorithmic problem: **Randomly sampling a dataset without repetition.**

## 🎯 Project Overview
The objective was to build an interactive quiz game that:
1. Picks a country randomly from a list.
2. Ensures no country is repeated within a single session.
3. Provides robust session controls (Next Question / Play Again / Exit).
4. Handles input sanitization (ensuring the user only enters 'y' or 'n').

---

## 🔹 Implementation V1: Tracking via Registry
**File:** `country_game_v1_tracking.py`

* **Methodology**: **In-place Index Tracking.**
* **Technical Logic**: The program maintains the original list and creates an auxiliary list called `choiceList`. 
* **Workflow**: Before presenting a country, it checks: `if choice not in choiceList`. If the index is already there, it re-rolls the random number.
* **Key Advantage**: Extremely memory-efficient as it does not duplicate the dataset. It simply monitors the "indices" already used.



---

## 🔹 Implementation V2: Dynamic List Manipulation (Refactored)
**File:** `country_game_v2_destructive.py`

* **Methodology**: **Destructive Sampling & State Restoration.**
* **Technical Logic**: This version creates a "Working Copy" of the dataset. As each country is picked, it is **deleted** from the list using `del tempCountryCapital[choice]`.
* **Deep Copy Usage**: Implements `copy.deepcopy()` to reset the game. This demonstrates an understanding of **Memory References** in Python—preventing the "Working Copy" from accidentally modifying the "Original Source."
* **Key Advantage**: Faster algorithmic execution. Since used items are removed, the computer never has to "re-roll" or "check" for duplicates—it simply picks from what remains.



---

## 🧠 Technical Competencies Demonstrated

* **Advanced State Management**: Effectively managing data across nested `while` loops and session restarts.
* **Input Sanitization**: Multi-layered validation logic that prevents the program from crashing due to unexpected user input.
* **Memory Optimization**: Correct application of `deepcopy` vs shallow copies for nested data structures.
* **Loop Control**: Professional use of `break` and `continue` to manage complex, multi-level program flow.

---
**Course:** ICT30120 Certificate III in IT (TAFE NSW)  
**Author:** [Tina Ying Wang](https://github.com/Tina-YingWang-AU)
