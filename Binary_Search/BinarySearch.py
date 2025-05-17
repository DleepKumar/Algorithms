# Binary Search is an Algorithm which is used to find the target value in the sorted Array
#We use Binary search when The array is sorted
def binarysearch(arr,target):
    n=len(arr)
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return f"Found Target at index {mid}"
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1
if __name__=='__main__':
    print("enter an Array")
    arr= list(map(int, input().split()))
    target=int(input())
    print(binarysearch(arr,target))

#Time Complexity:O(log n) ,Because every iteration it divides the array in to half
#Space Complexity:O(1) constant space 
    

