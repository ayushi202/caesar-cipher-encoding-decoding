alphabet=[]
alpha = 'a'
for i in range(0, 26): 
    alphabet.append(alpha) 
    alpha = chr(ord(alpha) + 1)  

def encoding(shift,msg):
    encode=""
    for i in msg:
        if i==" ":
            encode+=" "
        else:
            position=alphabet.index(i)
            encode+=alphabet[(position+shift)%26]
    print(f"your encoded msg is {encode}")
def decoding(shift,msg):
    decode=""
    for i in msg:
        if i==" ":
            decode+=" "
        else:
            position=alphabet.index(i)
            decode+=alphabet[(position-shift)%26]
    print(f"your decoded message is {decode}")

    
print('''
                                                                                                                                        
                                                                               88             88                                 
                                                                               ""             88                                 
                                                                                              88                                 
 ,adPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" a8P_____88 ""     `Y8 I8[    "" ""     `Y8 88P'   "Y8    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         8PP""""""" ,adPPPPP88  `"Y8ba,  ,adPPPPP88 88            8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa "8b,   ,aa 88,    ,88 aa    ]8I 88,    ,88 88            "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"'  `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"' `"8bbdP"Y8 88             `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                  88                                             
                                                                                  88                       
        
        ''')
types=input("You want to encode or decode? enter 'encode' for encoding and 'decode' for decoding: ")
swift_number=int(input("Enter the swift number: "))
message=input("Enter the msg: ")
if types=="encode":
    encoding(swift_number,message)
if types=="decode":
    decoding(swift_number,message)
