"""
Problem Set below:

Task: Implement a class named 'IntervalList'
A pair of integers define a interval, for example: [1, 5]. 
This range includes integers: 1, 2, 3, and 4.
A range list is an aggregate of these ranges: [1, 5], [10, 11], [100, 201]
NOTE: Feel free to add any extra member variables/functions you like.

Need to implement 4 main parts:
1. Add: Adds a range to the list
2. Remove: Removes a range from the list
3. Print: Prints out the list of ranges in the range list
4. Overriding Expression (<, >, <=, >=, ==, in)
< or > is true when the biggest number is smaller or bigger than the 
other’s biggest number. 

Ex) 
IntervalList([1, 4]) < IntervalList([2, 5]) => True
IntervalList([1, 4]) > IntervalList([0, 3]) => True
"""
from typing import List

class IntervalList:
    
    def __init__(self, list: List[int] = []) -> None:
        self._list = [list]

    def __repr__(self) -> str:
        return "".join(f'{item}' for item in self._list)
    
    def print(self) -> str:
        return print(self)
    
    def add(self, data: List[int]) -> None:           

        result = []
        for i in range(len(self._list)):           

            # data의 2번째 원소가 self._list 내 i번째 리스트 1번째 원소보다 작은 경우, 이 경우 겹치는 것이 없다. _list = [10, 20], [21, 30], data = [1, 5]
            if data[1] < self._list[i][0]:
                result.append(data)
                result += self._list[i:]
                self._list = result
                return                
            
            # data의 1번째 원소가 self._list 내 i번째 리스트 2번째 원소보다 큰 경우, 이 경우 겹치는 것이 없다. _list = [5, 7], [8, 10], data = [20, 30]
            elif data[0] > self._list[i][1]:
                result.append(self._list[i])

            # 겹치는 경우   _list = [1, 5], [10, 21], data = [3, 8] 
            else:
                first = min(self._list[i][0], data[0])
                second = max(self._list[i][1], data[1])
                data = [first, second]

        result.append(data)
        self._list = result
                
        
       
        

rl = IntervalList([1,5])
rl.print()
print(rl._list)
rl.add([10, 20])
rl.print()
rl.add([20, 21])
rl.print()
rl.add([2, 4])
rl.print()
rl.add([3, 8])
rl.print()