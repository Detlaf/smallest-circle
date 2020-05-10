def find_circle_galois(p1, p2, p3):
    p1 = complex(p1[0], p1[1])
    p2 = complex(p2[0], p2[1])
    p3 = complex(p3[0], p3[1])

    w = (p3 - p1) / (p2 - p1)
    c = ((p1 - p2) * (w - abs(w)**2)) / 2j /w.imag - p1

    circle = {}
    circle['center'] = []
    circle['center'].append(-(c.real))
    circle['center'].append(-(c.imag))
    circle['radius'] = abs(c + p1)

    return circle