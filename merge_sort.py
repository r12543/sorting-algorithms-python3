def MergeSort(array, l, r):
  if l < r:
    m = (l+r)/2
    MergeSort(array, l, m)
    MergeSort(array, m+1, r)
    merge(array, l, m, r)

def merge(array, l, m, r):
  
