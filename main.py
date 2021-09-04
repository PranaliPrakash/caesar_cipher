alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:    #iterating through the input start_text
    if char not in alphabet: #not in list
      end_text+= char        #if not in list add the char as it is in the end_text string
    else:  
      position = alphabet.index(char)      #for char in list
      new_position = position + shift_amount
      end_text += alphabet[new_position]
      
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?

choice="yes"
while choice=="yes":

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # if the user enters a shift that is greater than the number of letters in the alphabet

  if shift>26:
    condition=True
    while(condition==True):
      if shift%26==0:
        shift=shift//26    #shift=quotient as remainder=0
      
      else:
        shift=shift%26  #shift=remainder

      if shift<=26:
        condition=False  #condition to exit the loop

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  choice= input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()

print("goodbye")  