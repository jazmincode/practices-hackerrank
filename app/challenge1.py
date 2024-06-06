def is_the_right_len_arrays(nums1:list, nums2:list, m:int ,n:int)->bool:
    return m + n == len(nums1) and n == len(nums2) 
        

def is_the_right_len_mn(m:int ,n:int)->bool:
    return m >= 0 and n <=200


def is_the_right_len_mn(m:int ,n:int)->bool:
    return m >= 0 and n <=200 

def is_the_right_len_mplusn(m:int ,n:int)->bool:
    return m + n >= 1 and m + n <=200

def is_the_right_len_item(nums:list)->bool:
    for num in nums:
        if not (-10**9 <= num <= 10**9):
            return False
        
    return True

def valite_constraints(nums1:list, nums2:list, m:int ,n:int)->bool:

    if not is_the_right_len_arrays(nums1, nums2, m,n):
        return False

    if not is_the_right_len_mn(m,n):
        return False

    if not is_the_right_len_mplusn(m,n):
        return False
        
    if not (is_the_right_len_item(nums1)) or not (is_the_right_len_item(nums2)):
        return False

    return True

def validateXzeros_out(nums1:list, nums2:list, m:int ,n:int)-> list:
    
    if not valite_constraints(nums1, nums2, m,n):
        return []
    print("print: Nums1 Before-->", nums1)
    nums1 = [item for item in nums1 if item != 0]
    print("print: Nums1 After-->", nums1)
    nums1.extend(nums2)
    print("print: Extends-->", nums1)
    return nums1

def merge(nums1: list, nums2: list,m: int,  n: int) -> None:
    nums1=validateXzeros_out(nums1, nums2, m,n)
    nums1=sorted(nums1)
    print("print: Nums1-->", nums1)