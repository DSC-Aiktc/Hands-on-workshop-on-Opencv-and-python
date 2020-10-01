##INHERITANCE (USE python3 while execution)

#EXPLAIN INHERITANCE

class Father:
    def __init__(self):
        print('INSIDE FATHER CLASS')

class Son(Father):
    def __init__(self):
        print('INSIDE SON CLASS')
        super().__init__()

Son()
