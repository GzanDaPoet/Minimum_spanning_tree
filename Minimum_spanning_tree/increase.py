def check_prime(num):
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True
def longest_increase(lst):
    temp = []
    result = []
    count = 0
    while count < len(lst):
        for i in range(len(lst) - 1):
            if lst[i] < lst[i+1]:
                temp.append(lst[i])
            else:
                temp.append(lst[i])
                count = count + 1
                if (len(result) < len(temp)):
                    result = temp
                temp =[]
    return result

if __name__ == "__main__":
    a = input().split(" ")
    a = [int(b) for b in a]
    result = longest_increase(a)
    for i in result:
        if(check_prime(i)):
            print(i, " ", end="")