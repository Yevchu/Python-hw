# new_file = open('cats.txt', 'w', encoding='utf-8')
# new_file.write('60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5')
# new_file.close()

# def write_employees_to_file(employee_list, path):
    
#     file = open(path, 'w')
    
#     for el in employee_list:
#         for employee_info in el:
#             new_info = employee_info + '\n'
#             res = file.write(new_info)

#     file.close()
#     return res


# def read_employees_from_file(path):

#     file = open(path, 'r')    
#     return [line.rstrip('\n') for line in file]
    
        

# print(read_employees_from_file('D:\python\employee_list.txt'))


# def add_employee_to_file(record, path):
    
#     file = open(path, 'a')
#     new_str = record + '\n'
#     file.close()
#     return file.write(new_str)
    
# def get_cats_info(path):  #-- повернення списку
    
#     res = []

#     with open(path, 'r') as file:

#         for cat_info in file:
#             cat = cat_info.strip().split(',')
#             new_list = {'id': cat[0],
#                         'name': cat[1],
#                         'age': cat[2]}
#             res.append(new_list)
            
#     return res
    
            
# print(get_cats_info('D:\python\cats.txt'))


# def get_recipe(path, search_id) -> list:

    
#     with open(path, 'r') as file:
        
#         for line in file:
#             recipe_info = line.strip('\n').split(',')
#             recipe = {
#                 'id': recipe_info[0],
#                 'name': recipe_info[1],
#                 'ingredients': recipe_info[2:]
#             }
#             if recipe.get('id') == search_id:
#                 return recipe
                    
# print(get_recipe('D:\python\get_recipe.txt', '60b90c3b13067a15887e1ae4'))
# source = [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]               
 
# def save_applicant_data(source, output):

#     with open(output, 'w') as file:
#         for el in source:
#             res = ''
#             for value in el.values():
#                 res += str(value) + ','
#             if el:
#                 file.writelines(res.removesuffix(',') + '\n')
                


# save_applicant_data(source,'D:\python\output.txt')
        
# users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}

# def save_credentials_users(path, users_info):
    
#     with open(path, 'wb') as file: 
#         for el_key, el_value in users_info.items():
#             print(el_key, el_value)
#             file.write(el_key.encode() + b':' + el_value.encode() + b'\n')
                    

# print(save_credentials_users('D:\python\output.txt', users_info))

# def get_credentials_users(path):
    
#     with open(path, 'rb') as file:
#         res = []
#         new_str = ''
#         decode_info = file.readlines()
#         for line in decode_info:
#             new_str = line.decode('utf-8').strip()
#             res.append(new_str)
#     return res
        
# print(get_credentials_users('D:\python\output.txt'))
            
    
# import base64

# def encode_data_to_base64(data):
#     b64_data = []
#     for users_info in data:
#         bite_users_info = users_info.encode('utf-8')
#         b64_user_info = base64.b64encode(bite_users_info)
#         b64_user_info_decode = b64_user_info.decode('utf-8')
#         b64_data.append(b64_user_info_decode)
#     return b64_data
# print(encode_data_to_base64(['andry:uyro18890D', 'steve:oppjM13LL9e']))

# import shutil

# employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}

# def create_backup(path, file_name, employee_residence):
    
#     with open(path + '/' + file_name, 'wb') as file:
#         for el_key, el_value in employee_residence.items():
#             new_str = el_key + ' ' + el_value + '\n'
#             b_new_str = new_str.encode('utf-8')
#             file.write(b_new_str)
#     new_archive = shutil.make_archive('backup_folder', 'zip', path)
#     return new_archive
            
# print(create_backup('D:\python', 'b_backup_file.txt', employee_residence))

# import shutil


# def unpack(archive_path, path_to_unpack):
    
#     shutil.unpack_archive(archive_path, path_to_unpack)

# import re
# def is_integer(s):

#     pattern = re.findall(r'[a-zA-Z]', s)
#     sanitize = s.strip()
#     if len(sanitize) == 0:
#         print('0')
#         return False
#     if len(pattern) != 0:
#         print(pattern)
#         return False
#     if all(i.isalnum() or i in "+-*/" for i in sanitize):
#         return True
#     else: 
#         return False 
    
# print(is_integer('+34'))
# def capital_text(s):
#     s = s.strip()
#     result = ""
#     count = 0
#     while count < len(s):
#         count + 1
#         for i in range(len(s)):
#             if i == 0 or s[i-1] in [".", "!", "?"]:
#                 result += s[i].upper()
#             elif s[i-2] in [".", "!", "?"]:
#                 result += s[i].upper()
#             else:
#                 result += s[i]
#         return result
    
# print(capital_text('alert. boss i need a help! oh'))

# def solve_riddle(riddle, word_length, start_letter, reverse=False):

#     if reverse:
#         riddle = riddle[::-1]
#     for i in range(len(riddle) - word_length + 1):
#         if riddle[i] == start_letter and riddle[i + word_length - 1] != start_letter:
#             return riddle[i:i + word_length]
#     return "" 
                         
# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     # Якщо параметр reverse=True, перевернути рядок ребуса
#     if reverse:
#         riddle = riddle[::-1]
#     # Перевірити кожну можливу позицію в рядку ребуса
#     for i in range(len(riddle) - word_length + 1):
#         # Якщо літера на поточній позиції - це літера start_letter
#         # і літера на позиції word_length - 1 позицій вправо від поточної позиції - не літера start_letter,
#         # то знайдено шукане слово
#         if riddle[i] == start_letter and riddle[i + word_length - 1] != start_letter:
#             return riddle[i:i + word_length]
#     # Якщо слово не знайдене, повернути пустий рядок
#     return ""

# print(solve_riddle('mi1powerpret', 5, 'p'))

# def data_preparation(list_data: list) -> list:

#     res = []

#     for el in list_data:
#         if len(el) > 2:
#             el.remove(min(el))
#             el.remove(max(el))
#             res.extend(el)
#         else:
#             res.extend(el)
#     res.sort(reverse=True)
#     return res

# print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))
    
# import re
# def token_parser(s: str) -> list:

#     pattern = r'\d+|[\(\)\*\+\-\/]'
#     token = re.findall(pattern, s)

#     return token


# print((token_parser("2+ 34-5 * 3")))
    
    

# def all_sub_lists(data):
    
#     res = [[]]

#     for i in range(len(data)):
#         for j in range(i, len(data)):
#             res.append(data[i:j+1])
#     res.sort(key=len)

#     return res

# print(all_sub_lists([4, 6, 1, 3]))
            
# def make_request(keys, values):

#     res = {}

#     if len(keys) != len(values):
#         return {}
#     for i in range(len(keys)):
#         res[keys[i]] = values[i]
#     return res

# print(make_request(['name', 'age', 'email'], ['Nick', '23', 'nick@test.com']))

# TRANS = {
#     '.':1,
#     ',':11,
#     '?':111,
#     '!':1111,
#     ':':11111,
#     'A':2,
#     'B':22,
#     'C':222,
#     'D':3,
#     'E':33,
#     'F':333,
#     'G':4,
#     'H':44,
#     'I':444,
#     'J':5,
#     'K':55,
#     'L':555,
#     'M':6,
#     'N':66,
#     'O':666,
#     'P':7,
#     'Q':77,
#     'R':777,
#     'S':7777,
#     'T':8,
#     'U':88,
#     'V':888,
#     'W':9,
#     'X':99,
#     'Y':999,
#     'Z':9999,
#     ' ':0
# }

# def sequence_buttons(string):
#     new_str = ''
#     for el in string:
#         for key, value in TRANS.items():
#             if el.upper() == key:
#                 new_str += str(value)
#     return new_str      
# print(sequence_buttons("Hello, World!"))


# def file_operations(path, additional_info, start_pos, count_chars):
#     with open(path, 'a') as file:
#         file.write(additional_info)
#     with open(path, 'r') as fh:
#         fh.seek(start_pos)
#         new_str = fh.read(count_chars)
#         return new_str
    
# print(file_operations('D:\python/autho_test/b_backup_file.txt', 'Hello', 10, 5))

# def get_employees_by_profession(path, profession):
#     res = []
#     with open(path, 'r') as file:
#         new_str = file.readlines()
#         for el in range(len(new_str)):
#             if new_str[el].find(profession) != -1:
#                 res.append(new_str[el])
#         joined_str = ''.join(res)
#         joined_str = joined_str.replace('\n', ' ')
#         joined_str = joined_str.replace(f' {profession}', '') 
#     return joined_str
# print(get_employees_by_profession('D:\python/autho_test/b_backup_file.txt', 'courier'))

# def to_indexed(source_file, output_file):
    
#     with open(source_file, 'r') as read_file:
#         with open(output_file, 'w') as file:
#             readed_line = read_file.readlines()
#             for el in range(len(readed_line)):
#                 line_dict = {el: readed_line[el]}
#                 file.write(f'{el}: {line_dict.get(el)}')
# print(to_indexed('D:\python/autho_test/b_backup_file.txt', 'D:\python/autho_test/new_file.txt'))

# def flatten(data):

#     if len(data) == 0:
#         return []
#     if isinstance(data[0], list):
#         return flatten(data[0] + flatten(data[1:]))
#     return data[:1] + flatten(data[1:])

# print(flatten([1, [2, 3, [4, 5, 6]], 7]))

# def decode(data):
    
#     res = []

#     if not data: 
#         return []
#     else:
#         for i in range(0, data[1]):
#             res.append(data[0])
#         data.remove(data[1])
#         data.remove(data[0])
#         decode(data)
#         return res

# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))


# def encode(data):
#     if not data:
#         return []
#     else:
#         first = data[0]
#         rest = data[1:]
#         count = 1
#         while rest and rest[0] == first:
#             count += 1
#             rest = rest[1:]
#         if count == 1:
#             return [first, count] + encode(rest)
#         else: 
#             return [first, count] + encode(rest)

# def get_days_from_today(date):
    
#     date = date.split('-')
#     date_from_arg = datetime(year=int(date[0]), month=int(date[1]), day=int(date[2])).date()
#     real_date = datetime.now().date()
#     print(real_date)
#     print(date_from_arg)
    
#     diference = real_date - date_from_arg
#     return diference.days
    
# print(get_days_from_today("2021-10-09"))

# def get_days_in_month(month, year):
    
#     date = datetime(year=year, month=month, day=1)
#     next_month = date.replace(day=28) + datetime.timedelta(days=4)
#     return (next_month - datetime.timedelta(datetime=next_month.day)).day

# from datetime import date

# def get_days_in_month(month, year):

#     if month == 12:
#         return (date(year + 1, 1, 1) - date(year, month, 1)).days
#     else:
#         return (date(year, month + 1, 1) - date(year, month, 1)).days

# print(get_days_in_month(12, 2022))

# from datetime import datetime


# def get_str_date(date):

#     date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fz')
    
#     return date.strftime('%A %d %B %Y')
    
# print(get_str_date('2021-05-27 17:08:34.149Z'))

# from random import randrange, sample


# def get_numbers_ticket(min, max, quantity):

#     if min < 1 or max > 1000 or min > quantity or quantity > max:
#         return []
#     else:
#         numb = [i for i in range(randrange(min, max))]
#         res = sample(numb, k=quantity)
#         res.sort()
#         return res

# print(get_numbers_ticket(1, 1000, 6))

# import random

# participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }

# def get_random_winners(quantity, participants):
    
#     if quantity > len(participants):
#         return []
#     else:
#         participants_id = list(participants.keys())
#         random.shuffle(participants_id)
#         res = random.sample(participants_id, k=quantity)
#         res.sort()
#         return res
    
# print(get_random_winners(2, participants))

# from decimal import Decimal, getcontext


# def decimal_average(number_list, signs_count):
    
#     getcontext().prec = signs_count

#     res = Decimal(0.0)

#     for i in range(len(number_list)):
#         res += Decimal(number_list[i])
#     res = Decimal(res) / Decimal(i + 1)
    
#     return res

# print(decimal_average([3, 5, 77, 23, 0.57], 6))
    
# import collections

# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

# cat_list = [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]

# cat_tuple = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]

# def convert_list(cats):
#     res = []
#     for cat in cats:
#         if isinstance(cat, tuple):
#             res.append({
#                 'nickname': cat.__getattribute__('nickname'),
#                 'age': cat.__getattribute__('age'),
#                 'owner': cat.__getattribute__('owner')
#             })
#         else:
#             res.append(Cat(cat.get('nickname'), cat.get('age'), cat.get('owner')))
#     return res

# print(convert_list(cat_tuple))

# import re

# def find_word(text, word):

#     res = {
#         "result": bool,
#         "first_index": int,
#         "last_index": int,
#         "search_string": str,
#         "string": str
#         }
    

#     get_word = re.search(word, text)
#     if get_word:
#         res["result"] = True
#         res["first_index"] = get_word.start()
#         res["last_index"] = get_word.end()
#         res["search_string"] = get_word.group()
#         res["string"] = text
#     else:
#         res["result"] = False
#         res["first_index"] = None
#         res["last_index"] = None
#         res["search_string"] = word
#         res["string"] = text

#     return res

# print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "python"))
          
# import re

# def find_all_words(text, word):
    
#     find_word = re.findall(word, text, flags=re.IGNORECASE)
#     return find_word

# print(find_all_words("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "python"))

# import re

# def replace_spam_words(text, spam_words):

#     for spam in spam_words:
#         find_word = re.findall(spam, text, flags=re.IGNORECASE)
#         for spam in find_word:
#             text = re.sub(spam, '*'*len(spam), text, flags=re.IGNORECASE)
#     return text

# print(replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn', ['began', 'Python']))

# def logged_func(func):
#     def inner(x, y):
#         print(f'called with {x}, {y}')
#         result = func(x, y)
#         print(f'result: {result}')
#         return result
#     return inner


# @logged_func
# def complicated(x, y):
#     return x / y

# complicated(1, 3)

# for i in filter(lambda x: x % 2, range(1, 10+1)):
#     print(i)

# some_str = 'aaAbbB C F DDd EEe'
# for i in filter(lambda x: x.islower(), some_str):
#     print(i)

# def get_grade(key):
#     grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#     return grade.get(key, None)


# def get_description(key):
#     description = {
#         "A": "Perfectly",
#         "B": "Very good",
#         "C": "Good",
#         "D": "Satisfactorily",
#         "E": "Enough",
#         "FX": "Unsatisfactorily",
#         "F": "Unsatisfactorily",
#     }
#     return description.get(key, None)


# def get_student_grade(option):
#     if option == "get_grade":
#         return get_grade
#     elif option == "get_description":
#         return get_description
#     else: 
#         return None
    
# a = get_grade('A')
# b = get_description('A')

# some = get_student_grade

# some('get_grade')
# print(some)


# DEFAULT_DISCOUNT = 0.05


# def get_discount_price_customer(price: int, customer: dict) -> int:

#     if customer.get('discount') is not None:   
#         price = price * (1 - customer.get('discount'))
#     else: 
#         price = price * (1 - DEFAULT_DISCOUNT)
#     return price


# print(get_discount_price_customer(10, {"name": "Boris"}))
# def caching_fibonacci():
    
#     cache = {0:0, 1:1}
#     print(cache)
    
#     def fibonacci(n):
#         if n in cache:
#             return cache[n]
#         else:
#             cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#             return cache[n]
#     return fibonacci

# a = caching_fibonacci()
# f = a(20)
# print(f)

# def discount_price(discount):
#     def get_price(price):
#         price = price * (1 - discount)
#         return price
#     return get_price

# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)

# price = 100
# print(cost_15(price))
# print(cost_10(price))
# print(cost_05(price))

# def format_phone_number(func):
#     def inner(args):
#         if len(func(args)) == 12:
#             return f'+{func(args)}'
#         else:
#             return f'+38{func(args)}'
#     return inner

# @format_phone_number
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", "")
#     )
#     return new_phone

# a = sanitize_phone_number(" +38(050)123-32-34")

# print(a)
# import re
# def generator_numbers(string=""):
    
#     for numbers in re.findall(r'\d+', string):
#         yield int(numbers)
            

# def sum_profit(string):
    
#     res = 0
#     for i in generator_numbers(string):
#         res += i
#     return res

# get_numbers = generator_numbers("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000.")
# print(sum_profit(next(get_numbers)))

# name = ''
# name.title()

# def get_emails(list_contacts):
#     res = [email for email in map(lambda contact : contact.get('email'), list_contacts)]
#     return res
# print(get_emails())

# from functools import reduce


# def amount_payment(payment):
#     payments = [i for i in filter(lambda x: x > 0, payment)]
#     return reduce((lambda x, y: x + y), payments)

# print(amount_payment([100, -3, 400, 35, -100]))\



# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def info(self):
#         res = {
#             'name': self.name,
#             'age': self.age,
#             'address': self.address
#         }
#         return res

# class Dog(Animal):
#     def __init__(self, nickname, weight, breed):
#         self.breed = breed
#         super().__init__(nickname, weight)
#         self.owner = None

#     def say(self):
#         return "Woof"

#     def who_is_owner(self):
#         return self.owner.info()

# dog1 = Dog('Rex', 10, 'Bulldog')
# owner1 = Owner('John', 30, '123 Main St')
# dog1.owner = owner1
# print(dog1.who_is_owner())

# from collections import UserString


# class NumberString(UserString):
#     def number_count(self):
#         count = 0
#         for num in self.data:
#             if num.isdigit():
#                 count += 1
#         return count
    
# string = NumberString('The resulting profit was: from the southern possessions $123, from the northern colonies $45, and the king gave $67890.')
# print(string.number_count())


# class IDException(Exception):
#     pass


# def add_id(id_list: list, employee_id: str):
#     try:
#         if employee_id.startswith('01'):
#             id_list.append(employee_id)
#         else: 
#             raise IDException
#     except IDException:
#         print(f'ID must be start with numburs "01". Try again.')

#     return id_list
    
# print(add_id([], '0111231242312'))

# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         self.contacts.append(
#             {
#                 "id": Contacts.current_id,
#                 "name": name,
#                 "phone": phone,
#                 "email": email,
#                 "favorite": favorite,
#             }
#         )
#         Contacts.current_id += 1

#     def get_contact_by_id(self, id):
#         for contact in self.contacts:
#             if contact.get('id') == id:
#                 return contact
        
#     def remove_contacts(self, id):
#         for contact in self.contacts:
#             if contact.get('id') == id:
#                 self.contacts.remove(contact)
        

# contact1 = Contacts()
# contact1.add_contacts('Wylie Pope','(692) 802-2949', 'est@utquamvel.net', True)
# contact2 = Contacts()
# contact2.add_contacts('Wylie','(692) 802-2949', 'est@utquamvel', False)
# contact2.add_contacts('Pope','(692) 802-2949', 'est@utquamvel', False)
# contact2.add_contacts('Wyl','(692) 802-2949', 'est@utquamvel', False)
# contact2.add_contacts('Wy Pope','(692) 802-2949', 'est@utquamvel', False)
# contact2.add_contacts('Wy Pope','(692) 802-2949', 'est@utquamvel', False)

# contact2.remove_contacts(3)
# print(contact2.list_contacts())


class Phone():

    def __init__(self, phone_list) -> None:
        self.phone_list = phone_list
    
    def remove(self, number):
        new_phone_list = filter(lambda x: x != number, self.phone_list)
        return list(new_phone_list)

a = Phone(['1', '2', '3', '4'])
print(a.remove(1))