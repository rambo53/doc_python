import copy


class SelfReferencingClass:
    def set_parent(self, parent):
        self.parent = parent


class TestPrototype:
  

    def __init__(self, data, self_ref_obj):
        self.data = data
        self.self_ref_obj = self_ref_obj

    def __copy__(self):
        
        data = copy.copy(self.data)
        self_ref_obj = copy.copy(self.self_ref_obj)

  
        new = self.__class__(data, self_ref_obj)
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

       
        data = copy.deepcopy(self.data, memo)
        self_ref_obj = copy.deepcopy(self.self_ref_obj, memo)

     
        new = self.__class__( data, self_ref_obj )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    data = [['a','b'], 'c']
    self_ref_obj = SelfReferencingClass()
    original = TestPrototype( data, self_ref_obj)
    self_ref_obj.set_parent(original)

    simple_copy = copy.copy(original)

  
    simple_copy.data.append("new value 1")
    if original.data[-1] == "new value 1":
        print("Copy.copy: The change of the copy affet the original !")
    else:
        print("Copy.copy: The change of the copy doesn't affet the original !")


 
    original.data[0].append('new value 2')
    if 'new value 2' in simple_copy.data[0]:
        print("Copy.copy: The change of the original affet the copy !")
    else:
        print("Copy.copy: The change of the original doesn't affect the copy !")


    deep_copy= copy.deepcopy(original)

    
    deep_copy.data.append('new value 3')
    if original.data[-1] == 'new value 3':
        print("Copy.deepcopy: The change of the deep copy affet the original ???")
    else:
        print("Copy.deepcopy: The change of the deep copy doesn't affect the original !")

  
    original.data[0].append('new value 4')
    if 'new value 4' in deep_copy.data[0]:
         print("Copy.deepcopy: The change of the original affet the copy !")
    else:
        print("Copy.deepcopy: The change of the original doesn't affect the copy !")

    print(f"id(deep_copied_component.some_circular_ref.parent): {id(deep_copy.self_ref_obj.parent)}" )
    print(f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): {id(deep_copy.self_ref_obj.parent.self_ref_obj.parent)}")
  