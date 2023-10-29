def slice(old_list, len_):
    """Tranforma uma lista em uma lista de listas."""
    for index in range(0, len(old_list), len_):
        yield old_list[index: index + len_]

def drop_duplicates(seq): 
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

def fields_check(cols=6, rows=6, len_win=4) -> dict:
    """
        Conforme colunas, linhas tamanho de sequencia, 
        cria um dicionario para chegar o vencedor.
    """
    grid = list(range(cols * rows))
    horizontal = list(slice(grid, cols))
    vertical = [itens for itens in zip(*horizontal)]

    length = cols

    interval = horizontal[0][:cols - len_win + 1]

    grid_horizontal = list()
    grid_vertical = list()

    for index, num in enumerate(interval):
        list_vertical = list()
        list_horizontal = list()

        for num_diag in range(index, (length * rows) + 1, cols + 1):
            list_vertical.append(grid[num_diag])
            pos = num_diag + (cols - 1) * (index)
            if pos < len(grid):
                list_horizontal.append(grid[pos])
        
        if len(list_vertical) >= len_win:
            grid_horizontal.append(list_vertical)
        if len(list_horizontal) >= len_win:
            grid_vertical.append(list_horizontal)
        length -= 1

    vertical_left_right = grid_horizontal + grid_vertical

    length = cols

    interval = horizontal[0][(cols - len_win + 1) * -1:]

    grid_horizontal = list()
    grid_vertical = list()

    for index, num in enumerate(interval[::-1]):
        list_vertical = list()
        list_horizontal = list()

        for num_diag in range(num, length * rows - 1, cols - 1):
            list_vertical.append(grid[num_diag])
            pos = num_diag + cols + (index * (cols + 1))
            if pos < len(grid):
                list_horizontal.append(grid[pos])
        
        if len(list_vertical) >= len_win:
            grid_horizontal.append(list_vertical)
        if len(list_horizontal) >= len_win:
            grid_vertical.append(list_horizontal)
        length -= 1

    vertical_right_left = grid_horizontal + grid_vertical

    dict_fields = {
        0: drop_duplicates(horizontal),
        1: drop_duplicates(vertical),
        2: drop_duplicates(vertical_left_right),
        3: drop_duplicates(vertical_right_left)
    }
    return dict_fields


if __name__ == '__main__':
    print(fields_check())
