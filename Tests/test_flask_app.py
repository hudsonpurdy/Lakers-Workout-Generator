import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask_app import *
from ProductionCode.datasource import DataSource
data_source = DataSource()

class testPages(unittest.TestCase):

    def test_homepage(self):
        '''Tests for correct output on homepage'''
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h1>Lakers Exercise Generator</h1>", response.data)


    def test_musclegroup_datasource(self):
        '''Tests for correct output for the datasource file searching by muscle group'''
        self.assertEqual('Landmine twist', data_source.getExerciseByMuscle('Abdominals')[0][0])
    
    
    def test_equipment_datasource(self):
        '''Tests for correct output for the datasource file searching by equipment'''
        self.assertEqual('Palms-down wrist curl over bench', data_source.getExerciseByEquipment('Barbell')[0][0])
    

    def test_error(self):
        '''Tests for 404 error. Edge case because this would not usually happen if the user read the homepage'''
        self.app = app.test_client()
        response = self.app.get('/NothingHere', follow_redirects=True)
        self.assertIn(b"Error 404! Page not found. Please navigate back to the previous page or home.", response.data)

    def test_diagram(self):
         '''Test that the diagram page is functional'''
         self.app = app.test_client()
         response = self.app.get('/diagram', follow_redirects=True)
         self.assertIn(b'<img src="https://www.kingofthegym.com/images/muscle-anatomy-chart.jpg">', response.data)
        
if __name__ == '__main__':
        unittest.main()
