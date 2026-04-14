from abc import ABC,abstractmethod
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self,array:list):
        pass
class BubbbleSortStrategy(SortingStrategy):
    def sort(self,array:list):
        print("sortted using bubble sort")
class MergeSortStrategy(SortingStrategy):
    def sort(self,array:list):
        print("sorting using mergersort")
class Client:
    def __init__(self,s:SortingStrategy):
        self.s=s
    def sorting(self,array):
        return self.s.sort(array)
c=Client(BubbbleSortStrategy())
c.sorting([1,2,3])
