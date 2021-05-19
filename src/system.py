def line (tam=42):
    return '-' * tam

def header(txt):
    print(line())
    print(txt.center(42))
    print(line())

def menu(list):
    print(list)
