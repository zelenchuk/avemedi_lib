===============
This library help in getting a "average value of numbers list" 
and "get median (for ordered, unordered list of numbers and even or odd list values)". 

Enjoy.

Github rep - `https://github.com/zelenchuk/avemedi_lib`



Installing
============

.. code-block:: bash

    pip install avemedi_lib

Usage
=====

.. code-block:: python

   from avemedi_lib.functions import average, get_median, check_ordered_median

    test_even_array = [12, 32, 23, 43, 14, 44, 123, 15]
    test_odd_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    # Getting average value of list items
    print(average(test_even_array))  # 38.25

    # Getting median value for ordered or unordered numbers list
    print(get_median(test_even_array))  # 27.5
    print(get_median(test_odd_array))  # 27.5

    # You can use your own sorted and your count functions
    a = sorted(test_even_array)
    n = len(a)

    print(check_ordered_median(a, n))  # 27.5
