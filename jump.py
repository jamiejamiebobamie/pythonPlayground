"""Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index."""

def jump(arr):
    max_index = len(arr)-1
    def __helper(index,_min):
        if index == max_index:
            return _min
        return min(__helper(index+1,_min+1),__helper(index+arr[index],_min+1))
    return __helper(0,0)

arr = [2,3,1,1,4]
print(jump(arr))
