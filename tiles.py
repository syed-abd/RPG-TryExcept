# create a 4x5 map with each block containing a setting
map = [
    ["start", "janitor closet", "lab", "washroom", "gym"],
    ["gym", "classroom", "janitor closet", "lab", "washroom"],
    ["washroom", "gym", "classroom", "janitor closet", "lab"],
    ["lab", "washroom", "gym", "classroom", "janitor closet"]
]

tile = {
    "start": {"Description": "Your in the entrance of the school."},
    "classroom": {"Description": "You have entered the classroom take a seat at your desk."},
    "janitor closet": {"Description": "You have entered the janitor closet time to mop the floor."},
    "lab": {"Description": "You have entered the lab the chemical reactions will blow up!"},
    "washroom": {"Description": "You have entered the washroom the toilets smell stinky."},
    "gym": {"Description": "You have entered the gym listen to the loud echos of the basketball."},
}