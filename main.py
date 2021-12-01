from booking.bookings import Booking 

with Booking() as bot: 
    bot.land_first_page()
    # function to change the currency 
    # bot.change_currency()
    # function to change the selected country 
    bot.select_place('New York')
    bot.select_dates(check_in_date='2021-12-16', 
                     check_out_date='2021-12-23')
    bot.select_adults(count=2)
    bot.submit_query()
    print('Exiting ... ')