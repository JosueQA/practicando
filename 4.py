    ret = ""
    
    for i, letra in enumerate(code):
    
        pin_num = 0

        if letra == "[":
            if code[i+1] == "<":
                pin_num = str("")
                pin_num = ret[-1:]
            else:
            
                pin_num = int(code[i+1])
                pos_prov = i + 2

                while code[pos_prov] != "]":
                    if code[pos_prov] == "+":
                        pin_num = pin_num + 1
                    elif code[pos_prov] == "-":
                        pin_num = pin_num - 1        
                        
                    pos_prov = pos_prov + 1

                pin_num = str(pin_num)

                if int(pin_num) > 9:
                    pin_num = str(int(pin_num) - 10)
                elif int(pin_num) < 0:
                    pin_num = str(int(pin_num) + 10)

            ret = ret + str(pin_num)
    if len(ret) < 4:
        return None
    return ret
