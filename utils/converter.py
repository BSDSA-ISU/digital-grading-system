items = [
    (34, 50),
    (150, 450),
    (48, 60),
    (29, 30)
]

scaled_scores = [(got / total) * 100 for got, total in items]

total_score = sum(scaled_scores)

print(round(total_score, 2))
