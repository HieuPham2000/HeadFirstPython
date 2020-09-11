import requests 

urls = ('https://github.com/HieuPham2000', 'https://www.facebook.com/', 'https://translate.google.com/')

# use list comprehension
""" for res in [requests.get(url) for url in urls]:
    print(len(res.content), '->', res.status_code, '->', res.url) """

# use generator
for res in (requests.get(url) for url in urls):
    print(len(res.content), '->', res.status_code, '->', res.url)