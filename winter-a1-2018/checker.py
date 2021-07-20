import sys
sys.path.insert(0, 'pyta')

print("================= Start: checking coding style =================")

import python_ta
python_ta.check_all('wordlock_functions.py', config='pyta/a1_pyta.txt')

print("================= End: checking coding style =================\n")

print("================= Start: checking parameter and return types =================")

import builtins

# Check for use of functions print and input.

# IMPORTANT!
# If you are getting a syntax error here for the line:
#     our_print = print
# Then you are using the wrong version of Python! 
our_print = print
our_input = input


def disable_print(*args):
    raise Exception("You must not call print anywhere in your code!")

def disable_input(*args):
    raise Exception("You must not call input anywhere in your code!")


builtins.print = disable_print
builtins.input = disable_input

import wordlock_functions as wf

# Get the initial values of the constants
constants_before = [wf.SECTION_LENGTH, wf.ANSWER, wf.SWAP, wf.ROTATE, wf.CHECK]

# Type check wf.get_section_start
result = wf.get_section_start(1)
assert isinstance(result, int), \
       '''get_section_start should return an int, but returned {0}
       '''.format(type(result))

# Type check wf.is_valid_move
result = wf.is_valid_move('S')
assert isinstance(result, bool), \
       '''is_valid_move should return a bool, but returned {0}
       '''.format(type(result))

# Type check wf.is_valid_section
result = wf.is_valid_section(-1)
assert isinstance(result, bool), \
       '''is_valid_section should return a bool, but returned {0}
       '''.format(type(result))

# Type check wf.check_section
result = wf.check_section('CATDGOXOFIGP', 1)
assert isinstance(result, bool), \
       '''check_section should return a bool, but returned {0}
       '''.format(type(result))

# Type check wf.change_state
state = 'TACDGOXOFIGP'
result = wf.change_state(state, 1, 'S')
assert isinstance(result, str), \
       '''change_state should return an str, but returned {0}
       '''.format(type(result))
assert len(state) == len(result), \
       '''change_state should not change the length of the game state
       '''

# Type check wf.get_move_hint
result = wf.get_move_hint('TACDOGFOXPIG', 1)
assert isinstance(result, str), \
       '''get_move_hint should return a str, but returned {0}
       '''.format(type(result))
assert result in [wf.SWAP, wf.ROTATE, wf.CHECK], \
       '''get_move_hint should return a valid move
       '''

builtins.print = our_print
builtins.input = our_input

print("================= End: checking parameter and return types =================\n")

print("================= Start: checking whether constants are unchanged =================")

# Get the final values of the constants
constants_after = [wf.SECTION_LENGTH, wf.ANSWER, wf.SWAP, wf.ROTATE, wf.CHECK]

# Check whether the constants are unchanged.
assert constants_before == constants_after, \
       """Your function(s) modified the value of a constant(s). Edit your code
        so that the values of constants are unchanged by your functions."""
print("================= End: checking whether constants are unchanged =================\n")



print("The parameter and return type checker passed.")
print("This means we will be able to test your code.")
print("It does NOT mean your code is necessarily correct.")
print("You should run your own thorough tests to convince yourself your code is correct.")
print()
print("Scroll up to review the output of checking coding style.")


