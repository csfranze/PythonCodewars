#Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
#If it is the case we will return k, if not return -1.

#Note: n and p will always be given as strictly positive integers.

#dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
#dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
#dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
#dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

def dig_pow(n, p):
    n_digits_arr = [int(str(n)[i]) for i in range(0,len(str(n)))]
    S = sum([i**j for i,j in zip(n_digits_arr,range(p,p+len(str(n))))])
    if S % n == 0:
        return(S/n)
    else:
        return(-1)
