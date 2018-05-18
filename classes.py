class MyClass:
    def method(self):
        print("some sample print of Instance method")
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        print("some sample print of class method")
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        print("some sample print of static  method")
        return 'static method called'



MyClass.method()

MyClass.classmethod()

MyClass.staticmethod()





