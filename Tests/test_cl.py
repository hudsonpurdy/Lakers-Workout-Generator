import unittest
import sys
sys.path.append('../')
import subprocess

class TestClass(unittest.TestCase):

    def testMuscleGroup_OneOutput(self):
        '''Tests get exercises by muscle group with the input lower back. Input assumes one output.'''
        code = subprocess.Popen(['python3','command_line.py', '--m', "Lats"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output[4:20], 'Weighted pull-up')

    
    def testEquipmentType_OneOutput(self):
        '''Tests get exercises by equipment with the input Dumbbell. Input assumes one output.'''
        code = subprocess.Popen(['python3','command_line.py', '--e', "Body-Only"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()

        self.assertIn('Hanging Oblique Knee Raise', output)
    
    def testMuscleGroup_NAInput(self):
        '''Tests get exercises by muscle group with the input DoesNotExist. Input assumes no outputs.'''
        code = subprocess.Popen(['python3','command_line.py', '--m', "DoesNotExist"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output, '\n[]\n\n')
    
    def testInvalid(self):
        '''Tests the interface when the length of the input is 3 terms but the second one doesn't correspond to musclegroup, equipment, or help'''
        code = subprocess.Popen(['python3','command_line.py', 'DoesNotExist', "DoesNotExist"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertIn('Error: invalid command', output)

    def testHelp(self):
        '''Tests the help functionality returning the correct output'''
        code = subprocess.Popen(['python3','command_line.py', '--help'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertIn('--musclegroup (--m) for all exercises using input muscle, eg. Lats, Lower-Back', output)
    
    def testNoInput(self):
        '''Test that the command line interface responds to no input correctly'''
        code = subprocess.Popen(['python3','command_line.py'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertIn('Error: invalid input', output)

    def testManyInput(self):
        '''Test that the command line interface responds to too many inputs correctly'''
        code = subprocess.Popen(['python3','command_line.py', '1', '2', '3', '4'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertIn("Reminder: words should be separated with a hyphen '-'", output)

if __name__ == '__main__':
    unittest.main()

