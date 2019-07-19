class Dummy(object):
    
    @staticmethod
    def some_function():
        print("Static method dos not take any cls or self")

#both of these will have exactly the same effect
Dummy.some_function()
Dummy().some_function()