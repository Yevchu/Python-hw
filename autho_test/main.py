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
    
    

def all_sub_lists(data):
    
    res = [[]]

    for i in range(len(data)):
        for j in range(i, len(data)):
            res.append(data[i:j+1])
    res.sort(key=len)

    return res

print(all_sub_lists([4, 6, 1, 3]))
            
    
    
        
                
                