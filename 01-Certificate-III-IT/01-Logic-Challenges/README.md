# 🧩 Logic Comparison: Country-Capital Quiz Engine

This folder showcases the evolution of a quiz system through three distinct programmatic approaches. It demonstrates my ability to refactor code for better performance and enhanced user experience.

## 🎯 Project Overview
The objective was to build an interactive quiz game that manages a dataset of countries and capitals, handles user sessions, and ensures a robust experience through strict input validation.

---

### 🔹 [Implementation V0: Linear Progression](./country_game_v0_linear.py)
**Core Strategy:** Sequential Iteration.

* **Technical Logic**: Uses a straightforward `for` loop to iterate through the list in its fixed, original order.
* **Key Feature**: Introduces a **Scoring System** using formatted strings (`:.2f}%`) to provide real-time performance feedback.
* **Purpose**: Serves as the MVP (Minimum Viable Product), focusing on core UI/UX and scoring before introducing algorithmic complexity.

---

### 🔹 [Implementation V1: Tracking via Registry](./country_game_v1_tracking.py)
**Core Strategy:** In-place Index Tracking.

* **Technical Logic**: Maintains the original list while using an auxiliary `choiceList` to log used indices. It employs a **"Check-and-Reroll"** strategy to ensure uniqueness.
* **Key Advantage**: **Memory Efficiency.** It avoids duplicating the dataset, making it suitable for environments where memory conservation is prioritized.
* **Evolution**: Adds non-linear gameplay by introducing the `random` module.



---

### 🔹 [Implementation V2: Dynamic List Manipulation](./country_game_v2_destructive.py)
**Core Strategy:** Destructive Sampling & State Restoration.

* **Technical Logic**: Creates a temporary "Working Copy" of the dataset. Countries are **deleted** from the list as they are picked, inherently preventing repetitions.
* **Key Advantage**: **Algorithmic Efficiency.** Eliminates the need for collision checks or re-rolling, ensuring a $O(1)$ selection speed. It also showcases mastery of `copy.deepcopy()` to manage memory references correctly.



---

## 🧠 Technical Competencies Demonstrated

* **Iteration & Refactoring**: Demonstrating the journey from basic linear logic to optimized, non-linear algorithms.
* **Input Sanitization**: Multi-layered validation logic ensuring the program is resilient to unexpected user inputs.
* **Memory Management**: Correct application of `deepcopy` for nested data structures.
* **Session Management**: Professional use of nested `while` loops, `break`, and `continue` to manage complex program states.

---
**Course:** ICT30120 Certificate III in IT (TAFE NSW)  
**Author:** [Tina Ying Wang](https://github.com/Tina-YingWang-AU)
