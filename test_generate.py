from generate import GeneratePassword
import unittest

class TestGenerate(unittest.TestCase):
    def test_lengt(self) -> None:
        self.assertEqual(len(GeneratePassword(8).generate()), 8)
        self.assertEqual(len(GeneratePassword(9).generate()), 9)
        self.assertEqual(len(GeneratePassword(5).generate()), 5)
        self.assertEqual(len(GeneratePassword(6).generate()), 6)
        self.assertEqual(len(GeneratePassword(12).generate()), 12)
        self.assertEqual(len(GeneratePassword(120).generate()), 120)
    
    def test_velues(self) -> None:
        self.assertRaises(ValueError, GeneratePassword, -9)
        self.assertRaises(ValueError, GeneratePassword, -1)
        self.assertRaises(ValueError, GeneratePassword, 0)
        self.assertRaises(TypeError, GeneratePassword, True)
        self.assertRaises(TypeError, GeneratePassword, (1, 2, 3))
        self.assertRaises(TypeError, GeneratePassword, [1, 2, 3])
        self.assertRaises(TypeError, GeneratePassword, "ghbdtn")
        self.assertRaises(TypeError, GeneratePassword, {1: '1', 2: '2', 3:'3'})