def decodeSantaPin(code):
    
    ret = ""
    pin_num = ""
    for i, letra in enumerate(code):
        if code[pos_prov] == "<":
            pin_num = ret[-1:]
        elif letra = "[":
            pin_num = int(code[i+1])
            pos_prov = i + 2
            while code[pos_prov] != "]":

                if code[pos_prov] == "+":
                    pin_num = pin_num + 1

                elif code[pos_prov] == "-":
                    pin_num = pin_num - 1

                pos_prov = pos_prov + 1 
            ret = ret + str(pin_num)
    print(ret)

decodeSantaPin('[1++][2-][3+][<]')
