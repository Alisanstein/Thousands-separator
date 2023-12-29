def format_number(a):
    a = str(a)
    a = list(a)
    count = 0
    khali = []

    for i in a[::-1]:
        count += 1
        khali.append(i)

        if count%3==0:
            khali.append(',')

    r = list(reversed(khali))
    if r[0] == ',':
        r.remove(',')
    output = ''.join(r)
    
    return output
