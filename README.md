# Encryption with a very complex principle


| Letters       |       INDEX        |
|:-------------:|:------------------:|
| A  | 0 |
| B  | 1 |
| C  | 2 |
| D  | 3 |
| E  | 4 |
...
| Z  | 32|



### STEP 1 (INTPUT: Z)
To process the request, we find the character that we received as input and remember the index in the dictionary
In this example, we received "Z" as input, the index in the dictionary is 32, the name for the simplicity is "LetterIndex"

### Step 2
3.1  4  1  5  9  2  6  5  3  5  8  9  7 9  3

At the moment we see that LetterIndex is 32 the program at this point divides the values into 3 and 2. 
Now we find the value 3 in pi, it is in position 0. (remember). 
We do the same with the value 2, it is in 6th place in the number pi. 

### Step 3 (OUTPUT: 0/6)
At the output of the second stage, we got the values 0 6 remember that at the output of the first stage we had a two-digit number, which means that in order to give the correct answer, we take and put the sign "/"

And that the correct answer is 0/6

# Features
1. We gave an example with only one meaning but not a word or text. When processing text or words, the program uses to separate characters. This further confuses those who do not know how the algorithm works.

2. This algorithm uses only 11 characters to create an answer, which means that when using a dictionary with 11 characters, we will reduce the space in the file by more than 12 times. That is, we provided a algorithm that not only encrypts messages, but also compresses them. Further, you can apply another compression method, as in the binary system, the rows 0 and 1 were removed, write down how many 0 and 1 were used

3. If a value is not found in your dictionary, then the program put -1 in the answer. And when decrypted, it will be replaced by a space

# Examples

| Data       |       Result        |
|:-------------:|:------------------:|
| Hello World!  | 1/4.11.6/6.6/6.6/11.13/13.2/4.6/11.0/2.6/6.7.7/6 |
| The program was created by alexzai007  | 0/5.1/2.11.13/13.0/32.0/2.6/11.1/6.0/2.32.6/2.13/13.2/2.32.0/7.13/13.2.0/2.11.32.0/11.11.7.13/13.6.2/11.13/13.32.6/6.11.2/7.4/32.32.1/7.7/1.7/1.4/11 |
| Discord(admin@discord.com) - admin - 123456789best  | 13.1/7.0/7.2.6/11.0/2.7.13/32.32.7.6/2.1/7.6/7.7/0.7.1/7.0/7.2.6/11.0/2.7.13/7.2.6/11.6/2.13/1.13/13.13/6.13/13.32.7.6/2.1/7.6/7.13/13.13/6.13/13.4/6.4/0.4/2.4/4.4/7.4/13.4/11.4/5.7/32.6.11.0/7.0/11
 |
