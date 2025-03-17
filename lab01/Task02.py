#File55. Дана строка S0, целое число N (≤ 4) и N файлов целых чисел с именамиS1, …, SN.
# Объединить их содержимое в новом файле-архиве с именем S0, последовательно записываявнего следующие данные:
# размер (число элементов) первого исходного файла и все элементы этого файла, размер второго исходного файла
# и все его элементы, …, размер N-гоисходного файла и все его элементы.

def sozdati(S0,a):
    b=a+1
    for i in range(1,b):
        mas = [b'1\n', b'2\n', b'3\n', b'4\n', b'5\n', b'6\n', b'7\n', b'8\n', b'9\n', b'10\n', ]
        nazw=S0+str(i)+".bin"
        with open(nazw, mode="wb") as file:
            file.writelines(mas)
def otw(S0,a):
    b = a + 1
    m = []
    sum=[]
    for i in range(1, b):
        nazw = S0 + str(i) + ".bin"
        file= open(nazw, mode="rb")
        a = file.readlines()
        file.close()
        for i in range(len(a)):
            m.append(a[i])
        sum.append(len(a))

    nazw = S0+"0" + ".bin"
    with open(nazw, mode="wb") as file:
        for i in range(len(sum)):
            zap=bytes(str(sum[i]),encoding="utf-8")
            file.write(zap)
            file.write(b"\n")
            for j in range(sum[i]):
                file.write(m[j])
            m=m[sum[i]::]


S0=str(input("Введите строку S0\n"))
try:
    a = int(input("Введите число исходных файлов\n"))
    sozdati(S0, a)
    otw(S0, a)
except:
    print("Вы ввели не число")