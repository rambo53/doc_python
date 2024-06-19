from Algorithms.abstract_algorithm import AbstractSortAlgorithm

class BubbleSort(AbstractSortAlgorithm):

    def sort(self, dataset):
        print("Sorting with bubble sort algorithm !")
        
        for i in range(len(dataset)-1, 0, -1):
            print("Step",i)
            _sorted=True
            # Remonter le maximum à la dernière position de la liste
            for j in range(i):
                if dataset[j] > dataset[j+1]:
                    _sorted=False
                    temp = dataset[j]
                    dataset[j] = dataset[j+1]
                    dataset[j+1] = temp
            if _sorted :
                break
        return dataset