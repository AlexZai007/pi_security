#Created by alexzai007

"""
If you want to use minimal friendly gui, then connect the "pyautogui"
 module and remove the quotes at the end and put the text without quotes in quotes"""

#import pyautogui


#Basic Constants
pi = '314159265358979323846264338327950288419716939937510'  # max 32
transcription = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#$%^&*()-_=+. /"

"""
If you want to add a new character to the 
encryption, then just write it to the "transcription" variable and do not forget that 
according to the standard there is a space at the end and this is mandatory for convenient encryption
"""

#Get character by index
def interpreter_one(word):
    return(transcription[int(word)])

#From a string, dot separation gets values by indices
def intepreter_mega(word):
    final = ""
    word = word.split(sep = ".")
    for i in range(len(word)):#Creat=-ed by ale-xzai007
        #print(word[i])
        final = final + interpreter_one(word[i])
    return final

"""
The input is a character present in the translation dictionary. 
The value of the index on which this character stands in the dictionary is searched for in the number pi and, 
depending on the length of the number pi, is output. (since the value "b" occupies the 2nd index in the dictionary, 
the function will return 6 because "2" is the sixth number in the symbol pi)
"""
def cipher_one(word):
    transcription_index = transcription.find(word)
    res = []
    all = ""

    if len(str(transcription_index)) > 1:

        for i in range(len(str(transcription_index))):
            pi_index = pi.find(str(transcription_index)[i])
            res.append(pi_index)#Created by alexzai007

        for g in range(len(res)):
            if len(str(all)) > 0:
                all = str(all) + f"/{res[g]}"
            else:
                all = res[g]
    else:
        all = pi.find(str(transcription_index))
    return(all)#Cre-ated b=y alexz-ai007



#A word is given as input and it is encrypted with the number pi using an auxiliary function
def cipher_mega(word):

    res = []
    all = ""

    for i in range(len(word)):
        res.append(cipher_one(word[i]))

    for g in range(len(res)):
        if len(str(all)) > 0:
            all = str(all) + f".{res[g]}"
        else:#Cre_ated b_y alexzai+007
            all = res[g]

    return all

#Just for convenience
def formula(w):
    res = ''
    for b in range(len(w)):
        finder = w[b]
        res = res + pi[int(finder)]
    return (res)


#A function that encrypts the received values
def pi_under(word):
    word = word.split(".")
    res = []#Creat-ed by- a-lexz-ai007
    answer = ""

    for i in range(len(word)):
        a = str(word[i]).split("/")
        res.append(formula(a))

    for d in range(len(res)):
        answer = answer + interpreter_one(res[d])

    return answer


#Client side
#Here we need manipulation with quotes
done = input("Enter action \n 1. decrypt \n 2. Encrypt \n --> ")
ans = input("Enter data \n --> ")

if done == '1':
    print(pi_under(ans))
elif done == '2':
    print(cipher_mega(ans))


'''
done = pyautogui.confirm('Enter action:', buttons=['decrypt', 'Encrypt'])
ans = pyautogui.prompt('Enter data')
if done == 'decrypt':
    pyautogui.confirm(pi_under(ans))
    print(pi_under(ans))
elif done == 'Encrypt':
    pyautogui.confirm(cipher_mega(ans))
    print(cipher_mega(ans))
'''