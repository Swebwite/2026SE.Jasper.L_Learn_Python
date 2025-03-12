months = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
]

def main():
    while True:
        date = input('Whats the date? ')
        if any(x in date for x in months):
            date = wdateconvert(date)
            break
        elif '/' in date:
            date = ndateconvert(date)
            break
        else:
            print("Invalid date format. Please try again.")
    print(date)

def wdateconvert(xdate):
    xdate = xdate.strip()
    xdate = xdate.replace(',', '')
    month, day, year = xdate.split(' ')
    month = months.index(month)
    month = int(month)
    month += 1
    day = int(day)
    year = int(year)
    return(f'{year}-{month:02}-{day:02}')

def ndateconvert(xdate):
    xdate = xdate.strip()
    month, day, year = xdate.split('/')
    month = int(month)
    day = int(day)
    year = int(year)
    return(f'{year}-{month:02}-{day:02}')


main()