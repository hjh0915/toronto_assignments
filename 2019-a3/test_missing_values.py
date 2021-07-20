"""A3. Tester for the function patients_with_missing_values
in treatment_functions.
"""

import unittest
import treatment_functions as tfs

ERROR_MESSAGE = "Expected {}, but returned {}"


class TestPatientsWithMissingValues(unittest.TestCase):
    """Tester for the function patients_with_missing_values in
    treatment_functions.
    """

    def test_empty(self):
        """Empty dictionary."""

        id_to_attributes = {}
        name = 'xyz'
        expected = []
        actual = tfs.patients_with_missing_values(id_to_attributes, name)

        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_one_patient_no_missing(self):
        """One patient, with the value present."""

        id_to_attributes = {
            'Tom':  {'Pet': 'dog', 'Car': 'NA', 'Team': 'Leafs'}
        }
        name = 'Pet'
        expected = []
        actual = tfs.patients_with_missing_values(id_to_attributes, name)

        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    ### ADD YOUR TESTS HERE ###

    def test_read_patients_dataset(self):
        """
        Test patients_dataset is got.
        """
        id_to_attributes = {
            'tcga.5l.aat0': {'Age': '42', 'Gender': 'female', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0',
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_1', 'Lymph_Nodes': '0', 'Treatment': 'plan_1'},
            'tcga.aq.a54o': {'Age': '51', 'Gender': 'male', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0',
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_2', 'Lymph_Nodes': '0', 'Treatment': 'plan_2'},
            'tcga.aq.a7u7': {'Age': '55', 'Gender': 'female', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n2a',
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_1', 'Lymph_Nodes': '4', 'Treatment': 'plan_4'}
        }

        with open('medical_data_three.tsv', 'r') as file:
            actual = tfs.read_patients_dataset(file)
        expected = id_to_attributes
        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    
    def test_build_value_to_ids(self):
        """Test value_to_ids is got"""

        value_to_ids = {'male': ['tcga.aq.a54o'],
                        'female': ['tcga.5l.aat0', 'tcga.aq.a7u7']}

        id_to_attributes = {
            'tcga.5l.aat0': {'Age': '42', 'Gender': 'female', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0',
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_1', 'Lymph_Nodes': '0', 'Treatment': 'plan_1'},
            'tcga.aq.a54o': {'Age': '51', 'Gender': 'male', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0',
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_2', 'Lymph_Nodes': '0', 'Treatment': 'plan_2'},
            'tcga.aq.a7u7': {'Age': '55', 'Gender': 'female', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n2a',
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_1', 'Lymph_Nodes': '4', 'Treatment': 'plan_4'}
        }

        expected = value_to_ids
        actual = tfs.build_value_to_ids(id_to_attributes, 'Gender')
        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    
    def test_similarity_score(self):
        """Test similarity_score is got"""

        name1 = {'Age': '42', 'Gender': 'female', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0',
        'Cancer_Spread': 'm0', 'Histological_Type': 'NA', 'Lymph_Nodes': '0'}
        name2 = {'Age': '51', 'Gender': 'male', 'Tumor_Size': 't2','Nearby_Cancer_Lymphnodes': 'n0',
        'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_2', 'Lymph_Nodes': '0'}

        expected = 4.60
        actual = tfs.similarity_score(name1, name2)
        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_patient_similarities(self):
        """Test patient_similarities is got a dictionary that has ids and similarities
        """

        id_to_attributes = {
            'tcga.aq.a54o': {'Age': '51', 'Gender': 'male', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0', 
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_2', 'Lymph_Nodes': '0', 'Treatment': 'plan_2'},
            'tcga.aq.a7u7': {'Age': '55', 'Gender': 'female', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n2a',
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_1', 'Lymph_Nodes': '4', 'Treatment': 'plan_4'}, 
            'tcga.xx.a899': {'Age': '46', 'Gender': 'female', 'Tumor_Size': 't1c', 'Nearby_Cancer_Lymphnodes': 'n2a', 
                'Cancer_Spread': 'mx', 'Histological_Type': 'h_t_1', 'Lymph_Nodes': '5', 'Treatment': 'plan_4'}
        }

        name1 = {'Age': '55', 'Gender': 'male', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0',
        'Cancer_Spread': 'm0', 'Histological_Type': 'NA', 'Lymph_Nodes': '0'}

        expected = {'tcga.aq.a54o': 5.70, 'tcga.aq.a7u7': 3.70, 'tcga.xx.a899': 0.77}
        actual = tfs.patient_similarities(id_to_attributes, name1)
        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_patients_by_similarity(self):
        """测试是否按照降序排列"""

        id_to_attributes = {
            'tcga.aq.a7u7': {'Age': '55', 'Gender': 'female', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n2a',
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_1', 'Lymph_Nodes': '4', 'Treatment': 'plan_4'}, 
            'tcga.aq.a54o': {'Age': '51', 'Gender': 'male', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0', 
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_2', 'Lymph_Nodes': '0', 'Treatment': 'plan_2'}
        }

        name1 = {'Age': '55', 'Gender': 'male', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0',
        'Cancer_Spread': 'm0', 'Histological_Type': 'NA', 'Lymph_Nodes': '0'}

        expected = ['tcga.aq.a54o', 'tcga.aq.a7u7']
        actual = tfs.patients_by_similarity(id_to_attributes, name1)
        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_treatment_recommendations(self):
        """测试返回值是否为plan"""

        id_to_attributes = {
            'tcga.aq.a7u7': {'Age': '55', 'Gender': 'female', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n2a',
                'Cancer_Spread': 'm0', 'Histological_Type': 'NA', 'Lymph_Nodes': '4', 'Treatment': 'plan_4'}, 
            'tcga.aq.a54o': {'Age': '51', 'Gender': 'male', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0', 
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_2', 'Lymph_Nodes': '0', 'Treatment': 'plan_2'}, 
            'tcga.xx.a899': {'Age': '46', 'Gender': 'female', 'Tumor_Size': 't1c', 'Nearby_Cancer_Lymphnodes': 'n2a', 
                'Cancer_Spread': 'mx', 'Histological_Type': 'h_t_1', 'Lymph_Nodes': '5', 'Treatment': 'plan_4'}
        }

        name1 = {'Age': '55', 'Gender': 'male', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0',
        'Cancer_Spread': 'm0', 'Histological_Type': 'NA', 'Lymph_Nodes': '0'}

        expected = ['plan_2', 'plan_4']
        actual = tfs.treatment_recommendations(id_to_attributes, name1)
        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)

    def test_make_treatment_plans(self):
        """测试是否将'NA'转换为计划plan"""

        id_to_attributes = {
            'tcga.aq.a7u7': {'Age': '55', 'Gender': 'female', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n2a',
                'Cancer_Spread': 'm0', 'Histological_Type': 'NA', 'Lymph_Nodes': '4', 'Treatment': 'plan_4'}, 
            'tcga.aq.a54o': {'Age': '51', 'Gender': 'male', 'Tumor_Size': 't2', 'Nearby_Cancer_Lymphnodes': 'n0', 
                'Cancer_Spread': 'm0', 'Histological_Type': 'h_t_2', 'Lymph_Nodes': '0', 'Treatment': 'plan_2'}, 
            'tcga.xx.a899': {'Age': '46', 'Gender': 'female', 'Tumor_Size': 't1c', 'Nearby_Cancer_Lymphnodes': 'n2a', 
                'Cancer_Spread': 'mx', 'Histological_Type': 'h_t_1', 'Lymph_Nodes': '5', 'Treatment': 'plan_4'}
        }

        new_id_to_attributes = {
            'tcga.uu.a93s':
            {'Age': '63', 'Gender': 'female', 'Tumor_Size': 't4d',
            'Nearby_Cancer_Lymphnodes': 'n3b', 'Cancer_Spread': 'm1',
            'Histological_Type': 'h_t_2', 'Lymph_Nodes': 'NA', 'Treatment': 'NA'},
            'tcga.v7.a7hq':
            {'Age': '75', 'Gender': 'female', 'Tumor_Size': 't1c',
            'Nearby_Cancer_Lymphnodes': 'n2a', 'Cancer_Spread': 'm0',
            'Histological_Type': 'h_t_2', 'Lymph_Nodes': '5', 'Treatment': 'NA'},
            'tcga.xx.a899':
            {'Age': '46', 'Gender': 'female', 'Tumor_Size': 't1c',
            'Nearby_Cancer_Lymphnodes': 'n2a', 'Cancer_Spread': 'mx',
            'Histological_Type': 'h_t_1', 'Lymph_Nodes': '5', 'Treatment': 'NA'},
        }

        expected = {
            'tcga.uu.a93s':
            {'Age': '63', 'Gender': 'female', 'Tumor_Size': 't4d',
            'Nearby_Cancer_Lymphnodes': 'n3b', 'Cancer_Spread': 'm1',
            'Histological_Type': 'h_t_2', 'Lymph_Nodes': 'NA', 'Treatment': 'plan_4'},
            'tcga.v7.a7hq':
            {'Age': '75', 'Gender': 'female', 'Tumor_Size': 't1c',
            'Nearby_Cancer_Lymphnodes': 'n2a', 'Cancer_Spread': 'm0',
            'Histological_Type': 'h_t_2', 'Lymph_Nodes': '5', 'Treatment': 'plan_4'},
            'tcga.xx.a899':
            {'Age': '46', 'Gender': 'female', 'Tumor_Size': 't1c',
            'Nearby_Cancer_Lymphnodes': 'n2a', 'Cancer_Spread': 'mx',
            'Histological_Type': 'h_t_1', 'Lymph_Nodes': '5', 'Treatment': 'plan_4'},
        }

        actual = tfs.make_treatment_plans(id_to_attributes, new_id_to_attributes)
        msg = ERROR_MESSAGE.format(expected, actual)
        self.assertEqual(expected, actual, msg)



if __name__ == '__main__':
    unittest.main(exit=False)
