import time
import pandas as pd
import numpy as np

# Get Filters
"""
Asks user to specify a city, month, and day to analyze.

with open(chicago.csv) as csv
read csv

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
def get_city():
    print("Howdy pardner! I'm gonna learn you some U.S. bikeshare data!\n")
    cities = ['chicago', 'new_york_city', 'washington']
    chi_file = 'chicago.csv'
    ny_file = 'new_york_city.csv'
    wash_file = 'washington.csv'
    city = ''
    while city.lower not in cities:
        city = input('\nPlease Enter City:'
                     '\n Type 1 For Chicago'
                     '\n Type 2 for NY'
                     '\n Type 3 for Washington\n')
        if city == '1':
                     return chi_file
        elif city == '2':
                     return ny_file
        elif city == '3':
                     return wash_file
        else:
            print('\nInvalid Selection. Please Try Again.\n')

def get_month():
    months = ['1', '2', '3', '4', '5', '6', '0']
    jan = '1'
    feb = '2'
    mar = '3'
    apr = '4'
    may = '5'
    jun = '6'
    all = '0'
    month = ''
    while month.lower not in months:
        month = input('\nEnter Month:'
                      '\n Type 1 for January'
                      '\n Type 2 for February'
                      '\n Type 3 for March'
                      '\n Type 4 for April'
                      '\n Type 5 for May'
                      '\n Type 6 for June'
                      '\n Type 0 for All\n')
        if month == 'January' or month == 'Jan' or month == '1':
            return jan
        elif month == 'February' or month == 'Feb' or month == '2':
            return feb
        elif month == 'March' or month == 'Mar' or month == '3':
            return mar
        elif month == 'April' or month == 'Apr' or month == '4':
            return apr
        elif month == 'May' or month == '5':
            return May
        elif month == 'June' or month == 'Jun' or month == '6':
            return jun
        elif month == 'All' or month == '0':
            return all
        else:
            print('\nInvalid Selection. Please Try Again.\n')

def get_weekday():
    weekdays = ['1','2','3', '4', '5', '6', '7', '0']
    sun = '6'
    mon = '0'
    tue = '1'
    wed = '2'
    thu = '3'
    fri = '4'
    sat = '5'
    all = '8'
    day = ''
    while day.lower not in weekdays:
        day = input('\nEnter Day of Week:'
                      '\n Type 1 for Sunday'
                      '\n Type 2 for Monday'
                      '\n Type 3 for Tuesday'
                      '\n Type 4 for Wednesday'
                      '\n Type 5 for Thursday'
                      '\n Type 6 for Friday'
                      '\n Type 7 for Saturday'
                      '\n Type 0 for All\n')
        if day == 'sunday' or day == 'sun' or day == '1':
            return sun
        elif day == 'monday' or day == 'mon' or day == '2':
            return mon
        elif day == 'tuesday' or day == 'tue' or day == '3':
            return tue
        elif day == 'wednesday' or day == 'wed' or day == '4':
            return wed
        elif day == 'thursday' or day == 'thu' or day == '5':
            return thu
        elif day == 'friday' or day == 'fri' or day == '6':
            return fri
        elif day == 'saturday' or day == 'sat' or day == '7':
            return sat
        elif day == 'All' or day == '0':
            return all
        else:
            print('Invalid Selection. Please Try Again.')
def get_filters():
    return get_city(), get_month(), get_weekday()



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday
    df["day_of_week_name"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
    df["Trip"] = (df["Start Station"]+"-"+df["End Station"])

    if month != "0":
        df = df[df["month"] == int(month)]
    if day != "8":
        df = df[df["day_of_week"] == int(day)]
    return df

def data_prev(df):
    print ('Data Preview - 10 Rows:')
    print('-'*120)
    i=0
    dfid = df.rename(columns={"Unnamed: 0" : "ID"}).reset_index()

    while True:
        i+=10
        print(dfid.iloc[i-10:i])
        print()
        cont = input('\nContinue:'
                      '\n Type 1 for Yes'
                      '\n Type 2 for No\n')
        if cont != '1':
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('-'*120)

# TO DO: display the most common month

    if len(df["month"].unique()) > 1:
        # display the most common month
        popular_month = df["month"].mode()[0]
        popular_month_cnt = df["month"].value_counts()[6]
        print("Most Popular Month: {}".format(popular_month)+" ({})\n".format(popular_month_cnt))
    else:
        print('Most Popular Month: N\A (data filter)\n')

 # TO DO: display the most common day of week

    if len(df["day_of_week_name"].unique()) > 1:
        # display the most common month
        popular_day = df["day_of_week_name"].mode()[0]
        popular_day_cnt = df["day_of_week_name"].value_counts()[0]
        print("Most Popular Day of Week: {}".format(popular_day)+" ({})\n".format(popular_day_cnt))
    else:
        print('Most Popular Day of Week: N\A (data filter)')

    # TO DO: display the most common start hour

    if len(df["hour"].unique()) > 1:
        # display the most common month
        popular_hour = df["hour"].mode()[0]
        popular_hour_cnt = df["hour"].value_counts()[0]
        print("Most Popular Hour: {}".format(popular_hour)+" ({})\n".format(popular_hour_cnt))
    else:
        print('Most Popular Hour: N\A (data filter)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

# TO DO: display most commonly used start station

    popular_start = df["Start Station"].mode()[0]
    popular_start_cnt = df["Start Station"].value_counts()[0]
    print("Most Popular Start Station: {}".format(popular_start)+" ({})\n".format(popular_start_cnt))
    #print("Most Popular Start Station Count: {}\n".format(popular_start_cnt))

# TO DO: display most commonly used end station

    popular_end = df["End Station"].mode()[0]
    popular_end_cnt = df["End Station"].value_counts()[0]
    print("Most Popular End Station: {}".format(popular_end)+" ({})\n".format(popular_end_cnt))

# TO DO: display most frequent combination of start station and end station trip

    popular_trip = df["Trip"].mode()[0]
    popular_trip_cnt = df["Trip"].value_counts()[0]
    print("Most Popular Trip (Combination of Start & End Stations): {}".format(popular_trip)+" ({})\n".format(popular_trip_cnt))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration Stats...\n')
    start_time = time.time()

# TO DO: display total travel time

    total_dur = (df["Trip Duration"].sum())
    total_trips = (df["Trip"].value_counts().sum())
    tot_min, tot_sec = divmod(total_dur,60)
    tot_hr, tot_min = divmod(tot_min, 60)
    print("Total Trip Duration: {} hrs. {} mins. and {} secs.\n".format(tot_hr, tot_min, tot_sec))

# TO DO: display mean travel time

    avg_min, avg_sec = divmod(total_dur/total_trips, 60)
    avg_hr, avg_min = divmod(avg_min, 60)
    print("Average Trip Duration: {} hrs. {} mins. and {:0.1f} secs.\n".format(avg_hr, avg_min, avg_sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_cnt = df["User Type"].value_counts()
    user_type_cnt_dict = dict(user_type_cnt)
    print("Count by User Types:\n")
    for key, val in user_type_cnt_dict.items():
        print("{}: {:,}".format(key, val))

def gender_type_stats(df):
    """Displays statistics on bikeshare gender types."""

    print("\nCalculating Gender Type Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of gender
    gender_count = df["Gender"].value_counts()
    gender_count_dict = dict(gender_count)
    print("Count by gender:\n")
    for k, v in gender_count_dict.items():
        print("{}: {:,}".format(k, v))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)

def birth_yr_stats(df):
    """Displays statistics on bikeshare birth year types."""

    print("\nCalculating Birth Year Stats...\n")
    start_time = time.time()

     # Display Earliest Birth Year
    min_bd = df["Birth Year"].min().__int__()
    print('Earliest Birth Yr: {}\n'.format(min_bd))

    # Display Latest Birth Year
    max_bd = df["Birth Year"].max().__int__()
    print('Latest Birth Yr: {}\n'.format(max_bd))

    # Display Latest Birth Year
    most_common_bd = df["Birth Year"].mode().__int__()
    print('Most Common Birth Yr: {}\n'.format(most_common_bd))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*120)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print()
        data_preview = input('\nPreview Data?\n'
                                '\nType 1 for Yes'
                                '\nType 2 for No\n')
        print()
        if data_preview == '1':
            data_prev(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        if city in (['chicago.csv', 'new_york_city.csv']):
            gender_type_stats(df)
        else:
            print('\nCalculating Gender Type Stat...\n'
                  '\nGender Stats Unavailable: (Filter)')
        if city in (['chicago.csv', 'new_york_city.csv']):
            birth_yr_stats(df)
        else:
            print('Birth Year Stats Unavailable: (Filter)')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
