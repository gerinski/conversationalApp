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
        x = input("Would you be interested in searching for another product?")
        if len(x) > 1 and re.search('yes|yeah[^A-Z]?', x, re.IGNORECASE):
            print("Thank you for trusting us! Take a look again at our categories:")
            program()
        elif len(x) > 1 and re.search('no[^A-Z]?', x, re.IGNORECASE):
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
        if len(x) > 3 and re.search( 'phone[^A-Z]?|tablet[^A-Z]?', x, re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategory('Phones & Tablets', item_list)
                x = input("Do you prefer Apple or Samsung products? (apple/samsung)")
                if len(x) > 2 and re.search('apple|ios', x, re.IGNORECASE):
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        brandPreference = searchForBrand('Apple', categoryPreference)
                        x = input("Do you prefer a smaller or a bigger hard drive? (32 GBs/128 GBs)")
                        if len(x) > 1 and re.search('128|big[^A-Z]?', x, re.IGNORECASE):
                            productNamePreference = searchForProductNameContained('128GB', brandPreference)
                            while True and not re.match(x, 'exit', re.IGNORECASE):
                                x = input("Are you a fan of bigger or smaller screen sizes? (bigger/smaller)")
                                if len(x) > 2 and re.search('big[^A-Z]?', x, re.IGNORECASE):
                                    final_suggestion = searchForProductName('iPhone 7 Plus 128GB',
                                                                            productNamePreference)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                elif len(x) > 3 and re.search('small[^A-Z]?', x, re.IGNORECASE):
                                    final_suggestion = searchForProductName('iPhone 7 128GB', productNamePreference)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                else:
                                    print("Please select a valid choice!")
                            break
                        elif len(x) > 1 and re.search('32|small[^A-Z]?', x, re.IGNORECASE):
                            productNamePreference = searchForProductNameContained('32GB', brandPreference)
                            final_suggestion = searchForProductName('iPhone 7 32GB', productNamePreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print("Please select a valid choice!")
                    break
                elif len(x) > 3 and re.search('samsung[^A-Z]?', x, re.IGNORECASE):
                    brandPreference = searchForBrand('Samsung', categoryPreference)
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        x = input("Are you a fan of bigger or smaller screen sizes?")
                        if len(x) > 2 and re.search('big[^A-Z]?', x, re.IGNORECASE):
                            final_suggestion = searchForProductName('Galaxy S8+ 64GB', brandPreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        elif len(x) > 3 and re.search('small[^A-Z]?', x, re.IGNORECASE):
                            final_suggestion = searchForProductName('Galaxy S8 64GB', brandPreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print("Please select a valid choice!")
                    break
                else:
                    print("Please select a valid choice!")
            break
        elif len(x) > 3 and re.search('gaming|gadget[^A-Z]?', x, re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategories('Drones', 'Gaming & VR', item_list)
                x = input("Are you more interested in: VRs or Drones?")
                while True and not re.match(x, 'exit', re.IGNORECASE):
                    if len(x) > 2 and re.search('drone[^A-Z]?', x, re.IGNORECASE):
                        categoryPreference = searchForCategory('Drones', item_list)
                        x = input(
                            'Do you care for a more powerful, more robust and increased autonomy model, or could you'
                            ' settle for less? (Yes/No)')
                        if re.match('power|robust|increas|autonomy[^A-Z]?', x, re.IGNORECASE):
                            final_suggestion = searchForProductName('Drone BEBOP 2', categoryPreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        elif re.match('settle|less|worse|not good[^A-Z]?', x, re.IGNORECASE):
                            final_suggestion = searchForProductName('Drone BEBOP', categoryPreference)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print("Please select a valid choice!")
                            break
                    elif len(x) > 1 and re.search('vr[^A-Z]?', x, re.IGNORECASE):
                        categoryPreference = searchForCategory('Gaming & VR', item_list)
                        printFinalSuggestion(categoryPreference)
                        break
                    else:
                        print("Please select a valid choice!")
                        break
                break
            break
        elif len(x) > 2 and re.search('laptop|macbook|mac|windows|comput|software[^A-Z]?', x, re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategory('Computing', item_list)
                x = input("Are you a fan of the Windows or the iOS operating system?")
                if len(x) > 2 and re.search('ios|apple[^A-Z]?', x, re.IGNORECASE):
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        brandPreference = searchForBrand('Apple', categoryPreference)
                        x = input('Are you interested: (1) In a larger display but with less memory (RAM),'
                                  ' or (2) in a smaller display with more memory (RAM)?')
                        if len(x) > 2 and re.search('big|large|less[^A-Z]?', x, re.IGNORECASE):
                            while True and not re.match(x, 'exit', re.IGNORECASE):
                                choices_left = searchForProductNameContained('4GB RAM', brandPreference)
                                x = input('Would you prefer a larger hard disk or a smaller one? (500GB/128GB)')
                                if len(x) > 2 and re.search('500|large[^A-Z]?', x, re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('500', choices_left)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                elif len(x) > 2 and re.search('128|small[^A-Z]?', x, re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('128', choices_left)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                else:
                                    print('Please select a valid choice!')
                            break
                        if len(x) > 4 and re.search('small|more[^A-Z]?', x, re.IGNORECASE):
                            while True and not re.match(x, 'exit', re.IGNORECASE):
                                choices_left = searchForProductNameContained('8GB RAM', brandPreference)
                                x = input('Would you care for a more powerful (i7) or a simpler (i5) processor?')
                                if len(x) > 1 and re.search('no|simple|i5[^A-Z]?', x, re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('MacBook 12" M-5Y31', choices_left)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                elif re.search('yes|yeah|strong|powerful|i7[^A-Z]?', x, re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('i7', choices_left)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                else:
                                    print('Please select a valid choice!')
                            break
                        else:
                            print('Please select a valid choice!')
                    break
                elif len(x) > 3 and re.search('not apple|window[^A-Z]?', x, re.IGNORECASE):
                    brandPreference = searchForLackOfBrand('Apple', categoryPreference)
                    printFinalSuggestion(brandPreference)
                    break
                else:
                    print('Please select a valid choice!')
            break
        elif len(x) > 3 and re.search('wear|watch|smartwatch|smart-watch',x, re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategory('Wearables', item_list)
                x = input('Are you planning to use this smart watch mostly for sports activities, or as casual '
                          'wear?')
                if len(x) > 3 and re.search('yes|yeah|sport[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = searchForBrands('Suunto', 'Polar', categoryPreference)
                    printFinalSuggestion(final_suggestion)
                    break
                elif len(x) > 3 and re.search('no|casual|wear[^A-Z]?', x, re.IGNORECASE):
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        choices_left = searchForBrands('Apple', 'Asus', categoryPreference)
                        x = input("Are you a fan of Apple products? (yes/no)")
                        if len(x) > 2 and re.search('yeah|apple|yes[^A-Z]?', x, re.IGNORECASE):
                            while True and not re.match(x, 'exit', re.IGNORECASE):
                                next_choice = searchForBrand('Apple', choices_left)
                                x = input('Would you prefer a bigger watch, or a smaller one? (bigger/smaller)')
                                if len(x) > 2 and re.search('yes|yeah|big[^A-Z]?', x, re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('Watch 42mm', next_choice)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                elif len(x) > 1 and re.search('no|nope|small[^A-Z]?', x, re.IGNORECASE):
                                    final_suggestion = searchForProductNameContained('Watch 38mm', next_choice)
                                    printFinalSuggestion(final_suggestion)
                                    break
                                else:
                                    print('Please select a valid choice!')
                            break
                        elif len(x) > 1 and re.search('not apple|nope[^A-Z]?', x, re.IGNORECASE):
                            final_suggestion = searchForBrand('Asus', choices_left)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print('Please select a valid choice!')
                    break
                else:
                    print('Please select a valid choice!')
            break
        elif len(x) > 3 and re.search('intelligent|smart|home|house|robot|assist[^A-Z]?', x, re.IGNORECASE):
            while True and not re.match(x, 'exit', re.IGNORECASE):
                categoryPreference = searchForCategory('Smart Home', item_list)
                x = input('Are you interested in products for: listening to some music, cooking some tasty '
                          'milk creations, or cleaning your house?')
                if len(x) > 4 and re.search('leisure|entertain|music|listen[^A-Z]?', x, re.IGNORECASE):
                    while True and not re.match(x, 'exit', re.IGNORECASE):
                        next_choice = searchForBrand('Amazon', categoryPreference)
                        x = input('Would you prefer a stronger speaker, or a more '
                                  'compact one?')
                        if len(x) > 2 and re.search('yes|yeah|strong[^A-Z]?', x, re.IGNORECASE):
                            final_suggestion = searchForProductName('Alexa Echo', next_choice)
                            printFinalSuggestion(final_suggestion)
                            break
                        elif len(x) > 1 and re.search('no|nope|less|compact[^A-Z]?', x, re.IGNORECASE):
                            final_suggestion = searchForProductName('Alexa Dot', next_choice)
                            printFinalSuggestion(final_suggestion)
                            break
                        else:
                            print('Please select a valid choice!')
                elif len(x) > 3 and re.search('cook|tasty|milk|creat[^A-Z]?', x, re.IGNORECASE):
                    final_suggestion = searchForBrand('Tchibo', categoryPreference)
                    printFinalSuggestion(final_suggestion)
                    break
                elif len(x) > 4 and re.search('house|clean[^A-Z]?', x, re.IGNORECASE):
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
      "please type exit and then hit enter! ")
program()
