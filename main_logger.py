import datetime

def logger(old_function):
    
    def new_function(*args, **kwargs):
        name = old_function.__name__
        start = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        with open('generator.log', 'a', encoding='utf-8') as file:
            file.write(f"{start}: отработала функция {name} с аргументами {args}, {kwargs}.Функция вoзращает {result}")
        file.close()
    
        return result

    return new_function


@logger
def flat_generator(list_of_lists):
        for sub_list in list_of_lists:
            for elem in sub_list:
                yield elem


if __name__ == '__main__':
   
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    flat_generator(list_of_lists_1  )