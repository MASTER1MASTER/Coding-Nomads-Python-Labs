# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)


distance_in_miles = 10
time = 30.30

km_conversion = 1.6
distance_km = distance_in_miles * km_conversion
time_in_hrs = time/60

avg_speed = distance_km / time_in_hrs


print(avg_speed)