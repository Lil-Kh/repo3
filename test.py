import re

string = 'http://www.tsd.com, sss, https://www.fsdf.ru, https://www.fvcfd.r'
match = re.findall(r"https?://www.[\w\.]+[.][a-z]+", string)
# match = re.findall(r"https|http", string)
print(match)

# if re.findall(match, string):
#     print('url is valid')
# else:
#     print('url is not valid')