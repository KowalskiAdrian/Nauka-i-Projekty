class Animal:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Adrian', 'Peter', 'Lucas']

    def add_name(self, name):
        self.this_list.append(name)
        return self.this_list
    
    def this_is_a_method(self):
        print(self.this_list)
        
    @property
    def get_peter(self):
        return self.this_list[2]

the_animal = Animal()
# the_names.this_is_a_method()
# peter = the_names.get_peter
# print("The cutest name of all time is", peter)
the_animal.add_name("Filip")
print(the_animal.this_list)