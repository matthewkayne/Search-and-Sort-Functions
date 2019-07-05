#Linear Search Function (List must be sorted)

def Linear_Search(number):
    search=int(input("What number are you looking for? "))
    x = 0
    y = True
    while y == True:
        if search == number[x]:
            print("Index Position: ", x)
            y = False
        else:
            x += 1