#Binary Search (List must be sorted)

def Binary_Search(number):

    search=int(input("What number are you looking for? "))

    number_len=len(number)
    checker = int(number_len / 2)
    left = 0
    right = number_len - 1
    flag = True

    while flag == True:

        if search == number[checker]:
            print("It is at index position ", (checker))
            flag = False
            return

        elif search > number[checker]:
            checker=int((right - checker)/2)+checker
            left=checker+1

        elif search < number[checker]:
            right=checker-1
            checker=int(right/2)

        if left == right:
            right+=1