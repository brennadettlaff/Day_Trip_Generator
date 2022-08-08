##List of locations
from tkinter import Y


destinations = ["Denver", "Aspen", "Colorado Springs", "Glenwood Springs", "Durango", "Morrison", "Estas Park", "Grand Junction"]

##List of transportation
transportation_modes_general = ["car", "bus", "shuttle"]                           ##Morrison, Estas Park
transportation_modes_all = ["plane", "train", "car", "bus", "shuttle"]     ##Denver, Grand Junction
transportation_modes_plane = ["plane", "car", "bus", "shuttle"]            ##Aspen, Colorado Springs, Durango
transportation_modes_train = ["train", "car", "bus", "shuttle"]            ##Glenwood Springs

#Lists of Entertainment 
denver_entertainment = ["go shopping at 16th St Mall", "visit Denver Zoo", "visit Union Station"]         
aspen_entertainment = ["ski Snowmass", "ride the Silver Queen Gondola", "visit Wheeler Opera House", "go snowshoeing", "go iceskating"]     
colosprings_entertainment = ["visit Pikes Peak", "visit Garden of the Gods", "visit Manitou Hot Springs", "tour Cave of the Winds", "go rock climbing"]     
glensprings_entertainment = ["visit Glenwood Hot Springs", "visit Yampah Spa & Vapor Springs", "explore downtown", "go fishing"]          
durango_entertainment = ["ride Narrow Gauge Railroad", "visit San Juan National Forest", "visit Mesa Verde National Park", "visit Pinkerton Hot Springs"]      
morrison_entertainment = ["attend a concert at Red Rocks Amphitheatre", "visit Dinosaur Ridge", " drive Lariat Loop National Scenic Byway", "explore downtown Morrison"] 
estaspark_entertainment = ["visit Rocky Mountain National Park", "visit the Stanley Hotel", "explore downtown Estes Park", "go mountian biking" ]         
grandjunct_entertainment = ["visit Grand Mesa", "explore downtown Grand Junction", "visit Colorado National Monument", "go white water rafting"]      

##List of Restaurants
denver_restaurants = ["The Buckhorn Exchange", "El Five", "Root Down", "Gaetano's", "Williams & Graham"]
aspen_restaurants = ["Woody Creek Tavern", "Mawa's Kitchen", "Matsuhisa", "Cache Cache", "Bear Den Aspen"]
colosprings_restaurants = ["Cowboy Star", "Four by Brother Luck","The Margarita" , "Ristorante Del Lago", "The Golden Bee"]
glensprings_restaurants = ["CO Ranch House", "Vicco's Charcoalburger Drive-In", "Slope & Hatch", "19th Street Diner", "Glenwood Canyon Brewpub"]
durango_restaurants = ["Derailed Pour House", "Rice Monkeys", "El Moro Tavern", "Diamond Belle Saloon", "Steamworks Brewing Company"]
morrison_restaurants = ["The Fort Resaurant", "Morrison Inn", "Red Rocks Grill", "Sit N Bull Saloon", "Twin Forks Tavern"]
estaspark_restaurants = ["Rock Inn Mountain Tavern", "Smokin' Dave's BBQ & Brew", "Bird & Jim", "Twin Owls Steakhouse", "Dunraven"]
grandjunct_restaurants = ["Bin 707 Foodbar", "il Bistro Italiano", "Kannah Creek Brewing Company", "Rockslide Restaurant", "Pufferbelly Station"]


def generate_item(list_to_use):
    import random
    return random.choice(list_to_use)

def select_item(list_to_use, type_of_item):
    generated_item = generate_item(list_to_use)                                
    print(f"We have selected {generated_item} for your {type_of_item}.")
    return generated_item 

def user_confirmation(list_to_use, type_of_item):
    selected_item = select_item(list_to_use, type_of_item)
    while True:
        user_input = input(f"Is this an acceptible {type_of_item}? (enter y/n): ")
        if user_input == "y" or user_input == "Y":
            print("Perfect, lets move on.")
            break
        elif user_input == "n" or user_input == "N":
            print(f"We will select a different {type_of_item} for you.")
            selected_item = select_item(list_to_use, type_of_item)                    
        else:
            print("Please answer y or yes or n for no.")

    return selected_item

def select_other(trans_list, ent_list, rest_list):              
    user_confirmation(trans_list, "transportation")
    user_confirmation(ent_list, "entertainment")
    user_confirmation(rest_list, "restaurant")

def match_lists(selected_destination):
    if selected_destination == "Denver":                 
        select_other(transportation_modes_all, denver_entertainment, denver_restaurants)
    elif selected_destination == "Aspen":
        select_other(transportation_modes_plane, aspen_entertainment, aspen_restaurants)
    elif selected_destination == "Colorado Springs":
        select_other(transportation_modes_plane, colosprings_entertainment, colosprings_restaurants)
    elif selected_destination == "Glenwood Springs":
        select_other(transportation_modes_train, glensprings_entertainment, glensprings_restaurants)
    elif selected_destination == "Durango":
        select_other(transportation_modes_plane, durango_entertainment, durango_restaurants)
    elif selected_destination == "Morrison":
        select_other(transportation_modes_general, morrison_entertainment, morrison_restaurants)
    elif selected_destination == "Estas Park":
        select_other(transportation_modes_general, estaspark_entertainment, estaspark_restaurants)
    elif selected_destination == "Estas Park":
        select_other(transportation_modes_general, estaspark_entertainment, estaspark_restaurants)

select_destination = user_confirmation(destinations, "destination")
match_lists(select_destination)

