import pandas as pd

# Create the dataset
data = {
    "Loves Popcorn": ["Yes", "Yes", "No", "No", "Yes", "Yes", "No"],
    "Loves Soda": ["Yes", "No", "Yes", "Yes", "Yes", "No", "No"],
    "Age": [7, 12, 18, 35, 38, 50, 83],
    "Loves Cool As Ice": ["No", "No", "Yes", "Yes", "Yes", "No", "No"]
}

df = pd.DataFrame(data)

#print(data["Loves Popcorn"])

def calc_gini_impurity(data): #gets data which the last one is the outcome
    max_gini_impurity = 0
    max_key=""
    #'key': [


    for key in data[:-1]:  # all except the last key

