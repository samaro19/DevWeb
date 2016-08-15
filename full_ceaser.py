def Encode():
  ALPHABET = {
      '!': -2,
      '?': -1,
      ' ': 0,
      'a': 1,
      'b': 2,
      'c': 3,
      'd': 4,
      'e': 5,
      'f': 6,
      'g': 7,
      'h': 8,
      'i': 9,
      'j': 10,
      'k': 11,
      'l': 12,
      'm': 13,
      'n': 14,
      'o': 15,
      'p': 16,
      'q': 17,
      'r': 18,
      's': 19,
      't': 20,
      'u': 21,
      'v': 22,
      'w': 23,
      'x': 24,
      'y': 25,
      'z': 26,
  }
  word = input("Word: ")
  enc = []
  if word != '':
    word.split()
    for msg in word:
      lowerCase = msg.lower()
      print(ALPHABET[lowerCase])
      enc.append(int(ALPHABET[lowerCase]) + 3)
  enc = str(enc)
  print(" ")
  print(enc)
def Decode():
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

while 0 != 1:
  DorE = input("If you would like to decode a message input D, if you would like to encode a message input E: ")
  if DorE == "D":
    decode = Decode()
  if DorE == "E":
    encode = Encode()
  else:
    print("Please enter a valid letter (D or E)")
  
