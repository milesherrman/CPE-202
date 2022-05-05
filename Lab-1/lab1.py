# CPE 202 Lab 1

# Purpose: Iterate through a list and return the largest number
def max_list_iter(int_list: list) -> int:  
   if type(int_list) != list:
      raise ValueError
   elif len(int_list) == 0:
      return None
   else:
      max = int_list[0]
      for num in int_list:
         if num > max:
            max = num
      return max

# Purpose: Return a reversed list of numbers 
def reverse_rec(int_list: list) -> list:   
   if type(int_list) != list:
      raise ValueError
   elif len(int_list) == 0:
      return []
   else: 
      return [int_list[-1]] + reverse_rec(int_list[:-1])

# Purpose: Return the index of a target number in a list of integers
def bin_search(target: int, low: int, high: int, int_list: list) -> int:  
   mid = (low + high) // 2
   if type(int_list) != list:
      raise ValueError
   elif len(int_list) == 0:
      return None
   elif int_list[mid] != target and low == high:
      return None
   elif int_list[mid] == target:
      return mid
   elif int_list[mid] < target:
      return bin_search(target, mid + 1, high, int_list)
   else:
      return bin_search(target, low, mid - 1, int_list)
