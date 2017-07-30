import csv
import re
with open('input.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
#   for row in reader:
#        print(row)
#        print(row['product_id'],'-' + row['product_name'],'-' + row['brand'],'-' + row['category'],'-' +
#        row['subscription_plan'])
    item_list= list(reader)


def searchForCategory(category, item_list):
    return [element for element in item_list if element['category'] == category]


def searchForProductId(product_id, item_list):
    return [element for element in item_list if element['product_id'] == product_id]


def searchForProductName(product_name, item_list):
    return [element for element in item_list if element['product_name'] == product_name]


def searchForProductNameContained(product_name, item_list):
    return [element for element in item_list if product_name in element['product_name']]


def searchForBrand(brand, item_list):
    return [element for element in item_list if element['brand'] == brand]


def searchForBrands(brand1,brand2, item_list):
    return [element for element in item_list if element['brand'] == brand1 or element['brand'] == brand2]


def searchForLackOfBrand(brand, item_list):
    return [element for element in item_list if element['brand'] != brand]


def searchForSubscriptionPlan(subscription_plan, item_list):
    return [element for element in item_list if element['subscription_plan'] == subscription_plan]


def printFinalSuggestion(final_suggestion):
    print("Estimation Complete! We are suggesting the following item(s):")
    for d in final_suggestion:
        name = d['product_name']
        price = d['subscription_plan']
        print(name + ', with a subscription plan of: ' + price + '€')

print("Welcome to the application! If at any point you would like to finish your session,"
      "plese press exit and then enter!")
while True:
    x = input("In what type of item are you interested in?")
    if re.match(x, 'phones & tablets', re.IGNORECASE):
        while True and not re.match(x, 'exit', re.IGNORECASE):
            categoryPreference = searchForCategory('Phones & Tablets', item_list)
            print(categoryPreference)
            x = input("Do you prefer Apple or Samsung products?")
            if re.match(x, 'apple', re.IGNORECASE):
                while True and not re.match(x, 'exit', re.IGNORECASE):
                    brandPreference = searchForBrand('Apple', categoryPreference)
                    x = input("Do you prefer 32GBs or 128GBs of internal memory? (32/128)")
                    productNamePreference = searchForProductNameContained(x, brandPreference)
                    if x == '128':
                        while True and not re.match(x, 'exit', re.IGNORECASE):
                            x = input("Are you a fan of Bigger or Smaller screen sizes? (Bigger/Smaller)")
                            if re.match(x, 'bigger', re.IGNORECASE):
                                final_suggestion = searchForProductName('iPhone 7 Plus 128GB', productNamePreference)
                                printFinalSuggestion(final_suggestion)
                                break
                            elif re.match(x, 'smaller', re.IGNORECASE):
                                final_suggestion = searchForProductName('iPhone 7 128GB', productNamePreference)
                                printFinalSuggestion(final_suggestion)
                                break
                            else:
                                print("Please select a valid choice!")
                        break
                    elif x == '32':
                        final_suggestion = searchForProductName('iPhone 7 32GB', productNamePreference)
                        printFinalSuggestion(final_suggestion)
                        break
                    else:
                        print("Please select a valid choice!")
                break
            elif re.match(x, 'samsung', re.IGNORECASE):
                brandPreference = searchForBrand('Samsung', categoryPreference)
                while True and not re.match(x, 'exit', re.IGNORECASE):
                    x = input("Are you a fan of bigger or smaller screen sizes? (Bigger/Smaller)")
                    if re.match(x, 'bigger', re.IGNORECASE):
                        final_suggestion = searchForProductName('Galaxy S8+ 64GB', brandPreference)
                        printFinalSuggestion(final_suggestion)
                        break
                    elif re.match(x, 'smaller', re.IGNORECASE):
                        final_suggestion = searchForProductName('Galaxy S8 64GB', brandPreference)
                        printFinalSuggestion(final_suggestion)
                        break
                    else:
                        print("Please select a valid choice!")
                break
            else:
                print("Please select a valid choice!")
        break
    elif re.match(x, 'drones', re.IGNORECASE):
        while True and not re.match(x, 'exit', re.IGNORECASE):
            categoryPreference = searchForCategory('Drones', item_list)
            x = input("Do you care for a more powerful, more robust and increaded autonomy model, or could you settle "
                      "for less? (Yes/No)")
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
    elif re.match(x, 'gaming & vr', re.IGNORECASE):
        categoryPreference = searchForCategory('Gaming & VR', item_list)
        printFinalSuggestion(categoryPreference)
        break
    elif re.match(x, 'computing', re.IGNORECASE):
        while True and not re.match(x, 'exit', re.IGNORECASE):
            categoryPreference = searchForCategory('Computing', item_list)
            print(categoryPreference)
            x = input("Are you a fan of the Windows or the iOS operating system ?")
            if re.match(x, 'ios', re.IGNORECASE):
                while True and not re.match(x, 'exit', re.IGNORECASE):
                    brandPreference = searchForBrand('Apple', categoryPreference)
                    x = input('Are you interested: (1) In a larger display but with less memory (RAM),'
                              ' or (2) in a smaller display with more memory (RAM)? (larger/smaller)')
                    if re.match(x, 'larger', re.IGNORECASE):
                        while True and not re.match(x, 'exit', re.IGNORECASE):
                            choices_left = searchForProductNameContained('4GB RAM', brandPreference)
                            x = input('Would you prefer a hard disk of 500GB or 128GB? (500/128)')
                            if x == '500':
                                final_suggestion = searchForProductNameContained('500', choices_left)
                                printFinalSuggestion(final_suggestion)
                                break
                            elif x == '128':
                                final_suggestion = searchForProductNameContained('128', choices_left)
                                printFinalSuggestion(final_suggestion)
                                break
                            else:
                                print('Please select a valid choice!')
                        break
                    if re.match(x, 'smaller', re.IGNORECASE):
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
            elif re.match(x, 'windows', re.IGNORECASE):
                print(categoryPreference)
                brandPreference = searchForLackOfBrand('Apple', categoryPreference)
                printFinalSuggestion(brandPreference)
                break
            else:
                print('Please select a valid choice!')
        break
    elif re.match(x, 'wearables', re.IGNORECASE):
        while True and not re.match(x, 'exit', re.IGNORECASE):
            categoryPreference = searchForCategory('Wearables', item_list)
            x = input('Are you planning to use this smart watch mostly: (1) for sports activities, or (2) as casual '
                      'wear ?')
            if x == '1':
                final_suggestion = searchForBrands('Suunto', 'Polar', categoryPreference)
                printFinalSuggestion(final_suggestion)
                break
            elif x == '2':
                while True and not re.match(x, 'exit', re.IGNORECASE):
                    choices_left = searchForBrands('Apple', 'Asus', categoryPreference)
                    x = input("Are you: (1) a fan of Apple products, or (2) not a fan? (1/2)")
                    if x == '1':
                        while True and not re.match(x, 'exit', re.IGNORECASE):
                            next_choice = searchForBrand('Apple', choices_left)
                            x = input('Would you prefer a bigger watch, or a smaller one? (bigger/smaller)')
                            if re.match(x, 'bigger', re.IGNORECASE):
                                final_suggestion = searchForProductNameContained('Watch 42mm', next_choice)
                                printFinalSuggestion(final_suggestion)
                                break
                            elif re.match(x, 'smaller', re.IGNORECASE):
                                final_suggestion = searchForProductNameContained('Watch 38mm', next_choice)
                                printFinalSuggestion(final_suggestion)
                                break
                    elif x == '2':
                        final_suggestion = searchForBrand('Asus', choices_left)
                        printFinalSuggestion(final_suggestion)
                        break
                break
        break
    elif re.match(x, 'smart home', re.IGNORECASE):
        while True and not re.match(x, 'exit', re.IGNORECASE):
            categoryPreference = searchForCategory(x, item_list)
            x = input('Are you planning to: (1) listen to some music, (2) make some tasty smoothies, or (3) clean your '
                      'house?')
            if x == '1':
                while True and not re.match(x, 'exit', re.IGNORECASE):
                    next_choice = searchForBrand('Amazon', categoryPreference)
                    x = input('Would you prefer a: (1) stronger but bigger speaker, or (2) a less strong but more '
                              'compact one? (1/2)')
                    if x == '1':
                        final_suggestion = searchForProductName('Alexa Echo', next_choice)
                        printFinalSuggestion(final_suggestion)
                        break
                    elif x == '2':
                        final_suggestion = searchForProductName('Alexa Dot', next_choice)
                        printFinalSuggestion(final_suggestion)
                        break
            elif x == '2':
                final_suggestion = searchForBrand('Tchibo', categoryPreference)
                printFinalSuggestion(final_suggestion)
                break
            elif x == '3':
                final_suggestion = searchForBrand('Samsung', categoryPreference)
                printFinalSuggestion(final_suggestion)
                break
    if re.match(x, 'exit', re.IGNORECASE):
        print('Thank you very much for using our platform!')
        break
    else:
        print('Please select a valid choice!')
