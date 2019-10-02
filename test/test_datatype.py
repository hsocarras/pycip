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
        self.assertTrue(DataType.BOOL.validate_range(0))
        self.assertTrue(DataType.BOOL.validate_range(1))
        self.assertFalse(DataType.BOOL.validate_range(3))
        self.assertFalse(DataType.BOOL.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing BOOL encode")

        #bytes encoded acording to cip 0x01 for true
        self.byte_true_encoded = bytearray(1)
        self.byte_true_encoded[0] = 0x01

        self.assertEqual(DataType.BOOL.encode(True), self.byte_true_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.BOOL.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.BOOL.encode(3)

    #testing decode
    def test_decode(self):
        print("Testing BOOL decode")

        #bytes encoded acording to cip 0x01 for true
        byte_true_encoded = bytearray(1)
        byte_true_encoded[0] = 0x01
        byte_true_encoded = bytes(byte_true_encoded)

        self.byte_wrong_encoded = bytearray(2)
        self.byte_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.BOOL.decode(byte_true_encoded), 1)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.BOOL.decode(self.byte_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.BOOL.decode(bytes(self.byte_wrong_encoded))
      
        
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing BOOL getting id_code")
        self.assertEqual(DataType.BOOL.get_id_code(), 0xC1)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying BOOL")
        self.assertEqual(DataType.identify(0xC1), 'BOOL')

class TestDataTypeSINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing SINT Range")                
        self.assertTrue(DataType.SINT.validate_range(-128))
        self.assertTrue(DataType.SINT.validate_range(127))
        self.assertFalse(DataType.SINT.validate_range(196))
        self.assertFalse(DataType.SINT.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing SINT encode")

        #bytes encoded acording to cip 
        sint_encoded = bytearray(1)
        sint_encoded[0] = 0xDC #-36

        self.assertEqual(DataType.SINT.encode(-36), sint_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.SINT.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.SINT.encode(323)

    #testing decode
    def test_decode(self):
        print("Testing SELF decode")

        #bytes encoded acording to cip 0x01 for true
        sint_encoded = bytearray(1)
        sint_encoded[0] = 0xDC #-36
        sint_encoded = bytes(sint_encoded)

        sint_wrong_encoded = bytearray(2)
        sint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.SINT.decode(sint_encoded), -36)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.SINT.decode(sint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.SINT.decode(bytes(sint_wrong_encoded))
      
        
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing SINT getting id_code")
        self.assertEqual(DataType.SINT.get_id_code(), 0xC2)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying SINT")
        self.assertEqual(DataType.identify(0xC2), 'SINT')

class TestDataTypeINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing INT Range")                
        self.assertTrue(DataType.INT.validate_range(-32750))
        self.assertTrue(DataType.INT.validate_range(30520))
        self.assertFalse(DataType.INT.validate_range(-652369))
        self.assertFalse(DataType.INT.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing INT encode")

        #bytes encoded acording to cip 
        int_encoded = bytearray(2)
        int_encoded[0] = 0xE7
        int_encoded[1] = 0x9C #-25369

        self.assertEqual(DataType.INT.encode(-25369), int_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.INT.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.INT.encode(3230365)

    #testing decode
    def test_decode(self):
        print("Testing INT decode")

        #bytes encoded acording to cip 
        int_encoded = bytearray(2)
        int_encoded[0] = 0xE7
        int_encoded[1] = 0x9C #-25369
        int_encoded = bytes(int_encoded)

        int_wrong_encoded = bytearray(3)
        int_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.INT.decode(int_encoded), -25369)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.INT.decode(int_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.INT.decode(bytes(int_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing INT getting id_code")
        self.assertEqual(DataType.INT.get_id_code(), 0xC3)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying INT")
        self.assertEqual(DataType.identify(0xC3), 'INT')
   
class TestDataTypeDINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing DINT Range")                
        self.assertTrue(DataType.DINT.validate_range(-3275000))
        self.assertTrue(DataType.DINT.validate_range(30520569))
        self.assertFalse(DataType.DINT.validate_range(0xADEDEFC456))
        self.assertFalse(DataType.DINT.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing DINT encode")

        #bytes encoded acording to cip 
        dint_encoded = bytearray(4)
        dint_encoded[0] = 0xF9
        dint_encoded[1] = 0x55 
        dint_encoded[2] = 0x7C
        dint_encoded[3] = 0xFF #-8628743

        self.assertEqual(DataType.DINT.encode(-8628743), dint_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.DINT.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DINT.encode(323036509876554)

    #testing decode
    def test_decode(self):
        print("Testing INT decode")

        #bytes encoded acording to cip 
        dint_encoded = bytearray(4)
        dint_encoded[0] = 0xF9
        dint_encoded[1] = 0x55 
        dint_encoded[2] = 0x7C
        dint_encoded[3] = 0xFF #-8628743
        dint_encoded = bytes(dint_encoded)

        dint_wrong_encoded = bytearray(5)
        dint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.DINT.decode(dint_encoded), -8628743)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.DINT.decode(dint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DINT.decode(bytes(dint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing DINT getting id_code")
        self.assertEqual(DataType.DINT.get_id_code(), 0xC4)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying DINT")
        self.assertEqual(DataType.identify(0xC4), 'DINT')

class TestDataTypeLINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing LINT Range")                
        self.assertTrue(DataType.LINT.validate_range(-327505684500))
        self.assertTrue(DataType.LINT.validate_range(305205963269))
        self.assertFalse(DataType.LINT.validate_range(0xADEDEFC45689245631))
        self.assertFalse(DataType.LINT.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing LINT encode")

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

        self.assertEqual(DataType.LINT.encode(275731899328069), lint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.LINT.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LINT.encode(32303650987655489658745213658)

    #testing decode
    def test_decode(self):
        print("Testing LINT decode")

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

        self.assertEqual(DataType.LINT.decode(lint_encoded), 275731899328069)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.LINT.decode(lint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LINT.decode(bytes(lint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing LINT getting id_code")
        self.assertEqual(DataType.LINT.get_id_code(), 0xC5)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying LINT")
        self.assertEqual(DataType.identify(0xC5), 'LINT')

class TestDataTypeUSINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing USINT Range")                
        self.assertTrue(DataType.USINT.validate_range(0))
        self.assertTrue(DataType.USINT.validate_range(127))
        self.assertFalse(DataType.USINT.validate_range(-6))
        self.assertFalse(DataType.USINT.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing USINT encode")

        #bytes encoded acording to cip 
        usint_encoded = bytearray(1)
        usint_encoded[0] = 45
        

        self.assertEqual(DataType.USINT.encode(45), usint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.USINT.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.USINT.encode(263)

    #testing decode
    def test_decode(self):
        print("Testing USINT decode")

        #bytes encoded acording to cip 
        usint_encoded = bytearray(1)
        usint_encoded[0] = 45        
        usint_encoded = bytes(usint_encoded)

        usint_wrong_encoded = bytearray(2)
        usint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.USINT.decode(usint_encoded), 45)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.USINT.decode(usint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.USINT.decode(bytes(usint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing USINT getting id_code")
        self.assertEqual(DataType.USINT.get_id_code(), 0xC6)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying USINT")
        self.assertEqual(DataType.identify(0xC6), 'USINT')

class TestDataTypeUINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing UINT Range")                
        self.assertTrue(DataType.UINT.validate_range(0))
        self.assertTrue(DataType.UINT.validate_range(12750))
        self.assertFalse(DataType.UINT.validate_range(-6))
        self.assertFalse(DataType.UINT.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing USINT encode")

        #bytes encoded acording to cip 
        uint_encoded = bytearray(2)
        uint_encoded[0] = 0xD1
        uint_encoded[1] = 0x56      #22225 

        self.assertEqual(DataType.UINT.encode(22225), uint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.UINT.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UINT.encode(265693)

    #testing decode
    def test_decode(self):
        print("Testing USINT decode")

        #bytes encoded acording to cip 
        uint_encoded = bytearray(2)
        uint_encoded[0] = 0xD1
        uint_encoded[1] = 0x56      #22225       
        uint_encoded = bytes(uint_encoded)

        uint_wrong_encoded = bytearray(3)
        uint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.UINT.decode(uint_encoded), 22225)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.UINT.decode(uint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UINT.decode(bytes(uint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing UINT getting id_code")
        self.assertEqual(DataType.UINT.get_id_code(), 0xC7)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying UINT")
        self.assertEqual(DataType.identify(0xC7), 'UINT')

class TestDataTypeUDINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing UDINT Range")                
        self.assertTrue(DataType.UDINT.validate_range(0))
        self.assertTrue(DataType.UDINT.validate_range(4284967896))
        self.assertFalse(DataType.UDINT.validate_range(-6))
        self.assertFalse(DataType.UDINT.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing UDINT encode")

        #bytes encoded acording to cip 
        udint_encoded = bytearray(4)
        udint_encoded[0] = 0xD1
        udint_encoded[1] = 0x56      
        udint_encoded[2] = 0xF2
        udint_encoded[3] = 0xE1      #3790755537 

        self.assertEqual(DataType.UDINT.encode(3790755537), udint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.UDINT.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UDINT.encode(1270256556350)

    #testing decode
    def test_decode(self):
        print("Testing USINT decode")

        #bytes encoded acording to cip 
        udint_encoded = bytearray(4)
        udint_encoded[0] = 0xD1
        udint_encoded[1] = 0x56      
        udint_encoded[2] = 0xF2
        udint_encoded[3] = 0xE1      #3790755537        
        udint_encoded = bytes(udint_encoded)

        udint_wrong_encoded = bytearray(5)
        udint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.UDINT.decode(udint_encoded), 3790755537)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.UDINT.decode(udint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.UDINT.decode(bytes(udint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing UDINT getting id_code")
        self.assertEqual(DataType.UDINT.get_id_code(), 0xC8)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying UDINT")
        self.assertEqual(DataType.identify(0xC8), 'UDINT')

class TestDataTypeULINT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing ULINT Range")                
        self.assertTrue(DataType.ULINT.validate_range(0))
        self.assertTrue(DataType.ULINT.validate_range(428496789896))
        self.assertFalse(DataType.ULINT.validate_range(-6))
        self.assertFalse(DataType.ULINT.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing ULINT encode")

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

        self.assertEqual(DataType.ULINT.encode(55630791291803256), ulint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.ULINT.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.ULINT.encode(556307912918032565698563245)

    #testing decode
    def test_decode(self):
        print("Testing ULINT decode")

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

        self.assertEqual(DataType.ULINT.decode(ulint_encoded), 55630791291803256)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.ULINT.decode(ulint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.ULINT.decode(bytes(ulint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing ULINT getting id_code")
        self.assertEqual(DataType.ULINT.get_id_code(), 0xC9)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying ULINT")
        self.assertEqual(DataType.identify(0xC9), 'ULINT')

class TestDataTypeREAL(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing REAL Range")                
        self.assertTrue(DataType.REAL.validate_range(-23658 , integer = False))
        self.assertTrue(DataType.REAL.validate_range(4523.6895, integer = False))
        
    
    #testing encode
    def test_encode(self):
        print("Testing REAL encode")

        #bytes encoded acording to cip 
        real_encoded = bytearray(4)
        real_encoded[0] = 0xc1
        real_encoded[1] = 0xca      
        real_encoded[2] = 0x36
        real_encoded[3] = 0x42      #45.698
        

        self.assertEqual(DataType.REAL.encode(45.698), real_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.REAL.encode('foo')
        

    #testing decode
    def test_decode(self):
        print("Testing REAL decode")

        real_encoded = bytearray(4)
        real_encoded[0] = 0xc1
        real_encoded[1] = 0xca      
        real_encoded[2] = 0x36
        real_encoded[3] = 0x42      #45.698    
        real_encoded = bytes(real_encoded)

        real_wrong_encoded = bytearray(9)
        real_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.REAL.decode(real_encoded), 45.698 )
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.REAL.decode(real_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.REAL.decode(bytes(real_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing REAL getting id_code")
        self.assertEqual(DataType.REAL.get_id_code(), 0xCA)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying REAL")
        self.assertEqual(DataType.identify(0xCA), 'REAL')

class TestDataTypeLREAL(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing LREAL Range")                
        self.assertTrue(DataType.LREAL.validate_range(-236588565822324555.002589 , integer = False))
        self.assertTrue(DataType.LREAL.validate_range(4523.6895, integer = False))
        
    
    #testing encode
    def test_encode(self):
        print("Testing LREAL encode")

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
        

        self.assertEqual(DataType.LREAL.encode(-4589.69258), lreal_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.LREAL.encode('foo')
        

    #testing decode
    def test_decode(self):
        print("Testing LREAL decode")

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

        self.assertEqual(DataType.LREAL.decode(lreal_encoded), -4589.69258 )
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.LREAL.decode(lreal_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LREAL.decode(bytes(lreal_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing LREAL getting id_code")
        self.assertEqual(DataType.LREAL.get_id_code(), 0xCB)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying LREAL")
        self.assertEqual(DataType.identify(0xCB), 'LREAL')

class TestDataTypeDATE(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing UINT Range")                
        self.assertTrue(DataType.DATE.validate_range(0))
        self.assertTrue(DataType.DATE.validate_range(12750))
        self.assertFalse(DataType.DATE.validate_range(-6))
        self.assertFalse(DataType.DATE.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing USINT encode")

        #bytes encoded acording to cip 
        date_encoded = bytearray(2)
        date_encoded[0] = 0xD1
        date_encoded[1] = 0x56      #22225 

        self.assertEqual(DataType.DATE.encode(22225), date_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.DATE.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DATE.encode(265693)

    #testing decode
    def test_decode(self):
        print("Testing USINT decode")

        #bytes encoded acording to cip 
        uint_encoded = bytearray(2)
        uint_encoded[0] = 0xD1
        uint_encoded[1] = 0x56      #22225       
        uint_encoded = bytes(uint_encoded)

        uint_wrong_encoded = bytearray(3)
        uint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.DATE.decode(uint_encoded), 22225)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.DATE.decode(uint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DATE.decode(bytes(uint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing DATE getting id_code")
        self.assertEqual(DataType.DATE.get_id_code(), 0xCD)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying DATE")
        self.assertEqual(DataType.identify(0xCD), 'DATE')

    #testing to_string
    def test_to_string(self):
        print("Testing DATE to string")
        self.assertEqual(DataType.DATE.to_string(25), 'D#1972-01-26')
        with self.assertRaises(TypeError):
            DataType.DATE.to_string(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DATE.to_string(265693)

    #testing from_string
    def test_from_string(self):
        print("Testing DATE from string")
        self.assertEqual(DataType.DATE.from_string("D#1973-01-25"), 390)
        with self.assertRaises(TypeError):
            DataType.DATE.from_string("DT#1973-01-25")
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DATE.from_string("D#2973-01-25")

class TestDataTypeTOD(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing TOD Range")                
        self.assertTrue(DataType.TOD.validate_range(0))
        self.assertTrue(DataType.TOD.validate_range(12750))
        self.assertFalse(DataType.TOD.validate_range(87450000))
        self.assertFalse(DataType.TOD.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing TOD encode")

        #bytes encoded acording to cip 
        tod_encoded = bytearray(4)
        tod_encoded[0] = 0x50
        tod_encoded[1] = 0x76 
        tod_encoded[2] = 0xF2
        tod_encoded[3] = 0x00      #15890000

        self.assertEqual(DataType.TOD.encode(15890000), tod_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.TOD.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.TOD.encode(-265693)

    #testing decode
    def test_decode(self):
        print("Testing TOD decode")

        #bytes encoded acording to cip 
        tod_encoded = bytearray(4)
        tod_encoded[0] = 0x50
        tod_encoded[1] = 0x76 
        tod_encoded[2] = 0xF2
        tod_encoded[3] = 0x00      #15890000  
        tod_encoded = bytes(tod_encoded)

        tod_wrong_encoded = bytearray(9)
        tod_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.TOD.decode(tod_encoded), 15890000)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.TOD.decode(tod_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.TOD.decode(bytes(tod_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing TOD getting id_code")
        self.assertEqual(DataType.TOD.get_id_code(), 0xCE)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying TOD")
        self.assertEqual(DataType.identify(0xCE), 'TOD')

    #testing to_string
    def test_to_string(self):
        print("Testing TOD to string")
        self.assertEqual(DataType.TOD.to_string(15890000), 'TOD#04:24:50.000')
        with self.assertRaises(TypeError):
            DataType.TOD.to_string(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.TOD.to_string(87495000)

    #testing from_string
    def test_from_string(self):
        print("Testing TOD from string")
        self.assertEqual(DataType.TOD.from_string("TOD#04:24:50.025"), 15890025)
        with self.assertRaises(TypeError):
            DataType.TOD.from_string("DT#1973-01-25")
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.TOD.from_string("TOD#24:24:50.025")

class TestDataTypeDT(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing DT Range")                
        self.assertTrue(DataType.DT.validate_range(0, 2))
        self.assertTrue(DataType.DT.validate_range(12750, 896))
        self.assertFalse(DataType.DT.validate_range(87450000, 25))
        self.assertFalse(DataType.DT.validate_range(12750, 75000))

    #testing encode
    def test_encode(self):
        print("Testing TOD encode")

        #bytes encoded acording to cip 
        tod_encoded = bytearray(4)
        tod_encoded[0] = 0x50
        tod_encoded[1] = 0x76 
        tod_encoded[2] = 0xF2
        tod_encoded[3] = 0x00      #15890000

        date_encoded = bytearray(2)
        date_encoded[0] = 0xD1
        date_encoded[1] = 0x56      #22225 

        self.assertEqual(DataType.DT.encode(15890000, 22225), bytes(tod_encoded + date_encoded))
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.DT.encode(0.1, date_encoded)
            DataType.DT.encode(tod_encoded, 0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DT.encode(-265693, 25)

    #testing decode
    def test_decode(self):
        print("Testing DT decode")

        #bytes encoded acording to cip 
        tod_encoded = bytearray(4)
        tod_encoded[0] = 0x50
        tod_encoded[1] = 0x76 
        tod_encoded[2] = 0xF2
        tod_encoded[3] = 0x00      #15890000  
       

        date_encoded = bytearray(2)
        date_encoded[0] = 0xD1
        date_encoded[1] = 0x56      #22225 
        tod_encoded = bytes(tod_encoded + date_encoded)

        tod_wrong_encoded = bytearray(9)
        tod_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.DT.decode(tod_encoded), (15890000, 22225))

        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.DT.decode(tod_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DT.decode(bytes(tod_wrong_encoded))
        

    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing DT getting id_code")
        self.assertEqual(DataType.DT.get_id_code(), 0xCF)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying DT")
        self.assertEqual(DataType.identify(0xCF), 'DT')

    #testing to_string
    def test_to_string(self):
        print("Testing DT to string")
        self.assertEqual(DataType.DT.to_string(15890000, 3), 'DT#1972-01-04-04:24:50.000')
        with self.assertRaises(TypeError):
            DataType.DT.to_string(0.1, 54)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DT.to_string(87495000, 68500)

    #testing from_string
    def test_from_string(self):
        print("Testing DT from string")
        self.assertEqual(DataType.DT.from_string("DT#1972-01-05-04:24:51.025"), (15891025, 4))
        with self.assertRaises(TypeError):
            DataType.DT.from_string("DaT#1972-1-5-04:24:51.025")
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DT.from_string("DT#1972-1-5-24:24:51.025")

class TestDataTypeSTRING(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing String Range")                
        self.assertTrue(DataType.STRING.validate_range('I love python and nodejs'))
        
    
    #testing encode
    def test_encode(self):
        print("Testing STRING encode")

        #bytes encoded acording to cip 
        str_encoded = bytearray(15)
        str_encoded[0] = 13
        str_encoded[1] = 0x00
        str_encoded[2] = 0x49
        str_encoded[3] = 0x20
        str_encoded[4] = 0x6C
        str_encoded[5] = 0x6F
        str_encoded[6] = 0x76
        str_encoded[7] = 0x65
        str_encoded[8] = 0x20
        str_encoded[9] = 0x70
        str_encoded[10] = 0x79
        str_encoded[11] = 0x74
        str_encoded[12] = 0x68
        str_encoded[13] = 0x6F
        str_encoded[14] = 0x6E
        

        self.assertEqual(DataType.STRING.encode('I love python'), str_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.STRING.encode(0.1)
        

    #testing decode
    def test_decode(self):
        print("Testing STRING decode")

       #bytes encoded acording to cip 
        str_encoded = bytearray(15)
        str_encoded[0] = 13
        str_encoded[1] = 0x00
        str_encoded[2] = 0x49
        str_encoded[3] = 0x20
        str_encoded[4] = 0x6C
        str_encoded[5] = 0x6F
        str_encoded[6] = 0x76
        str_encoded[7] = 0x65
        str_encoded[8] = 0x20
        str_encoded[9] = 0x70
        str_encoded[10] = 0x79
        str_encoded[11] = 0x74
        str_encoded[12] = 0x68
        str_encoded[13] = 0x6F
        str_encoded[14] = 0x6E      
        str_encoded = bytes(str_encoded)

        usint_wrong_encoded = bytearray(2)
        usint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.STRING.decode(str_encoded), 'I love python')
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.STRING.decode(usint_wrong_encoded)
        
        
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing STRING getting id_code")
        self.assertEqual(DataType.STRING.get_id_code(), 0xD0)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying STRING")
        self.assertEqual(DataType.identify(0xD0), 'STRING')

class TestDataTypeBYTE(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing BYTE Range")                
        self.assertTrue(DataType.BYTE.validate_range(0))
        self.assertTrue(DataType.BYTE.validate_range(127))
        self.assertFalse(DataType.BYTE.validate_range(-6))
        self.assertFalse(DataType.BYTE.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing BYTE encode")

        #bytes encoded acording to cip 
        usint_encoded = bytearray(1)
        usint_encoded[0] = 45
        

        self.assertEqual(DataType.BYTE.encode(45), usint_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.BYTE.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.BYTE.encode(263)

    #testing decode
    def test_decode(self):
        print("Testing BYTE decode")

        #bytes encoded acording to cip 
        usint_encoded = bytearray(1)
        usint_encoded[0] = 45        
        usint_encoded = bytes(usint_encoded)

        usint_wrong_encoded = bytearray(2)
        usint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.BYTE.decode(usint_encoded), 45)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.BYTE.decode(usint_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.BYTE.decode(bytes(usint_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing BYTE getting id_code")
        self.assertEqual(DataType.BYTE.get_id_code(), 0xD1)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying BYTE")
        self.assertEqual(DataType.identify(0xD1), 'BYTE')

    #testing set flag
    def test_set_flag(self):
        print("Testing set flag in BYTE")
        self.assertEqual(DataType.BYTE.set_flag(0b01011001, 2, True), 0b01011101)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.BYTE.set_flag(0.1 , 2, False)
            DataType.BYTE.set_flag(0x14 , 0.2, False)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.BYTE.set_flag(263, 5, False)
            DataType.BYTE.set_flag(0x54, 15, False)

    #testing get flag
    def test_get_flag(self):
        print("Testing get flag in BYTE")
        self.assertEqual(DataType.BYTE.get_flag(0b01011001, 4), True)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.BYTE.get_flag(0.1 , 2)
            DataType.BYTE.get_flag(0x14 , 0.2)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.BYTE.get_flag(263, 5)
            DataType.BYTE.get_flag(0x54, 15)

class TestDataTypeWORD(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing WORD Range")                
        self.assertTrue(DataType.WORD.validate_range(0))
        self.assertTrue(DataType.WORD.validate_range(12700))
        self.assertFalse(DataType.WORD.validate_range(-6))
        self.assertFalse(DataType.WORD.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing WORD encode")

        #bytes encoded acording to cip       
        word_encoded = bytearray(2)
        word_encoded[0] = 0xD1
        word_encoded[1] = 0x56      #22225 
        

        self.assertEqual(DataType.WORD.encode(22225), word_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.WORD.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.WORD.encode(68956)

    #testing decode
    def test_decode(self):
        print("Testing WORD decode")

        #bytes encoded acording to cip 
        word_encoded = bytearray(2)
        word_encoded[0] = 0xD1
        word_encoded[1] = 0x56      #22225     
        word_encoded = bytes(word_encoded)

        word_wrong_encoded = bytearray(9)
        word_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.WORD.decode(word_encoded), 22225)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.WORD.decode(word_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.WORD.decode(bytes(word_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing WORD getting id_code")
        self.assertEqual(DataType.WORD.get_id_code(), 0xD2)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying WORD")
        self.assertEqual(DataType.identify(0xD2), 'WORD')

    #testing set flag
    def test_set_flag(self):
        print("Testing set flag in WORD")
        self.assertEqual(DataType.WORD.set_flag(0b0101100111001101, 12, False), 0b0100100111001101)
        self.assertEqual(DataType.WORD.set_flag(0b0101100111001101, 1, True), 0b0101100111001111)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.WORD.set_flag(0.1 , 2, False)
            DataType.WORD.set_flag(0x14 , 0.2, False)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.WORD.set_flag(96263, 5, False)
            DataType.WORD.set_flag(0x54, 18, False)

    #testing get flag
    def test_get_flag(self):
        print("Testing get flag in WORD")
        self.assertEqual(DataType.WORD.get_flag(0b0101100111101100, 14), True)
        self.assertEqual(DataType.WORD.get_flag(0b0101100111101100, 4), False)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.WORD.get_flag(0.1 , 2)
            DataType.WORD.get_flag(0x14 , 0.2)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.WORD.get_flag(75263, 5)
            DataType.WORD.get_flag(0x5425, 17)

class TestDataTypeDWORD(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing WORD Range")                
        self.assertTrue(DataType.DWORD.validate_range(0))
        self.assertTrue(DataType.DWORD.validate_range(0xACDE1234))
        self.assertFalse(DataType.DWORD.validate_range(-6))
        self.assertFalse(DataType.DWORD.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing DWORD encode")

        #bytes encoded acording to cip 
        dword_encoded = bytearray(4)
        dword_encoded[0] = 0xD1
        dword_encoded[1] = 0x56      
        dword_encoded[2] = 0xF2
        dword_encoded[3] = 0xE1      #3790755537 

        self.assertEqual(DataType.DWORD.encode(3790755537), dword_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.DWORD.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DWORD.encode(1270256556350)

    #testing decode
    def test_decode(self):
        print("Testing DWORD decode")

        #bytes encoded acording to cip 
        dword_encoded = bytearray(4)
        dword_encoded[0] = 0xD1
        dword_encoded[1] = 0x56      
        dword_encoded[2] = 0xF2
        dword_encoded[3] = 0xE1      #3790755537        
        dword_encoded = bytes(dword_encoded)

        dword_wrong_encoded = bytearray(5)
        dword_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.DWORD.decode(dword_encoded), 3790755537)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.DWORD.decode(dword_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DWORD.decode(bytes(dword_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing DWORD getting id_code")
        self.assertEqual(DataType.DWORD.get_id_code(), 0xD3)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying DWORD")
        self.assertEqual(DataType.identify(0xD3), 'DWORD')

    #testing set flag
    def test_set_flag(self):
        print("Testing set flag in DWORD")
        self.assertEqual(DataType.DWORD.set_flag(0xD012C456, 23,True), 0xD092C456)
        self.assertEqual(DataType.DWORD.set_flag(0xD012C456, 11, True), 0xD012CC56)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.DWORD.set_flag(0.1 , 2, False)
            DataType.DWORD.set_flag(0x14 , 0.2, False)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DWORD.set_flag(0xDC12457854, 5, False)
            DataType.DWORD.set_flag(0x54, 33, False)

    #testing get flag
    def test_get_flag(self):
        print("Testing get flag in WORD")
        self.assertEqual(DataType.DWORD.get_flag(0xDC451278, 22), True)
        self.assertEqual(DataType.DWORD.get_flag(0b0101100111101100, 8), True)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.DWORD.get_flag(0.1 , 2)
            DataType.DWORD.get_flag(0x14 , 0.2)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DWORD.get_flag(0xDACDEF121, 5)
            DataType.DWORD.get_flag(0x5425, 35)

class TestDataTypeLDWORD(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing LWORD Range")                
        self.assertTrue(DataType.LWORD.validate_range(0))
        self.assertTrue(DataType.LWORD.validate_range(0xACDE12345678))
        self.assertFalse(DataType.LWORD.validate_range(-6))
        self.assertFalse(DataType.LWORD.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing LWORD encode")

        #bytes encoded acording to cip 
        lword_encoded = bytearray(8)
        lword_encoded[0] = 0x78
        lword_encoded[1] = 0x96      
        lword_encoded[2] = 0x85
        lword_encoded[3] = 0xF1      
        lword_encoded[4] = 0xE8
        lword_encoded[5] = 0xA3      
        lword_encoded[6] = 0xC5
        lword_encoded[7] = 0x00      #55630791291803256

        self.assertEqual(DataType.LWORD.encode(55630791291803256), lword_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.DWORD.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.DWORD.encode(556307912918032565698563245)

    #testing decode
    def test_decode(self):
        print("Testing ULINT decode")

        #bytes encoded acording to cip 
        lword_encoded = bytearray(8)
        lword_encoded[0] = 0x78
        lword_encoded[1] = 0x96      
        lword_encoded[2] = 0x85
        lword_encoded[3] = 0xF1      
        lword_encoded[4] = 0xE8
        lword_encoded[5] = 0xA3      
        lword_encoded[6] = 0xC5
        lword_encoded[7] = 0x00      #55630791291803256       
        lword_encoded = bytes(lword_encoded)

        lword_wrong_encoded = bytearray(9)
        lword_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.LWORD.decode(lword_encoded), 55630791291803256)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.LWORD.decode(lword_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LWORD.decode(bytes(lword_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing LWORD getting id_code")
        self.assertEqual(DataType.LWORD.get_id_code(), 0xD4)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying LWORD")
        self.assertEqual(DataType.identify(0xD4), 'LWORD')

    #testing set flag
    def test_set_flag(self):
        print("Testing set flag in LWORD")
        self.assertEqual(DataType.LWORD.set_flag(0x1012C456FE1556AD, 53, True), 0x1032C456FE1556AD)
        self.assertEqual(DataType.LWORD.set_flag(0x1012C456FE1556AD, 41, True), 0x1012C656FE1556AD)
        self.assertEqual(DataType.LWORD.set_flag(0x1012C456FE1556AD, 29,False), 0x1012C456DE1556AD)
        self.assertEqual(DataType.LWORD.set_flag(0x1012C456FE1556AD, 7, False), 0x1012C456FE15562D)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.LWORD.set_flag(0.1 , 2, False)
            DataType.LWORD.set_flag(0x14 , 0.2, False)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LWORD.set_flag(0xD012C456FE1556AD01, 5, False)
            DataType.LWORD.set_flag(0x54, 65, False)

    #testing get flag
    def test_get_flag(self):
        print("Testing get flag in WORD")
        self.assertEqual(DataType.LWORD.get_flag(0xD012C456FE1556AD, 55), False)
        self.assertEqual(DataType.LWORD.get_flag(0xD012C456FE1556AD, 41), False)
        self.assertEqual(DataType.LWORD.get_flag(0xD012C456FE1556AD, 23), False)
        self.assertEqual(DataType.LWORD.get_flag(0xD012C456FE1556AD, 10), True)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.LWORD.get_flag(0.1 , 2)
            DataType.LWORD.get_flag(0x14 , 0.2)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LWORD.get_flag(0xD012C456FE1556AD01, 5)
            DataType.LWORD.get_flag(0x5425, 305)

class TestDataTypeFTIME(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing FTIME Range")                
        self.assertTrue(DataType.FTIME.validate_range(-725869))
        self.assertTrue(DataType.FTIME.validate_range(1275058))
        self.assertFalse(DataType.FTIME.validate_range(0x1010257801))
        self.assertFalse(DataType.FTIME.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing FTIME encode")

        #bytes encoded acording to cip 
        ftime_encoded = bytearray(4)
        ftime_encoded[0] = 0xF9
        ftime_encoded[1] = 0x55 
        ftime_encoded[2] = 0x7C
        ftime_encoded[3] = 0xFF #-8628743

        self.assertEqual(DataType.FTIME.encode(-8628743), ftime_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.FTIME.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.FTIME.encode(323036509876554)

    #testing decode
    def test_decode(self):
        print("Testing INT decode")

        #bytes encoded acording to cip 
        ftime_encoded = bytearray(4)
        ftime_encoded[0] = 0xF9
        ftime_encoded[1] = 0x55 
        ftime_encoded[2] = 0x7C
        ftime_encoded[3] = 0xFF #-8628743
        ftime_encoded = bytes(ftime_encoded)

        ftime_wrong_encoded = bytearray(5)
        ftime_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.FTIME.decode(ftime_encoded), -8628743)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.FTIME.decode(ftime_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.FTIME.decode(bytes(ftime_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing FTIME getting id_code")
        self.assertEqual(DataType.FTIME.get_id_code(), 0xD6)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying Ftime")
        self.assertEqual(DataType.identify(0xD6), 'FTIME')

    #testing to_string
    def test_to_string(self):
        print("Testing FTIME to string")
        self.assertEqual(DataType.FTIME.to_string(158900000), 'T#02m38.900000s')
        with self.assertRaises(TypeError):
            DataType.FTIME.to_string(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.FTIME.to_string(323036509876554)

    #testing from_string
    def test_from_string(self):
        print("Testing FTIME from string")
        self.assertEqual(DataType.FTIME.from_string("T#-21m24.529025s"), -1284529025)
        with self.assertRaises(TypeError):
            DataType.FTIME.from_string("DT#1973-01-25")
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.FTIME.from_string("T#54m45.078025s")

class TestDataTypeLTIME(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing LTIME Range")                
        self.assertTrue(DataType.LTIME.validate_range(-327505684500))
        self.assertTrue(DataType.LTIME.validate_range(305205963269))
        self.assertFalse(DataType.LTIME.validate_range(0xADEDEFC45689245631))
        self.assertFalse(DataType.LTIME.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing LTIME encode")

        #bytes encoded acording to cip 
        ltime_encoded = bytearray(8)
        ltime_encoded[0] = 0x45
        ltime_encoded[1] = 0xA6 
        ltime_encoded[2] = 0xE9
        ltime_encoded[3] = 0xD5
        ltime_encoded[4] = 0xC6
        ltime_encoded[5] = 0xFA 
        ltime_encoded[6] = 0x00
        ltime_encoded[7] = 0x00 #275731899328069

        self.assertEqual(DataType.LTIME.encode(275731899328069), ltime_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.LTIME.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LTIME.encode(32303650987655489658745213658)

    #testing decode
    def test_decode(self):
        print("Testing LTIME decode")

        #bytes encoded acording to cip 
        ltime_encoded = bytearray(8)
        ltime_encoded[0] = 0x45
        ltime_encoded[1] = 0xA6 
        ltime_encoded[2] = 0xE9
        ltime_encoded[3] = 0xD5
        ltime_encoded[4] = 0xC6
        ltime_encoded[5] = 0xFA 
        ltime_encoded[6] = 0x00
        ltime_encoded[7] = 0x00 #275731899328069
        ltime_encoded = bytes(ltime_encoded)

        ltime_wrong_encoded = bytearray(9)
        ltime_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.LTIME.decode(ltime_encoded), 275731899328069)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.LTIME.decode(ltime_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LTIME.decode(bytes(ltime_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing LTIME getting id_code")
        self.assertEqual(DataType.LTIME.get_id_code(), 0xD7)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying LTIME")
        self.assertEqual(DataType.identify(0xD7), 'LTIME')

    #testing to_string
    def test_to_string(self):
        print("Testing LTIME to string")
        self.assertEqual(DataType.LTIME.to_string(915898965232584), 'T#10600d16h22m45.232584s')
        with self.assertRaises(TypeError):
            DataType.LTIME.to_string(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LTIME.to_string(0x123456789887654321)

    #testing from_string
    def test_from_string(self):
        print("Testing LTIME from string")
        self.assertEqual(DataType.LTIME.from_string("T#-115265d06h34m42.325810s"), -9958919682325810)
        with self.assertRaises(TypeError):
            DataType.LTIME.from_string("DT#1973-01-25")
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.LTIME.from_string("T#106751991d06h34m42.325810s")

class TestDataTypeITIME(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing ITIME Range")                
        self.assertTrue(DataType.ITIME.validate_range(-32750))
        self.assertTrue(DataType.ITIME.validate_range(30520))
        self.assertFalse(DataType.ITIME.validate_range(-652369))
        self.assertFalse(DataType.ITIME.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing ITIME encode")

        #bytes encoded acording to cip 
        itime_encoded = bytearray(2)
        itime_encoded[0] = 0xE7
        itime_encoded[1] = 0x9C #-25369

        self.assertEqual(DataType.ITIME.encode(-25369), itime_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.ITIME.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.ITIME.encode(3230365)

    #testing decode
    def test_decode(self):
        print("Testing ITIME decode")

        #bytes encoded acording to cip 
        itime_encoded = bytearray(2)
        itime_encoded[0] = 0xE7
        itime_encoded[1] = 0x9C #-25369
        itime_encoded = bytes(itime_encoded)

        itime_wrong_encoded = bytearray(3)
        itime_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.ITIME.decode(itime_encoded), -25369)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.ITIME.decode(itime_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.ITIME.decode(bytes(itime_wrong_encoded))
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing ITIME getting id_code")
        self.assertEqual(DataType.ITIME.get_id_code(), 0xD8)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying ITIME")
        self.assertEqual(DataType.identify(0xD8), 'ITIME')

    #testing to_string
    def test_to_string(self):
        print("Testing ITIME to string")
        self.assertEqual(DataType.ITIME.to_string(2584), 'T#02s584ms')
        with self.assertRaises(TypeError):
            DataType.ITIME.to_string(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.ITIME.to_string(45216)

    #testing from_string
    def test_from_string(self):
        print("Testing ITIME from string")
        self.assertEqual(DataType.ITIME.from_string("T#-22s810ms"), -22810)
        with self.assertRaises(TypeError):
            DataType.ITIME.from_string("DT#1973-01-25")
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.ITIME.from_string("T#42s155ms")

class TestDataTypeSHORTSTRING(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing ShortString Range")                
        self.assertTrue(DataType.SHORTSTRING.validate_range('I love python and nodejs'))
        
    
    #testing encode
    def test_encode(self):
        print("Testing SHORTSTRING encode")

        #bytes encoded acording to cip 
        str_encoded = bytearray(14)
        str_encoded[0] = 13        
        str_encoded[1] = 0x49
        str_encoded[2] = 0x20
        str_encoded[3] = 0x6C
        str_encoded[4] = 0x6F
        str_encoded[5] = 0x76
        str_encoded[6] = 0x65
        str_encoded[7] = 0x20
        str_encoded[8] = 0x70
        str_encoded[9] = 0x79
        str_encoded[10] = 0x74
        str_encoded[11] = 0x68
        str_encoded[12] = 0x6F
        str_encoded[13] = 0x6E
        

        self.assertEqual(DataType.SHORTSTRING.encode('I love python'), str_encoded)
        # check that  fails when the value is not int
        with self.assertRaises(TypeError):
            DataType.SHORTSTRING.encode(0.1)
        

    #testing decode
    def test_decode(self):
        print("Testing STRING decode")

       #bytes encoded acording to cip 
        str_encoded = bytearray(14)
        str_encoded[0] = 13        
        str_encoded[1] = 0x49
        str_encoded[2] = 0x20
        str_encoded[3] = 0x6C
        str_encoded[4] = 0x6F
        str_encoded[5] = 0x76
        str_encoded[6] = 0x65
        str_encoded[7] = 0x20
        str_encoded[8] = 0x70
        str_encoded[9] = 0x79
        str_encoded[10] = 0x74
        str_encoded[11] = 0x68
        str_encoded[12] = 0x6F
        str_encoded[13] = 0x6E      
        str_encoded = bytes(str_encoded)

        usint_wrong_encoded = bytearray(2)
        usint_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.SHORTSTRING.decode(str_encoded), 'I love python')
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.SHORTSTRING.decode(usint_wrong_encoded)
        
        
      
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing SHORTSTRING getting id_code")
        self.assertEqual(DataType.SHORTSTRING.get_id_code(), 0xDA)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying SHORTSTRING")
        self.assertEqual(DataType.identify(0xDA), 'SHORTSTRING')

class TestDataTypeTIME(unittest.TestCase):


    #testing Range
    def test_Range(self):
        print("Testing TIME Range")                
        self.assertTrue(DataType.TIME.validate_range(-32750857))
        self.assertTrue(DataType.TIME.validate_range(30520965))
        self.assertFalse(DataType.TIME.validate_range(-65236998563245))
        self.assertFalse(DataType.TIME.validate_range(0.1))
    
    #testing encode
    def test_encode(self):
        print("Testing TIME encode")

        #bytes encoded acording to cip 
        time_encoded = bytearray(4)
        time_encoded[0] = 0xF9
        time_encoded[1] = 0x55 
        time_encoded[2] = 0x7C
        time_encoded[3] = 0xFF #-8628743

        self.assertEqual(DataType.TIME.encode(-8628743), time_encoded)
        # check that  fails when the value is not a bulean or int
        with self.assertRaises(TypeError):
            DataType.TIME.encode(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.TIME.encode(323036509876554)

    #testing decode
    def test_decode(self):
        print("Testing TIME decode")

        #bytes encoded acording to cip 
        time_encoded = bytearray(4)
        time_encoded[0] = 0xF9
        time_encoded[1] = 0x55 
        time_encoded[2] = 0x7C
        time_encoded[3] = 0xFF #-8628743
        time_encoded = bytes(time_encoded)

        time_wrong_encoded = bytearray(5)
        time_wrong_encoded[0] = 0x01

        self.assertEqual(DataType.TIME.decode(time_encoded), -8628743)
    
        # check that  fails when the value is not a bytes 
        with self.assertRaises(TypeError):
            DataType.TIME.decode(time_wrong_encoded)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.TIME.decode(bytes(time_wrong_encoded))
 
    #testing getting ID_Code
    def test_get_id_code(self):
        print("Testing TIME getting id_code")
        self.assertEqual(DataType.TIME.get_id_code(), 0xDB)

    #testing identify
    def test_identify(self):
        print("Testing Identifiying ITIME")
        self.assertEqual(DataType.identify(0xDB), 'TIME')

    #testing to_string
    def test_to_string(self):
        print("Testing TIME to string")
        self.assertEqual(DataType.TIME.to_string(91589566), 'T#1d01h26m29.566s')
        with self.assertRaises(TypeError):
            DataType.TIME.to_string(0.1)
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.TIME.to_string(0xFFFFFFFF1)

    #testing from_string
    def test_from_string(self):
        print("Testing TIME from string")
        self.assertEqual(DataType.TIME.from_string("T#-11d12h38m11.968s"), -995891968)
        with self.assertRaises(TypeError):
            DataType.TIME.from_string("DT#1973-01-25")
        # check that  fails when the value is out of range
        with self.assertRaises(ValueError):
            DataType.TIME.from_string("T#24d20h38m11.968s")

if __name__ == '__main__':
    unittest.main() 
    