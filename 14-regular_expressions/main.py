# Regular Expressions
# Regular expressions are patterns used to match or search for specific text patterns in a string.

# Import the re module, which provides support for regular expressions in Python
import re

# Example 1: Matching a string
# The pattern 'hello' matches the string 'hello'
print(re.search('hello', 'hello world'))            # Output: <re.Match object; span=(0, 5), match='hello'>

# Example 2: Matching a digit
# The pattern '\d' matches any digit
print(re.search('\d', 'hello123'))                  # Output: <re.Match object; span=(5, 6), match='1'>

# Example 3: Matching a word character (alphanumeric plus underscore)
# The pattern '\w' matches any word character
print(re.search('\w', 'hello_world'))               # Output: <re.Match object; span=(0, 1), match='h'>

# Example 4: Matching a whitespace character
# The pattern '\s' matches any whitespace character
print(re.search('\s', 'hello world'))               # Output: <re.Match object; span=(5, 6), match=' '>

# Example 5: Matching a non-digit
# The pattern '\D' matches any non-digit
print(re.search('\D', 'hello123'))  # Output: <re.Match object; span=(0, 1), match='h'>

# Example 6: Matching a non-word character
# The pattern '\W' matches any non-word character
print(re.search('\W', 'hello_world'))               # Output: <re.Match object; span=(5, 6), match='_'>

# Example 7: Matching a non-whitespace character
# The pattern '\S' matches any non-whitespace character
print(re.search('\S', 'hello world'))               # Output: <re.Match object; span=(0, 1), match='h'>

# Example 8: Matching the start of a string
# The pattern '^hello' matches the string 'hello' at the start of the string
print(re.search('^hello', 'hello world'))           # Output: <re.Match object; span=(0, 5), match='hello'>

# Example 9: Matching the end of a string
# The pattern 'world$' matches the string 'world' at the end of the string
print(re.search('world$', 'hello world'))           # Output: <re.Match object; span=(6, 11), match='world'>

# Example 10: Matching a character class
# The pattern '[abc]' matches any of the characters 'a', 'b', or 'c'
print(re.search('[abc]', 'helloabc'))               # Output: <re.Match object; span=(5, 6), match='a'>

# Example 11: Matching a negated character class
# The pattern '[^abc]' matches any character that is not 'a', 'b', or 'c'
print(re.search('[^abc]', 'helloabc'))              # Output: <re.Match object; span=(0, 1), match='h'>

# Example 12: Matching a range of characters
# The pattern '[a-zA-Z]' matches any letter (either uppercase or lowercase)
print(re.search('[a-zA-Z]', 'helloABC'))            # Output: <re.Match object; span=(0, 1), match='h'>

# Example 13: Matching a repeated pattern
# The pattern 'a*' matches zero or more occurrences of the character 'a'
print(re.search('a*', 'helloaa'))                   # Output: <re.Match object; span=(0, 0), match=''> (matches an empty string)

# Example 14: Matching a repeated pattern (at least one occurrence)
# The pattern 'a+' matches one or more occurrences of the character 'a'
print(re.search('a+', 'helloaa'))                   # Output: <re.Match object; span=(5, 7), match='aa'>

# Example 15: Matching a repeated pattern (exactly n occurrences)
# The pattern 'a{3}' matches exactly three occurrences of the character 'a'
print(re.search('a{3}', 'helloaaa'))                # Output: <re.Match object; span=(5, 8), match='aaa'>

# Example 16: Matching a repeated pattern (at least n occurrences)
# The pattern 'a{3,}' matches three or more occurrences of the character 'a'
print(re.search('a{3,}', 'helloaaaa'))              # Output: <re.Match object; span=(5, 9), match='aaaa'>

# Example 17: Matching a repeated pattern (at most n occurrences)
# The pattern 'a{,3}' matches zero to three occurrences of the character 'a'
print(re.search('a{,3}', 'hello'))                  # Output: <re.Match object; span=(0, 0), match=''> (matches an empty string)

# Example 18: Matching a phone number
phone_number = "Call me at 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"  # \d matches any digit, {3} matches exactly 3 times
match = re.search(pattern, phone_number)
if match:
    print("Phone number:", match.group())           # Output: Phone number: 123-456-7890
    

# Example 19: Matching an email address
email = "My email is john.doe@example.com."
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"  # [] matches any character inside, + matches one or more times
match = re.search(pattern, email)
if match:
    print("Email:", match.group())                  # Output: Email: john.doe@example.com
    

# Example 20: Matching a date (YYYY-MM-DD)
date = "My birthday is 1990-02-28."
pattern = r"\d{4}-\d{2}-\d{2}"                      # \d matches any digit, {4} matches exactly 4 times, etc.
match = re.search(pattern, date)
if match:
    print("Date:", match.group())                   # Output: Date: 1990-02-28
   

# Example 21: Matching a credit card number (with spaces)
credit_card = "My credit card number is 1234 5678 9012 3456."
pattern = r"\d{4} \d{4} \d{4} \d{4}"                # \d matches any digit, {4} matches exactly 4 times, space matches a space
match = re.search(pattern, credit_card)
if match:
    print("Credit card number:", match.group())     # Output: Credit card number: 1234 5678 9012 3456
    
print("---")

# Advanced Example: Matching multiple groups (name, email, phone number)

text = "My name is John Doe, email is john.doe@example.com, and phone number is 123-456-7890."
pattern = r"My name is ([a-zA-Z ]+), email is ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+), and phone number is (\d{3}-\d{3}-\d{4})"  # () creates a group, [a-zA-Z ]+ matches one or more letters or spaces
match = re.search(pattern, text)
if match:
    print("Name:", match.group(1))                  # Extract the first group (name)
    print("Email:", match.group(2))                 # Extract the second group (email)
    print("Phone number:", match.group(3))          # Extract the third group (phone number)
    # Output:
    # Name: John Doe
    # Email: john.doe@example.com
    # Phone number: 123-456-7890

# Accessing groups
print("match.groups():", match.groups())            # Output: match.groups(): ('John Doe', 'john.doe@example.com', '123-456-7890')

# Iterate over the groups
for group in match.groups():
    print("Group:", group)
    # Output:
    # Group: John Doe
    # Group: john.doe@example.com
    # Group: 123-456-7890   