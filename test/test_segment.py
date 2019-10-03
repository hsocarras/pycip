'''
El script debe invocarse con el flag -m
El script debe invocarse sin .py
El script debe invocarse desde el directorio ../pcip

'''
import unittest
from ..segment import segment
from ..segment import LogicalSegment
from ..segment import PortSegment

class TestSegment(unittest.TestCase):
    pass

class TestLogicalSegment(unittest.TestCase):
    def test_constructor(self):
        lseg = LogicalSegment(0, 1)

        self.assertEqual(lseg.logical_type, 0)
        self.assertEqual(lseg.logical_format, 1)
        with self.assertRaises(TypeError):
            lseg = LogicalSegment(0.1)
        with self.assertRaises(ValueError):
            lseg = LogicalSegment(7)
        with self.assertRaises(ValueError):
            lseg = LogicalSegment('class')
        with self.assertRaises(TypeError):
            lseg = LogicalSegment(0, 0.1)
        with self.assertRaises(ValueError):
            lseg = LogicalSegment(0, 7)
        with self.assertRaises(ValueError):
            lseg = LogicalSegment(6, 1)

    def test_asigment(self):
        lseg0 = LogicalSegment(0, 0)
        lseg1 = LogicalSegment(0, 1)

        with self.assertRaises(ValueError):
            lseg2 = LogicalSegment(0, 2)
        lseg2 = LogicalSegment(1, 2)

        lseg0.logical_value = 105
        self.assertEqual(lseg0._logical_value, bytes([105]))

        lseg1.logical_value = 258
        self.assertEqual(lseg1._logical_value, bytes([0x02, 0x01]))
        
        lseg2. logical_value = 1532
        self.assertEqual(lseg2._logical_value, bytes([0xFC, 0x05, 0x00, 0x00]))

        with self.assertRaises(OverflowError):
            lseg0.logical_value = 278
  
    def test_encode(self):
        lseg0 = LogicalSegment(0, 0)
        lseg1 = LogicalSegment(0, 1)
        lseg0.logical_value = 105
        lseg1.logical_value = 258

        self.assertEqual(lseg0.encode(False), bytes([0b00100000, 105]))
        self.assertEqual(lseg0.encode(True), bytes([0b00100000, 105]))

        self.assertEqual(lseg1.encode(False), bytes([0b00100001, 0x02, 0x01]))
        self.assertEqual(lseg1.encode(True), bytes([0b00100001, 0x00, 0x02, 0x01]))
    
    def test_decode(self):
        lseg = LogicalSegment.decode(bytes([0b00100001, 0x00, 0x02, 0x01]))

        self.assertEqual(lseg.logical_type, 0)
        self.assertEqual(lseg.logical_format, 1)
        self.assertEqual(lseg.logical_value, 258)

    def test_calc_len(self):
        
        self.assertEqual(LogicalSegment.calc_len(bytes([0x21]),True), 4)
        self.assertEqual(LogicalSegment.calc_len(bytes([0x21]),False), 3)

class TestPortSegment(unittest.TestCase):
    def test_constructor(self):
        pseg1 = PortSegment(2, 6)
        pseg2 = PortSegment(18, 1)
        pseg3 = PortSegment(5, bytes('130.151.137.105', 'ascii'))

        self.assertEqual(pseg2._port_identifier, 15)
        self.assertEqual(pseg2._extended_port_identifier, 18)
        self.assertEqual(pseg3._link_address_size, 15)

        with self.assertRaises(TypeError):
            pseg = PortSegment(0.1)
        with self.assertRaises(ValueError):
            pseg = PortSegment(0, 7)
        
        with self.assertRaises(TypeError):
            pseg = PortSegment(2, 0.1)
        with self.assertRaises(ValueError):
            pseg = PortSegment(2, 277)
   
    def test_asigment(self):
        pseg1 = PortSegment(2, 6)
        pseg2 = PortSegment(18, 1)

        with self.assertRaises(ValueError):
            pseg2 = PortSegment(0, 2)
        

        self.assertEqual(pseg2._extended_port_identifier, 18)
        pseg2.port_identifier = 12
        self.assertEqual(pseg2._extended_port_identifier, None)
        self.assertEqual(pseg2._port_identifier, 12)
        
        self.assertEqual(pseg1._link_address_size, None)      
        pseg1.link_address = bytes([0x11, 0x22])
        self.assertEqual(pseg1._extended_link_address_size, True)
        self.assertEqual(pseg1._link_address_size, 2)

    def test_encode(self):
        pseg1 = PortSegment(2, 6)
        pseg2 = PortSegment(18, 1)
        pseg3 = PortSegment(5, bytes('130.151.137.105', 'ascii'))

        self.assertEqual(pseg1.encode(), bytes([0x02, 0x06]))
        self.assertEqual(pseg2.encode(), bytes([0x0F, 0x12, 0x00, 0x01]))
        self.assertEqual(pseg3.encode(), bytes([0x15, 0x0F, 0x31, 0x33, 0x30, 0x2E,
                                                0x31, 0x35, 0x31, 0x2E, 0x31, 0x33,
                                                0x37, 0x2E, 0x31, 0x30, 0x35, 0x00]))
        
    
    def test_decode(self):
        pseg1 = PortSegment(2, 6)
        pseg2 = PortSegment(18, 1)
        pseg3 = PortSegment(5, bytes('130.151.137.105', 'ascii'))       

        self.assertEqual(PortSegment.decode(bytes([0x02, 0x06])), pseg1)
        self.assertEqual(PortSegment.decode(bytes([0x0F, 0x12, 0x00, 0x01])), pseg2)

        buffer3 =bytes([0x15, 0x0F, 0x31, 0x33, 0x30, 0x2E, 0x31, 0x35, 0x31, 0x2E, 0x31, 0x33, 0x37, 0x2E, 0x31, 0x30, 0x35, 0x00])
        self.assertEqual(PortSegment.decode(buffer3), pseg3)

    def test_calc_len(self):

        buffer3 =bytes([0x15, 0x0F, 0x31, 0x33, 0x30, 0x37, 0x2E, 0x31, 0x30, 0x35, 0x00])

        self.assertEqual(PortSegment.calc_len(bytes([0x02, 0x06])), 2)
        self.assertEqual(PortSegment.calc_len(bytes([0x0F, 0x12])), 4)
        self.assertEqual(PortSegment.calc_len(buffer3), 18)



if __name__ == '__main__':
    unittest.main()