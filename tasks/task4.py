# tasks/task4.py

def solve():
# Ниже пишите решение задачи
  a, b, z = map(int, input().split())
  result = (a + b > z) and (a + z > b) and (b + z > a) 
  print(result)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()