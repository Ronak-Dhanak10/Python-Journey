# 6. Weather Monitoring System
#    A system checks weather conditions:

# * If temperature ≥ 30 → Hot day
# * If humidity ≥ 70 → High humidity alert

# Input:
# Enter temperature: 32
# Enter humidity: 75

# Output:
# Hot day
# High humidity alert
tem = int(input("Enter the themperature:"))
humidity = int(input("Enter the humidity:"))
if tem >= 30:
    print("Hot Day")
if humidity >=70:
    print("High humidity alert:")
# else:
#     print("cold DAY")