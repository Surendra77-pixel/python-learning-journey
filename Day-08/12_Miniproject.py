#  Quiz Game Mini Project (Single File)

def get_questions():
    return [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web apps?",
            "options": ["A. Python", "B. Java", "C. JavaScript", "D. All"],
            "answer": "D"
        },
        {
            "question": "What does CPU stand for?",
            "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Processor Unit"],
            "answer": "B"
        },
        {
            "question": "Which is a Python data type?",
            "options": ["A. list", "B. tuple", "C. set", "D. All"],
            "answer": "D"
        },
        {
            "question": "Who developed Python?",
            "options": ["A. Elon Musk", "B. Guido van Rossum", "C. Bill Gates", "D. Mark Zuckerberg"],
            "answer": "B"
        }
    ]


def run_quiz(questions):
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\n Question {i}: {q['question']}")

        for option in q["options"]:
            print(option)

        answer = input(" Enter your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer is {q['answer']}")

    return score


def show_result(score, total):
    percentage = (score / total) * 100

    print("\n ===== RESULT =====")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 50:
        print(" PASS")
    else:
        print(" FAIL")


def main():
    questions = get_questions()

    while True:
        score = run_quiz(questions)
        show_result(score, len(questions))

        replay = input("\n Do you want to play again? (yes/no): ").strip().lower()

        if replay != "yes":
            print(" Thank you for playing!")
            break


if __name__ == "__main__":
    main()