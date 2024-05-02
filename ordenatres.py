a = input("Digite o primeiro número: ")

b = input("Digite o segundo número: ")

c = input("Digite o terceiro número: ")

if a<=b:
    if c<=a:
        print(f"Os números em ordem são {c}, {a} e {b}")
    elif c<=b:
        print(f"Os números em ordem são {a}, {c} e {b}")
    else:
        print(f"Os números em ordem são {a}, {b} e {c}")
else:
    if c<=b:
        print(f"Os números em ordem são {c}, {b} e {a}")
    elif c<=a:
        print(f"Os números em ordem são {b}, {c} e {a}")
    else:
        print(f"Os números em ordem são {b}, {a} e {c}")
        
