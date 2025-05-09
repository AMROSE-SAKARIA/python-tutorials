
sec = int(input("Enter time in seconds: "))
hours = sec // 3600
min = (sec % 3600) // 60
sec = sec % 60
print(f"Time in HH:MM:SS format: {hours:02}:{min:02}:{sec:02}")