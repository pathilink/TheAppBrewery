alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet duplicated

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_position):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
# '''
    plain_text_index = []
    encode_index = []
    cipher_text = ''

    for char in plain_text:
        plain_text_index.append(alphabet.index(char))
    # print(plain_text_index)

    for i in plain_text_index:    
        encode_index.append(i + shift_position)
    # print(encode_index)

    for j in encode_index:
        cipher_text += ' '.join(alphabet[j])
    # print(cipher_text)  
# '''

    '''TEMPLATE
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        print(position)
        new_position = position + shift_position
        print(new_position)
        new_letter = alphabet[new_position]
        print(new_letter)
        cipher_text += new_letter
        print(cipher_text)
    '''
    
    print(f"The encoded text is {cipher_text}")
    
    
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)
