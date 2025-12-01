class InvalidAgeError(Exception):
    pass

def safelist(x):
    if x < 25:
        raise InvalidAgeError("Hey you are not eligible")
    else:
        return x


safelist(5)