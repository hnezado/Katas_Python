# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
# For example:
#
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
    start, end = 0, 0
    if 'http' in url: start = url.index('/')+2
    if 'www.' in url: start, end = url.index('.')+1, url.index('.', url.index('.')+1, -1)
    else: end = url.index('.')
    return url[start:end]


print(domain_name("https://youtube.com"))
