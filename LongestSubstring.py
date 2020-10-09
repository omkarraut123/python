def StringPeriods(s):

  for i in range(int(len(s)/2), 0,-1):
    a = s[:i]
    count = 2
    b = ''

    while len(b) < len(s):
      b = a * count

      if b == s:
        return a
      count += 1
  return -1