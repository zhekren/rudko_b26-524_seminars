def f():
    maxi = 0
    st = ''
    while True:
        stroke = input()
        if stroke == "STOP":
            break
        st_low = stroke.lower()
        if maxi < len(set(st_low)):
            maxi = len(set(st_low))
            st = stroke
    print(st, maxi)

f()

