from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

FOODS = [
        {
            'id': 1,
            'calories': 152,
            'carbs': 12,
            'fat': 8,
            'name': '1 cup milk',
            'protein': 8
        },
        {
            'id': 2,
            'calories': 100,
            'carbs': 25,
            'fat': 0,
            'name': '1 apple',
            'protein': 0
        },
        {
            'id': 3,
            'calories': 88,
            'carbs': 21,
            'fat': 0,
            'name': '1 orange',
            'protein': 1
        },
        {
            'id': 4,
            'calories': 20,
            'carbs': 4,
            'fat': 0,
            'name': '1 tomato',
            'protein': 1
        },
        {
            'id': 5,
            'calories': 36,
            'carbs': 8,
            'fat': 0,
            'name': '1 carrot',
            'protein': 1
        },
        {
            'id': 6,
            'calories': 69,
            'carbs': 0,
            'fat': 5,
            'name': '1 egg',
            'protein': 6
        },
        {
            'id': 7,
            'calories': 318,
            'carbs': 45,
            'fat': 14,
            'name': '1 portion fries',
            'protein': 3
        },
        {
            'id': 8,
            'calories': 332,
            'carbs': 8,
            'fat': 20,
            'name': '1 burger',
            'protein': 30
        },
        {
            'id': 9,
            'calories': 501,
            'carbs': 53,
            'fat': 21,
            'name': '1 pizza',
            'protein': 25
        },
        {
            'id': 10,
            'calories': 265,
            'carbs': 24,
            'fat': 17,
            'name': '1 icecream',
            'protein': 4
        },
    ]

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    # describe column headers and the data type
    at.Table1.custom.cols = [
        # {"field": "id", "headerName": "ID"},
        {"field": "name", "headerName": "Food"},
        {"field": "fat", "headerName": "Fat (g)", "type": "number"},
        {"field": "carbs", "headerName": "Carbohidrates (g)", "type": "number"},
        {"field": "protein", "headerName": "Protein (g)", "type": "number"},
        {"field": "calories", "headerName": "Calories (cal)", "type": "number"},
    ]
    

    # add dropdown
    at.Dropdown1.custom.values = [item['name'] for item in FOODS]


def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass


def handle_event(at: Atri, req: Request, res: Response):
    """
    This function is called whenever an event is received. An event occurs when user
    performs some action such as click button.
    """
    
    if at.Button1.onClick:
        at.Button1.custom.text == "Added"
        # get food selected in Dropdown1
        food_item = next(
            (item for item in FOODS if item['name'] == at.Dropdown1.custom.selectedValue),
             None)

        # add row
        at.Table1.custom.rows.append(food_item)
