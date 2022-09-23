# TODO more error handling just in case
class ErrorDay(Exception):
    pass


class ErrorMonth(Exception):
    pass


class ErrorYear(Exception):
    pass


def test_day(d):
    if d > 31:
        raise ErrorDay("Wrong day value too high {}", d)
    elif d < 1:
        raise ErrorDay("Wrong day value too low {}", d)


def test_month(m):
    if m > 12:
        raise ErrorDay("Wrong month value too high {}", m)
    elif m < 1:
        raise ErrorDay("Wrong month value too low {}", m)


def test_year(y):
    if y > 2022:
        raise ErrorDay("Wrong year value too high {}", y)
    elif y < 1900:
        raise ErrorDay("Wrong year value too low {}", y)
