dict = {
    -2: '!',
    -1: '?',
    0: ' ',
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
}
message = input("input text to decode: ")
three_back = []
decoded = []
if message != '':
  message = message.split(", ")
  print(message)
  for msg1 in message:
    three_back.append(int(msg1) - 3)
  print(three_back)
  for msg in three_back:
    print(dict[int(msg)])
    decoded.append(dict[int(msg)])
print(" ")
print(''.join(decoded))
