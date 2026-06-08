'''
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4
'''
Total_sec = int(input("Enter total seconds:"))
Hr = Total_sec//3600
Mi = (Total_sec-Hr*3600)//60
sec =(Total_sec-Hr*3600-Mi*60)
print(f"Hours {Hr}\nMinutes {Mi}\nSeconds {sec}")