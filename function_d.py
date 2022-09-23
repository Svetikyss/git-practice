def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    max_number = max(numbers)
    return max_number

requency_index = {}
    max_frequency = -1
    most_common_value = None
    for num in number_list:
        if frequency_index.get(num):
            frequency_index[num] += 1
        else:
            frequency_index[num] = 1

        if max_frequency < frequency_index[num]:
            max_frequency = frequency_index[num]
            most_common_value = num

    return most_common_value
    
if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
