from basketball_reference_scraper.seasons import get_schedule, get_standings
import time



start_year = 2000
schedule = get_schedule(start_year, playoffs=False)
print(schedule)







