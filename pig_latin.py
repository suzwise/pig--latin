# convert regular words into something more confusing

original=input("please enter a sentence  ").strip().lower()
 #split the sentence into words 
words = original.split()

# loop through words and convert to pig latin
new_words=[]
for word in words:
    if word[0] in "aeiou":    # if vowel add yay
        new_word= word +"yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:    # lookin out for the vowel
            if letter not in "aeiou":  
                vowel_pos=vowel_pos + 1
            else:
                break
        cons= word[:vowel_pos]
        the_rest=word[vowel_pos:]
        new_word = the_rest + cons +"ay"
        new_words.append(new_word) 



output ="".join(new_words)  # stick the word back together
print(output)


