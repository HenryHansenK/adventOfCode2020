def part1(data):
  __import__('time').sleep(1)
  
  c = 0
  trees = 0
  rem = 0
  line = data.splitlines()

  for x in line:
    if x[c] == "#":
      trees = trees + 1
    c = c + 3
    if c - len(x) >= 0:
      rem = c - len(x)
      c = rem
  return trees


def part2(data):
  __import__('time').sleep(1)
  
  c = 0
  tr1 = 0
  tr2 = 0 
  tr3 = 0
  tr4 = 0
  tr5 = 0
  rem = 0
  h = 0
  line = data.splitlines()

  for x in line:
    if x[c] == "#":
      tr1 = tr1 + 1
    c = c + 1
    if c - len(x) >= 0:
      rem = c - len(x)
      c = rem
  print(tr1)
  c = 0

  for x in line:
    if x[c] == "#":
      tr2 = tr2 + 1
    c = c + 3
    if c - len(x) >= 0:
      rem = c - len(x)
      c = rem
  print(tr2)
  c = 0

  for x in line:
    if x[c] == "#":
      tr3 = tr3 + 1
    c = c + 5
    if c - len(x) >= 0:
      rem = c - len(x)
      c = rem
  print(tr3)
  c = 0

  for x in line:
    if x[c] == "#":
      tr4 = tr4 + 1
    c = c + 7
    if c - len(x) >= 0:
      rem = c - len(x)
      c = rem
  print(tr4)
  c = 0

  for x in line:
    if h%2 == 0:
      if x[c] == "#":
        tr5 = tr5 + 1
      c = c + 1
      if c - len(x) >= 0:
        rem = c - len(x)
        c = rem
    h = h+1 
  print(tr5)

  return tr1 * tr2 * tr3 * tr4 * tr5