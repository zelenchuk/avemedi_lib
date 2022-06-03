# avemedi_lib

This library help in getting a "average value of numbers list" and "get median (for ordered, unordered list of numbers and even or odd list values)".

Enjoy.

### Install lib

`pip install avemedi_lib`

### Usage

`from avemedi_lib.functions import average, get_median, get_median_custom`


`test_even_array = [12, 32, 23, 43, 14, 44, 123, 15]`

`test_odd_array = [1, 2, 3, 4, 5, 6, 7, 8, 9] `

#### Getting average value of list items

`print(average(test_even_array)) # 38.25`

#### Getting median value for ordered or unordered numbers list.

`print(get_median(test_even_array)) # 27.5 `

`print(get_median(test_odd_array)) # 27.5`

#### You can use your own sorted and your count functions

`a = sorted(test_even_array) n = len(a)`

`print(get_median_custom(a, n)) # 27.5 `
