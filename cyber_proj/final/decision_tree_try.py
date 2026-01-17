

import pandas as pd
from binary_tree import BinaryTreeNode

# Create the dataset
data = {
    "Loves Popcorn": ["Yes", "Yes", "No", "No", "Yes", "Yes", "No"],
    "Loves Soda": ["Yes", "No", "Yes", "Yes", "Yes", "No", "No"],
    "Age": [7, 12, 18, 35, 38, 50, 83],
    "Loves Cool As Ice": ["No", "No", "Yes", "Yes", "Yes", "No", "No"]
}

df = pd.DataFrame(data)

#print(data["Loves Popcorn"])

def sort_by_number(num_list, outcomes):
    pairs = zip(num_list, outcomes)
    sorted_pairs = sorted(pairs, key=lambda x: x[0])
    return map(list, zip(*sorted_pairs))

def calc_gini_impurity(col, outcome): #gets data which the last one is the outcome
    '''gets a col of data and a col of outcomes. The program will calculate the gini inpurity value of that column. If the coloumn values are int: a tuple with the
    gini impurity and the num. If the column values are strings, a tuple with the gini impurity only will be returned -> x[0] gini impurity'''
    if not col:
        return #list empty
    outcome_yes = 0 #how much from the 'yes' in col are 'yes' in outcome
    not_outcome_yes = 0 #how much from the 'yes' in col are 'no' in outcome
    #-----
    outcome_no = 0 #how much from the 'no' in col are 'yes' in outcome
    not_outcome_no = 0 #how much from the 'no' in col are 'no' in outcome
    if isinstance(col[0], str):
        '''yes or no'''
        for i in range(len(col)):
            if col[i].lower() =='yes': #the feature is right
                if outcome[i].lower() == 'yes': #the outcome is right
                    outcome_yes +=1
                else: ##the outcome is false
                    outcome_no+=1
            else:    #the feature is wrong
                if outcome[i].lower() == 'yes': #the outcome is right
                    not_outcome_yes +=1
                else: #: #the outcome is false
                    not_outcome_no+=1

        left_total = outcome_no + outcome_yes  # all of the 'yes' of the feature
        gini_impu_left = 1 - (outcome_yes / left_total) ** 2 - (outcome_no / left_total) ** 2

        right_total = not_outcome_no + not_outcome_yes  # all of the 'no' of the feature
        gini_impu_right = 1 - (not_outcome_yes / right_total) ** 2 - (not_outcome_no / right_total) ** 2

        total_gini = (gini_impu_left * left_total + gini_impu_right * right_total) / (left_total + right_total)


    elif isinstance(col[0], int): #-----------------------------int
        '''yes or no'''
        num_sorted, outcomes_sorted = sort_by_number(col, outcome)

        avg = [] #the averages of nearby col int values, for example ages
        gini_impu_nums = []
        for i in range(len(num_sorted)-1):
            avg.append((num_sorted[i]+num_sorted[i+1])/2)


        for num in avg:
            outcome_yes, outcome_no, not_outcome_yes, not_outcome_no = 0 , 0 , 0 , 0
            for i in range(len(num_sorted)): #through all of the col
                if  num_sorted[i] < num:  # the feature is right
                    if outcomes_sorted[i].lower() == 'yes':  # the outcome is right
                        outcome_yes += 1
                    else:  ##the outcome is false
                        outcome_no += 1
                else:  # the feature is wrong
                    if outcomes_sorted[i].lower() == 'yes':  # the outcome is right
                        not_outcome_yes += 1
                    else:  #: #the outcome is false
                        not_outcome_no += 1

            left_total = outcome_no + outcome_yes  # all of the 'yes' of the feature
            gini_impu_left = 1 - (outcome_yes / left_total) ** 2 - (outcome_no / left_total) ** 2

            right_total = not_outcome_no + not_outcome_yes  # all of the 'no' of the feature
            gini_impu_right = 1 - (not_outcome_yes / right_total) ** 2 - (not_outcome_no / right_total) ** 2

            total_gini = (gini_impu_left * left_total + gini_impu_right * right_total) / (
                        left_total + right_total)  # calculating the gini impurity for that avg ages sum

            gini_impu_nums.append(total_gini)

        total_gini = min(gini_impu_nums)
        idx = gini_impu_nums.index(total_gini) # to find the avrg we need check when gini is min
        return (total_gini, avg[idx])






    return (total_gini,)

def sort_data_by_key(data_dict, sort_key, num=None):
    """gets a daca_dict and a key and sorts by wether the key is right or not. returns a tuple with the data of the left ('Yes') and data of the right ('No')
    The tuple is the result of the calc_gini_impurity which the first one is the gi, and the second is a certain num if the col is numbers"""

    if not data_dict:
        return

    sort_by_num = True
    if not num:
        sort_by_num=False



    data_left = {} #if true
    data_right = {}  # if false
    new_data_dict= {} #the key that we don't need when adding the values
    for key in data_dict: #each new data dict will be already with all of the keys that the original have, *except* the sorting key
        if key != sort_key:
            data_left[key] = []
            data_right[key] = []
            new_data_dict[key] = data_dict[key].copy() #copying



    sorting_data_list = data_dict[sort_key] #the data from the col we need to sort the data



    if sort_by_num:
        sorting_num = num #the num we sort by
        for i in range(len(sorting_data_list)):
            if sorting_data_list[i]<sorting_num:
                for key in data_left:
                    data_left[key].append(new_data_dict[key][i]) #add the new value for each key in the left_data dict
            else:
                for key in data_right:
                    data_right[key].append(new_data_dict[key][i]) #add the new value for each key in the right_data dict
    else: #not sort by num
        for i in range(len(sorting_data_list)):
            if sorting_data_list[i].lower()=='yes':
                for key in data_left:
                    data_left[key].append(new_data_dict[key][i]) #add the new value for each key in the left_data dict
            else: #no
                for key  in data_right:
                    data_right[key].append(new_data_dict[key][i]) #add the new value for each key in the right_data dict

    return (data_left, data_right)







def is_majority(lst, value):
    """
    Returns True if `value` appears in more than half of the elements in `lst`.
    A tie does not count as a majority.
    """
    if not lst:
        return False
    return lst.count(value) > len(lst) // 2

def count_two_values(lst, val1, val2):
    """
    Returns a tuple with the number of occurrences of `val1` and `val2`
    in the list `lst`, in the order (val1_count, val2_count).
    """
    return lst.count(val1), lst.count(val2)




def create_decision_tree(data_dict, tree = BinaryTreeNode()):
    """the last key is the outcome"""
    used_keys = [] #keys that are already used in the tree

    outcomes = data_dict[next(reversed(data_dict))]
    last_key = next(reversed(data_dict))
    yes_no = count_two_values(outcomes, 'Yes', 'No') #(yes, no)

    if not data_dict or len(data_dict)==1: #len(data_dict)==2 means there is a fetuare and an outcome
        return

    if all(x.lower() == 'yes' for x in outcomes):
        return BinaryTreeNode('yes '+last_key+" "+str(yes_no))

    if all(x.lower() == 'no' for x in outcomes):
        return BinaryTreeNode('no '+last_key+" "+str(yes_no))

    if len(data_dict) == 2:
        if is_majority(outcomes, 'yes'):
            return BinaryTreeNode('yes ' + last_key+" "+str(yes_no))
        else: #no
            return BinaryTreeNode('no ' + last_key+" "+str(yes_no))







    outcome_key, outcome_list = next(reversed(data_dict.items())) #last key and value

    items = list(data_dict.items()) #list of the items


    min_gini_impurity = (10,) #the feature which have the lowest gini impurtiy, gini impurtiy will always be between 0-1
    min_gini_feature = ""
    current_gini_impurity = () #the gini impurity of the current key

    for key, data_list in items[:-1]: #everything except the last key which is the outcome
        current_gini_impurity = calc_gini_impurity(data_list, outcome_list) #current col of data and outcome data list
        #print(current_gini_impurity)

        if current_gini_impurity[0]<min_gini_impurity[0]: #comparing the tuples first value = gini impurity
            min_gini_impurity = current_gini_impurity #updating
            min_gini_feature = key #the feature which have the lowest gini impurity





    try:
        num = min_gini_impurity[1] #if there is a num we need to check by
        new_dicts = sort_data_by_key(data_dict, min_gini_feature, num)
        tree = BinaryTreeNode(min_gini_feature + "<"+str(num)+"?")  # set the value of the current node-----------------
    except:
        tree = BinaryTreeNode(min_gini_feature + "?")  # set the value of the current node-----------------
        new_dicts = sort_data_by_key(data_dict, min_gini_feature)

    #new_dicts = sort_data_by_key(data_dict, min_gini_feature, num)
    tree.set_left(create_decision_tree(new_dicts[0],tree.get_left())) #recursive call for left node
    tree.set_right(create_decision_tree(new_dicts[1], tree.get_right())) #recursive call for right node

    return tree










data = {
    "Loves Popcorn": ["Yes", "Yes", "No", "No", "Yes", "Yes", "No", 'Yes'],
    "Loves Soda": ["Yes", "No", "Yes", "Yes", "Yes", "No", "No", 'No'],
    "Age": [7, 12, 18, 35, 38, 50, 83, 90],
    "Loves Cool As Ice": ["No", "No", "Yes", "Yes", "Yes", "No", "No", 'Yes']
}

#print(calc_gini_impurity(data["Loves Popcorn"], data["Loves Cool As Ice"]))
#print(calc_gini_impurity(data["Age"], data["Loves Cool As Ice"]))




final_tree = create_decision_tree(data)

final_tree.print_tree()



