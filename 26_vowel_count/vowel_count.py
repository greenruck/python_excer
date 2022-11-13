Vowels = set("a,e,i,o,u")

def vowel_count(phrase):
    phrase = phrase.lower()
    count ={}
    for letter in phrase:
        if letter in Vowels:
            count[letter] = count.get(letter, 0) + 1
    return count
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """