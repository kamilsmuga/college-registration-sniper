import mechanize
import ConfigParser

# init and read config
config = ConfigParser.RawConfigParser()
config.read('config.cfg')
# setup mechanize browser
br = mechanize.Browser()
br.set_handle_robots(False)

def login():
    process_request(config.get('links', 'login'))
    br.select_form(nr=0)
    br['username'] = config.get('credentials', 'username')
    br['password'] = config.get('credentials', 'password')
    res = br.submit()
    print res.get_data()

def process_request(url):
    br.open(url)
    return br.response()

res = login()
