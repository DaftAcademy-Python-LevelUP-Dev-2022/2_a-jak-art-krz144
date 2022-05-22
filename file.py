from functools import wraps


def greeter(func):
    @wraps(func)
    def inner(*args, **kwargs):
        val = func(*args, **kwargs)
        return "Aloha " + val.title()
    return inner


def sums_of_str_elements_are_equal(func):
    @wraps(func)
    def inner(*args, **kwargs):
        numbers = func(*args, **kwargs).split(' ')
        sums = []
        for str in numbers:
            sum = 0
            if str[0] == '-':
                for char in str[1:]:
                    sum += -1*int(char)
            else:
                for char in str:
                    sum += int(char)
            sums.append(sum)

        sign = "==" if sums[0] == sums[1] else "!="
        retv = f'{sums[0]} {sign} {sums[1]}'
        return retv
    return inner


def format_output(*required_keys):
    keys = required_keys

    def true_decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            val = func(*args, **kwargs)  # val to dict zwracany przez func
            new_dict = dict()
            try:
                for key in keys:
                    if "__" in key:
                        lista = key.split('__')
                        value = ''
                        for el in lista:
                            value += val[el] + ' '
                        value = value[:-1]
                    else:
                        value = val[key]
                    if value == '':
                        value = 'Empty value'
                    new_dict.update({key: value})
                return new_dict
            except KeyError:
                raise ValueError
        return inner
    return true_decorator


def add_method_to_instance(klass):
    def true_decorator(func):
        @wraps(func)
        def inner(*args):  # argument self
            return func()
        setattr(klass, func.__name__, inner)
        return inner
    return true_decorator
