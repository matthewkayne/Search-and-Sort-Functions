#Bubble Sort (Reverse Order) Function

def Bubble_Sort_Reverse(s):
    n=len(s)
    swapped=True
    while swapped == True:
        swapped=False
        for i in range(1,n):
            if s[i-1] < s[i]:
                temp=s[i-1]
                s[i-1]=s[i]
                s[i] = temp
                swapped = True
    return s
