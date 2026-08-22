def reverse(x: int) -> int:
        sign = -1 if x < 0 else 1

        reversed_num = int(str(abs(x))[::-1])
        reversed_num *= sign

        if reversed_num < -2147483648 or reversed_num > 2147483647:
            return 0

        return reversed_num


print(reverse(123))          # 321
print(reverse(-123))         # -321
print(reverse(120))          # 21
print(reverse(1534236469))   # 0

# reverse numbers