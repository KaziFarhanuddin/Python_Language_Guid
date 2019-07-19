class Dummy(object):

    @classmethod
    def some_function(cls):
        print(cls)

#both of these will have exactly the same effect
Dummy.some_function()
Dummy().some_function()