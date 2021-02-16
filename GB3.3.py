def summa(a, b, c):
    znach = [a, b, c]
    maximum = []
    m_1 = max(znach)
    maximum.append(m_1)
    znach.remove(m_1)
    m_2 = max(znach)
    maximum.append(m_2)
    print(sum(maximum))
summa(5, 6, 2)


