from Algorithms.abstract_algorithm import AbstractSortAlgorithm

class MinSort(AbstractSortAlgorithm):

    def sort(self, dataset):
        print("Sorting with min sort algorithm !")
        for i in range(len(dataset)-1):
            # recherche du minimum entre l'indice i et la fin du tableau
            print("Step",i)
            for j in range(i+1,len(dataset)):
                if dataset[i] > dataset[j]:
                    temp = dataset[j]
                    dataset[j] = dataset[i]
                    dataset[i] = temp
        return dataset
        


