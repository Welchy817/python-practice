for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int((1*(pow(10, i) - 1)) /9) * int((1*(pow(10, i) - 1)) /9))