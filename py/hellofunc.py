import skilstak.colors as c

def print_plain(name="Sam"):
    print("Hello " + name)

def print_hello(name="-h"):
    print("Hello")

def print_color(name="-c"):
    print("Hello " + (c.cyan + name))

def print_multi(name="-m"):
    print(c.multi("Hello " + name))

def print_random(name="-r"):
    print(c.random() + "Hello " + name)
