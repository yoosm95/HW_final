import numpy as np
import glob, os

def MOTA(path, output):
    temp = open(output, "w")
    for files in sorted(os.listdir(path)):
        undet = 0
        for i in range(99):
            file = open(os.path.join(path, f'{files}/undet/{i+1}.csv'))
            numpy_array = np.loadtxt(file, delimiter=",")
            undet+=numpy_array.size

        untrks = 0
        for i in range(99):
            file = open(os.path.join(path, f'{files}/untrk/{i+1}.csv'))
            numpy_array = np.loadtxt(file, delimiter=",")
            untrks+=numpy_array.size

        list = []
        for i in range(1, 99):
            file = open(os.path.join(path, f'{files}/matched/{i+1}.csv'))
            numpy_array = np.loadtxt(file, delimiter=",")
            list.append(numpy_array)

        idsw = 0
        for i in range(len(list)-1):
            for j in range(len(list[i])):
                for k in range(len(list[i+1])):
                    try:
                        if list[i+1][k][0] == list[i][j][0]:
                            if list[i+1][k][1] == list[i][j][1]:
                                pass
                            else:
                                idsw +=1
                    except:
                        a = 1

        file = open(os.path.join(path, f'{files}/det/det.txt'))
        array = np.loadtxt(file, delimiter=',')
        MOTA = 1 - (idsw + undet + untrks) / (len(array) - len(array[0]))

        temp.write(files)
        temp.write(" : ")
        temp.write(str(MOTA))
        temp.write("\n")

        # print(files ," : ", MOTA)

    temp.close()
    return None
#
# print("MOTA : ", MOTA)
# MOTA("./car/train", "mota_car.txt")
MOTA("./person/train", "mota_person.txt")




