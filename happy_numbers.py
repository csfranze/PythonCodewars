#Math geeks and computer nerds love to anthropomorphize numbers and assign emotions and personalities to them. Thus there is defined the concept of a "happy" number. A happy number is defined as an integer in which the following sequence ends with the number 1.

#Start with the number itself.
#Calculate the sum of the square of each individual digit.
#If the sum is equal to 1, then the number is happy. If the sum is not equal to 1, then repeat steps 1 and 2. A number is considered unhappy once the same number occurs multiple times in a sequence because this means there is a loop and it will never reach 1.
#For example, the number 7 is a "happy" number:

#72 = 49 --> 42 + 92 = 97 --> 92 + 72 = 130 --> 12 + 32 + 02 = 10 --> 12 + 02 = 1

#Once the sequence reaches the number 1, it will stay there forever since 12 = 1

#On the other hand, the number 6 is not a happy number as the sequence that is generated is the following: 6, 36, 45, 41, 17, 50, 25, 29, 85, 89, 145, 42, 20, 4, 16, 37, 52, 29

#Once the same number occurs twice in the sequence, the sequence is guaranteed to go on infinitely, never hitting the number 1, since it repeat this cycle.

#Your task is to write a program which will print a list of all happy numbers between 1 and x (both inclusive), where 2 <= x <= 5000

def happy_numbers_bool(n):
    n_arr = [int(str(n)[i]) for i in range(0,len(str(n)))]
    n_sq_sum = sum([i**2 for i in n_arr])
    results = [n]
    while n_sq_sum > 0:
        results.append(n_sq_sum)
        if n_sq_sum == 1:
            return(1)
            break
        else:
            new_n_arr = [int(str(n_sq_sum)[i]) for i in range(0,len(str(n_sq_sum)))]
            new_sq_sum = sum([i**2 for i in new_n_arr])
            n_sq_sum = new_sq_sum
            if n_sq_sum not in results:
                pass
            else:
                results.append(n_sq_sum)
                return(0)
                break
def happy_numbers(n):
    happy_list = []
    for i in range(1,n+1):
        if happy_numbers_bool(i) == 1:
            happy_list.append(i)
    return(happy_list)
