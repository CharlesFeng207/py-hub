def deco(func):
    print("deco")
    return func


class TestClass(object):
    def __init__(self):
        self.func_dict = {}

    def deco(self, func_type):
        def wrapper(func):
            if func_type == 'A':
                self.func_dict[func_type] = func
            if func_type == 'B':
                self.func_dict[func_type] = func
            else:
                self.func_dict['other'] = func
            return func

        return wrapper

    def run(self):
        print('hello')
        self.func_dict['A']('Hi mark this is Func-A ')
        self.func_dict['B']('Hi mark this is Func-B ')


test = TestClass()


@test.deco('A')
def my_func(msg):
    print(f'this is the message from run: {msg}')


@test.deco('B')
def my_func2(msg):
    print(f'this is the message from run: {msg}')


@deco
def my_func3():
    print(f'my_func3')


test.run()
