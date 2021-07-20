from network_functions import load_profiles

f = open('profiles.txt', 'r')
friendships = {}
networks = {}
load_profiles(f, friendships, networks)

print("friendships:", friendships)
print("networks:", networks)