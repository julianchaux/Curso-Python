import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  new_key = ""
  shift1 = shift
  for i in text:
    index1 = alphabet.index(i)
    #26
    if index1 + shift > len(alphabet)-1:
      shift1 = index1 + shift - len(alphabet)
      new_key += alphabet[shift1]
    else:
      shift1 = shift
      new_key += alphabet[index1 + shift1]    
  print(f"The encoded text is {new_key}")

def decrypt(text, shift):
  new_key = ""
  shift1 = shift
  for i in text:
    index1 = alphabet.index(i)
    #26
    if index1 - shift < 0:
      shift1 = index1 - shift
      new_key += alphabet[shift1]
    else:
      shift1 = shift
      new_key += alphabet[index1 - shift1]    
  print(f"The encoded text is {new_key}")

print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)