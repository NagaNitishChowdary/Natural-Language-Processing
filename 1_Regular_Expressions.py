# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:48:04 2024

@author: Naga Nitish
"""

import re


# =============================================================================

# REGEX IN CUSTOMER SUPPORT

# =============================================================================


# Finding phone numbers using regular expressions
# Phone numbers can be seen as 2 ways 
# 1 ---> XXXXXXXXXX, (XXX)-XXX-XXXX

text = "My number is 9876543210 and another is (123)-456-7890 and my emails are \
     abcA@xyz.com, abX_82@google.com, knnc@har.com"

pattern = r'\d{10}'
# pattern = r'\d\d\d\d\d\d\d\d\d\d'

matches = re.findall(pattern,text)
matches
# ['9876543210']

pattern2 = r'\(\d{3}\)-\d{3}-\d{3}'
matches2 = re.findall(pattern2,text)
matches2
# ['(123)-456-789']

# match both type of phone numbers at the same time 
final_pattern = r'\d{10}|\(\d{3}\)-\d{3}-\d{4}'
final_matches = re.findall(final_pattern, text)
final_matches
# ['9876543210', '(123)-456-7890']

# =============================================================================

# Finding e-mails using regular expressions 

pattern3 = r'[a-z]*@'

matches3 = re.findall(pattern3, text)
matches3
# ['@', '@', 'knnc@']


pattern4 = r'[a-zA-Z]*@'

matches4 = re.findall(pattern4, text)
matches4
# ['abcA@', '@', 'knnc@']


prefinal_pattern2 = r'[a-zA-Z0-9_]*@'

prefinal_matches2 = re.findall(prefinal_pattern2, text)
prefinal_matches2
# ['abcA@', 'abX_82@', 'knnc@']


final_pattern2 = r'[a-zA-Z0-9_]*@[a-zA-Z0-9]*\.[a-zA-Z]*'

final_matches2 = re.findall(final_pattern2, text)
final_matches2
# ['abcA@xyz.com', 'abX_82@google.com', 'knnc@har.com']


# =============================================================================

# MINI-CHATBOT

chat1='codebasics: Hello, I am having an issue with my order # 412889912'
chat2='codebasics: I have a problem with my order number is 412889912'
chat3='codebasics: My order 4912 is having an issue, I was charged 300$ when online it says 280$'

pattern5 = r'order[^\d]*\d*'                 
# [^\d] --> anything other than number

matches5_1 = re.findall(pattern5, chat1)
matches5_1
# ['order # 412889912']

matches5_2 = re.findall(pattern5, chat2)
matches5_2
# ['order number is 412889912']

matches5_3 = re.findall(pattern5, chat3)
matches5_3
# ['order 4912']



_pattern5 = r'order[^\d]*(\d*)'   # () ---> to grab particular one 

_matches5_1 = re.findall(_pattern5, chat1)
_matches5_1
# ['412889912']


# =============================================================================

# * ---> zero or more 
# + ---> one or more 

# =============================================================================




# =============================================================================

# REGEX FOR INFORMATION EXTRACTION 

# =============================================================================

# Taken from WikiPedia

text1='''
Born	Elon Reeve Musk
June 28, 1971 (age 50)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa (1971–present)
Canada (1971–present)
United States (2002–present)
Education	University of Pennsylvania (BS, BA)
Title	
Founder, CEO and Chief Engineer of SpaceX
CEO and product architect of Tesla, Inc.
Founder of The Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI, and Zip2
Spouse(s)	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''


# EXTRACTING AGE 
age = r'age (\d+)'

re.findall(age, text1)
# ['50']


# EXTRACTING FULL NAME 
full_name = r'Born(.*)\n'

re.findall(full_name, text1)[0].strip()
# 'Elon Reeve Musk'


# EXTRACTING BIRTH DATE 
birth_date = r'Born.*\n(.*)\(age'

re.findall(birth_date, text1)[0].strip()
# 'June 28, 1971'


# EXTRACTING BIRTH PLACE
birth_place = r'\(age \d+\)\n(.*)'

re.findall(birth_place, text1)[0].strip() 
# 'Pretoria, Transvaal, South Africa'



def extract_personal_details(text1):
    _age = re.findall(age, text1)
    _full_name = re.findall(full_name, text1)
    _birth_date = re.findall(birth_date, text1)
    _birth_place = re.findall(birth_place, text1)
    
    return {
        'age' : int(_age[0]),
        'name' : _full_name[0].strip(),
        'birth_date' : _birth_date[0].strip(),
        'birth_place' : _birth_place[0].strip(),
        }

extract_personal_details(text1)

"""
{'age': 50,
 'name': 'Elon Reeve Musk',
 'birth_date': 'June 28, 1971',
 'birth_place': 'Pretoria, Transvaal, South Africa'}
"""



text2 = '''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 64)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Stanford University (drop-out)
Occupation	Chairman and MD, Reliance Industries
Spouse(s)	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent(s)	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''

extract_personal_details(text2)
"""
{'age': 64,
 'name': 'Mukesh Dhirubhai Ambani',
 'birth_date': '19 April 1957',
 'birth_place': 'Aden, Colony of Aden'}
"""

# =============================================================================
