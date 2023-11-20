def fibonacci():
    curr_num = 0
    next_num = 1
    while True:
        yield curr_num
        curr_num, next_num = next_num, curr_num + next_num


