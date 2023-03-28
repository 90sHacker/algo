# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

word = ''

def longest_string(a,b,c,string):
    global word

    if len(string) > len(word):
        word = string
    if a > 0 and check(string, 'a'):
        longest_string(a-1, b, c, string + 'a')
    if b > 0 and check(string, 'b'):
        longest_string(a, b-1, c, string + 'b')
    if c > 0 and check(string, 'c'):
        longest_string(a, b, c-1, string + 'c')



def check(str, strtoadd):
    if len(str) < 2:
        return True
    elif str[-1] == strtoadd and str[-2] == strtoadd:
        return False
    return True

def solution(A, B, C):
    # write your code in Python 3.8.10

    longest_string(A,B,C,word)

    return word

if __name__ == '__main__':
  print(solution(3,3,4))