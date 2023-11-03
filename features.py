import urllib

def bb(bool_val):
    if bool_val == True:
        return 1
    return 0

def n_alpha(url):
    return len([char for char in url if char.isalpha()])

def extract_features(url):

    readability = bb(True)
    if(url != urllib.parse.unquote(url)):
      readibility = bb(False)

    url = urllib.parse.unquote(url).lower()

    print(url)
    def p(ch):
        return bb(ch in url)

    def letters_ratio():
        return  len([char for char in url if char.isalpha()])/len(url)

    def symbols_ratio():
        symbols = [char for char in url if not char.isalpha()]
        return len(symbols)/len(url)

    def numbers_ratio():
        numbers = [char for char in url if char.isdigit()]
        return len(numbers)/len(url)

    return [
            p('<'),
        p('<script'),
        0,
        p('""><'),
        p("'><"),
        p('&'),
        p('%'),
        p('/'),
        p('\\'),
        p('+'),
        p('document.'),
        p('window.'),
        p('onload='),
        p('onerror='),
        p('<div'),
        p('<iframe'),
        p('<img'),
        p('src='),
        p('var'),
        p('eval('),
        p('.href'),
        p('document.cookie'),
        p('String.fromCharCode'),
        p("'"),
        p('?'),
        p('!'),
        p(';'),
        bb(p('http') and not p('https')),
        p('.js'),
        p('#'),
        p('='),
        p('['),
        p(']'),
        p('[]'),
        p('$'),
        p('('),
        p(')'),
        p('*'),
        p(','),
        p('-'),
        p('<'),
        p('>'),
        p('@'),
        p('_'),
        p('location.'),
        p('.search'),
        p('&#'),
        p(':'),
        p('.'),
        p('{'),
        p('}'),
        p('~'),
        p(' '),
        p('"'),
        p('`'),
        p('=='),
        p('//'),
        p('|'),
        p('^'),
        p('¦'),
        p('alert('),
        p('<br'),
        letters_ratio(),
        numbers_ratio(),
        symbols_ratio()
    ]
