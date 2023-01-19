from random_word import RandomWords
import termcolor
import pyfiglet
import pymysql

'''
# Currently broken, working on a V2
'''

# This part is dedicated to connecting to MySQL
connection = pymysql.connect(host='localhost',user='root',password='Admin',db='entries')
cursor = connection.cursor()


# This part is dedicated to generating the random word so that we can test our logic against it
random_word = RandomWords()

word = random_word.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective", minDictionaryCount = 3, minLength=5, maxLength=5)
word_list = list(word.upper())
print(word)

# This part is dedicated to deciding how many chances the user is to be given (to be finished)
tries_left = 6

# This part is dedicated to testing and displaying wether our user has got the answer right or not
while tries_left != 0:
    print("Tries left = ", tries_left)
    user_int_str = input("Please enter your guess: ")
    user_int = list(user_int_str.upper())

# This part makes sure that the entry given by the user is in a clean format (capitalised, letters only and 5 entries)
    while len(user_int) != 5:
# Test for 5 entries only
        print("Please enter only 5 words in your guess")
        user_int_str = input("Please enter your guess: ")
        user_int = list(user_int_str.upper())
        continue

    for char in user_int:
        if char not in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
# Test for only letter entries
            print("Please enter only English letters (A,B,C.... etc)")
            print(f"{char} is not a valud input")
        continue

# Test for checking if the word is a real word or not
    x = ()
    while x == ():
        sql = "select * from entries where word like '%s' ;" %(user_int_str)
        cursor.execute(sql)
        x = cursor.fetchall()
        if x == ():
            print("Sorry, word entered is not found in the dictionary, please try again")
            print("Please enter only 5 letter English words (there,heard.... etc) ")
            user_int_str = input("Please enter your guess :")
            user_int = list(user_int_str.upper())
            sql = "select * from entries where word like '%s' ;" %(user_int_str)
            cursor.execute(sql)
            x = cursor.fetchall()
            continue
        
    print(user_int)

    num = [0,1,2,3,4]
    correct_entries = 0
    output = ""
    for char in num :
        if user_int[char] == word_list[char]:
            temp = termcolor.colored(user_int[char], on_color="on_green")
            correct_entries += 1
            output += temp
            output += " "
        elif user_int[char] in word_list:
            temp = termcolor.colored(user_int[char], on_color="on_yellow")
            
            output += temp
            output += " "
        else:
            temp = termcolor.colored(user_int[char], on_color="on_grey")
            
            output += temp
            output += " "
    
    print(output)
    
    if correct_entries == 5:
        print("Congratulations, you've guessed the word!")
        break
    output = ""
    tries_left -= 1
    correct_entries = 0

    if tries_left == 0:
        print("Sorry, game over")
        break

print("\nThank you for playing")