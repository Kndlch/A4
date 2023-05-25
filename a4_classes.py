# a4_classes.py
# Cornelius Boateng(cob32) and Lenhard Thomas(lot5), Jan 2023

"""Defines classes Food and Student."""


class Food:
  """
  Instance attributes:
    * name [non-empty string]: the name of the food
    * time [int >= 0]: the number of minutes required to prepare the food
    * ingredients [possibly empty list of Food]: items that make up this Food
  """

  def __init__(self, n, t=0, i=None):
    """
    An instance of Food with name [n] that takes [t] minutes to cook
    and is made of ingredients [i].

    Parameter n: the name of the food
    Precondition: non-empty string

    Parameter t: the amount of time it takes to make the food
    Precondition: a non-negative int

    Parameter i: the foods that make up this Food
    Precondition: list of Food objects such that this Food is not an immediate
    ingredient not a sub-ingredient
    """
    assert isinstance(n, str), "name is not a string"
    assert len(n) >= 0, "name is empty string"
    assert isinstance(t, int), "time is not an int"
    assert t >= 0, "time is not non-negative"
    if i is not None:
      assert isinstance(i, list), "ingredients is not a list"
      assert all((isinstance(x, Food)
                  for x in i)), "not everything in ingredients is a food"

    self.name = n
    self.time = t
    self.ingredients = i if i is not None else []

  def __repr__(self) -> str:
    return self.name

  def __lt__(self, other):
    """Sort by cooking time"""
    assert isinstance(other, Food), "Can only compare foods with foods"
    return self.time < other.time


class Student:
  """
  Instance attributes:
    * name [non-empty string]: name of this student
    * allergies [possibly empty list of str]: names of foods that this
                                              student is allergic to
  """

  def __init__(self, n, a):
    """
    An instance of Student with name [n] who is allergic to the foods in [a].

    Parameter n: the name of the student
    Precondition: non-empty string

    Parameter a: the list of names of foods that the student is allergic to
    Precondition: a list of str
    """
    assert isinstance(n, str), "name of the student is not a string"
    assert len(n) >= 0, "name is not a non-empty string"
    assert isinstance(a, list), "allergies is not a list"
    assert all((isinstance(x, str)
               for x in a)), "allergies is not a list of str"

    self.name = n
    self.allergies = a

  def __repr__(self):
    return self.name
