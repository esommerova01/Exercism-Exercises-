"""How long does it take to cook a lasagna?"""
#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers): 
    """Calculate the prep time based on number of layers"""
    return number_of_layers * PREPARATION_TIME

#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time): 
    """Total cook and prep time"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time