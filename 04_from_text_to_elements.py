input_text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
input_text = input_text.replace(".","")
input_text = input_text.replace(",","")
input_text = input_text.split()

ans_dict = {}

for index, value in enumerate(input_text,start=1):
    if index in (1, 5, 6, 7, 8, 9, 15, 16, 19):
        ans_dict[value[:1]] = index
    else:
        ans_dict[value[:2]] = index

print(ans_dict)
