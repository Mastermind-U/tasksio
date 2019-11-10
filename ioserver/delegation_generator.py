

def coroutine(func):
    def wrap(*args, **kwargs):
        generator = func(*args, **kwargs)
        generator.send(None)
        return generator
    return wrap


class StubException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print('kha kha kha!')
            break
        else:
            print('.....', message)

    return 'Returned from subgen!'


@coroutine
def delegator(generator):
    # while True:
    #     try:
    #         data = yield
    #         generator.send(data)
    #     except StubException as ex:
    #         generator.throw(ex)
    result = yield from generator
    print(result)
