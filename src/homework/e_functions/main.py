# import functions
import value_return

total_seconds_input = int(input("Enter the total amount of seconds to figure out the time: "))
get_hour = value_return.get_hours(total_seconds_input)
get_minute = value_return.get_minutes(total_seconds_input)
get_second = value_return.get_seconds(total_seconds_input)

print("This is the time: ", "%02d" % get_hour, ":", "%02d" % get_minute, ":", "%02d" % get_second, sep='')