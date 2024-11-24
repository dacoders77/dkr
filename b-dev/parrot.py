class Math:

    @staticmethod # Decorator
    def add5(x): # No need to pass self or cls
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")

Math.pr()



