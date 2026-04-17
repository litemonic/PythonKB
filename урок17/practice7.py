text = "Hello world!"
vovel = "aeiyuoAEYUIO"
i = 0
while i < len(text):
    if text[i] in vovel:
        print(f"В этом слове есть гласная: {text[i]}")
    i+=1
