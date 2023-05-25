# a4.py
# Kene Chukwuma (ebc68) and Monalise Almeida (mca74)
# Sources/people consulted: FILL IN OR WRITE "NONE"
# PUT DATE YOU COMPLETED THIS HERE
# release code by Cornelius Boateng(cob32) and Lenhard Thomas(lot5), Jan 2023

""" A package of helpful functions for preparing and enjoying Food. """

from a4_classes import Food, Student


def remove_dups(lst):
    """
    Returns a list containing all the unique elements of `lst` while preserving
    order such that the first instance of a duplicate is kept.

    Example:
    remove_dups([1, 2, 2, 3]) returns [1, 2, 3]

    Precondition:
    `lst` is a (possibly empty) list
    """
    assert isinstance(lst, list), "lst is not a list"
    acc = []
    for x in lst:
        if x not in acc:
            acc.append(x)
    return acc


def convert_time(minutes):
    """
    Returns a string representation of `minutes` in the format HH:MM, where
    HH represents the number of hours and MM represents the number of minutes.

    Example:
    convert_time(150) returns "02:30"

    Precondition:
    `minutes` is a non-negative int
    """
    assert isinstance(minutes, int), "minutes is not an int"
    assert minutes >= 0, "minutes is not non-negative"
    return "{:02d}:{:02d}".format(*divmod(minutes, 60))


def safe_to_eat(food, student):
    """
    Returns: True if `student` can safely eat `food`
    `student` cannot eat `food` if the name of `food` or any ingredient (or
    sub-ingredient) of `food` is found on the list of `allergies` of `student`

    `food` and `student` should not be modified by this function

    Examples:
    tom = Food("tomato")
    lime = Food("lime")
    avo = Food("avocado")
    guac = Food("guacamole", 10, [tom, lime, avo])
    joey = Student("Joey", ["avocado"])

    safe_to_eat(tom, joey) -> True
    safe_to_eat(avo, joey) -> False
    safe_to_eat(guac, joey) -> False

    Precondition:
    `food`: an instance of Food, not None
    `student`: an instance of Student, not None
    """
    assert isinstance(food, Food), "food is not a Food object"
    assert isinstance(student, Student), "student is not a Student object"
    # STUDENTS: IMPLEMENT THIS FUNCTION with Recursion
    #pass
    if student.allergies == []:
        return True
    if food.name not in student.allergies and food.ingredients == []:             
        return True
    else: 
        for simpfood in food.ingredients:
            safe_to_eat(simpfood, student) != True
    return False       
        
   



def shopping_list(food):
    """
    Returns: a sorted list of the unique names of all simple Food that are
    needed to cook `food`.

    `food` should not be modified by this function

    Examples:
    tomato = Food("tomato")
    garlic = Food("garlic")
    beef = Food("beef")
    eggs = Food("eggs")
    breadcrumbs = Food("breadcrumbs")
    spaghetti = Food("spaghetti")

    marinara = Food("marinara", 50, [tomato, garlic])
    meatballs = Food("meatball", 40, [beef, garlic, eggs, breadcrumbs])
    saucy_pasta = Food("Spaghetti w/ meatballs", 25,
                       [spaghetti, marinara, meatballs])

    shopping_list(tomato) -> ["tomato"]
    shopping_list(meatballs) -> ["beef", "breadcrumbs", "eggs", "garlic"]
    shopping_list(saucy_pasta) -> ["beef", "breadcrumbs", "eggs", "garlic",
                                   "spaghetti", "tomato"]

    Precondition:
    `food` is an instance of Food, not None.
    """
    assert isinstance(food, Food), "food is not a Food object"
    # STUDENTS: IMPLEMENT THIS FUNCTION with Recursion
    #pass

    result = []

    if food.ingredients == []:
        return [food.name]
    else:
        shoplist = [] 
        for ingre in food.ingredients:
            shoplist += shopping_list(ingre)  
        for x in shoplist:
            if x not in result:
                result.append(x)
                
    return sorted(result)



def total_cooking_time(food):
    """
    Returns: the total time in minutes needed to cook `food`.

    Note: the `time` attribute for each food is independent of its ingredients
    and assumes that the ingredients are already prepared and available.

    `food` should not be modified by this function

    Examples:
    tomato = Food("tomato")
    garlic = Food("garlic")
    beef = Food("beef")
    eggs = Food("eggs")
    breadcrumbs = Food("breadcrumbs")
    spaghetti = Food("spaghetti")

    marinara = Food("marinara", 50, [tomato, garlic])
    meatballs = Food("meatball", 40, [beef, garlic, eggs, breadcrumbs])
    saucy_pasta = Food("Spaghetti w/ meatballs", 25,
                       [spaghetti, marinara, meatballs])

    total_cooking_time(tomato) -> 0
    total_cooking_time(meatballs) -> 40
    total_cooking_time(saucy_pasta) -> 115 (25 + 50 + 40)

    Precondition:
    `food` is an instance of Food, not None
    """
    assert isinstance(food, Food), "food is not a Food object"
    # STUDENTS: IMPLEMENT THIS FUNCTION with Recursion
    #pass

    
    if food.ingredients == []:
        return food.time
    else: 
        duration = food.time
        for ingre in food.ingredients:
            duration += total_cooking_time(ingre) 
        return duration
    

    

def cooks_first(food1, food2):
    """
    Returns: a 2-item list containing:
       - the name of the Food (of food1 or food2) that will be cooked first
       - the total time it takes to be cooked in HH:MM format

    If both will take the same total time, `food1` is preferred.

    Examples:
    tomato = Food("tomato")
    garlic = Food("garlic")
    beef = Food("beef")
    eggs = Food("eggs")
    breadcrumbs = Food("breadcrumbs")
    spaghetti = Food("spaghetti")

    marinara = Food("marinara", 50, [tomato, garlic])
    meatballs = Food("meatball", 40, [beef, garlic, eggs, breadcrumbs])
    saucy_pasta = Food("Spaghetti w/ meatballs", 25,
                       [spaghetti, marinara, meatballs])

    cooks_first(eggs, marinara) -> ["eggs", "00:00"]
    cooks_first(garlic, eggs) -> ["garlic", "00:00"]
    cooks_first(meatballs, marinara) -> ["meatballs", "00:40"]
    cooks_first(saucy_pasta, saucy_pasta) -> ["Spaghetti w/ meatballs", "01:55"]

    Precondition:
    `food1` and `food2` are both instances of Food, not None.
    """
    assert isinstance(food1, Food), "food1 is not a Food object"
    assert isinstance(food2, Food), "food2 is not a Food object"
    # STUDENTS: Notice the helper function for converting minutes into HH:MM
    #pass

    result = []
    if total_cooking_time(food1) == total_cooking_time(food2):
        result.append(food1.name)
        foody = convert_time (total_cooking_time(food1))
        result.append(foody)
        return result
    elif total_cooking_time(food1) > total_cooking_time(food2):
        result.append(food2.name)
        foody = convert_time (total_cooking_time(food2))
        result.append(foody)
        return result
    else:
        result.append(food1.name)
        foody = convert_time (total_cooking_time(food1))
        result.append(foody)
        return result
    

    '''
    fooda = total_cooking_time(food1)
    foodb = total_cooking_time(food2)

    if fooda <= foodb: 
        list = [food1.name]
        time = convert_time(fooda)
    else:
        list = [food2.name]
        time = convert_time(fooda)
    list.append(time)
    return list
    '''