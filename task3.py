import wordtool

words = wordtool.get_nouns()
# for i in range(10):
#     print(words[i])

def has_all_characters(word, chlist) -> bool:
    """
    this function returns True if the word contains all characters in the chlist otherwise returns false
    """
    count = 0 
    for x in chlist:
        if x in word:
            count = count + 1

    if len(chlist) == count:
        return True
    return False

def find_word_containing(words, chlist):
    """
    this function print the last word from the list which has all characters in the chlist other wise print no word found against given chlist
    """
    position = -1
    while (len(words) + position) >= 0:
      # while loop here to find the last word (alphabetically) that contains all of the characters in the chlist and set the variable `position` to its index otherwise, do not change `position`` from -1
        if has_all_characters(words[position], chlist):
            position = len(words) + position
            break
        position = position - 1
 
    # This branch prints the result in expected format
    if position >= 0:
        print('Found', words[position], 'at position', position, 'containing', ', '.join(chlist))
    else:
        print('Did not find a word containing', ', '.join(chlist))
    
# words = wordtool.get_nouns()
find_word_containing(words, ['a','e','i','o','u'])
find_word_containing(words, ['a','s','d','f','g'])
find_word_containing(words, ['q','w','e','r','t'])
find_word_containing(words, ['l','m','n','o','p'])
find_word_containing(words, ['a','d','z','e'])