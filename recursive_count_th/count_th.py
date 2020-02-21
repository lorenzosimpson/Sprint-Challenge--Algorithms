'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # want it to return how many 'th' occurs in the word
    target = 'th'

    def count_helper(word, count):
        print(word, count)
        if len(word) > 1:
            if word[:len(target)] == target:
                return count_helper(word[1:], count + 1)
            else:
                return count_helper(word[1:], count)
        else:
            return count
    
    counter = count_helper(word, 0)
    return counter
  

print(count_th('abcthabcthth'))