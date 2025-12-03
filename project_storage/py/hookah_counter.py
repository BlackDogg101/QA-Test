def hookah_counter(input_sum):
    """Считаем сумму кальянов и отнимаем долю заведения"""
    hookahs = list(map(int, input_sum.split()))
    summ = 0
    
    for h in hookahs:
        if h in (5000, 6000, 8000):
            summ += (h - 1500)
        elif h in (2500, 3000, 4000):
            summ += (h - 1000)
        else:
            print("Ошибка цены")
            
    print(f"Сумма кальянов: {summ}")

hookah_counter(input('Вставить список: '))