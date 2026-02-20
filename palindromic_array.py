def isPalinArray(arr):
    for i in arr:
        num=i
        reverse=0
        while num>0:
            digit=num%10
            reverse=reverse*10+digit
            num=num//10
        if reverse!=i:
            return False
    return True
