def C_to_F(C):
    try:
        C = float(C)
        if C > -273.15:
            F = (C*9/5)+32
            print(F)
        else:
            print("Lower than absolute zero")    
    except:
        print("not a number")

C_to_F(200)