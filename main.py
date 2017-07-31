import csv
import re

'''
#Opening the csv file and reading the contents into item_list, as a dictionary of dictionaries.
'''
with open('input.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    item_list = list(reader)

'''
# Function for searching for the category of a specific item.
'''
def searchForCategory(category, item_list):
    return [element for element in item_list if element['category'] == category]

'''
# Function for searching for the category of an item if it matches two specific categories.
'''
def searchForCategories(category1, category2, item_list):
    return [element for element in item_list if element['category'] == category1 or element['category'] == category2]

'''
# Function for searching for the product_id of a specific item.
'''
def searchForProductId(product_id, item_list):
    return [element for element in item_list if element['product_id'] == product_id]

'''
# Function for searching for the product_name of a specific item.
'''
def searchForProductName(product_name, item_list):
    return [element for element in item_list if element['product_name'] == product_name]

'''
# Function for searching for the category of a specific item, if it is contained in a string.
'''
def searchForProductNameContained(product_name, item_list):
    return [element for element in item_list if product_name in element['product_name']]

'''
# Function for searching for the brand of a specific item.
'''
def searchForBrand(brand, item_list):
    return [element for element in item_list if element['brand'] == brand]

'''
# Function for searching for the brand of a specific item, if it matches two specific brand names.
'''
def searchForBrands(brand1, brand2, item_list):
    return [element for element in item_list if element['brand'] == brand1 or element['brand'] == brand2]

'''
# Function for searching for the lack of a brand of a specific item.
'''
def searchForLackOfBrand(brand, item_list):
    return [element for element in item_list if element['brand'] != brand]

'''
# Function for searching for the subscription_plan of a specific item.
'''
def searchForSubscriptionPlan(subscription_plan, item_list):
    return [element for element in item_list if element['subscription_plan'] == subscription_plan]

'''
# Function for printing the final suggestion(item) to the user.
# In the end, it asks whether the user wants to inquire for another item or not.
# If not, it exits the program. If yes, it repeats the main function main() of the program
'''
def printFinalSuggestion(final_suggestion):
    print("Estimation Complete! We are suggesting the following item(s):")
    for d in final_suggestion:
        name = d['product_name']
        price = d['subscription_plan']
        print(name + ', with a subscription plan of: ' + price + '€')
    while True:
        x = input("Would you be interested in searching for another product? (Yes/No)")
        if re.match(x, 'yes', re.IGNORECASE):
            program()
        elif re.match(x, 'no', re.IGNORECASE):
            print('Thank you for using our app! Hope to see you again in the future!')
            break
        else:
            print('Please select a valid choice!')
        break

'''
# Function for printing the main menu of the program
'''
def printMenu():
    print("Please select what type of product you would like to purchase:")
    print('*** Phones & Tablets ***')
    print('*** Gaming & Gadgets ***')
    print('*** Computing ***')
    print('*** Wearables ***')
    print('*** Smart Home ***')


'''
# Implements the main logic of the program by reading the user's input at each stage
'''
def program():
    while True:
        printMenu()
        x = input("Type in one of the above categories!")
        if len(x) > 3 and re.search(x, 'phones & tablets', re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategory('Phones & Tablets', item_list)
                x = input("Do you prefer Apple or Samsung products? (apple/samsung)")
                if len(x) > 3 and re.match(x, 'apple', re.IGNORECASE):
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        brandPreference = searchForBrand('Apple', categoryPreference)
                        x = input("Do you prefer 32GBs or 128GBs of internal memory? (32/128)")
                        productNamePreference = searchForProductNameContained(x, brandPreference)
                        if len(x) > 1 and re.search(x, '128gbs', re.IGNORECASE):
                            while True and not re.match(x, 'exit', re.IGNORECASE):
                                x = input("Are you a fan of bigger or smaller screen sizes? (bigger/smaller)")
                                if len(x) > 2 and re.search(x, 'bigger', re.IGNORECASE):
                                    final_suggestion = searchForProductName('iPhone 7 Plus 128GB',
                                                                            productNamePreference)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                elif len(x) > 3 and re.search(x, 'smaller', re.IGNORECASE):
                                    final_suggestion = searchForProductName('iPhone 7 128GB', productNamePreference)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                else:
                                    print("Please select a valid choice!")
                            break
                        elif len(x) > 1 and re.search(x, '32gbs', re.IGNORECASE):
                            final_suggestion = searchForProductName('iPhone 7 32GB', productNamePreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print("Please select a valid choice!")
                    break
                elif len(x) > 3 and re.search(x, 'samsung', re.IGNORECASE):
                    brandPreference = searchForBrand('Samsung', categoryPreference)
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        x = input("Are you a fan of bigger or smaller screen sizes?")
                        if len(x) > 2 and re.search(x, 'bigger', re.IGNORECASE):
                            final_suggestion = searchForProductName('Galaxy S8+ 64GB', brandPreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        elif len(x) > 3 and re.search(x, 'smaller', re.IGNORECASE):
                            final_suggestion = searchForProductName('Galaxy S8 64GB', brandPreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print("Please select a valid choice!")
                    break
                else:
                    print("Please select a valid choice!")
            break
        elif len(x) > 3 and re.search(x, 'Gaming & Gadgets', re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategories('Drones', 'Gaming & VR', item_list)
                x = input("Are you interested in: VRs or Drones?")
                while True and not re.match(x, 'exit', re.IGNORECASE):
                    if len(x) > 2 and re.search(x, 'drones', re.IGNORECASE):
                        categoryPreference = searchForCategory('Drones', item_list)
                        x = input(
                            "Do you care for a more powerful, more robust and increased autonomy model, or could you"
                            " settle for less? (Yes/No)")
                        if re.match(x, 'yes', re.IGNORECASE):
                            final_suggestion = searchForProductName('Drone BEBOP 2', categoryPreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        elif re.match(x, 'no', re.IGNORECASE):
                            final_suggestion = searchForProductName('Drone BEBOP', categoryPreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print("Please select a valid choice!")
                            break
                    elif len(x) > 1 and re.search(x, 'vrs', re.IGNORECASE):
                        categoryPreference = searchForCategory('Gaming & VR', item_list)
                        printFinalSuggestion(categoryPreference)
                        break
                    else:
                        print("Please select a valid choice!")
                        break
                break
            break
        elif len(x) > 3 and re.search(x, 'computing', re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategory('Computing', item_list)
                x = input("Are you a fan of the Windows or the iOS operating system?")
                if re.match(x, 'ios', re.IGNORECASE):
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        brandPreference = searchForBrand('Apple', categoryPreference)
                        x = input('Are you interested: (1) In a larger display but with less memory (RAM),'
                                  ' or (2) in a smaller display with more memory (RAM)?')
                        if len(x) > 4 and re.search(x, 'larger display', re.IGNORECASE):
                            while True and not re.match(x, 'exit', re.IGNORECASE):
                                choices_left = searchForProductNameContained('4GB RAM', brandPreference)
                                x = input('Would you prefer a hard disk of 500GBs or 128GBs?')
                                if len(x) > 2 and re.search(x, '500gbs', re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('500', choices_left)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                elif len(x) > 2 and re.search(x, '128gbs', re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('128', choices_left)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                else:
                                    print('Please select a valid choice!')
                            break
                        if len(x) > 4 and re.search(x, 'smaller display', re.IGNORECASE):
                            while True and not re.match(x, 'exit', re.IGNORECASE):
                                choices_left = searchForProductNameContained('8GB RAM', brandPreference)
                                x = input('Would you care for an i7 or an i5 processor? (i5/i7)')
                                if re.match(x, 'i5', re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('MacBook 12" M-5Y31', choices_left)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                elif re.match(x, 'i7', re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('i7', choices_left)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                else:
                                    print('Please select a valid choice!')
                            break
                        else:
                            print('Please select a valid choice!')
                    break
                elif len(x) > 3 and re.search(x, 'windows', re.IGNORECASE):
                    print(categoryPreference)
                    brandPreference = searchForLackOfBrand('Apple', categoryPreference)
                    printFinalSuggestion(brandPreference)
                    break
                else:
                    print('Please select a valid choice!')
            break
        elif len(x) > 3 and re.search(x, 'wearables', re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategory('Wearables', item_list)
                x = input('Are you planning to use this smart watch mostly for sports activities, or as casual '
                          'wear ?')
                if len(x) > 3 and re.search(x, 'sports activities', re.IGNORECASE):
                    final_suggestion = searchForBrands('Suunto', 'Polar', categoryPreference)
                    printFinalSuggestion(final_suggestion)
                    break
                elif len(x) > 3 and re.search(x, 'casual wear', re.IGNORECASE):
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        choices_left = searchForBrands('Apple', 'Asus', categoryPreference)
                        x = input("Are you a fan of Apple products? (yes/no)")
                        if re.match(x, 'yes', re.IGNORECASE):
                            while True and not re.match(x, 'exit', re.IGNORECASE):
                                next_choice = searchForBrand('Apple', choices_left)
                                x = input('Would you prefer a bigger watch, or a smaller one? (bigger/smaller)')
                                if len(x) > 2 and re.search(x, 'bigger watch', re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('Watch 42mm', next_choice)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                elif len(x) > 2 and re.search(x, 'smaller watch', re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('Watch 38mm', next_choice)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                else:
                                    print('Please select a valid choice!')
                            break
                        elif re.match(x, 'no', re.IGNORECASE):
                            final_suggestion = searchForBrand('Asus', choices_left)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print('Please select a valid choice!')
                    break
                else:
                    print('Please select a valid choice!')
            break
        elif len(x) > 3 and re.search(x, 'smart home', re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategory('Smart Home', item_list)
                x = input('Are you interested in products for: (1) listening to some music, (2) making some tasty '
                          'milk creations, or (3) cleaning your house?')
                if len(x) > 4 and re.search(x, 'listening to music', re.IGNORECASE):
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        next_choice = searchForBrand('Amazon', categoryPreference)
                        x = input('Would you prefer a: (1) stronger speaker, or (2) a more '
                                  'compact one? (1/2)')
                        if len(x) > 4 and re.search(x, 'stronger', re.IGNORECASE):
                            final_suggestion = searchForProductName('Alexa Echo', next_choice)
                            printFinalSuggestion(final_suggestion)
                            break
                        elif len(x) > 4 and re.search(x, 'a more compact', re.IGNORECASE):
                            final_suggestion = searchForProductName('Alexa Dot', next_choice)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print('Please select a valid choice!')
                elif len(x) > 3 and re.search(x, 'making tasty '
                                                 'milk creations', re.IGNORECASE):
                    final_suggestion = searchForBrand('Tchibo', categoryPreference)
                    printFinalSuggestion(final_suggestion)
                    break
                elif len(x) > 4 and re.search(x, 'cleaning house', re.IGNORECASE):
                    final_suggestion = searchForBrand('Samsung', categoryPreference)
                    printFinalSuggestion(final_suggestion)
                    break
                else:
                    print('Please select a valid choice!')
            break
        if re.match(x, 'exit', re.IGNORECASE):
            print('Thank you very much for using our platform!')
            break
        else:
            print('Please select a valid choice!')


print("Welcome to the application! If at any point you would like to finish your session, "
      "please type exit and then hit enter!")
program()
