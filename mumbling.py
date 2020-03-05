#Examples:

#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    s_lower = s.lower()
    s_upper = s.upper()
    output = ''
    for i in range(0,len(s)):
        output = output+s_upper[i]+(s_lower[i]*i)+'-'
    return output[:-1]
