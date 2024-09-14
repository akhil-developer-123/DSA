#Create a program to count the number of vowels in a given string

# a,e,i,o,u, A, E, I, O, U

def countVowels(s): # "akhil is coding. Aakash is also coding"
    answer = 0
    vowels = 'aeiouAEIOU'
    for character in s:
        if character in vowels:
            print(character)
            answer += 1 
    return answer

result = countVowels("akhil is coding. Aakash is also coding")
print(result)
