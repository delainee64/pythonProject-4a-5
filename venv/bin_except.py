# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 01/28/2023
# Description: Modify the binary search function from the exploration so that, 
# instead of returning -1 when the target value is not in the list, raises 
# a TargetNotFound exception (you'll need to define this exception class). 

class TargetNotFound(Exception):
  """User-defined exception when target isn't found."""
  pass

def bin_except(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, returns -1, indicating the target value isn't in the list
  """
  first = 0
  last = len(a_list) - 1
  try:
    while first <= last:
      if target < min(a_list) or target > max(a_list):
        raise TargetNotFound
      middle = (first + last) // 2
      if a_list[middle] == target:
        return middle
      if a_list[middle] > target:
        last = middle - 1
      else:
        first = middle + 1

  except TargetNotFound:
    print("Target not found")