
import unittest
import network_functions

person_to_friends = {
    'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], 
    'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], 
    'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], 
    'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'], 
    'Alex Dunphy': ['Luke Dunphy'], 
    'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'], 
    'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], 
    'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 
    'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 
    'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'], 
    'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']
}

class TestGetFriends(unittest.TestCase):
    def test(self):
        actual = network_functions.get_friends_of_friends(person_to_friends, 'Alex Dunphy')
        expected = ['Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']
        self.assertEqual(actual, expected)

unittest.main()
           