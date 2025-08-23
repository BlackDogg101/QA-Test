def hookah_counter():
    """Считаем сумму кальянов и отнимаем долю заведения"""
    hookahs = list(map(int, input('Вставить список: ').split()))
    summ = 0
    for h in hookahs:
        if h < 4999:
            summ += h - 1000
        else:
            summ += h - 1500
    print(f"Сумма кальянов: {summ}")

hookah_counter()