def part1(data):
  __import__('time').sleep(1)
  
  min = 0
  max = 0
  valid = 0
  minstr = ""
  maxstr = ""
  key = ""
  lines = data.splitlines()

  for x in lines:
    if x[1].isdigit():
      minstr = x[0:2]
      maxstr = x[3:5]
      key = x[6]
    elif x[3].isdigit():
      minstr = x[0]
      maxstr = x[2:4]
      key = x[5]
    else:
      minstr = x[0]
      maxstr = x[2]
      key = x[4]
    min = int(minstr)
    max = int(maxstr)
    print(minstr, maxstr, key)
    if (x.count(key) - 1) < min or (x.count(key) - 1) > max:
      print("invalid")
    else:
      print("valid")
      valid = valid + 1
  print(valid)



def part2(data):
  __import__('time').sleep(1)
  p1 = 0
  p2 = 0
  valid = 0
  minstr = ""
  maxstr = ""
  key = ""
  password = ""
  lines = data.splitlines()

  for x in lines:
    if x[1].isdigit():
      minstr = x[0:2]
      maxstr = x[3:5]
      key = x[6]
      password = x[9:]
      
    elif x[3].isdigit():
      minstr = x[0]
      maxstr = x[2:4]
      key = x[5]
      password = x[8:]
    else:
      minstr = x[0]
      maxstr = x[2]
      key = x[4]
      password = x[7:]
    p1 = int(minstr) -1
    p2 = int(maxstr) -1
    print(p1, p2, key, password)

    if password[p1] == key and password[p2] != key:
      #print("valid")
      valid = valid + 1
    elif password[p1] != key and password[p2] == key:
      #print("valid")
      valid = valid + 1
  return valid