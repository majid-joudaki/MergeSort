# merge two sorted list -> sorted list
def Merge(A,B):
    C = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1
    return C

# sort a list based on Merge sort
def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2
        left = MergeSort(A[:mid])
        right = MergeSort(A[mid:])
        return Merge(left, right)

# main function
def main():
    A = [10,8,5,7,3,4,6,2,9,1]
    print(MergeSort(A))

if __name__ == "__main__":
    main()

    

    
    
    
    


    

    