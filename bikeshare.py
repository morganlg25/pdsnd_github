import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city not in CITY_DATA:
            print('What you have entered is invalid. Please type Chicago, New York City, or Washington.\n')
        else:
            break 

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('If you would like to filter by month, please enter "January", "February", "March", "April", "May" or "June". For all months, please enter "all".\n').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month != "all" and month not in months:
            print('Please try again and enter a valid month option.\n')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('If you would like to filter by day, please enter a day of the week. Otherwise, enter "all" to seee data for all days.\n').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day != "all" and day not in days:
            print('Please try again and enter a valid day option.\n')
        else:
            break    

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    top_month = df['month'].mode()[0]
    print('The most common month for travel was: ', top_month)

    # TO DO: display the most common day of week
    top_day = df['day_of_week'].mode()[0]
    print('The most common day for travel was: ', top_day)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    top_hour = df['Hour'].mode()[0]
    print('The most common start hour for travel was: ', top_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station was: ', top_start_station)

    # TO DO: display most commonly used end station
    top_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station was: ', top_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    top_combo_station = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('The most common combination of start and end stations were: ', top_combo_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_traveltime = df['Trip Duration'].sum()
    print('The total travel time was: ', total_traveltime, 'in seconds, ', total_traveltime/60, 'in minutes, and ', total_traveltime/3600, 'in hours.')

    # TO DO: display mean travel time
    avg_traveltime = df['Trip Duration'].mean()
    print('The mean travel time was: ', avg_traveltime, 'in seconds, ', avg_traveltime/60, 'in minutes, and ', avg_traveltime/3600, 'in hours.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User type counts were: \n', user_types)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('Gender counts were: \n', gender_counts)
    except:
        print('There is no gender information available using this filter.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = df['Birth Year'].min()
        most_recent_birthyear = df['Birth Year'].max()
        most_common_birthyear = df['Birth Year'].mode()[0]
        print('The earliest user birth year was: ', earliest_birthyear,'\n The most recent user birth year was: ', most_recent_birthyear,'\n The most common user birth year was: ', most_common_birthyear)
    except:
        print('There is no birth year information available using this filter.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def dis_raw_data(df):
    row_start = 0
    raw_data = input('Do you wish to see 5 rows of raw data used in these calculations? Please answer "Yes" or "No". '.lower())
    while True:
        if raw_data == 'no':
            break
        elif raw_data == 'yes':
            print(df[row_start : row_start + 5])
            row_start += 5
            raw_data = input('Do you wish to see an additional 5 rows of raw data? Please answer "Yes" or "No". '.lower())
        else:
            print('Your response was invalid. Please answer "Yes" or "No". '.lower())
    return raw_data

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        dis_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
