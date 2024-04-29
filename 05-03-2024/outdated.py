months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

while True:
    user_input = input("Date: ")

    if "/" in user_input:
        date = user_input.split("/")
    elif "," in user_input:
        date = user_input.replace(",", "").split(" ")
    else:
        continue

    try:
        month = int(date[0]) if date[0].isdigit() else months.index(date[0]) + 1
        day = int(date[1])
        year = int(date[2])
        if month < 1 or month > 12 or day < 1 or day > 31 or year < 1:
            continue
        break
    except (ValueError, IndexError):
        pass

print(f"{year}-{month:02}-{day:02}")
