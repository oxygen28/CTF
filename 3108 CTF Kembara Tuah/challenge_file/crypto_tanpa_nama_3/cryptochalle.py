def xor_with_binary(binary_str, xor_str):
    binaries = binary_str.split()
    xor_num = int(xor_str, 2)
    xor_results = []
    for b in binaries:
        num = int(b, 2)
        result_num = num ^ xor_num
        xor_results.append(format(result_num, '08b'))
    return ' '.join(xor_results)

binary_str = "01010110 01010100 01010101 01011101 00011110 00110110 01010100 00101000 00110101 00101001 01010110 00111010 00100110 00110111 00110101 00111100 00110001 01010101 00111010 00100110 00101101 00100100 00101001 00101001 00100000 00101011 00100010 00100000 00011000"
xor_str = "01100101"
