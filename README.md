# CodeAlpha_Basic_Chatbot

A simple, interactive, rule-based chatbot application developed in Python as part of the CodeAlpha Python Programming Internship program.

## 📋 Project Overview
This project satisfies the requirements for **Task 4: Basic Chatbot** from the CodeAlpha internship task list. The goal of this application is to build a lightweight, rule-based conversation agent that interacts with users through the console interface, interpreting fundamental text inputs and matching them instantly against preconfigured conditional loops.

## 🚀 Key Features
* **Interactive Main Loop:** Runs continuously in the terminal environment until an explicit exit command is passed by the user.
* **Predefined Reply Logic:** Structured entirely around conditional logic patterns (`if-elif-else`) to guarantee quick, predictable string response parsing.
* **Robust Text Normalization:** Converts incoming text parameters to lowercase and trims extra whitespaces to maximize user intent matching efficiency.

## 🧠 Key Concepts Covered
* Control Flow Statements (`if-elif-else`)
* User Input Parsing & String Manipulation
* Infinite Execution Loops (`while True`)
* Modular Functional Programming

## 🛠️ Code Implementation
The chatbot maps out incoming input variations to distinct preset responses:
* **Greetings:** Responds dynamically to phrases like `"hello"` or `"hi"`.
* **State Assessment:** Evaluates queries regarding state or condition like `"how are you"`.
* **Identification:** Answers queries regarding identity like `"your name"`.
* **Termination:** Safely handles the session exit when the user inputs `"bye"` or `"goodbye"`.

## 💻 How to Run Locally

### Prerequisites
Make sure you have Python installed on your local computer system (Python 3.6 or higher is recommended).

### Steps
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Jignesh-435/CodeAlpha_Basic_Chatbot.git](https://github.com/Jignesh-435/CodeAlpha_Basic_Chatbot.git)
