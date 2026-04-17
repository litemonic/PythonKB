def gyometricalProgression(report, count, base = 1, index = 0):
    if index >= count:
        return 0
    return base + gyometricalProgression(report, count, base * report, index+1)
    
report = 2 #знаменатель прогрессии
count = 5 #количество слагаемых
result = gyometricalProgression(report, count)
print(f"сумма геометрической прогрессии (1 + {report} + {report**2} + ... + {report**(count - 1)}): {result}")