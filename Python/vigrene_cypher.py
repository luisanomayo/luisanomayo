#key = 'hello'
#key_list = list(key)
#alpha_index = ' abcdefghijklmnopqrstuvwxyz'
#alpha_cap_index = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#key_index = []

"""def finding_key_index (key):
	for alpha in alpha_index:
		index = 0
		while index <= len(key_list) - 1:
			if alpha == key_list[index]:
				key_index.append (alpha_index.find(alpha))
			index += 1
	return key_index"""


"""def finding_cap_key_index (key):
	for alpha in alpha_cap_index:
		index = 0
		while index <= len(key_list) - 1:
			if alpha == key_list[index]:
				key_index.append (alpha_cap_index.find(alpha))
			index += 1
	return key_index"""

#determine the index of the key

#key = "HELLO"


alpha_lowcap =  ' abcdefghijklmnopqrstuvwxyz'
alpha_cap = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

low_alpha = 'abcdefghijklmnopqrstuvwxyz'
cap_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'      

def finding_key_index (key):
	key_list = list(key)
	key_index = []
	for char in key_list:
		if char in alpha_cap:
			key_index.append(alpha_cap.find(char))
		elif char in alpha_lowcap:
			key_index.append(alpha_lowcap.find(char))
	return key_index

key = 'amen'
key_index = finding_key_index(key)
plain_text = "hello everyone"

"""def vigrene_cypher(plain_text):
	encrypted_text = ''
	for char in plain_text:
		for index in key_index:
			if char in alpha_lowcap:
				text_index = alpha_lowcap.index(char) + index
				encrypted_text += alpha_lowcap[text_index]
			elif char  in alpha_cap:
				text_index = alpha_cap.index(char) + index
				encrypted_text += alpha_cap[text_index]
			else:
				encrypted_text += char
	return(encrypted_text)"""

"""def vigrene_cypher():
	encrypted_text = ''
	for char in plain_text:
		if char in alpha_lowcap:
			for index in key_index:
				text_index = alpha_lowcap.index(char)+index
				if text_index <= 26:
					encrypted_text += alpha_lowcap[text_index]
				else:
					encrypted_text += alpha_lowcap[26]
				if len(encrypted_text) == len(plain_text):
					break
	return encrypted_text"""



def vigrene_cypher ():
  encrypted_word = ''
  for char in plain_text:
    
    if char in alpha_lowcap:
      
      char_index = alpha_lowcap.index(char)
      for index in key_index:
      	
      	encrypt_index = char_index + index
      	if encrypt_index <= 26:
     		
      		encrypted_word += alpha_lowcap[encrypt_index]
      	else:
      		encrypted_word += alpha_lowcap[26]
      
    elif char in alpha_cap:
    	char_index = alpha_cap.index(char)
    	for index in key_index:
    		encrypt_index = char_index +index
    		if encrypt_index <= 26:
    			encrypted_word += alpha_cap[encrypt_index]
    		else:
    			encrypted_word += alpha_cap[26]  
    else:
      encrypted_word += char
  return encrypted_word

print (vigrene_cypher()) 