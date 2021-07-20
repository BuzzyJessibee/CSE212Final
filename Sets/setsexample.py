def unique_letters(text):
    """ 
    Determine if there are any duplicate letters in the text provided
    """
    # Compare all letters to all other letters
    for i in range(len(text)):  
        for j in range(len(text)):
            if i != j:  # Don't want to compare to yourself ... that will 
                        # always result in a match.
                if text[i] == text[j]:
                    return False
    return True

# Tests
test1 = "abcdefghjiklmnopqrstuvwxyz"  # Expect True because all letters unique
print(unique_letters(test1))

test2 = "racecar"  # Expect False because r,a,c are repeated
print(unique_letters(test2))

test3 = "" 
print(unique_letters(test3))          # Expect True because its an empty string