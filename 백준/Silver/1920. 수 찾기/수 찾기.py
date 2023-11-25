# 1920번 수 찾기
import sys
input = sys.stdin.readline

size = int(input())
info_list = list(map(int,input().strip().split()))
search = int(input())
find_list = list(map(int,input().strip().split()))

# 값을 찾을 리스트 (n_list) 정렬
info_list.sort()

# n : 찾을 수 ( find_list 의 원소 )
# info_list : 찾을 리스트 
def binary_search(n, info_list, start, finish):
    if start > finish: 
        return 0
    mid = (finish + start)//2
    if info_list[mid]==n:
        return 1
    elif info_list[mid]>n:
        return binary_search(n,info_list,start,mid-1)
    else:
        return binary_search(n,info_list,mid+1,finish)
    
for num in find_list:
    print(binary_search(num, info_list,0,size-1))