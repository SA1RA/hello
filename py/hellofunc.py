import skilstak.colors as c

def print_plain(name="Sam"):
    print("Hello " + name)

def print_sir(name="Sir"):
    print("Hello " + name)

def print_color(name="-c"):
    print("Hello " + (c.cyan + name))

def print_multi(name="-m"):
    print("Hello " + (c.multi + name))
