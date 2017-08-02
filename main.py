import csv
import re


'''
#Opening the csv file and reading the contents into item_list, as a dictionary of dictionaries.
'''
with open('input.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    item_list = list(reader)


'''
#Opening the csv file and reading the contents into item_list, as a dictionary of dictionaries.
'''
with open('input.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    item_list = list(reader)

'''
# Function for searching for the category of a specific item.
'''

def search_for_category(category, item_list):
    return [element for element in item_list if element['category'] == category]


'''
# Function for searching for the product_id of a specific item.
'''
def search_for_product_id(product_id, item_list):
    return [element for element in item_list if element['product_id'] == product_id]

'''
# Function for searching for the product_name of a specific item.
'''
def search_for_product_name(product_name, item_list):
    return [element for element in item_list if element['product_name'] == product_name]

'''
# Function for searching for the category of a specific item, if it is contained in a string.
'''
def search_for_product_name_contained(product_name, item_list):
    return [element for element in item_list if product_name in element['product_name']]

'''
# Function for searching for the brand of a specific item.
'''
def search_for_brand(brand, item_list):
    return [element for element in item_list if element['brand'] == brand]

'''
# Function for searching for the brand of a specific item, if it matches two specific brand names.
'''
def search_for_brands(brand1, brand2, item_list):
    return [element for element in item_list if element['brand'] == brand1 or element['brand'] == brand2]

'''
# Function for searching for the lack of a brand of a specific item.
'''
def search_for_lack_of_brand(brand, item_list):
    return [element for element in item_list if element['brand'] != brand]

'''
# Function for searching for the subscription_plan of a specific item.
'''
def search_for_subscription_plan(subscription_plan, item_list):
    return [element for element in item_list if element['subscription_plan'] == subscription_plan]

'''
# Function for printing the final suggestion(item) to the user.
# In the end, it asks whether the user wants to inquire for another item or not.
# If not, it exits the program. If yes, it repeats the main function main() of the program
'''
def print_final_suggestion(final_suggestion):
    print("Estimation Complete! We are suggesting the following item(s):")
    for d in final_suggestion:
        name = d['product_name']
        price = d['subscription_plan']
        print(name + ', with a subscription plan of: ' + price + '€')
    while True:
        x = input("Would you be interested in searching for another product?")
        if len(x) > 1 and re.search('yes|yeah[^A-Z]?', x, re.IGNORECASE):
            print("Thank you for trusting us! Take a look again at our categories:")
            program()
        elif len(x) > 1 and re.search('no[^A-Z]?', x, re.IGNORECASE):
            print('Thank you for using our app! Hope to see you again in the future!')
            break
        else:
            print('Please select a valid choice!!!!!')
        break

'''
# Function for printing the main menu of the program
'''
def print_menu():
    print("Please select what type of product you would like to purchase:")
    print('*** Phones & Tablets ***')
    print('*** Gaming & Gadgets ***')
    print('*** Computing ***')
    print('*** Wearables ***')
    print('*** Smart Home ***')

'''
# Function for searching for phones and tablets
'''
def search_for_phones_and_tablets():
        while True:
            category_preference = search_for_category('Phones & Tablets', item_list)
            x = input("Do you prefer Apple or Samsung phones?")
            if len(x) > 2 and re.search('apple|ios[^A-Z]?', x, re.IGNORECASE):
                search_for_item_iphone(category_preference)
                break
            elif len(x) > 3 and re.search('samsung[^A-Z]?', x, re.IGNORECASE):
                brand_preference = search_for_brand('Samsung', category_preference)
                while True:
                    x = input("Are you a fan of bigger or smaller screen sizes?")
                    if len(x) > 2 and re.search('big[^A-Z]?', x, re.IGNORECASE):
                        final_suggestion = search_for_product_name('Galaxy S8+ 64GB', brand_preference)
                        print_final_suggestion(final_suggestion)
                        break
                    elif len(x) > 3 and re.search('small[^A-Z]?', x, re.IGNORECASE):
                        final_suggestion = search_for_product_name('Galaxy S8 64GB', brand_preference)
                        print_final_suggestion(final_suggestion)
                        break
                    elif re.search('exit', x, re.IGNORECASE):
                        break
                    else:
                        print("Please select a valid choice!")
                break
            elif re.search('exit', x, re.IGNORECASE):
                break
            else:
                print("Please select a valid choice!")


'''
# Function for searching for gaming and gadgets
'''
def search_for_gaming_and_gadgets():
        while True:
            x = input("Are you more interested in: VRs or Drones?")
            if len(x) > 2 and re.search('drone[^A-Z]?', x, re.IGNORECASE):
                category_preference = search_for_category('Drones', item_list)
                while True:
                    x = input(
                        'Do you care for a more powerful, more robust and increased autonomy model, or could you'
                        ' settle for less? (Yes/No)')
                    if len(x) > 2 and re.search('yeah|yes|power|robust|increas|autonomy[^A-Z]?', x, re.IGNORECASE):
                        final_suggestion = search_for_product_name('Drone BEBOP 2', category_preference)
                        print_final_suggestion(final_suggestion)
                        break
                    elif len(x) > 1 and re.search('nope|settle|less|worse|not good[^A-Z]?', x, re.IGNORECASE):
                        final_suggestion = search_for_product_name('Drone BEBOP', category_preference)
                        print_final_suggestion(final_suggestion)
                        break
                    elif re.search('exit', x, re.IGNORECASE):
                        break
                    else:
                        print("Please select a valid choice!")
                break
            elif len(x) > 1 and re.search('vr[^A-Z]?', x, re.IGNORECASE):
                category_preference = search_for_category('Gaming & VR', item_list)
                print_final_suggestion(category_preference)
                break
            elif re.search('exit', x, re.IGNORECASE):
                break
            else:
                print("Please select a valid choice!")


'''
# Function for searching for computers
'''
def search_for_computing():
    while True:
        category_preference = search_for_category('Computing', item_list)
        x = input("Are you a fan of the Windows or the iOS operating system?")
        if len(x) > 2 and re.search('ios|apple[^A-Z]?', x, re.IGNORECASE):
            search_for_item_macbook()
        elif len(x) > 3 and re.search('not apple|window[^A-Z]?', x, re.IGNORECASE):
            brand_preference = search_for_lack_of_brand('Apple', category_preference)
            print_final_suggestion(brand_preference)
            break
        elif re.search('exit', x, re.IGNORECASE):
            break
        else:
            print('Please select a valid choice!')


'''
# Function for searching for wearables
'''
def search_for_wearables():
    while True:
        category_preference = search_for_category('Wearables', item_list)
        x = input('Are you planning to use this smart watch mostly for sports activities, or as casual '
                  'wear?')
        if len(x) > 3 and re.search('yes|yeah|sport[^A-Z]?', x, re.IGNORECASE):
            final_suggestion = search_for_brands('Suunto', 'Polar', category_preference)
            print_final_suggestion(final_suggestion)
            break
        elif len(x) > 3 and re.search('no|casual|wear[^A-Z]?', x, re.IGNORECASE):
            while True:
                choices_left = search_for_brands('Apple', 'Asus', category_preference)
                x = input("Are you a fan of Apple products? (yes/no)")
                if len(x) > 2 and re.search('yeah|apple|yes[^A-Z]?', x, re.IGNORECASE):
                    while True:
                        next_choice = search_for_brand('Apple', choices_left)
                        x = input('Would you prefer a bigger watch, or a smaller one? (bigger/smaller)')
                        if len(x) > 2 and re.search('yes|yeah|big[^A-Z]?', x, re.IGNORECASE):
                            final_suggestion = search_for_product_name_contained('Watch 42mm', next_choice)
                            print_final_suggestion(final_suggestion)
                            break
                        elif len(x) > 1 and re.search('no|nope|small[^A-Z]?', x, re.IGNORECASE):
                            final_suggestion = search_for_product_name_contained('Watch 38mm', next_choice)
                            print_final_suggestion(final_suggestion)
                            break
                        elif re.search('exit', x, re.IGNORECASE):
                            break
                        else:
                            print('Please select a valid choice!')
                    break
                elif len(x) > 1 and re.search('not apple|nope[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = search_for_brand('Asus', choices_left)
                    print_final_suggestion(final_suggestion)
                    break
                elif re.search('exit', x, re.IGNORECASE):
                    break
                else:
                    print('Please select a valid choice!')
            break
        else:
            print('Please select a valid choice!')


'''
# Function for searching for smart home gadgets
'''
def search_for_smart_home():
    while True:
        category_preference = search_for_category('Smart Home', item_list)
        x = input('Are you interested in products for: listening to some music, cooking some tasty '
                  'milk creations, or cleaning your house?')
        if len(x) > 4 and re.search('leisure|entertain|music|listen[^A-Z]?', x, re.IGNORECASE):
            while True:
                next_choice = search_for_brand('Amazon', category_preference)
                x = input('Would you prefer a stronger speaker, or a more '
                          'compact one?')
                if len(x) > 2 and re.search('yes|yeah|strong[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = search_for_product_name('Alexa Echo', next_choice)
                    print_final_suggestion(final_suggestion)
                    break
                elif len(x) > 1 and re.search('no|nope|less|compact[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = search_for_product_name('Alexa Dot', next_choice)
                    print_final_suggestion(final_suggestion)
                    break
                elif re.search('exit', x, re.IGNORECASE):
                    break
                else:
                    print('Please select a valid choice!')
            break
        elif len(x) > 3 and re.search('cook|tasty|milk|creat[^A-Z]?', x, re.IGNORECASE):
            final_suggestion = search_for_brand('Tchibo', category_preference)
            print_final_suggestion(final_suggestion)
            break
        elif len(x) > 4 and re.search('house|clean[^A-Z]?', x, re.IGNORECASE):
            final_suggestion = search_for_product_name_contained('Vacuum', category_preference)
            print_final_suggestion(final_suggestion)
            break
        elif re.search('exit', x, re.IGNORECASE):
            break
        else:
            print('Please select a valid choice!')


def search_for_item_vacuum():
    print_final_suggestion(search_for_product_name_contained('Vacuum Cleaner', item_list))


def search_for_item_drone():
    print_final_suggestion(search_for_product_name_contained('Drone', item_list))


'''
# Function for searching for macbooks directly
'''
def search_for_item_macbook():
    while True:
        brand_preference = search_for_product_name_contained('MacBook', item_list)
        x = input('Are you interested: (1) In a larger display but with less memory (RAM),'
                  ' or (2) in a smaller display with more memory (RAM)?')
        if len(x) > 2 and re.search('big|large|less[^A-Z]?', x, re.IGNORECASE):
            while True:
                choices_left = search_for_product_name_contained('4GB RAM', brand_preference)
                x = input('Would you prefer a larger hard disk or a smaller one? (500GB/128GB)')
                if len(x) > 2 and re.search('500|large[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = search_for_product_name_contained('500', choices_left)
                    print_final_suggestion(final_suggestion)
                    break
                elif len(x) > 2 and re.search('128|small[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = search_for_product_name_contained('128', choices_left)
                    print_final_suggestion(final_suggestion)
                    break
                elif re.search('exit', x, re.IGNORECASE):
                    break
                else:
                    print('Please select a valid choice!')
            break
        elif len(x) > 3 and re.search('small|more[^A-Z]?', x, re.IGNORECASE):
            while True:
                choices_left = search_for_product_name_contained('8GB RAM', brand_preference)
                x = input('Would you care for a more powerful (i7) or a simpler (i5) processor?')
                if len(x) > 1 and re.search('no|simple|i5[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = search_for_product_name_contained('MacBook 12" M-5Y31', choices_left)
                    print_final_suggestion(final_suggestion)
                    break
                elif re.search('yes|yeah|strong|more|powerful|i7[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = search_for_product_name_contained('i7', choices_left)
                    print_final_suggestion(final_suggestion)
                    break
                elif re.search('exit', x, re.IGNORECASE):
                    break
                else:
                    print('Please select a valid choice!')
            break
        elif re.search('exit', x, re.IGNORECASE):
            break
        else:
            print('Please select a valid choice!')


'''
# Function for searching for VR glasses directly
'''
def search_for_item_glasses():
    print_final_suggestion(search_for_category('Gaming & VR', item_list))


'''
# Function for searching for iphones directly
'''
def search_for_item_iphone(preference):
    while True:
        brand_preference = search_for_product_name_contained('iPhone', preference)
        x = input("Do you prefer a smaller or a bigger hard drive for your iPhone? (32 GBs/128 GBs)")
        if len(x) > 1 and re.search('128|big[^A-Z]?', x, re.IGNORECASE):
            product_name_preference = search_for_product_name_contained('128GB', brand_preference)
            while True and not re.match(x, 'exit', re.IGNORECASE):
                x = input("Are you a fan of bigger or smaller screen sizes? (bigger/smaller)")
                if len(x) > 2 and re.search('big[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = search_for_product_name('iPhone 7 Plus 128GB', product_name_preference)
                    print_final_suggestion(final_suggestion)
                    break
                elif len(x) > 3 and re.search('small[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = search_for_product_name('iPhone 7 128GB', product_name_preference)
                    print_final_suggestion(final_suggestion)
                    break
                elif re.search('exit', x, re.IGNORECASE):
                    break
                else:
                    print("Please select a valid choice!")
            break
        elif len(x) > 1 and re.search('32|small[^A-Z]?', x, re.IGNORECASE):
            product_name_preference = search_for_product_name_contained('32GB', brand_preference)
            final_suggestion = search_for_product_name('iPhone 7 32GB', product_name_preference)
            print_final_suggestion(final_suggestion)
            break
        elif re.search('exit', x, re.IGNORECASE):
            break
        else:
            print("Please select a valid choice!")


'''
# Implements the main logic of the program by reading the user's input at each stage
'''


def program():
    while True:
        print_menu()
        x = input("Type in one of the above categories! \nAlternatively, you can type in specific items that you would "
                  "like to check!")
        if len(x) > 3 and re.search('\\bphone\\b|tablet[^A-Z]?', x, re.IGNORECASE):
            search_for_phones_and_tablets()
            break
        elif len(x) > 3 and re.search('gaming|gadget[^A-Z]?', x, re.IGNORECASE):
            search_for_gaming_and_gadgets()
            break
        elif len(x) > 2 and re.search('laptop|windows|comput|software[^A-Z]?', x, re.IGNORECASE):
            search_for_computing()
            break
        elif len(x) > 3 and re.search('wear|watch|smartwatch|smart-watch', x, re.IGNORECASE):
            search_for_wearables()
            break
        elif len(x) > 3 and re.search('intelligent|smart|home|house|robot|assist[^A-Z]?', x, re.IGNORECASE):
            search_for_smart_home()
            break
        elif len(x) > 3 and re.search('vacuum|cleaner[^A-Z]?', x, re.IGNORECASE):
            search_for_item_vacuum()
            break
        elif len(x) > 3 and re.search('drone[^A-Z]?', x, re.IGNORECASE):
            search_for_item_drone()
            break
        elif len(x) > 2 and re.search('mac[^A-Z]?', x, re.IGNORECASE):
            search_for_item_macbook()
            break
        elif len(x) > 2 and re.search('virtual|reality|glass[^A-Z]?', x, re.IGNORECASE):
            search_for_item_glasses()
            break
        elif re.search('\\biphone\\b', x, re.IGNORECASE):
            search_for_item_iphone(item_list)
            break
        elif re.match('exit', x, re.IGNORECASE):
            break
        else:
            print('Please select a valid choice!')


print("Welcome to the application! If at any point you would like to finish your session, "
      "please type exit and then hit enter! ")

program()
print('Thank you very much for using our platform!')
