

def coroutine(func):
    def wrap(*args, **kwargs):
        generator = func(*args, **kwargs)
        generator.send(None)
        return generator
    return wrap


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen recieved', message)


class StubException(Exception):
    pass


@coroutine
def avg():
    count = 0
    summ = 0
    avg = None

    while True:
        try:
            x = yield avg
        except StopIteration:
            print('done!')
            break
        except StubException:
            print('..................')
            break
        else:
            count += 1
            summ += x
            avg = round(summ / count, 2)

    return avg
