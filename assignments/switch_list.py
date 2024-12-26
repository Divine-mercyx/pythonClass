def switch_list(numbers: list, number: int):
    if type(numbers) is not list or type(number) is not int:
        raise TypeError("not list or int")
        
    for _ in range(number):
        each = numbers[0]
        numbers.remove(numbers[0])
        numbers.append(each)
        
    return numbers



def split_array(numbers: list):
    if type(numbers) is not list:
        raise TypeError("not list")
        
    length = 0
    first = []
    second = []
    if len(numbers) % 2 == 0:
        length = int(len(numbers) / 2)
        first = numbers[0:length]
        second = numbers[length:]
    else:
        length = int(len(numbers) / 2)
        first = numbers[0:length]
        second = numbers[length:]
    return f"{first}  {second}"



def boolean_list(numbers: list):
    if type(numbers) is not list:
        raise TypeError("not list")
        
    booleans_list = []
    for number in numbers:
        if number % 2 == 0:
            booleans_list.append(True)
        else:
            booleans_list.append(False)
    return booleans_list
