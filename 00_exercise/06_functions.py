def highest_even(input_list):
    result = 0
    for item in input_list:
        if item % 2 == 0 and item > result:
            result = item
    return result


ans = highest_even([10, 2, 3, 4, 8, 11])
print(ans)
