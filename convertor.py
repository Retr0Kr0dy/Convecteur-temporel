import math

def main():
    print ("""       
--____-___--____-_---_-_____--____-_| |_-___---____--
 / ___) _ \|  _ \ | | | ___ |/ ___|_   _) _ \ / ___)
( (__| |_| | | | \ V /| ____| |     | || |_| | |    
 \____)___/|_| |_|\_/ |_____)_|      \__)___/|_|    
-----------------------------------------------------                                          
""")
    print ("Choose a pills.\n\n")
    print ("[1] - DEC -> BIN\n[2] - BIN -> DEC\n[3] - DEC -> HEX\n[4] - HEX -> DEC\n[5] - BIN -> HEX\n[6] - HEX -> BIN\n")
    to_do = input("\nEnter a number : ")
    if to_do == 1:
        DECtoBIN()
    if to_do == 2:
        BINtoDEC()

def DECtoBIN():
    response = []
    num = int(input("\nEnter a decimal value : "))
    a = num
    if a % 2 == 0:
        x = 0
        response.append(x)
    else:
        x = 1
        response.append(x)
    while a > 1:
        a = a / 2
        a = math.trunc(a)
        if a % 2 == 0:
            x = 0
            response.append(x)
        else:
            x = 1
            response.append(x)
    response.reverse()
    response = ''.join([str(element) for element in response])
    r_response = f"DEC ; {num} ==> BIN ; {response}"
    print (r_response)

def BINtoDEC():
    response = []
    r = 0
    question = []
    num = (input("\nEnter a binary value : "))
    for element, a in enumerate(num):
        question.append(int(a))
    question.reverse()
    question = [int(i) for i in question]
    x = 0
    y = 1
    while question:
        if question[x] == 1:
            r = r + y
            question.pop(x)
            y = y * 2
        elif question[x] == 0:
            question.pop(x)
            y = y * 2
    else:
        r = f"BIN ; {num} ==> DEC ; {response}"
        print(r)

if __name__ == "__main__":
    main()
