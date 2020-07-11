class Dome(object):
    __message = None

    def __new__(cls, *args, **kwargs):
        if cls.__message == None:
            cls.__message = object.__new__(cls)
        return cls.__message


d1 = Dome()
d2 = Dome()
print(id(d1))
print(id(d2))
