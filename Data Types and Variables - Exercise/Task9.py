N = int(input())

max_value = 0
max_snow = 0
max_time = 0
max_quality = 0

for i in range(N):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())

    snowballValue = (snowballSnow / snowballTime) ** snowballQuality
    if snowballValue > max_value:
        max_value = snowballValue
        max_snow = snowballSnow
        max_time = snowballTime
        max_quality = snowballQuality


print(f"{max_snow} : {max_time} = {max_value:.0f} ({max_quality})")