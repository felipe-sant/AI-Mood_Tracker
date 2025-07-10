def translate(label):
    stars = int(label.split()[0])
    if stars <= 2:
        return "Negative"
    elif stars == 3:
        return "Neutral"
    else:
        return "Positive"