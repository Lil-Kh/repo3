def url_checker(rand_str):
    if rand_str.startswith('http') or rand_str.startswith('https'):
        print('url is valid')
    else:
        print('url is not valid')