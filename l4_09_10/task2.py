"""Задача #2 – олимпиада"""


def check_winners(scores: list[int], student_score: int) -> None:

    winners = [scores.pop(scores.index(max(scores))) for _ in range(3)]
    print("Вы в тройке победителей!" if student_score in winners else "Вы не попали в тройку победителей.")


scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
student_score = 20

check_winners(scores, student_score)
