import os
from datetime import datetime
from functools import wraps
def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('test_generator.log', 'a') as file:
            file.write(f'{datetime.now()} - {old_function.__name__} - args: {args}, kwargs: {kwargs}, result: {result}\n')
        return result
    return new_function

@logger
def flat_generator(list_of_lists):
    for i in list_of_lists:
        if isinstance(i, list):
            yield from flat_generator(i)
        else:
            yield i

if __name__ == '__main__':
    f = flat_generator([
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ])