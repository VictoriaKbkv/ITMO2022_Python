from PIL import Image

SIZE = 100
WHITE = (255, 255, 255)
GREY = (242, 242, 242)
GREEN = (0, 255, 0)
COLOR_STEP = 50


def get_initial_config(input_file):
    """
    Функция получает начальную конфигурацию из текстового файла
    Жевые ячейки = 1, нежевые ячейки =0, разделены пробелом
    """
    source_file = open(input_file, 'r')
    source = source_file.read()
    source_file.close()
    life_string = []
    for line in source.split('\n'):
        items = line.split(' ')
        life_string.append(items)
    output_life = []
    for lineitem in life_string:
        line = []
        for item in lineitem:
            line.append(int(item))
        output_life.append(line)
    return output_life


def simulate_life(input_life):
    new_life = []
    for lineitem in input_life:
        line = []
        for item in lineitem:
            line.append(int(item))
        new_life.append(line)
    for i in range(0, len(input_life)):
        for j in range(0, len(input_life[i])):
            count = 0
            for row_delta in [-1, 0, 1]:
                for column_delta in [-1, 0, 1]:
                    if not (row_delta == 0 and column_delta == 0):
                        try:
                            if input_life[i + row_delta][j + column_delta] > 0:
                                count += 1
                        except:
                            pass
            if input_life[i][j] == 0 and count == 3:
                new_life[i][j] = 1
            elif input_life[i][j] > 0 and (count == 2 or count == 3):
                new_life[i][j] = input_life[i][j] + 1
            else:
                new_life[i][j] = 0
    return new_life


def print_life(input_life):
    for lineitem in input_life:
        print(lineitem)
    print()


def snapshot_life(input_life, number):
    file_path = r"C:\Users\Victoria\Documents\ITMO_Course\Python\ITMO2022_Python\Files_Practice3"
    file_name = r"\snapshot"
    file_type = r".png"
    snapshot = Image.new('RGB', (len(input_life)*SIZE, len(input_life[0])*SIZE))
    pixel_map = snapshot.load()
    for i in range(0, len(input_life)):
        for j in range(0, len(input_life[i])):
            if input_life[i][j] == 0:
                if (i + j) % 2 == 0:
                    for pixel_column in range(SIZE * i, SIZE * i + SIZE):
                        for pixel_row in range(SIZE * j, SIZE * j + SIZE):
                            pixel_map[pixel_row, pixel_column] = WHITE
                else:
                    for pixel_column in range(SIZE * i, SIZE * i + SIZE):
                        for pixel_row in range(SIZE * j, SIZE * j + SIZE):
                            pixel_map[pixel_row, pixel_column] = GREY
            else:
                for pixel_column in range(SIZE * i, SIZE * i + SIZE):
                    for pixel_row in range(SIZE * j, SIZE * j + SIZE):
                        pixel_map[pixel_row, pixel_column] = (GREEN[0], max(0, GREEN[1] - COLOR_STEP * (input_life[i][j])), GREEN[2])
    snapshot.save(file_path + file_name + str(number) + file_type)


def game_life(input_file, number_of_steps):
    life = get_initial_config(input_file)
    snapshot_life(life, 0)
    for iterator in range(1, number_of_steps+1):
        life = simulate_life(life)
        snapshot_life(life, iterator)


file = r"C:\Users\Victoria\Documents\ITMO_Course\Python\ITMO2022_Python\Files_Practice3\InitialConfig.txt"
game_life(file, 20)
