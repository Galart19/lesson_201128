print('Hello, world')
GPU = [
    ['MSI', '152 990 ₽', '59 999 ₽', '59 590 ₽'],
    ['GIGABYTE', '154 990 ₽', '57 990 ₽', '27 679 ₽'],
    ['ASUS', '175 990 ₽', '68 900 ₽', '44 190 ₽'],
    ['Palit', '146 239 ₽', '57 000 ₽', '33 935 ₽']
]


def show_price_3090(GPU_3090_price):
    print('Цена на видеокарту 3090  - ', GPU_3090_price[0], GPU_3090_price[1:2])


def show_price_2080(GPU_2080_price):
    print('Цена на видеокарту 2080  - ', GPU_2080_price[0], GPU_2080_price[2:3])


def show_price_1080(GPU_1080_price):
    print('Цена на видеокарту 1080  - ', GPU_1080_price[0], GPU_1080_price[3:4])


for price in GPU:
    show_price_3090(price)
    show_price_2080(price)
    show_price_1080(price)
