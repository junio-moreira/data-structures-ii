from smallest_element import *
from arrays import *
from bubblesort import *


if __name__ == "__main__":
    
    unsorted_array = test_arrays["array_slides"]
    print(unsorted_array)
    
    sorted_array = bubble_sort(unsorted_array)
    print(sorted_array)
   