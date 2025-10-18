import sys
n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().strip().split(' ')))
n_len=len(n_list)
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().strip().split(' ')))

# m_list 요소 하나하나가 n_list 안에 있는지 탐색 (이분 탐색)
def binary_search(arr,target,start,end):
   while start<=end:
      mid=(start+end)//2

      if arr[mid]==target: return 1
      elif arr[mid]>target: end=mid-1
      else: start=mid+1
   return 0

n_list.sort()
for ml in m_list:
   result=binary_search(n_list,ml,0,n_len-1)
   print(result)