average_speed = float(input("Enter your average speed (mph): ")) 
speed_limit = float(input("Enter the speed limit (mph): ")) 
distance = float(input("Enter the distance travelled (miles): ")) 
time_at_limit = distance / speed_limit 
time_at_average_speed = distance / average_speed 
time_saved_minutes = (time_at_limit - time_at_average_speed) * 60 
print(f"You saved {time_saved_minutes:.0f} minutes.") 