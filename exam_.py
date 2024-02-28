# question 1
a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2
print(a)

# question 2
print(2+3*6/2)

# question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

# question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def palindrome(word):
    return word == word[::-1]

strings = [
    "0974101607733149676776769413377061014790",
    "4257304920394478392772938744930294037524",
    "2704702208931031198668911301398022074072",
    "7798338247658278460338648728567428338977"
]

for s in strings:
    if not palindrome(s):
        print(f"The string {s} is not a palindrome.")

# question 5
def find_pattern_occurrences(text):
    """
    Finds all occurrences of a pattern that starts with 'C', has any number of letters, and ends with 'jeb'.

    Args:
    - text (str): The text to search the pattern in.

    Returns:
    - int: The number of matches found in the text.
    """
    # Split the text into words
    words = text.split()
    # Initialize the count of matches
    count = 0
    # Iterate over each word in the text
    for word in words:
        # Check if the word starts with 'C' and ends with 'jeb'
        if word.startswith('C') and word.endswith('jeb'):
            count += 1
    return count


# Example usage:
text_to_search = "Conejeb is a pattern, Ctwojeb is another, but not Cjebend or startCjeb."
number_of_matches = find_pattern_occurrences(text_to_search)
print(f"Number of matches: {number_of_matches}")

# question 6

my_list = [1, 2, 3]
print("Original List:", my_list)

# Add a new element
my_list.append(4)
print("List after adding an element:", my_list)

# Remove an element
my_list.remove(2)
print("List after removing an element:", my_list)

my_string = "hello"
print("Original String:", my_string)

# Attempt to modify an element (this will produce an error)
try:
    my_string[0] = "H"
except TypeError as e:
    print("Error:", e)

# Create a new string by concatenation
my_string = "H" + my_string[1:]
print("New String after modification:", my_string)

# question 7
import random

# Generate the list of random numbers
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Continue by replacing the numbers greater than 80 with their corresponding negative value
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]

# Print the modified list
print(random_numbers)

# question 8
def is_valid_url(url):
    # Check if the URL starts with "http://" or "https://"
    if not (url.startswith('http://') or url.startswith('https://')):
        return False

    # Check if there is a space in the URL (which would be invalid)
    if ' ' in url:
        return False

    # If both checks pass, we consider the URL valid
    return True


# Example usage
print(is_valid_url("http://example.com"))  # Expected: True
print(is_valid_url("https://example.com"))  # Expected: True
print(is_valid_url("http://example com"))  # Expected: False
print(is_valid_url("://example.com"))  # Expected: False

# question 9
def days_since_birthday(birthday):
    # Extract the year from the birthday and convert it to an integer
    birth_year = int(birthday.split('-')[2])

    # Assume the current year as 2024, since we cannot import datetime to get the current year
    current_year = 2024

    # Calculate the number of full years since the birth year
    full_years = current_year - birth_year - 1

    # Calculate the number of leap years in the range
    leap_years = sum(1 for year in range(birth_year + 1, current_year)
                     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

    # Calculate the total number of days (365 for each full year plus one extra for each leap year)
    total_days = (full_years * 365) + leap_years

    return total_days


# Example usage
print(days_since_birthday("14-02-2003"))
