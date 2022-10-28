def d_log(num):
    i = 1
    while num >= 10 ** i:
        i += 1
    return(i)


print(d_log(0))