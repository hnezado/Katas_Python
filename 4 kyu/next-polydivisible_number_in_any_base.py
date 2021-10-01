# Given a base between 2 and 62 ( inclusive ), and a non-negative number in that base,
# return the next bigger polydivisible number in that base, or an empty value like null or Nothing.
#
# A number is polydivisible if its first digit is cleanly divisible by 1, its first two digits by 2,
# its first three by 3, and so on. There are finitely many polydivisible numbers in any base.
#
# Numbers in a particular base are encoded as Strings, with digits ['0'..'9'] + ['A'..'Z'] + ['a'..'z'].

def check_poly(n):
    num = ''
    for d in str(n):
        num += str(d)
        if int(num) % len(num) != 0:
            return False
    return True


def next_num(b, n):
    while True:
        num = n
        for i in range(b):
            if int(str(num)[-1])+1 < b:
                num += 1
                if check_poly(num): return num
        return None


print(next_num(10, 123220))
