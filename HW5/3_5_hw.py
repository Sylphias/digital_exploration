def hanoi(n):
  if n == 0:
    return 1
  return n+hanoi(n-1)
print hanoi(3)

