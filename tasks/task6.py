# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    a, b, z = map(int, input().split())
    x = a*a
    y = b*b
    z = z*z
    print(x == y + z or y == x + z or z == x+y)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()