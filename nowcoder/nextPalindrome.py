import os

def get_nextpalindrome(number):
    while True:
        if str(number) != str(number)[::-1]:
            number += 1
        else:
            break
    print(number)
    return number


if __name__ == '__main__':
    fptr = open('test.txt', 'w')
    number = int(input().strip())

    result = get_nextpalindrome(number)
    fptr.write(str(result) + '\n')
    fptr.close()
