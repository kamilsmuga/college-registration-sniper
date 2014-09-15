import mechanize
import ConfigParser
import logging

# init and read config
config = ConfigParser.RawConfigParser()
config.read('config.cfg')
# setup mechanize browser
br = mechanize.Browser()
br.set_handle_robots(False)

logging.basicConfig(filename="out.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

def login():
    try:
        process_request(config.get('links', 'login'))
        br.select_form(nr=0)
        br['username'] = config.get('credentials', 'username')
        br['password'] = config.get('credentials', 'password')
    except:
        logging.error("Nie udalo sie otworzyc strony do logowania.")
        return

def process_request(url):
    br.open(url, timeout=360)
    return br.response()

def patologia():
    process_request(config.get('links', 'patologia'))
    br.select_form(name='grupy')
    br.form['zajecia[286396][]']
    br.submit()
    print br.response().get_data()

def neurobiologia():
    try:
        process_request(config.get('links', 'neurobiologia'))
        br.form = list(br.forms())[0]
        res = br.submit()
    except:
        logging.error("Nie udalo sie otworzyc strony do rejestracji.")
        return
    if "nie jest teraz otwarta" in res.read():
        logging.info("Chyba sie udalo!")
    else:
        logging.debug("Jeszcze zamkniete.")
