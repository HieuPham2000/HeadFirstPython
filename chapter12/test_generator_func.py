from url_utils import gen_from_urls
from pprint import pprint

urls = ('https://github.com/HieuPham2000', 'https://www.facebook.com/', 'https://translate.google.com/')

# test 1
for res_len, res_status, res_url in gen_from_urls(urls):
    print(res_len, '->', res_status, '->', res_url)

# test 2
urls_res = { url: size for size, _, url in gen_from_urls(urls)}
pprint(urls_res)

