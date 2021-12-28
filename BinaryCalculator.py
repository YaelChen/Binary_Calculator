def bin_to_dec(bin_num):
    """the function takes a binary number and converts it to a decimal number.
    :param bin_num: binary number
    :type bin_num: str
    :return final: decimal number
    :rtype final: int"""

    for d in bin_num:
        if d != "0" and d != "1":
            return "Binary number containing numbers '1' and '0' only."

    n = 1  # number that will multiply itself for adding in each step.
    final = 0  # will add up to the final decimal number.
    for digit in str(bin_num[::-1]):  # calculates the number from the end.
        final += int(digit) * n
        n *= 2
    return final


# print(bin_to_dec("0"))
print(bin_to_dec(input("insert a binary number to convert: ")))

print("---")


def dec_to_bin(dec_num):
    """the function takes a decimal number and converts it to a binary number.
    :param dec_num: decimal number
    :type dec_num: int
    :return final_bin: binary number
    :rtype final_bin: str"""

    def bin_calc(num):
        """the function calculates the base for each digit and puts "1" in it's right spot of the binary number.
        :param num: decimal number
        :type num: int
        :return new_value: highest base in given decimal number
        :return ind: the index for the base number in the binary number
        :rtype new_value: int
        :rtype ind: int"""

        new_value = 1  # number that will multiply itself for adding in each step.
        ind = 0  # number that will add 1 for each step to know the right index for "1".
        while new_value * 2 <= num:
            new_value *= 2
            ind += 1

        return new_value, ind  # returns the highest multiples that fits in the given number, and its index.

    if not str(dec_num).isnumeric():  # checks if the given input is s number.
        return "Error: only numbers please"
    elif int(dec_num) == 0:
        return 0
    else:
        dec_num = int(dec_num)
        number, index = bin_calc(dec_num)
        back = list("1".zfill(index + 1))  # makes the base of the binary number by filling "0" to the length of the index +1.
        while dec_num > 0:
            number, index = bin_calc(dec_num)  # uses bin_calc until the given number resets to 0.
            back[index] = "1"  # writes "1" in the correct index for the remainder.
            dec_num -= number  # subtract the number that was already been written to the binary number.

        final_bin = "".join(back)[::-1]  # joins and reverse the list of numbers to the final binary number.

        return final_bin


# print(dec_to_bin(0))
print(dec_to_bin(int(input("insert a decimal number to convert: "))))
