# Algorithm for Palindrome

def isPalindrome(str):
    leftIndex = 0
    rightIndex = len(str) - 1
    avg = rightIndex / 2
    for x in str:
        if leftIndex > avg:
            break
        if str[leftIndex] != str[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1
    return True

print(isPalindrome('racecar'))