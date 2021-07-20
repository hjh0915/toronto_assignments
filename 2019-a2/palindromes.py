"""Assignment 2: Palindromes"""


# Delete these two lines and write your Task 1 code here.  Don't forget to 
# run a2_simple_check.py to check parameter and return types, and style!

def is_palindrome_word(words: str) -> bool:
    """判断words是否为回文
    >>> is_palindrome_word("Madam, I'm Adam")
    False
    >>> is_palindrome_word("I'm a girl")
    False
    >>> is_palindrome_word("nurses run")
    True
    """
    if words.islower():
        words = words.replace(' ','')
        if words == words[::-1]:
            return True
    return False

def is_palindrome_phrase(words: str) -> bool:
    """即使words中有非字符，有大小写，也可以为回文
    >>> is_palindrome_phrase("Madam, I'm Adam")
    True
    >>> is_palindrome_phrase("I'm a girl")
    False
    """
    words = words.lower()
    s = ""
    for w in words:
        if w.isalpha():
            s += w
    if s == s[::-1]:
        return True
    return False

def get_odd_palindrome_at(words: str, position: int) -> str:
    """返回一段回文，在words中最长的奇数长度的回文，并且集中在指定索引位置
    >>> get_odd_palindrome_at("that nurses run is right", 10)
    'nurses run '
    """
    i = 0 
    s = []
    s1 = []
    while i < position < len(words)-i+1:
        x = words[position-i:position+i+1]
        if is_palindrome_word(x) and len(x)>1 and len(x)%2 != 0:
            s.append((x, len(x)))
        i = i + 1

    for a, b in s:
        s1.append(b)
        if b == max(s1):
            return a
        else:
            return ""
        

if __name__ == '__main__':
    # pass

    # Uncomment the next two lines to run the examples in your docstrings.
    import doctest
    doctest.testmod()
