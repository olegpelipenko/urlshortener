

urls_cache = {}

def store_short_url(short_code, long_url):
    urls_cache[short_code] = long_url
    return 


def get_long_url(short_code):
    return urls_cache[short_code]


def remove_short_code(short_code):
    del urls_cache[short_code]


def is_short_code_exists(short_code):
    return short_code in urls_cache