import urllib.request, json


######################################### Currency Converter ######################################################
try:
    with urllib.request.urlopen("https://free.currencyconverterapi.com/api/v5/convert?q=USD_ILS&compact=n&apiKey=372ec2039e2062c636c3") as url:
        data = json.loads(url.read().decode())
except OSError as e:
    print("could not open url:",e)
except Exception as e:
    print("something has gone wrong:",e)

usd_to_ils = float(data['results']['USD_ILS']['val'])

print("Welcome to currency converter")


def converter():
    user_input = input("Please enter an amount of shekels to convert: ")
    try:
        user_input = float(user_input)
    except ValueError:
        print("please insert a number using digits only, please try again")
        converter()
    except Exception:
        print("there was an error please try again")
        converter()
    print("the value in usd is:",user_input/usd_to_ils)


converter()
print("Thanks for using our currency converter")

#############################################################################################################

##################################### GOOGLE API ############################################################

with urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Jerusalem&key=AIzaSyD2she6rJGiE9vDeJnEkl6hbwq6KheCXgE") as url:
    data = json.loads(url.read().decode())

results = data['results']
print("latitude of first result:", results[1]['geometry']['location']['lat'])
print("longtitude of first result:", results[1]['geometry']['location']['lng'])


############################################################################################################