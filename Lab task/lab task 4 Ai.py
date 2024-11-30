#!/usr/bin/env python
# coding: utf-8

# In[1]:


def luhn_check(card_number):
    card_number = ''.join(filter(str.isdigit, card_number))
    digits = [int(d) for d in card_number]
    total_sum = 0
    for i in range(len(digits)):
        digit = digits[i]
        if (len(digits) - i) % 2 == 0:  
            doubled = digit * 2
            if doubled > 9: 
                total_sum += (doubled - 9)
            else:
                total_sum += doubled
        else:
            total_sum += digit
    return total_sum % 10 == 0
card_number = "4539 1488 0343 6467"
is_valid = luhn_check(card_number)
print(f"The card number {card_number} is {'valid' if is_valid else 'invalid'}.")


# In[2]:


def remove_punctuations(input_string):
    punctuation_marks = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    return input_string.translate(str.maketrans('', '', punctuation_marks))
user_input = input("Enter a string: ")
print("Original string:", user_input)
result = remove_punctuations(user_input)
print("String without punctuations:", result)


# In[3]:


def sort_with_builtin(input_string):
    return ''.join(sorted(input_string))
input_string = input("Enter a word: ")
sorted_string = sort_with_builtin(input_string)
print("Sorted word:", sorted_string)


# In[ ]:




