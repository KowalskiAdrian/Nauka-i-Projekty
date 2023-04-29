# def thing1():
#     print("Welcome in thing 1")
    
#     def thing2():
#         print("Welcome to thing 2")
#     thing2()
    
# thing1()

def thing1(name):
    print("Welcome in thing 1", name)
    
    def thing2():
        print("Welcome to thing 2", name)
    thing2()
    
thing1("Adrian")