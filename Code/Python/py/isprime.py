def is_prime(x):
  for i in range(2,x):
    if x % i == 0:
      return False
  else:
    return True

for i in range(2,1000):
  if is_prime(i):
    print i
