
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Quiz Data
# -------------------------------
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "James Gosling"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
        "answer": "Blue Whale"
    }
]

score = 0
q_index = 0

# -------------------------------
# Functions
# -------------------------------
def load_question():
    global q_index
    if q_index < len(questions):
        question_label.config(text=questions[q_index]["question"])
        for i in range(4):
            option_buttons[i].config(
                text=questions[q_index]["options"][i],
                state="normal"
            )
        score_label.config(text=f"Score: {score}")
    else:
        messagebox.showinfo("Quiz Finished", f"Your final score: {score}/{len(questions)}")
        root.destroy()

def check_answer(selected_option):
    global score, q_index
    correct_answer = questions[q_index]["answer"]
    if questions[q_index]["options"][selected_option] == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "Well done!")
    else:
        messagebox.showwarning("Wrong!", f"Correct answer: {correct_answer}")
    q_index += 1
    load_question()

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Quiz Game")
root.geometry("400x300")
root.resizable(False, False)

question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=350, justify="center")
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=20,
                    command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    option_buttons.append(btn)

score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 14))
score_label.pack(pady=10)

load_question()

root.mainloop()
