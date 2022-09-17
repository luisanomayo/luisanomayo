key = input ('Enter your Desired Key: ')
plain_text = input('Enter The Text to be Encrypted:')
alpha_lowcap =  ' abcdefghijklmnopqrstuvwxyz'
alpha_cap = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#create index from the key given
def finding_key_index (key):
	key_list = list(key)
	key_index = []
	for char in key_list:
		if char in alpha_cap:
			key_index.append(alpha_cap.find(char))
		elif char in alpha_lowcap:
			key_index.append(alpha_lowcap.find(char))
	return key_index
  
key_index = finding_key_index(key)


#create index from the key given
def finding_key_index (key):
	key_list = list(key)
	key_index = []
	for char in key_list:
		if char in alpha_cap:
			key_index.append(alpha_cap.find(char))
		elif char in alpha_lowcap:
			key_index.append(alpha_lowcap.find(char))
	return key_index

#import cycle from itertools for infinite iteration over the key_index list
#this is needed when `len(plain_text)` is longer than the lenght of the key given
from itertools import cycle

#to iterate/loop over the key_index for as long as needed
keyindex_cycle = cycle(key_index)

#function to implement the move through the infinite iteration/loop
def next_keyindex():
	return next(keyindex_cycle)

#main cypher function
def vigrene_cypher():
	#the cypher outputed when the function is called
	encrypted_text = ''
	#loop through the plain text inputted
	for char in plain_text:
		#to main any spaces included in the plain text
		if char == ' ':
			encrypted_text += ' '
		else:
			#check if each character in the plain text is lower case
			if char in alpha_lowcap:
				#call infinite loop function and place the current iterate in a variable 
				#for use to update the index of each character in the plain text
				keyindex = next_keyindex()
				char_index = alpha_lowcap.index(char)
				#create index for each encryption
				encrypt_index = char_index + keyindex
				#to resolve index out of range. 
				if encrypt_index <= 26:
					encrypted_text += alpha_lowcap[encrypt_index]
				else:
					encrypted_text += alpha_lowcap[26]
			#check if each character in the plain text is upper case		
			elif char in alpha_cap:
				char_index = alpha_cap.index(char)
				encrypt_index = char_index + keyindex
				if encrypt_index <= 26:
					encrypted_text += alpha_cap[encrypt_index]
				else:
					encrypted_text += alpha_cap[26]
			#to maintain non alphabets included in plain text		
			else:
				encrypted_text += char
	return (encrypted_text)
