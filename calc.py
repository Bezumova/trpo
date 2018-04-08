def calc(ch, a, b):
    a = int(a)
    b = int(b)
    return{
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b
    }[ch]

def calc_line(line):
    (ch, a ,b) = tuple(filter(None, line.split(' ')))
    return calc(ch, a, b)
