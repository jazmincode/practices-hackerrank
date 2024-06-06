from app.challenge1 import *

def main(nums1:list, nums2:list,m:int,n:int)->None:
    merge(nums1,nums2,n,m)
    print("print: Main")


if __name__=="__main__":
    nums1 = [0]
    nums2 = [1]
    n = 1
    m = 0
    main(nums1, nums2,n,m)