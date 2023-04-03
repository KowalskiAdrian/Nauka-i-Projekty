def funkcja(arg1, arg2="World", *args):   # lista argumentów
    print(arg1, arg2, args, len(args))
    for x in args:
        print(x) 
    
funkcja("Hello")
funkcja("Hi", "Youtube")
funkcja("Hi", "Youtube", "!", ":-)")


def funkcja(arg1, arg2="World", *args, **kwargs):   # lista argumentów
    print(arg1, arg2, args, len(args), kwargs)
    for x in args:
        print(x)
    for x in kwargs.values():
        print(x) 
    
funkcja("Hello")
funkcja("Hi", "Youtube")
funkcja("Hi", "Youtube", "!", ":-)", autor="Sebastian", rok="2022" )

