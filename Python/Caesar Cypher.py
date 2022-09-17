enter_key =int(input("Enter your desired index: "))
plain_text = input("Enter the text you wish to encrypt:")

def ceasar_cypher ():
  cap_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  low_alphabets = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_word = ""
  for alphabet in plain_text:
    if alphabet in cap_alphabets:
      alphabet_index = cap_alphabets.index(alphabet)
      alphabet_index += enter_key
      encrypted_word += cap_alphabets[alphabet_index]
    elif alphabet in low_alphabets:
      alphabet_index = low_alphabets.index(alphabet)
      alphabet_index += enter_key
      encrypted_word += low_alphabets[alphabet_index]
    else:
      encrypted_word += alphabet
  return encrypted_word

print (ceasar_cypher()) 
  
