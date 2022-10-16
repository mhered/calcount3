import collections
from datetime import date, datetime
from pprint import pprint


# Source: https://www.wikihow.com/Calculate-Food-Calories
cal_per_gram = {
    "protein": 4,
    "carbs": 4,
    "fat": 9,
    # "alcohol": 7
}


TARGET_CALS_PER_DAY = 2100

target_cals_percent_from = {
    "protein": 15,
    "carbs": 55,
    "fat": 30,
}


# Food = collections.namedtuple('Food', 'name fat carbs protein')


class Food:

    def __init__(self, name, fat, carbs, protein):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def __repr__(self):
        _repr = "{}(name='{}', fat={}, carbs={}, protein={})"
        return _repr.format(
            self.__class__.__name__,
            self.name,
            self.fat,
            self.carbs,
            self.protein
        )

    def _calc_cals(self):
        return self.fat*cal_per_gram['fat'] + \
            self.carbs*cal_per_gram['carbs'] + \
            self.protein*cal_per_gram['protein']


# Source: https://www.webmd.com/diet/healthtool-food-calorie-counter
FOODS = {
    '1': Food(name="1 cup milk", fat=8, carbs=12, protein=8),
    '2': Food(name="1 apple", fat=0, carbs=25, protein=0),
    '3': Food(name="1 orange", fat=0, carbs=21, protein=1),
    '4': Food(name="1 tomato", fat=0, carbs=4, protein=1),
    '5': Food(name="1 carrot", fat=0, carbs=8, protein=1),
    '6': Food(name="1 egg", fat=5, carbs=0, protein=6),
    '7': Food(name="1 portion fries", fat=14, carbs=45, protein=3),
    '8': Food(name="1 burger", fat=20, carbs=8, protein=30),
    '9': Food(name="1 pizza", fat=21, carbs=53, protein=25),
    '10': Food(name="1 icecream", fat=17, carbs=24, protein=4),
}


def target_grams_per_day_of(nutrient, cal_per_day):
    return cal_per_day*target_cals_percent_from[nutrient]/100/cal_per_gram[nutrient]


print(f"For a target intake of {TARGET_CALS_PER_DAY} calories per day:")
for nutrient in ["fat", "carbs", "protein"]:
    grams = target_grams_per_day_of(nutrient, TARGET_CALS_PER_DAY)
    print(f"- {round(grams)}g of {nutrient}")

for food in FOODS.values():
    print(f"{food.name} has {food._calc_cals()} calories.")


def add_food(date, food_item):
    """add a food_item to history on a given date
        if food_item is None returns False"""
    if food_item:
        history.setdefault(date.strftime("%d/%m/%Y"), []).append(food_item)
        return True
    return False


def _pick_food_item(food_list=FOODS):
    """TUI to pick food items from a list
            Returns a Food object or None"""

    pprint(food_list)
    while True:
        key = input("Select a food item (c to Cancel): ")
        if key == "c":
            print("Cancelled")
            return None
        try:
            return food_list[str(key)]
        except KeyError:
            print(f"{key} is not a valid selection")
            continue


"""
history = {}
while add_food(date.today(), _pick_food_item()):
    pass
pprint(history)
"""

HISTORY = {
    '11/10/2022': [
        Food(name='1 milk cup', fat=8, carbs=12, protein=8),
        Food(name='1 burger', fat=20, carbs=8, protein=30),
        Food(name='1 tomato', fat=0, carbs=4, protein=1),
        Food(name='1 tomato', fat=0, carbs=4, protein=1),
        Food(name="1 orange", fat=0, carbs=21, protein=1),
        Food(name="1 portion fries", fat=14, carbs=45, protein=3),
        Food(name="1 carrot", fat=0, carbs=8, protein=1),
        Food(name="1 pizza", fat=21, carbs=53, protein=25),
        Food(name="1 icecream", fat=17, carbs=24, protein=4),
    ],
    '12/10/2022': [
        Food(name='1 milk cup', fat=8, carbs=12, protein=8),
        Food(name='1 apple', fat=0, carbs=25, protein=0),
        Food(name='1 tomato', fat=0, carbs=4, protein=1),
        Food(name='1 egg', fat=5, carbs=0, protein=6),
        Food(name="1 portion fries", fat=14, carbs=45, protein=3),
        Food(name="1 carrot", fat=0, carbs=8, protein=1),
        Food(name="1 pizza", fat=21, carbs=53, protein=25),
        Food(name="1 pizza", fat=21, carbs=53, protein=25),
    ],
    '13/10/2022': [
        Food(name='1 milk cup', fat=8, carbs=12, protein=8),
        Food(name='1 apple', fat=0, carbs=25, protein=0),
        Food(name='1 apple', fat=0, carbs=25, protein=0),
        Food(name='1 burger', fat=20, carbs=8, protein=30),
        Food(name="1 portion fries", fat=14, carbs=45, protein=3),
        Food(name="1 portion fries", fat=14, carbs=45, protein=3),
        Food(name="1 pizza", fat=21, carbs=53, protein=25),
    ],
    '14/10/2022': [
        Food(name='1 apple', fat=0, carbs=25, protein=0),
        Food(name="1 orange", fat=0, carbs=21, protein=1),
        Food(name="1 orange", fat=0, carbs=21, protein=1),
        Food(name='1 tomato', fat=0, carbs=4, protein=1),
        Food(name='1 egg', fat=5, carbs=0, protein=6),
        Food(name='1 egg', fat=5, carbs=0, protein=6),
        Food(name="1 pizza", fat=21, carbs=53, protein=25),
        Food(name="1 icecream", fat=17, carbs=24, protein=4),
        Food(name="1 icecream", fat=17, carbs=24, protein=4),
        Food(name='1 burger', fat=20, carbs=8, protein=30),
    ],
    '15/10/2022': [
        Food(name='1 milk cup', fat=8, carbs=12, protein=8),
        Food(name='1 apple', fat=0, carbs=25, protein=0),
        Food(name='1 burger', fat=20, carbs=8, protein=30),
        Food(name='1 burger', fat=20, carbs=8, protein=30),
        Food(name='1 tomato', fat=0, carbs=4, protein=1),
        Food(name='1 tomato', fat=0, carbs=4, protein=1),
        Food(name='1 tomato', fat=0, carbs=4, protein=1),
        Food(name='1 egg', fat=5, carbs=0, protein=6),
        Food(name="1 portion fries", fat=14, carbs=45, protein=3),
        Food(name="1 carrot", fat=0, carbs=8, protein=1),
        Food(name="1 carrot", fat=0, carbs=8, protein=1),
        Food(name="1 carrot", fat=0, carbs=8, protein=1),
        Food(name="1 icecream", fat=17, carbs=24, protein=4),
    ]
}


def printout_intake(history):
    """
    printout of the history of intake
    """
    for day, food_list in history.items():
        date = datetime.strptime(day, "%d/%m/%Y")
        total_fat = sum(food.fat for food in food_list)
        total_carbs = sum(food.carbs for food in food_list)
        total_protein = sum(food.protein for food in food_list)
        total_calories = sum(food._calc_cals() for food in food_list)
        print(f"{date.strftime('%d/%m/%y')}: {total_fat=}g {total_carbs=}g {total_protein=}g {total_calories=}cals")


printout_intake(HISTORY)

lst = []
for key, value in FOODS.items():
    lst.append({"id": int(key),
                "name": value.name,
                "fat": value.fat,
                "carbs": value.carbs,
                "protein": value.protein,
                "calories": value._calc_cals()
                })

pprint(lst)
