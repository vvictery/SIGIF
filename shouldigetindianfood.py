from datetime import datetime
import random
nowtime = datetime.now()
today = str(nowtime.date())
mtime = str(nowtime.time().isoformat(timespec="seconds"))
greendays = ('2024-12-06', '2024-12-11', '2024-12-20', '2025-01-03', '2025-01-17', '2025-01-31', '2025-02-07', '2025-02-21', '2025-03-07', '2025-03-21', '2025-04-04', '2025-04-18', '2025-05-02', '2025-05-16', '2025-05-30', '2025-06-13', '2025-06-27', '2025-07-11', '2025-07-25', '2025-08-08', '2025-08-22', '2025-09-12', '2025-09-26', '2025-10-10', '2025-10-24', '2025-11-07', '2025-11-21', '2025-12-05', '2025-12-19', '2026-01-02', '2026-01-16', '2026-01-30', '2026-02-06', '2026-02-20', '2026-03-06', '2026-03-20', '2026-04-03', '2026-04-17', '2026-05-08', '2026-05-22', '2026-06-12', '2026-06-26', '2026-07-10', '2026-07-24', '2026-08-07', '2026-08-21', '2026-09-04', '2026-09-18', '2026-10-02', '2026-10-16', '2026-10-30', '2026-11-13', '2026-11-27', '2026-12-11', '2026-12-25', '')
specialdays = {
    "2024-12-12" : "Test Day",
    "2024-12-25" : "Christmas",
    "2024-12-31" : "New Years Eve",
    "2025-01-01" : "New Years Day",
    "2025-04-15" : "Tax Day",
    "2025-12-25" : "Christmas",
    "2025-12-31" : "New Years Eve",
    "2026-01-01" : "New Years Day",
    "2026-04-15" : "Tax Day",
    
}
vegoptions = ('Vegetable Biryani', 'Vegetable Malai Kofta', 'Matar Paneer', 'Palak Paneer', 'Navratan Curry', 'Dal Makhni', 'Baingen Bhartha', 'Dum Aloo', 'Vegetable Jalfrezi', 'Paneer Masala', 'Kadhi Kofta', 'Aloo Palak', 'Tarka Dal', 'Punjabi Bhaji', 'Bhindi Masala', 'Mixed Vegetables', 'Vegetarian Thali',)
#veganoptions = ('Channa Masala', 'Aloo Gobi', )

def shouldigetindianfood():
    print ('------------------------------------------------------------------')
    print ('                             Welcome to                           ')
    print(r'      ___                       ___                       ___     ')
    print(r'     /\__\                     /\__\                     /\__\    ')
    print(r'    /:/ _/_       ___         /:/ _/_       ___         /:/ _/_   ')
    print(r'   /:/ /\  \     /\__\       /:/ /\  \     /\__\       /:/ /\__\  ')
    print(r'  /:/ /::\  \   /:/__/      /:/ /::\  \   /:/__/      /:/ /:/  /  ')
    print(r' /:/_/:/\:\__\ /::\  \     /:/__\/\:\__\ /::\  \     /:/_/:/  /   ')
    print(r' \:\/:/ /:/  / \/\:\  \__  \:\  \ /:/  / \/\:\  \__  \:\/:/  /    ')
    print(r'  \::/ /:/  /   ~~\:\/\__\  \:\  /:/  /   ~~\:\/\__\  \::/__/     ')
    print(r'   \/_/:/  /       \::/  /   \:\/:/  /       \::/  /   \:\  \     ')
    print(r'     /:/  /        /:/  /     \::/  /        /:/  /     \:\__\    ')
    print(r'     \/__/         \/__/       \/__/         \/__/       \/__/    ')
    print ()
    print ('                        Today is: ' + today)
    print ('------------------------------------------------------------------')
    print ('Who is it?')
    uname = input()
    if uname in  ('Joe', 'joe', 'JOE',):
        print (r"01001000 01101001 00100000 01001010 01101111 01100101")
    else:
        print ('Hi ' + uname)
    input ('Password: ')
# note the password input is tied to nothing, essentially a pass func that waits on the user to 'enter'
    print ('------------------------------------------------------------------')
    print ("Why wouldn't you get Indian food?")
    print ('Time or Money?')
    reason = input()
    if reason in ("Time", "time", "TIME",):
        print ('It is currently: ' + mtime)        
        if '22:00:00' > mtime > '11:00:00':
            print ('India Hut is probably open!')
        else:
            pass
    elif reason in ("Money", "money", "MONEY",):
        if today in greendays :
            print ('It is a payday!')
        elif today in specialdays :
            print ('Today is ' + specialdays[today])
        else:
            print ('There is always payday...')
            print ('Goodbye!')
            exit()
    else: 
        print ('Not a good reason')
        print ("Just get some Indian food")
    print ('------------------------------------------------------------------')
    print ('Do you need help picking your entree?')
    answer = input()
    if answer in ('y', 'yes', 'YES', 'Yes',) :
        print ((random.choice(vegoptions)) + " Is Vegetarian!")
#        print ((random.choice(veganoptions)) + " Is Vegan!")
    elif answer in ('n', 'no', 'NO', 'No',) :
        print ('Goodbye!')
        exit()
    else :
        print ('Goodbye!')
        exit()
        
# should I get Indian food today?
# probably doesn't require all this to figure it out.

shouldigetindianfood ()