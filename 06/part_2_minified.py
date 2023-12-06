t,d=[int(l.replace(' ','').split(':')[1])for l in open('input.txt')];o=(t**2-4*d)**0.5/2;print(int(t/2+o)-int(t/2-o))  # noqa
