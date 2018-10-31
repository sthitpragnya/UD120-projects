#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []

    ### your code goes here
    for i in range(len(predictions)):
        cleaned_data.append((ages[i], net_worths[i], abs(net_worths[i] - predictions[i])))
    
    cleaned_data.sort(key=lambda tup: tup[2], reverse = True)
    
    del cleaned_data[0:9]
    
    return cleaned_data

