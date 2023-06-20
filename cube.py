def cube(n):
    result = ""
    # generar parte arriba
    for i in range(n):
        result +=" "*(n-i-1)+"/\\"*(i+1) + "_\\"*n+"\n"

    #generar parte de abajo
    for i in range(n):
        result += " "*(i) + "\\/"*(n-i)+"_/"*n+"\n"
    return result
print(cube(4))
