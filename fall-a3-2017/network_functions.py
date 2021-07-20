""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    content = profiles_file.read()
    graphs = content.split('\n\n')
    for graph in graphs:
        lines = graph.split('\n')
        name = lines[0].split(',')
        new_name = name[1].strip() + ' ' + name[0]
        
        rest = set(lines[1:])
        if rest != set():
            friends = [x.split(',')[1].strip() + ' ' + x.split(',')[0] \
                        for x in rest if ',' in x]
            friends.sort()
            person_to_friends[new_name] = friends

            net_names = [x for x in rest if ',' not in x and x != '']
            if net_names != []:
                net_names.sort()
                person_to_networks[new_name] = net_names


def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """
    Return the average number of friends that people who appear as keys in 
    the given "person to friend" dictionary have.

    >>> person_to_firends = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett'], 'Claire Dunphy': ['Jay Pritchett', 'Phil Dunphy']}
    >>> get_average_friend_count(person_to_friends)
    2.0
    """
    x = len(person_to_friends.keys())
    y = sum([len(x) for x in person_to_friends.values()])
    if x != 0:
        return float(y / x)
    else:
        return 0.0
    
def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Return a "last name to first names" dictionary based on the given "person
    to friends" dictionary .
    """
    d = {}
    # 将字典中的所有内容放到一个列表中
    all_names = list(person_to_friends) + \
                [y for v in person_to_friends.values() for y in v]
    all_not_repeated_names = set(all_names)
    # 遍历列表
    for names in all_not_repeated_names:
        first_name, last_name = names.split(' ')
        if last_name not in d:
            d[last_name] = [first_name,]
        else:
            d[last_name].append(first_name)
    for _, v in d.items():
        v.sort()
    return d 

def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Return a "network to people" dictionary based on the given "person to 
    networks" dictionary.
    """
    d = {}
    k = list(person_to_networks)
    v = list(person_to_networks.values())
    # 遍历将每个 value 标上数字，便于判断索引位置
    s = []
    for i, j in enumerate(v):
        for x in j:
            s.append((i, x))
    # 通过索引数字找key, 放到字典中
    for x0, x1 in s:
        if x1 not in d:
            d[x1] = [k[x0]]
        else:
            d[x1].append(k[x0]) 
    return d 

def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
    person: str) -> List[str]:
    """
    Return a list of names of people who are friends of the named 
    person's friends.
    """
    s = []
    for friend in person_to_friends.get(person, []):
        for y in person_to_friends.get(friend, []):
            if y != person:
                s.append(y)
    s.sort()
    return s 

def get_potential_friends(person: str, person_to_friends: \
                          Dict[str, List[str]]) -> List[str]:
    """
    Return potential friends
    """
    all_not_repeated_name = set(list(person_to_friends) + \
                [y for v in person_to_friends.values() for y in v])
    potential_friends = [x for x in all_not_repeated_name \
                        if x not in person_to_friends.get(person, []) and x != person]
    return potential_friends
        
def insert_sort_potential_friends(s: List[Tuple[str, int]], \
                                  score: int, person: str) -> None:
    """
    insert and sort potential friends
    """
    if score != 0:
        founda = False
        foundb = False
        i = 0 
        while i < len(s) and (not founda) and (not foundb):
            x = s[i]
            if score > x[1]:
                s.insert(i, (person, score))
                founda = True
            
            if (score == x[1]) and (person <= x[0]):
                s.insert(i, (person, score))
                foundb = True
            i = i + 1

        if not founda and not foundb:
            s.append((person, score))

def get_net_name_score(person: str, person_b: str, \
                       net_names: Dict[str, List[str]]) -> int:
    """
    Return net_name score
    """
    for _, v in net_names.items():
        if person in v and person_b in v:
            return 1
    return 0

def get_mutual_friends_score(person: str, person_b: str, \
                             person_to_friends: Dict[str, List[str]]) -> int:
    """
    Return mutual friends score
    """
    score = 0
    f1 = get_friends_of_friends(person_to_friends, person)
    f2 = get_friends_of_friends(person_to_friends, person_b)
    if person in f2:
        score += f2.count(person)
    if person_b in f1:
        score += f1.count(person_b)
    return score

def get_last_name_score(person: str, person_b: str) -> int:
    """
    Return last_name score
    """
    if person_b.split()[-1] == person.split()[-1]:
        return 1
    return 0

def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """
    Return the friend recommendations for the given person as a list 
    of tuples.
    """
    s = []
    net_names = invert_network(person_to_networks)
    potential_friends = get_potential_friends(person, person_to_friends)

    for person_b in potential_friends:
        score = 0
        # 处理共同朋友
        score += get_mutual_friends_score(person, person_b, person_to_friends)
        
        # 处理网名相同
        score += get_net_name_score(person, person_b, net_names)
        
        # 处理姓相同
        score += get_last_name_score(person, person_b)
        
        # 处理排序
        insert_sort_potential_friends(s, score, person_b)

    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()
