from urllib.parse import urlsplit


# from urlparse import urlsplit
# print(urlparse('https://ru.stackoverflow.com/questions'))

def domain_name(url):
    result = urlsplit(url, scheme='http')
    if result.netloc:
        if 'www' in result.netloc:
            return result.netloc.split('.')[1]
        return result.netloc.split('.')[0]
    return result.path.split('.')[1] if 'www' in result.path else result.path.split('.')[0]


print(domain_name("http://google.com"), "google")
print(domain_name("www.xakep.ru"))
print(domain_name("icann.org"), "icann")

# def domain_name(url):
#     url = url.replace('www.', '')
#     url = url.replace('https://', '')
#     url = url.replace('http://', '')
#
#     return url[0:url.find('.')]
