"""Assignment 3 - Medical Treatment Planning
"""

from typing import Dict, List, TextIO
from constants import (NA, TREATMENT, PATIENT_ID_INDEX, NAME_TO_VALUE,
                       ID_TO_ATTRIBUTES, VALUE_TO_IDS, ID_TO_SIMILARITY)
from constants import (THREE_PATIENTS, PATIENTS_WITH_NA, NEW_PATIENT_INFO,
                       NEW_PATIENTS, NEW_PATIENTS_RECOMMENDATIONS)


def read_patients_dataset(patients_file: TextIO) -> ID_TO_ATTRIBUTES:
    """Return an ID_TO_ATTRIBUTES dictionary that contains all
    information from patients_file.

    Preconditions: patients_file is a TSV file,
                   patients_file is open for reading.

    >>> patients_file = open("medical_data_three.tsv")
    >>> id_to_attributes = read_patients_dataset(patients_file)
    >>> patients_file.close()
    >>> id_to_attributes == THREE_PATIENTS
    True
    """

    # TODO: complete this function body

    all_lines = patients_file.readlines()
    head = all_lines[0][:-1].split()

    d1 = {}
    for row in all_lines[1:]:
        d2 = {}
        x = row[:-1].split()
        for i in range(1, len(head)):
            d2[head[i]] = x[i]

        d1[x[0]] = d2

    return d1

def build_value_to_ids(id_to_attributes: ID_TO_ATTRIBUTES,
                       name: str) -> VALUE_TO_IDS:
    """Return a VALUE_TO_IDS dictionary, in which the keys are all
    possible values of an attribute with name name that appear in
    id_to_attributes, and the values are lists of all patient IDs that
    have that value for this attribute name.

    Precondition: name is a name of an attribute that appears in
                  id_to_attributes.

    >>> value_to_ids = build_value_to_ids(THREE_PATIENTS, 'Gender')
    >>> expected = {'male': ['tcga.aq.a54o'],
    ...             'female': ['tcga.5l.aat0', 'tcga.aq.a7u7']}
    >>> same_key_to_list_dicts(expected, value_to_ids)
    True
    """

    # TODO: complete this function body

    d = {}
    for k, v in id_to_attributes.items():
        for x in v.keys():
            if x == name:
                if v[x] not in d:
                    d[v[x]] = []
                d[v[x]].append(k)
    return d


def patients_with_missing_values(id_to_attributes: ID_TO_ATTRIBUTES,
                                 name: str) -> List[str]:
    """TODO: complete this docstring using the Function Design Recipe.
    返回一个列表，内容为patient_ids字符串，前提为name为Histological_Type并且name=NA
    >>> patients_with_missing_values(PATIENTS_WITH_NA, 'Histological_Type')
    ['tcga.5l.aat0']
    """

    # TODO: complete this function body
    
    s = []
    for k, v in id_to_attributes.items():
        for x in v.keys():
            if x == name and v[x] == 'NA':
                s.append(k)
    return s


def similarity_score(name_to_value_1: NAME_TO_VALUE,
                     name_to_value_2: NAME_TO_VALUE) -> float:
    """Return the total similarity score, rounded to 2 places after the
    decimal point, for the two patients with data name_to_value_1 and
    name_to_value_2, respectively. Ignore attribute TREATMENT in the 
    calculation.

    The total similarity score is the sum of the similarity scores for each
    of the patient's attributes. The total similarity score is to be rounded
    to 2 places after the decimal point. Do not round each individual
    attribute similarity score, only round the total.

    Each attribute similarity score is determined as follows:

    For each attribute other than TREATMENT:
      1. If either patient has an attribute value of NA, the similarity
         score for the attribute is 0.5.
      2. If the two attribute values are numeric, the similarity score for
         the attribute is 1 / ( (the absolute difference of the values) + 1 ).
      3. Otherwise, the similarity score for the attribute is 0.0 if the
         two patient attribute values are different or 1.0 if the two
         patient attribute values are the same.

    >>> p1 = THREE_PATIENTS['tcga.5l.aat0']
    >>> p2 = THREE_PATIENTS['tcga.aq.a54o']
    >>> abs(similarity_score(p1, p2) - 4.1) < 0.01
    True
    >>> p1 = PATIENTS_WITH_NA['tcga.5l.aat0']
    >>> p2 = PATIENTS_WITH_NA['tcga.aq.a7u7']
    >>> abs(similarity_score(p1, p2) - 4.07) < 0.01
    True
    """

    # TODO: complete this function body
    s = 0
    for k1, v1 in name_to_value_1.items():
        if k1 in name_to_value_2.keys(): 
            v2 = name_to_value_2[k1]
            if v1 == 'NA' or v2 == 'NA':
                x = 0.5

            elif v1.isdigit() and v2.isdigit():
                x = 1 / (abs(int(v1)-int(v2)) + 1) 
            else:
                if v1 == v2:
                    x = 1
                else: 
                    x = 0
            s = s + x

    return round(s, 2)


def patient_similarities(id_to_attributes: ID_TO_ATTRIBUTES,
                         name_to_value: NAME_TO_VALUE) -> ID_TO_SIMILARITY:
    """TODO: complete this docstring using the Function Design Recipe.
    返回一个ID_TO_SIMILARITY = Dict[str, float]，其中str为ID_TO_ATTRIBUTES中的patient_ID,
    float为由函数similarity_score得到的对应相似值
    """

    # TODO: complete this function body

    d = {}
    for k, v in id_to_attributes.items():
        similarities = similarity_score(v, name_to_value)
        d[k] = similarities

    return d


def patients_by_similarity(id_to_attributes: ID_TO_ATTRIBUTES,
                           name_to_value: NAME_TO_VALUE) -> List[str]:
    """TODO: complete this docstring using the Function Design Recipe.
    返回列表，其中为所有患者的ID，需要进行排序处理，根据函数patient_similarities得到
    每一个患者的id及相似度，由相似度的大小降序排列，如果相似度相同，则由字母表排序（字符串默认）
    """

    # TODO: complete this function body

    d = patient_similarities(id_to_attributes, name_to_value)
    x = []
    for k, v in d.items():
        x.append((k, v))

    x.sort(key=lambda s: s[1], reverse=True) #降序排列

    xscore = []
    for i in x:
        xscore.append(i[0])

    return xscore


def treatment_recommendations(id_to_attributes: ID_TO_ATTRIBUTES,
                              name_to_value: NAME_TO_VALUE) -> List[str]:
    """TODO: complete this docstring using the Function Design Recipe.
    返回列表，其中为'Treatment'的value值，其中第一个值必须为相似度最大的患者的'Treatment'的value值，
    按顺序排列'Treatment'的value值。若是在id_to_attributes中含有'NA'，则不加入列表，并且列表中的值不可重复
    """

    # TODO: complete this function body

    patients_ids = patients_by_similarity(id_to_attributes, name_to_value)
    x = []
    for pid in patients_ids:
        plan = id_to_attributes[pid]['Treatment']
        for k, v in id_to_attributes.items():
            for k1, v1 in v.items():
                if v1 != 'NA' and plan not in x:
                    x.append(plan)
    return x


def make_treatment_plans(id_to_attributes: ID_TO_ATTRIBUTES,
                         new_id_to_attributes: ID_TO_ATTRIBUTES) -> ID_TO_ATTRIBUTES:
    """Modify new_id_to_attributes by replacing the values of the
    TREATMENT attribute with the first recommended treatment for each patient,
    according to the existing patient data in id_to_attributes.
    根据id_to_attributes中现有的患者数据，用每个患者的第一个推荐治疗替代
    治疗属性的值来修改new_id_to_attributes

    >>> new_id_to_attributes = NEW_PATIENTS.copy()
    >>> make_treatment_plans(THREE_PATIENTS, new_id_to_attributes)
    >>> new_id_to_attributes == NEW_PATIENTS_RECOMMENDATIONS
    True
    """

    # TODO: complete this function body

    for k, v in new_id_to_attributes.items():
        x = treatment_recommendations(id_to_attributes, v)
        v['Treatment'] = v['Treatment'].replace('NA', x[0])
    return new_id_to_attributes


# Provided helper functions - can be used to test two objects for `sameness'.

def same_key_to_list_dicts(key_to_list1: Dict[str, List[str]],
                           key_to_list2: Dict[str, List[str]]) -> bool:
    """Return True if and only if key_to_list1 and key_to_list2 are equal
    dictionaries, regardless of the order in which elements occur in the 
    dictionaries' values.

    >>> same_key_to_list_dicts({'a': [], 'b': ['x'], 'c': ['x', 'y', 'z']},
    ...                        {'a': [], 'b': ['x'], 'c': ['y', 'z', 'x']})
    True
    >>> same_key_to_list_dicts({'a': [], 'b': ['x'], 'c': ['x', 'y', 'z']},
    ...                        {'a': [], 'b': ['x'], 'c': ['y', 'z', 'w']})
    False
    >>> same_key_to_list_dicts({'a': [], 'b': ['x'], 'd': ['x', 'y', 'z']},
    ...                        {'a': [], 'b': ['x'], 'c': ['y', 'z', 'x']})
    False
    """

    if key_to_list1.keys() != key_to_list2.keys():
        return False

    for key in key_to_list1:
        if not same_lists(key_to_list1[key], key_to_list2[key]):
            return False

    return True


def same_lists(list1: list, list2: list) -> bool:
    """Return True if and only if list1 and list2 are equal lists, regardless 
    of the order in which elements occur.

    >>> same_lists(['x', 'y', 'z'], ['y', 'z', 'x'])
    True
    >>> same_lists(['x', 'y', 'k'], ['y', 'z', 'x'])
    False
    """

    return sorted(list1) == sorted(list2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    medical_data_file = 'medical_data.tsv'
    patients_data_file = open(medical_data_file)
    patient_id_to_attributes = read_patients_dataset(patients_data_file)
    patients_data_file.close()

    medical_data_file = 'new_patients.tsv'
    new_patients_data_file = open(medical_data_file)
    new_patient_id_to_attributes = read_patients_dataset(new_patients_data_file)
    new_patients_data_file.close()

    make_treatment_plans(patient_id_to_attributes, 
                         new_patient_id_to_attributes)
    
    for new_patient_id in new_patient_id_to_attributes:
        recommend_str = (
            'The recommended treatment for patient {} is {}.'.format(
                new_patient_id,
                new_patient_id_to_attributes[new_patient_id][TREATMENT]))
        # Uncomment the line below to view the treatment plans but
        #  re-comment out before submitting solution.
        print(recommend_str)
