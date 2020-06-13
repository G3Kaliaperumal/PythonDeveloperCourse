# By extending list class super_list can access all the methods of list class.
class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
super_list1.append(10)
print(len(super_list1))
