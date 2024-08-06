def add_everything_up(a, b):
    c = 1
    try:
        c = a + b
    except TypeError as exc:
        if isinstance(a, str) or isinstance(b, str):
            c = str(a)  + str(b)
            #print(exc)
    else :
            c = a+b
    finally :
            pass
    return c



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

