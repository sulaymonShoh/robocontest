def find_smallest_num(sum_of_digits):
    # If sum of digits is more than the maximum possible sum
    if sum_of_digits > 9 * 19:
        return -1

    # Create an array to store digits
    res = [0] * 19

    # Fill the array from most significant digit to least
    i = 18
    while sum_of_digits > 0:
        # Fill 9 first to make the number smallest
        if sum_of_digits >= 9:
            res[i] = 9
            sum_of_digits -= 9
        else:
            res[i] = sum_of_digits
            sum_of_digits = 0
        i -= 1

    # Convert list to string then to int
    num = int("".join(map(str, res)))

    return num


# Test the function
n = int(input())
print(find_smallest_num(n))
