import os
import unittest
from ACME.utils import *


class TestStringMethods(unittest.TestCase):
    def test_check_file_extesion(self):
        if os.name == 'nt':
            txt_file = 'test\\data\\test_acme.txt'
        else:
            txt_file = 'test//data//test_acme.txt'

        self.assertEqual(check_file_extesion(txt_file), [('ASTRID', [('MO', '10:00', '12:00'), ('TH', '12:00', '14:00'), ('SU', '20:00',\
 '21:00')]), ('RENE', [('MO', '10:00', '12:00'), ('TU', '10:00', '12:00'), ('TH'\
, '01:00', '03:00'), ('SA', '14:00', '18:00'), ('SU', '20:00', '21:00')])])



if __name__ == '__main__':
    unittest.main()