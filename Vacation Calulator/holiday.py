#function for city options 
def city_flight(): 
    print("Please enter the number corresponding to the city you'd wish to fly to, enter 4 to exit: ")
    print("1. Johannesburg")
    print("2. Accra")
    print("3. London")
    print("4. Lisbon")
    print("5. Exit")
# function with dictionary containing all cities information
cities = [
    {'name': 'Johannesburg', 'hotel': 2000, 'plane': 2000, 'car_rental': 300},
    {'name': 'Accra', 'hotel': 4000, 'plane': 11000, 'car_rental': 1000},
    {'name': 'London', 'hotel': 6000, 'plane': 10000, 'car_rental': 300},
    {'name': 'Lisbon', 'hotel': 4000, 'plane': 15000, 'car_rental': 200}
]

# Func for hotel costs
def hotel_cost(city, num_nights):
    return city['hotel'] * num_nights
# Func for plane costs
def plane_cost(city):
    return city['plane']
# Func for car rentals costs
def car_rental(city, rental_days):
    return city['car_rental'] * rental_days
# Func for total holiday costs
def holiday_cost(hotel_cost, plane_cost, car_rental_cost):
    return hotel_cost + plane_cost + car_rental_cost

print("This program will calculate your total holiday costs to your chosen city: ")
city_flight_choice = "0"
while city_flight_choice != "5":
    city_flight()
    city_flight_choice = input("Please enter your choice: ")

    selected_city = 0 # reseting the loop 
    
# check if input is a digits and if it's one of the city options
    if city_flight_choice.isdigit() and 1 <= int(city_flight_choice) <= len(cities): 
# if both conditions are true, program pulls corresponding info from function cities. 
# '-1' adjustment because list indices start from 0, while city numbering starts from 1
        selected_city = cities[int(city_flight_choice) - 1]
# Asks no. of nights + car rental days, calculates plane costs, hotel cost, car rent and total holiday costs
        num_nights = int(input("How many nights will you stay at the hotel?: "))
        selected_hotel_cost = hotel_cost(selected_city, num_nights)

        selected_plane_cost = plane_cost(selected_city)

        rental_days = int(input("How many days will you rent the car?: "))
        
        selected_car_rental_cost = car_rental(selected_city, rental_days)

        total_cost = holiday_cost(selected_hotel_cost, selected_plane_cost, selected_car_rental_cost)
#Prints all calculations
        print(f"Hotel costs for {num_nights} night(s) is R{selected_hotel_cost}")
        print(f"A return plane ticket will cost R{selected_plane_cost}")
        print(f"Car rental will cost R{selected_car_rental_cost}")
        print(f"Total holiday costs R{total_cost}")
    elif city_flight_choice == "5":
        print("Goodbye!")
        break
    else:
        print("\nInvalid input, please enter an integer between 1 and 5")