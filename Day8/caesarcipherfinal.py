from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char.isdecimal() or char == " " or char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + (shift_amount % 26)
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
userinp = 'y'
while userinp == 'y':
  if userinp == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  userinp = input("Press Y to run again or any other key to exit.\n").lower()
  if userinp != "y":
    print("Goodbye.")