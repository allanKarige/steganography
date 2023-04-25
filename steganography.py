from PIL import Image
import os


def string_to_bits(message):
    string = str(message)
    bytes_list = bytes(string, 'utf-8')
    bits = []
    mags = []
    for byte in bytes_list:
        bins = bin(byte)
        bits.append(bins)
        mags.append(len(bins) - 2)

    return bits, mags


def replace_at_end(string, letter):
    chars = list(string)
    chars.pop(-1)
    chars.append(letter)
    res = ''.join(chars)
    return res


def conv2list(tuples_in_list):
    box = []
    for tuple in tuples_in_list:
        box.append(list(tuple))

    return box


def conv2tuple(lists_in_list):
    box = []
    for list in lists_in_list:
        box.append(tuple(list))

    return box


def decimal_to_bits(list):
    box = []
    for byte in list:
        box.append(bin(byte))

    return box


def bits_to_decimal(list):
    box = []
    for byte in list:
        box.append(int(byte, 2))

    return box


def get_sum(seq):
    sum = 0
    for num in seq:
        sum += num

    return sum


def msg_data2string(message_data, mags):
    res = []
    j = 0
    for mag in mags:
        byte = []
        for i in range(mag):
            byte.append(str(message_data[j]))
            j += 1
        byte = ''.join(byte)
        res.append(byte)

    result = []
    for word in res:
        result.append(f'0b{word}')

    chars = []
    for l in result:
        chars.append(int(l, 2))

    chars2 = bytes(chars)
    msg = str(chars2, 'utf-8')

    return msg


def to_pixels(num):
    res = num // 255
    modulo = num % 255
    fin = []
    for i in range(res):
        fin.append(255)
    fin.append(modulo)

    return fin


def encode(image, msg):
    img = Image.open(image)
    msg_bit_list, mag = string_to_bits(msg)
    length = get_sum(mag)
    total_digits = int(length)
    pixels0 = conv2list(list(img.getdata())[:total_digits])

    img_bits = []
    for i in range(total_digits):
        img_bits.append(pixels0[i][0])

    red_pixel_values = decimal_to_bits(img_bits)
    i = 0
    new_red_pixels = []
    for byte in msg_bit_list:
        for bit in byte[2:]:
            new_red_pixel = replace_at_end(red_pixel_values[i], bit)
            new_red_pixels.append(new_red_pixel)
            i += 1

    encoded_red_pixels = bits_to_decimal(new_red_pixels)
    pixels1 = conv2list(list(img.getdata()))

    for i in range(len(encoded_red_pixels)):
        pixels1[i][0] = encoded_red_pixels[i]

    number_of_words = len(mag)
    word_list = to_pixels(number_of_words)
    for i in range(len(word_list)):
        j = i + 1
        pixels1[-j][0] = word_list[i]
    pixels1[-1][2] = len(word_list)

    for j in range(number_of_words):
        pixels1[j][2] = mag[j]

    pixels2 = conv2tuple(pixels1)
    img.putdata(pixels2)

    return img


def decode(image):
    img = Image.open(image)
    pixels0 = list(img.getdata())

    word_list = []
    for i in range(pixels0[-1][2]):
        j = i + 1
        word_list.append(pixels0[-j][0])

    number_of_words = get_sum(word_list)
    mag = []
    for p in range(number_of_words):
        mag.append(pixels0[p][2])

    length = get_sum(mag)
    total_digits = int(length)

    encoded_red_pixels = []
    for i in range(total_digits):
        encoded_red_pixels.append(pixels0[i][0])

    reds_bits = decimal_to_bits(encoded_red_pixels)

    message_data = []
    for byte in reds_bits:
        message_data.append(str(byte[-1]))

    msg = msg_data2string(message_data, mag)

    return msg


if __name__ == '__main__':
    print(decode('to_beauty.png'))
