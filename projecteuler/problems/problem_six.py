"""Problem six of https://github.com/heathy/project_euler"""

sum_of_squares = 0

for x in range(1, 101):
    sum_of_squares += (x ** 2)

square_of_sum = sum(range(1, 101)) ** 2
answer = square_of_sum - sum_of_squares

print(answer)
