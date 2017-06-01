





def func():
    try:
        f = "filename"
        raise OSError("something went wrong")
    except OSError as err:
        raise OSError(str(err),f)


try:
    func()

except OSError as err:
    print(' ... '.join(err.args))