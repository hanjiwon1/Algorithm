while(True):
    n = input()
    if n== '0': break
    print(['no','yes'][n==n[::-1]])
