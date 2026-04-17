recept_steps = ["Награеть сковородку",
                "Добавить масло",
                "Положить нарезанные овощи"
                "Обжарить до готовности"
                "Посыпать специями и можно подавать блюдо"
                ]
step_iterator = iter(recept_steps)

count = 1
while True:
    try:
        step = next(step_iterator)
        print(f"Шаг {count}: {step}")
        count += 1
    except StopIteration:
        print("Рецепт завершен")
        break

