ta=int(input("Escolha o número da tabuada que deseja saber: "))

for count in range(10):
    a = count+1
    result = ta* a

    print("{} x {} = {}".format(ta,a, result ))
