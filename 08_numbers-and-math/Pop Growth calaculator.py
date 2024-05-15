current_pop = 380123456


time_in_seconds = 365*24*60*60*3
births = time_in_seconds/6
deaths = time_in_seconds/12
immigrants = time_in_seconds/40


new_pop = (births + immigrants - deaths) + current_pop

print(new_pop)


