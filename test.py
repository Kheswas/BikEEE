import pytest

def load_cases():
    # read_csv
    class Case:
        def __init__(self, number):
            self.i = number

    def __repr__(self):
            return '{number}'.format(number=self.i)

    return [Case(i) for i in range(5)]


def parametrize(name, values):
    # function for readable description
    return pytest.mark.parametrize(name, values, ids=map(repr, values))


@parametrize("case", load_cases())
def test_responses(case):
    print(case.i)