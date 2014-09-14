import mechanize

login_url = 'https://login.uj.edu.pl/login'
br = mechanize.Browser()

def login():
    return process_request(login_url)

def process_request(url):
    br.open(url)
    return br.response()

res = login()
