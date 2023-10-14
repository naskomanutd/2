def factorial(n):
  """
  Изчислява факториела на дадено число.

  Args:
    n: Числото, чиято факториела да се изчисли.

  Returns:
    Факториела на n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


def main():
  """
  Точка на влизане в програмата.
  """

  n = int(input("Въведете число: "))
  print(f"Факториелът на {n} е {factorial(n)}")


if __name__ == "__main__":
  main()