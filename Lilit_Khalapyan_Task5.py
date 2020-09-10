import re


def url_checker(rand_str):
    match = r"https?://www.[\w\.]+[.][a-z]+"
    if re.findall(match, rand_str):
        print('url is valid')
    else:
        print('url is not valid')