import random
#import quicksort libary
#create a merge sort function
def merge_sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist
#create an array of size 10 called my_array
my_array = [1,2,3,4,5,6,7,8,9,10]
#fill my array with random numbers between 1 and 100
for i in range(len(my_array)):
    my_array[i] = random.randint(1,100)
#sort the array in assending order using bubble sort
merge_sort(my_array)
#print the sorted array
print(my_array)

