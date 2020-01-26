If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

def solution(number):
    if number%3 == 0:
        a = 1
    else:
        a = 0
    if number%5 == 0:
        b = 1
    else:
        b = 0
    if number%15 == 0:
        c = 1
    else:
        c = 0
    return((3*(((number//3-a)*(number//3-a+1))//2)+5*((number//5-b)*(number//5-b+1))//2-15*((number//15-c)*(number//15-c+1))//2))
