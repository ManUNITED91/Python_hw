def print_operation_table(operation, num_rows=6, num_columns=6):
    for col in range(num_columns + 1):
        print(str(col).ljust(3), end=' ')
    print()
    print('----' * (num_columns + 1))


    for i in range(1, num_rows + 1):
        print(f'{str(i).ljust(2)}|', end=' ')

        for j in range(1, num_columns + 1):
            print(str(operation(i, j)).ljust(3), end=' ')
        print()
    

print_operation_table(lambda x, y: x * y, 5, 5)
