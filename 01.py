

def part1(data):
  __import__('time').sleep(1)
    # Data is automatically read from 01.txt
  num1 = 0;
  num2 = 0;
  num3 = 0;
  n1 = "";
  n2 = "";
  n3 = "";
  lines = data.splitlines()
 
  for x in lines:
    num1 = x
    n1 = int(num1)
    for z in lines:
      num2 = z
      n2 = int(num2)
      for y in lines:
        num3 = y
        n3 = int(num3)
        if n1 + n2 + n3 == 2020:
          return n1 * n2 * n3
