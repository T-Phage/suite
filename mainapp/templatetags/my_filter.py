from django import template
from django.utils.safestring import SafeString
 
register = template.Library()

@register.filter
def replace_punc(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    my_str = string

    # To take input from the user
    # my_str = input("Enter a string: ")

    # remove punctuation from the string
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct
    # return string.replace(':', '')

@register.filter
def to_string(sring):
    return str(sring)

@register.filter
def remove_user(string):
    
    return string[8:-1]
