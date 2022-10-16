import create from "zustand";

// unsafe merge state
// and mew properties will added or existing properties will be changed
// but the type of value of the property must not change
function mergeState(baseState, newState) {
  if (
    typeof newState === "object" &&
    !Array.isArray(newState) &&
    newState !== null
  ) {
    const keys = Object.keys(newState);
    keys.forEach((key) => {
      // create a new key in base if not exists
      if (!(key in baseState)) {
        baseState[key] = {};
      }
      if (typeof newState[key] === "object" && !Array.isArray(newState[key]))
        mergeState(baseState[key], newState[key]);
      else baseState[key] = newState[key];
    });
  }
}

const useStore = create((set) => {
  return {
    setPage: (pageName, newState) =>
      set((state) => {
        const pageState = JSON.parse(JSON.stringify(state[pageName]));
        mergeState(pageState, newState);
        return { [pageName]: pageState };
      }),
  };
});

export function updateStoreStateFromController(pageName, newState) {
  useStore.getState().setPage(pageName, newState);
}

const desktopModeProps = {
  ...{
  "Home": {
    "Div1": {
      "callbacks": {}
    },
    "Div2": {
      "callbacks": {}
    },
    "Table1": {
      "custom": {
        "rows": [],
        "cols": [
          {
            "field": "name",
            "headerName": "Food"
          },
          {
            "field": "fat",
            "headerName": "Fat (g)",
            "type": "number"
          },
          {
            "field": "carbs",
            "headerName": "Carbohidrates (g)",
            "type": "number"
          },
          {
            "field": "protein",
            "headerName": "Protein (g)",
            "type": "number"
          },
          {
            "field": "calories",
            "headerName": "Calories (cal)",
            "type": "number"
          }
        ],
        "checkboxSelection": false
      },
      "callbacks": {}
    },
    "Dropdown1": {
      "custom": {
        "values": [
          "1 cup milk",
          "1 apple",
          "1 orange",
          "1 tomato",
          "1 carrot",
          "1 egg",
          "1 portion fries",
          "1 burger",
          "1 pizza",
          "1 icecream"
        ]
      },
      "callbacks": {}
    },
    "Button1": {
      "custom": {
        "text": "Add"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    },
    "TextBox1": {
      "custom": {
        "text": "What did you eat today?"
      },
      "callbacks": {
        "onClick": [
          {
            "sendEventData": true
          }
        ]
      }
    }
  }
}};

useStore.setState(desktopModeProps);

export default useStore;
