input_string = (12, '気温', 22.4)

def concat_string(x, y, z):
    return str(x) + 'の時の' + str(y) + 'は' + str(z)

print(concat_string(input_string[0],input_string[1],input_string[2]))