import random
characters = ['a', 'b', 'c',' ','ç', 'd','.', 'e', 'f','*', 'g','ğ','!', 'h','ı',
               '?', 'i','+','-', 'j', 'k',':', 'l', 'm', 'n', 'o','ö', 'p', 'q','4', 'r',
               's','ş','0','3', 't', 'u','ü', 'v','2', 'w', 'x','5', 'y', 'z','A','B','C',
               '1','Ç','D','E','F','6','G','Ğ','H','I','8','7','İ','J','K','L','M','N','O',
               'Ö','P','9','Q','R','S','Ş',';','T','U','Ü','V','W',',','X','Y','Z','\n','/']

while True:
    operation = int(input("Write 1 for encrypt, 2 for decrypt, 3 for exit: "))
                
    if operation == 1:
        text = input("Text: ")
        textList = []
        txtNumList =[]
        newTxtList = []
        newTxt = ''
        key = ''
        keyRnd = int(input("Write 1 for generate random key, write 2 for write your own key:  "))
        
        if keyRnd == 1:                
            for a in range(10):    
                key = key + str(random.randint(1,9))
            
        elif keyRnd == 2:
            key = input("Please write your key (must be 10 numbers without 0): ")
            
        print(key)
        
        for a in range(len(text)):
            textList.append(text[a])    
            txtNumList.append(characters.index(text[a]))
        
        for a in range(len(textList)):
            if (a+1)%30 == 0 :
                txtNumList[a] += int(key[0])     
            elif (a+1)%15 == 0:
                txtNumList[a] += int(key[1])
            elif (a+1)%10 == 0:
                txtNumList[a] += int(key[2])
            elif (a+1)%6 == 0:
                txtNumList[a] += int(key[3])
            elif (a+1)%2 == 0 or a == 0:
                txtNumList[a] += int(key[4])
            elif (a+1)%3 == 0:
                txtNumList[a] += int(key[5])
            elif (a+1)%5 == 0:
                txtNumList[a] += int(key[6])
        
            txtNumList[a] += int(key[7])   
            
            if txtNumList[a]> (len(characters) -1):
                    txtNumList[a] -= len(characters)   
                    
        txtNumList.reverse()       
        
        for a in range(len(textList)):
            if a %2 == 0:
                txtNumList[a]+= int(key[8])
            else:
                txtNumList[a]+= int(key[9])
            if txtNumList[a]> (len(characters) -1):
                    txtNumList[a] -= len(characters)      
                    
        for a in range(len(txtNumList)):    
            newTxtList.append(characters[txtNumList[a]])
            
        for a in range(len(newTxtList)):
            newTxt = newTxt+newTxtList[a]
        print(newTxt)

    elif operation == 2:
        
        txtList = []
        txtNumList =[]
        newTxtList = []
        newTxt = ''
        
        text = input("Write encrypted text: ")
        key = input("Write key: ")
        
        for a in range(len(text)):
            txtList.append(text[a])    
            txtNumList.append(characters.index(text[a]))
            
        for a in range(len(txtList)):
            if a %2 == 0:
                txtNumList[a]-= int(key[8])
            else:
                txtNumList[a]-= int(key[9])
                
            if txtNumList[a]< 0:
                    txtNumList[a] += len(characters)
                    
        txtNumList.reverse() 
        
        for a in range(len(txtList)):
            
            txtNumList[a] -= int(key[7])
            
            if (a+1)%30 == 0 :
                txtNumList[a] -= int(key[0])     
            elif (a+1)%15 == 0:
                txtNumList[a] -= int(key[1])
            elif (a+1)%10 == 0:
                txtNumList[a] -= int(key[2])
            elif (a+1)%6 == 0:
                txtNumList[a] -= int(key[3])
            elif (a+1)%2 == 0 or a == 0:
                txtNumList[a] -= int(key[4])
            elif (a+1)%3 == 0:
                txtNumList[a] -= int(key[5])
            elif (a+1)%5 == 0:
                txtNumList[a] -= int(key[6])
        
            if txtNumList[a]> (len(characters) -1):
                txtNumList[a] -= len(characters)    
            
        for a in range(len(txtNumList)):    
            newTxtList.append(characters[txtNumList[a]])
            
        for a in range(len(newTxtList)):
            newTxt = newTxt+newTxtList[a]
        print(newTxt)
        
    elif operation == 3:
        print("Exit")
        break

