def caeser_cipher(message, shift):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  specialChar = "!@#$%^&*()_+\{\}[]<>/?\|,."
  encrypted = ''
  # Making a for loop for interating all the alphabet from text 
  for char in message:  
    if char == ' ':
      encrypted += char

    elif char in specialChar:
      encrypted += char

    elif char in alphabet:
      # Shifting the index of character in text 
      new_charIndex = (alphabet.index(char) + shift) % len(alphabet)
      encrypted += alphabet[new_charIndex]  # Cancatinating the character 

    elif char in ALPHABET:
      new_charIndex = (ALPHABET.index(char) + shift) % len(ALPHABET)
      encrypted += ALPHABET[new_charIndex]  # Cancatinating the character

  return encrypted


def main():
  text = input("Enter the message you want to hide: ")
  shift = int(input("Enter the Key value: "))
  print(caeser_cipher(message=text, shift=shift))

main()