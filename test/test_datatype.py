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
        self.assertEqual(DataType.Identify(0xC1), 'BOOL')

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
        self.assertEqual(DataType.Identify(0xC2), 'SINT')

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
        self.assertEqual(DataType.Identify(0xC3), 'INT')
   
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
        self.assertEqual(DataType.Identify(0xC4), 'DINT')

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
        self.assertEqual(DataType.Identify(0xC5), 'LINT')

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
        self.assertEqual(DataType.Identify(0xC6), 'USINT')

class TestDataTypeUINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing UINT Range")                
        self.assertTrue(DataType.UINT.ValidateValue(0))
        self.assertTrue(DataType.UINT.ValidateValue(12750))
        self.assertFalse(DataType.UINT.ValidateValue(-6))
        self.assertFalse(DataType.UINT.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing USINT Encode")

        #bytes encoded acording to cip 
        uint_encoded = bytearray(2)
        uint_encoded[0] = 0xD1
        uint_encoded[1] = 0x56      #22225 

        self.assertEqual(DataType.UINT.Encode(22225), uint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.UINT.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UINT.Encode(265693)

    #testing Decode
    def test_Decode(self):
        print("Testing USINT Decode")

        #bytes encoded acording to cip 
        uint_encoded = bytearray(2)
        uint_encoded[0] = 0xD1
        uint_encoded[1] = 0x56      #22225       
        uint_encoded = bytes(uint_encoded)

        uint_wrong_encoded = bytearray(3)
        uint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.UINT.Decode(uint_encoded), 22225)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.UINT.Decode(uint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UINT.Decode(bytes(uint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing UINT getting id_code")
        self.assertEqual(DataType.UINT.GetIDCode(), 0xC7)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying UINT")
        self.assertEqual(DataType.Identify(0xC7), 'UINT')

class TestDataTypeUDINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing UDINT Range")                
        self.assertTrue(DataType.UDINT.ValidateValue(0))
        self.assertTrue(DataType.UDINT.ValidateValue(4284967896))
        self.assertFalse(DataType.UDINT.ValidateValue(-6))
        self.assertFalse(DataType.UDINT.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing UDINT Encode")

        #bytes encoded acording to cip 
        udint_encoded = bytearray(4)
        udint_encoded[0] = 0xD1
        udint_encoded[1] = 0x56      
        udint_encoded[2] = 0xF2
        udint_encoded[3] = 0xE1      #3790755537 

        self.assertEqual(DataType.UDINT.Encode(3790755537), udint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.UDINT.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UDINT.Encode(1270256556350)

    #testing Decode
    def test_Decode(self):
        print("Testing USINT Decode")

        #bytes encoded acording to cip 
        udint_encoded = bytearray(4)
        udint_encoded[0] = 0xD1
        udint_encoded[1] = 0x56      
        udint_encoded[2] = 0xF2
        udint_encoded[3] = 0xE1      #3790755537        
        udint_encoded = bytes(udint_encoded)

        udint_wrong_encoded = bytearray(5)
        udint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.UDINT.Decode(udint_encoded), 3790755537)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.UDINT.Decode(udint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UDINT.Decode(bytes(udint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing UDINT getting id_code")
        self.assertEqual(DataType.UDINT.GetIDCode(), 0xC8)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying UDINT")
        self.assertEqual(DataType.Identify(0xC8), 'UDINT')

class TestDataTypeULINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing ULINT Range")                
        self.assertTrue(DataType.ULINT.ValidateValue(0))
        self.assertTrue(DataType.ULINT.ValidateValue(428496789896))
        self.assertFalse(DataType.ULINT.ValidateValue(-6))
        self.assertFalse(DataType.ULINT.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing ULINT Encode")

        #bytes encoded acording to cip 
        ulint_encoded = bytearray(8)
        ulint_encoded[0] = 0x78
        ulint_encoded[1] = 0x96      
        ulint_encoded[2] = 0x85
        ulint_encoded[3] = 0xF1      
        ulint_encoded[4] = 0xE8
        ulint_encoded[5] = 0xA3      
        ulint_encoded[6] = 0xC5
        ulint_encoded[7] = 0x00      #55630791291803256

        self.assertEqual(DataType.ULINT.Encode(55630791291803256), ulint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.ULINT.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.ULINT.Encode(556307912918032565698563245)

    #testing Decode
    def test_Decode(self):
        print("Testing ULINT Decode")

        ulint_encoded = bytearray(8)
        ulint_encoded[0] = 0x78
        ulint_encoded[1] = 0x96      
        ulint_encoded[2] = 0x85
        ulint_encoded[3] = 0xF1      
        ulint_encoded[4] = 0xE8
        ulint_encoded[5] = 0xA3      
        ulint_encoded[6] = 0xC5
        ulint_encoded[7] = 0x00      #55630791291803256        
        ulint_encoded = bytes(ulint_encoded)

        ulint_wrong_encoded = bytearray(9)
        ulint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.ULINT.Decode(ulint_encoded), 55630791291803256)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.ULINT.Decode(ulint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.ULINT.Decode(bytes(ulint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing ULINT getting id_code")
        self.assertEqual(DataType.ULINT.GetIDCode(), 0xC9)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying ULINT")
        self.assertEqual(DataType.Identify(0xC9), 'ULINT')

class TestDataTypeREAL(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing REAL Range")                
        self.assertTrue(DataType.REAL.ValidateValue(-23658 , integer = False))
        self.assertTrue(DataType.REAL.ValidateValue(4523.6895, integer = False))
        
    
    #testing encode
    def test_Encode(self):
        print("Testing REAL Encode")

        #bytes encoded acording to cip 
        real_encoded = bytearray(4)
        real_encoded[0] = 0xc1
        real_encoded[1] = 0xca      
        real_encoded[2] = 0x36
        real_encoded[3] = 0x42      #45.698
        

        self.assertEqual(DataType.REAL.Encode(45.698), real_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.REAL.Encode('foo')
        

    #testing Decode
    def test_Decode(self):
        print("Testing REAL Decode")

        real_encoded = bytearray(4)
        real_encoded[0] = 0xc1
        real_encoded[1] = 0xca      
        real_encoded[2] = 0x36
        real_encoded[3] = 0x42      #45.698    
        real_encoded = bytes(real_encoded)

        real_wrong_encoded = bytearray(9)
        real_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.REAL.Decode(real_encoded), 45.698 )
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.REAL.Decode(real_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.REAL.Decode(bytes(real_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing REAL getting id_code")
        self.assertEqual(DataType.REAL.GetIDCode(), 0xCA)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying REAL")
        self.assertEqual(DataType.Identify(0xCA), 'REAL')

class TestDataTypeLREAL(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing LREAL Range")                
        self.assertTrue(DataType.LREAL.ValidateValue(-236588565822324555.002589 , integer = False))
        self.assertTrue(DataType.LREAL.ValidateValue(4523.6895, integer = False))
        
    
    #testing encode
    def test_Encode(self):
        print("Testing LREAL Encode")

        #bytes encoded acording to cip 
        lreal_encoded = bytearray(8)
        lreal_encoded[0] = 0xdd
        lreal_encoded[1] = 0x41      
        lreal_encoded[2] = 0xEC
        lreal_encoded[3] = 0x4C 
        lreal_encoded[4] = 0xB1
        lreal_encoded[5] = 0xED      
        lreal_encoded[6] = 0xB1
        lreal_encoded[7] = 0xC0 #-4589.69258     
        

        self.assertEqual(DataType.LREAL.Encode(-4589.69258), lreal_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.LREAL.Encode('foo')
        

    #testing Decode
    def test_Decode(self):
        print("Testing LREAL Decode")

        lreal_encoded = bytearray(8)
        lreal_encoded[0] = 0xdd
        lreal_encoded[1] = 0x41      
        lreal_encoded[2] = 0xEC
        lreal_encoded[3] = 0x4C 
        lreal_encoded[4] = 0xB1
        lreal_encoded[5] = 0xED      
        lreal_encoded[6] = 0xB1
        lreal_encoded[7] = 0xC0 #-4589.69258   
        lreal_encoded = bytes(lreal_encoded)

        lreal_wrong_encoded = bytearray(9)
        lreal_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.LREAL.Decode(lreal_encoded), -4589.69258 )
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.LREAL.Decode(lreal_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LREAL.Decode(bytes(lreal_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing LREAL getting id_code")
        self.assertEqual(DataType.LREAL.GetIDCode(), 0xCB)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying LREAL")
        self.assertEqual(DataType.Identify(0xCB), 'LREAL')

class TestDataTypeDATE(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing UINT Range")                
        self.assertTrue(DataType.UINT.ValidateValue(0))
        self.assertTrue(DataType.UINT.ValidateValue(12750))
        self.assertFalse(DataType.UINT.ValidateValue(-6))
        self.assertFalse(DataType.UINT.ValidateValue(0.1))
    
    #testing encode
    def test_Encode(self):
        print("Testing USINT Encode")

        #bytes encoded acording to cip 
        uint_encoded = bytearray(2)
        uint_encoded[0] = 0xD1
        uint_encoded[1] = 0x56      #22225 

        self.assertEqual(DataType.UINT.Encode(22225), uint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.UINT.Encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UINT.Encode(265693)

    #testing Decode
    def test_Decode(self):
        print("Testing USINT Decode")

        #bytes encoded acording to cip 
        uint_encoded = bytearray(2)
        uint_encoded[0] = 0xD1
        uint_encoded[1] = 0x56      #22225       
        uint_encoded = bytes(uint_encoded)

        uint_wrong_encoded = bytearray(3)
        uint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.UINT.Decode(uint_encoded), 22225)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.UINT.Decode(uint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UINT.Decode(bytes(uint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_GetIDCode(self):
        print("Testing DATE getting id_code")
        self.assertEqual(DataType.DATE.GetIDCode(), 0xCD)

    #testing Identify
    def test_Identify(self):
        print("Testing Identifiying DATE")
        self.assertEqual(DataType.Identify(0xCD), 'DATE')

    #testing ToString
    def test_ToString(self):
        print("Testing DATE to string")
        self.assertEqual(DataType.DATE.ToString(25), 'D#1972-01-26')

    #testing ToString
    def test_FromString(self):
        print("Testing DATE from string")
        self.assertEqual(DataType.DATE.FromString("D#1973-01-25"), 390)


if __name__ == '__main__':
    unittest.main() 
    