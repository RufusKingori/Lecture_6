def main():
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    result5 = []

    for i in range (1,100):
        if i%7==0 and i%3==0:
            result1.append(i)
        if i%7==0 and i%3!=0:
            result2.append(i)
            if i%2!=0:
                result3.append(i)
        sum_of_digits = sum(int(digit) for digit in str(i))
        if i%sum_of_digits==0:
            result4.append(i)
            if (pow(sum_of_digits, 2)) == i:
                result5.append(i)

    print("divisible by 7 & 3:",result1)
    print("\n divisible by 7 and not 3:",result2)
    print("\n odd numbers divisible by 7 and not 3:",result3)
    print("\n divisinle by sum of it's digits:",result4)
    print("equal to the square of the sum of it's digits:",result5)

main()

