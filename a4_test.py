# a4_test.py
# Cornelius Boateng(cob32) and Lenhard Thomas(lot5), March 2023
"""
Testing script for a4.py
"""

from a4 import *
from a4_classes import Food, Student
import cornellasserts as ca

# Simple Food
water = Food("water")
salt = Food("salt")
sw = Food("seaweed")

tomato = Food("tomato")
lime = Food("lime")
avo = Food("avocado")

garlic = Food("garlic")
beef = Food("beef")
eggs = Food("eggs")
breadcrumbs = Food("breadcrumbs")
spaghetti = Food("spaghetti")

# Complex Food
guacamole = Food("guacamole", 10, [tomato, lime, avo])

marinara = Food("marinara", 50, [tomato, garlic])
meatballs = Food("meatballs", 40, [beef, garlic, eggs, breadcrumbs])
saucy_pasta = Food("Spaghetti w/ meatballs", 25,
                   [spaghetti, marinara, meatballs])

# Students
joey_scillia = Student("Joey", ["avocado"])


def test_convert_time():
  # The method being tested was already completed for you but this is kept here
  # as a sanity check

  # both are zero
  ca.assert_equals("00:00", convert_time(0))

  # just hours is zero
  ca.assert_equals("00:21", convert_time(21))

  # just minutes is zero
  ca.assert_equals("12:00", convert_time(720))

  # single digit hours
  ca.assert_equals("01:15", convert_time(75))

  # single digit minutes
  ca.assert_equals("12:10", convert_time(730))

  # neither is single digit
  ca.assert_equals("12:12", convert_time(732))


def test_remove_dups():
  # This method being tested was already completed for you but is kept here
  # as a sanity check

  # no duplicates
  out = remove_dups([water, salt, sw])
  ca.assert_equals([water, salt, sw], out)

  # one duplicate
  out = remove_dups([water, salt, water, sw])
  ca.assert_equals([water, salt, sw], out)

  # multiple duplicates of same thing
  out = remove_dups([water, water, water, water])
  ca.assert_equals([water], out)

  # multiple duplicates of diff things
  out = remove_dups([water, salt, sw, sw, salt, water])
  ca.assert_equals([water, salt, sw], out)


def test_safe_to_eat():
  # Note that this test case may or may not be exhaustive;
  # feel free to add more test cases as needed.

  # Food is safe to eat
  out = safe_to_eat(tomato, joey_scillia)
  ca.assert_equals(True, out)

  # Food is the student's allergy
  out = safe_to_eat(avo, joey_scillia)
  ca.assert_equals(False, out)

  # Food is made up of student's allergy
  out = safe_to_eat(guacamole, joey_scillia)
  ca.assert_equals(False, out)


def test_shopping_list():
  # Note that this test case may or may not be exhaustive;
  # feel free to add more test cases as needed

  # Simple food
  out = shopping_list(tomato)
  ca.assert_equals(["tomato"], out)

  # Complex food with no duplicates
  out = shopping_list(meatballs)
  ca.assert_equals(["beef", "breadcrumbs", "eggs", "garlic"], out)

  # Complex food with duplicates
  out = shopping_list(saucy_pasta)
  ca.assert_equals(["beef", "breadcrumbs", "eggs",
                        "garlic", "spaghetti", "tomato"], out)


def test_total_cooking_time():
  # Note that this test case may or may not be exhaustive;
  # feel free to add more test cases as needed.

  # Simple food
  ca.assert_equals(0, total_cooking_time(tomato))

  # Complex food with simple food ingredients
  ca.assert_equals(40, total_cooking_time(meatballs))

  ca.assert_equals(115, total_cooking_time(saucy_pasta))


def test_cooks_first():
  # Note that this test case may or may not be exhaustive; feel free to add more
  # test cases as needed.

  # One simple food
  ca.assert_equals(["eggs", "00:00"], cooks_first(eggs, marinara))

  # No simple food
  ca.assert_equals(["meatballs", "00:40"],
                        cooks_first(meatballs, marinara))
# First input is None
  #ca.assert_equals(None, cooks_first(None, marinara))

    # Second input is None
  #ca.assert_equals(None, cooks_first(marinara, None))

    # Both inputs are None
  #ca.assert_equals(None, cooks_first(None, None))

    # Same total cooking time for both inputs
  ca.assert_equals(["eggs", "00:00"], cooks_first(eggs, tomato))

    # Recursive inputs
  ca.assert_equals(["Spaghetti w/ meatballs", "01:55"],
                      cooks_first(saucy_pasta, marinara))

    # Inputs with same name
  beef1 = Food("beef")
  beef2 = Food("beef", time=30)
  ca.assert_equals(["beef (1)", "00:00"], cooks_first(beef1, beef2))
  ca.assert_equals(["beef (2)", "00:30"], cooks_first(beef2, beef1))  

def testing_suite():
  print("Beginning the testing suite!\n")
  suite = [
      test_convert_time,
      test_remove_dups,
      test_safe_to_eat,
      test_shopping_list,
      test_total_cooking_time,
      test_cooks_first
  ]

  for test in suite:
    print(f"  Starting test for: {test.__name__}")
    test()
    print(f"  Successfully ran {test.__name__}\n")
  print("Amazing! The entire testing suite has been completed")


if __name__ == "__main__":
  testing_suite()
