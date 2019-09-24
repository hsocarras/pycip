'''
El script debe invocarse con el flag -m
El script debe invocarse sin .py
El script debe invocarse desde el directorio ../pcip

'''
import unittest
from ..data_type import DataType


class TestDataTypeBOOL(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing BOOL Range")                
        self.assertTrue(DataType.BOOL.ValidateValue(0))
        self.assertTrue(DataType.BOOL.ValidateValue(1))
        self.assertFalse(DataType.BOOL.ValidateValue(3))
        self.assertFalse(DataType.BOOL.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing BOOL Encode")

        #bytes encoded acording to cip 0x01 for true
        self.byte_true_encoded = bytearray(1)
        self.byte_true_encoded[0] = 0x01

        self.assertEqual(DataType.BOOL.Encode(True), self.byte_true_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.BOOL.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.BOOL.Encode(3)

    #testing Decode
    def test_Decode(self):
        print("Testing BOOL Decode")

        #bytes encoded acording to cip 0x01 for true
        byte_true_encoded = bytearray(1)
        byte_true_encoded[0] = 0x01
        byte_true_encoded = bytes(byte_true_encoded)

        self.byte_wrong_encoded = bytearray(2)
        self.byte_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.BOOL.Decode(byte_true_encoded), 1)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.BOOL.Decode(self.byte_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.BOOL.Decode(bytes(self.byte_wrong_encoded))
      
        
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing BOOL getting id_code")
        self.assertEqual(DataType.BOOL.GetIDCode(), 0xC1)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying BOOL")
        self.assertEqual(DataType.BOOL.Identify(0xC1), 'BOOL')

class TestDataTypeSINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing SINT Range")                
        self.assertTrue(DataType.SINT.ValidateValue(-128))
        self.assertTrue(DataType.SINT.ValidateValue(127))
        self.assertFalse(DataType.SINT.ValidateValue(196))
        self.assertFalse(DataType.SINT.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing SINT Encode")

        #bytes encoded acording to cip 
        sint_encoded = bytearray(1)
        sint_encoded[0] = 0xDC #-36

        self.assertEqual(DataType.SINT.Encode(-36), sint_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.SINT.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.SINT.Encode(323)

    #testing Decode
    def test_Decode(self):
        print("Testing SELF Decode")

        #bytes encoded acording to cip 0x01 for true
        sint_encoded = bytearray(1)
        sint_encoded[0] = 0xDC #-36
        sint_encoded = bytes(sint_encoded)

        sint_wrong_encoded = bytearray(2)
        sint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.SINT.Decode(sint_encoded), -36)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.SINT.Decode(sint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.SINT.Decode(bytes(sint_wrong_encoded))
      
        
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing SINT getting id_code")
        self.assertEqual(DataType.SINT.GetIDCode(), 0xC2)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying SINT")
        self.assertEqual(DataType.SINT.Identify(0xC2), 'SINT')

class TestDataTypeINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing INT Range")                
        self.assertTrue(DataType.INT.ValidateValue(-32750))
        self.assertTrue(DataType.INT.ValidateValue(30520))
        self.assertFalse(DataType.INT.ValidateValue(-652369))
        self.assertFalse(DataType.INT.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing INT Encode")

        #bytes encoded acording to cip 
        int_encoded = bytearray(2)
        int_encoded[0] = 0xE7
        int_encoded[1] = 0x9C #-25369

        self.assertEqual(DataType.INT.Encode(-25369), int_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.INT.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.INT.Encode(3230365)

    #testing Decode
    def test_Decode(self):
        print("Testing INT Decode")

        #bytes encoded acording to cip 
        int_encoded = bytearray(2)
        int_encoded[0] = 0xE7
        int_encoded[1] = 0x9C #-25369
        int_encoded = bytes(int_encoded)

        int_wrong_encoded = bytearray(3)
        int_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.INT.Decode(int_encoded), -25369)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.INT.Decode(int_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.INT.Decode(bytes(int_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing INT getting id_code")
        self.assertEqual(DataType.INT.GetIDCode(), 0xC3)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying INT")
        self.assertEqual(DataType.INT.Identify(0xC3), 'INT')
   
class TestDataTypeDINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing DINT Range")                
        self.assertTrue(DataType.DINT.ValidateValue(-3275000))
        self.assertTrue(DataType.DINT.ValidateValue(30520569))
        self.assertFalse(DataType.DINT.ValidateValue(0xADEDEFC456))
        self.assertFalse(DataType.DINT.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing DINT Encode")

        #bytes encoded acording to cip 
        dint_encoded = bytearray(4)
        dint_encoded[0] = 0xF9
        dint_encoded[1] = 0x55 
        dint_encoded[2] = 0x7C
        dint_encoded[3] = 0xFF #-8628743

        self.assertEqual(DataType.DINT.Encode(-8628743), dint_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.DINT.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DINT.Encode(323036509876554)

    #testing Decode
    def test_Decode(self):
        print("Testing INT Decode")

        #bytes encoded acording to cip 
        dint_encoded = bytearray(4)
        dint_encoded[0] = 0xF9
        dint_encoded[1] = 0x55 
        dint_encoded[2] = 0x7C
        dint_encoded[3] = 0xFF #-8628743
        dint_encoded = bytes(dint_encoded)

        dint_wrong_encoded = bytearray(5)
        dint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.DINT.Decode(dint_encoded), -8628743)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.DINT.Decode(dint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DINT.Decode(bytes(dint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing DINT getting id_code")
        self.assertEqual(DataType.DINT.GetIDCode(), 0xC4)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying DINT")
        self.assertEqual(DataType.DINT.Identify(0xC4), 'DINT')

class TestDataTypeLINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing LINT Range")                
        self.assertTrue(DataType.LINT.ValidateValue(-327505684500))
        self.assertTrue(DataType.LINT.ValidateValue(305205963269))
        self.assertFalse(DataType.LINT.ValidateValue(0xADEDEFC45689245631))
        self.assertFalse(DataType.LINT.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing LINT Encode")

        #bytes encoded acording to cip 
        lint_encoded = bytearray(8)
        lint_encoded[0] = 0x45
        lint_encoded[1] = 0xA6 
        lint_encoded[2] = 0xE9
        lint_encoded[3] = 0xD5
        lint_encoded[4] = 0xC6
        lint_encoded[5] = 0xFA 
        lint_encoded[6] = 0x00
        lint_encoded[7] = 0x00 #275731899328069

        self.assertEqual(DataType.LINT.Encode(275731899328069), lint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.LINT.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LINT.Encode(32303650987655489658745213658)

    #testing Decode
    def test_Decode(self):
        print("Testing LINT Decode")

        #bytes encoded acording to cip 
        lint_encoded = bytearray(8)
        lint_encoded[0] = 0x45
        lint_encoded[1] = 0xA6 
        lint_encoded[2] = 0xE9
        lint_encoded[3] = 0xD5
        lint_encoded[4] = 0xC6
        lint_encoded[5] = 0xFA 
        lint_encoded[6] = 0x00
        lint_encoded[7] = 0x00 #275731899328069
        lint_encoded = bytes(lint_encoded)

        lint_wrong_encoded = bytearray(9)
        lint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.LINT.Decode(lint_encoded), 275731899328069)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.LINT.Decode(lint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LINT.Decode(bytes(lint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing LINT getting id_code")
        self.assertEqual(DataType.LINT.GetIDCode(), 0xC5)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying LINT")
        self.assertEqual(DataType.LINT.Identify(0xC5), 'LINT')

class TestDataTypeUSINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing USINT Range")                
        self.assertTrue(DataType.USINT.ValidateValue(0))
        self.assertTrue(DataType.USINT.ValidateValue(127))
        self.assertFalse(DataType.USINT.ValidateValue(-6))
        self.assertFalse(DataType.USINT.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing USINT Encode")

        #bytes encoded acording to cip 
        usint_encoded = bytearray(1)
        usint_encoded[0] = 45
        

        self.assertEqual(DataType.USINT.Encode(45), usint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.USINT.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.USINT.Encode(263)

    #testing Decode
    def test_Decode(self):
        print("Testing USINT Decode")

        #bytes encoded acording to cip 
        usint_encoded = bytearray(1)
        usint_encoded[0] = 45        
        usint_encoded = bytes(usint_encoded)

        usint_wrong_encoded = bytearray(2)
        usint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.USINT.Decode(usint_encoded), 45)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.USINT.Decode(usint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.USINT.Decode(bytes(usint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing USINT getting id_code")
        self.assertEqual(DataType.USINT.GetIDCode(), 0xC6)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying USINT")
        self.assertEqual(DataType.USINT.Identify(0xC6), 'USINT')

if __name__ == '__main__':
    unittest.main() 
    