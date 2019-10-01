from .base_datatype import BaseDatatype


class BYTE(BaseDatatype):
    """Class to implement USINT datatype of CIP especification.

    Methods
    -------
    class encode

    class decode

    classmethod validate_range

    classmethod GetIDCode

    staticmethod Identify

    classmethod set_flag

    classmethod get_flag

    """ 

    _id_code = 0xD1
    _min_value = 0x00
    _max_value = 0xFF

    @classmethod
    def encode(cls, value):
        """ encode a value in a byte array

        Parameters
        -----------
        value: int range from -2^63 to 2^63-1
            Value to encode

        Return
        -------
        Byte Array --  encoded value in a byte array to send trough a network

        """
        if isinstance(value, int):
            buffer = None
            if cls.validate_range(value):
                buffer = value.to_bytes(1, 'little')
                return buffer
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int')

        

    @classmethod
    def decode(cls, buffer):
        """ decode a value from a byte array

        Parameters
        -----------
        buffer: bytes
            buffer to decode

        Return
        -------
        value : int
            encoded value in the byte array received

        """
        if isinstance(buffer, bytes):
            value = None

            if len(buffer) == 1:
                value = int.from_bytes(buffer, 'little', signed=False)
                return value
            else:
                raise ValueError('buffer length mitsmatch with USINT encoding')
        else:
            raise TypeError('buffer must be bytes')

    @classmethod
    def set_flag(cls, value, offset = 0, flag = True):
        """ set the boolean flag value in a byte's offset position 
        Parameters
        -----------
        value: int range from 0 to 255
        offset: int range 0 to 7
        flag : boolean
                    

        Return
        -------
        return int

        """
        if isinstance(value, int) and isinstance(offset, int):
            
            if cls.validate_range(value) and offset >= 0 and offset <= 7:
                if flag == True:
                    true_masks = {
                        0 : 0b00000001,
                        1 : 0b00000010,
                        2 : 0b00000100,
                        3 : 0b00001000,
                        4 : 0b00010000,
                        5 : 0b00100000,
                        6 : 0b01000000,
                        7 : 0b10000000
                    }

                    return value | true_masks.get(offset)

                elif flag == False:
                    false_masks = {
                        0 : 0b11111110,
                        1 : 0b11111101,
                        2 : 0b11111011,
                        3 : 0b11110111,
                        4 : 0b11101111,
                        5 : 0b11011111,
                        6 : 0b10111111,
                        7 : 0b01111111
                    }

                    return value & false_masks.get(offset)
                else:
                    raise ValueError('flag must be a valid boolean')
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int')

    @classmethod
    def get_flag(cls, value, offset = 0):
        """ get the boolean value in a byte's offset position

        Parameters
        -----------
        value: int range from 0 to 255
        offset: int range 0 to 7
                 

        Return
        -------
        return int

        """
        if isinstance(value, int) and isinstance(offset, int):
            
            if cls.validate_range(value) and offset >= 0 and offset <= 7:                
                true_masks = {
                    0 : 0b00000001,
                    1 : 0b00000010,
                    2 : 0b00000100,
                    3 : 0b00001000,
                    4 : 0b00010000,
                    5 : 0b00100000,
                    6 : 0b01000000,
                    7 : 0b10000000
                }

                if value & true_masks.get(offset) >= 1:
                    return True
                else:
                    return False
                
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int')