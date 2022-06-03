# https://docs.pytest.org/en/6.2.x/assert.html

from avemedi_lib.functions import average, get_median, count, quicksort


def test_count():
    array = [1, 2, 3, 4, 5, 6]

    assert count(array) == len(array)


def test_quicksort():
    array = [6, 1, 2, 3, 4, 5, 17, 25]

    assert quicksort(array) == sorted(array)
    assert quicksort([10]) == [10]


def test_average():
    assert average([5.24, 6.97, 8.56, 7.32, 6.23]) == 6.864


def test_get_even_median():
    assert get_median([4, 1, 2, 3, 3, 1]) == 2.5


def test_get_odd_median():
    assert get_median([11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 32, 72]) == 7.0
    assert get_median([50, 50, 50]) == 50
