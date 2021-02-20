import pandas as pd


ANSWER_KEY = ('B ', 'C ', 'B ')

okkar_answers_csv = pd.read_csv('./okkar_answers.csv', header=None)
surabhi_answers_csv = pd.read_csv('./surabhi_answers.csv', header=None)

# print(okkar_answers_csv)
# print(surabhi_answers_csv)

okkar_answers = okkar_answers_csv.iloc[0][1], okkar_answers_csv.iloc[1][1], okkar_answers_csv.iloc[2][1]
surabhi_answers = surabhi_answers_csv.iloc[0][1], surabhi_answers_csv.iloc[1][1], surabhi_answers_csv.iloc[2][1]

# print(okkar_answers)
# print(surabhi_answers)


def show_result(student_answer):
    if student_answer == ANSWER_KEY:
        print('Good job! 100 % correct 😄')
        return

    # which question did this student answered wrongly?
    wrong_answers = [student_answer[i] for i in range(
        3) if student_answer[i] != ANSWER_KEY[i]]

    for q_num, answer in enumerate(wrong_answers):
        print(
            f'Question {q_num} is wrong ❌ Correct: {ANSWER_KEY[q_num]} Answered {answer}')


# show_result(okkar_answers)
show_result(surabhi_answers)
