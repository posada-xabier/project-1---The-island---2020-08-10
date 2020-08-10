

answer = "a"

while not answer == "quit":
    

    answer = input(" \n\n\n Do you want to 'cipher' or 'decrypt' or 'quit' ?  :  ")
        
    if answer == "decrypt":

        ciphertext = input("\n\n\n\tPlease, write the encrypted ciphertext :  ").lower()
        caesar_key_number = int(input("\n\n\n\tPlease, write the caesar_key_number,(0 < n < 25)  :  "))
        plaintext = []
        # plaintext = plaintext.lower()
        # caesar_key_number = 3

        # plaintext = "Mens sana in corpore sano".lower()
        # plaintext = input("introduce the text you want to encrypt")

        

        alfa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
        beto = ["o","p","q","r","s","t","u","v","w","x","y","z"]
        alfabeto = alfa + beto

        "key = the caesar number, that is, the shift parameter"
        k = caesar_key_number
        # caesar_key_letter = alfabeto[k]
        slice_a = alfabeto[0:k]
        slice_b = alfabeto[k:]
        clavicordio = slice_b + slice_a

        for x in ciphertext:    
            if x == " ":
                plaintext.append(" ")
            else:
                ordinal = -1
                for letter in clavicordio:
                    ordinal +=1
                    if letter == x:
                        plaintext.append(alfabeto[ordinal])        
                
        
        print("\n\n\t","The Plaintext is = ","".join(plaintext), "\n\n")




    if answer == "cipher":
        
        plaintext = input("\n\n\n\tPlease, intro the plain, open text you want to hide :  ").lower()
        
        caesar_key_number = int(input("\n\n\n\tPlease, intro the Caesar Key \n\t Number you want to use to hide the text (0 < n < 25)  :  "))

        # plaintext = "Mens sana in corpore sano".lower()
        # plaintext = input("introduce the text you want to encrypt")

        ciphertext = []

        alfa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
        beto = ["o","p","q","r","s","t","u","v","w","x","y","z"]
        alfabeto = alfa + beto

        "key = the caesar number, that is, the shift parameter"
        k = caesar_key_number
        # caesar_key_letter = alfabeto[k]
        slice_a = alfabeto[0:k]
        slice_b = alfabeto[k:]
        clavicordio = slice_b + slice_a

        for x in plaintext:    
            if x == " ":
                ciphertext.append(" ")
            else:
                ordinal = -1
                for letter in alfabeto:
                    ordinal +=1
                    if letter == x:
                        ciphertext.append(clavicordio[ordinal])        
                
        
        print("\n\n\t","The 'ciphertext' is = ","".join(ciphertext), "\n\n")






