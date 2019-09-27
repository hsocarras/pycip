from .base_datatype import BaseDatatype
from .byte import BYTE


class WORD(BaseDatatype):
    """Class to implement USINT datatype of CIP especification.

    Methods
    -------
    class encode

    class decode

    classmethod validate_range

    classmethod GetIDCode

    staticmethod Identify

    """ 

    _id_code = 0xD2
    _min_value = 0x00
    _max_value = 0xFFFF

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
                buffer = value.to_bytes(2, 'little')
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

            if len(buffer) == 2:
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
        value: int range from 0 to 0xFFFF
        offset: int range 0 to 15
        flag : boolean
                    

        Return
        -------
        return int

        """
        if isinstance(value, int) and isinstance(offset, int) and isinstance(flag, bool):
            
            if cls.validate_range(value):

                buffer = value.to_bytes(2, 'little')

                if offset >=0 and offset <= 7:
                    return BYTE.set_flag(buffer[0], offset, flag)
                elif offset >=8 and offset <= 15:
                    return BYTE.set_flag(buffer[1], offset - 8, flag)
                else:
                    raise ValueError('offset is nat in valid range')
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int')

    @classmethod
    def get_flag(cls, value, offset = 0):
        """ get the boolean value in a byte's offset position

        Parameters
        -----------
        value: int range from 0 to 0xFFFF
        offset: int range 0 to 15
                 

        Return
        -------
        return int

        """
        if isinstance(value, int) and isinstance(offset, int):
            
            if cls.validate_range(value):  

                buffer = value.to_bytes(2, 'little')

                if offset >=0 and offset <= 7:
                    return BYTE.get_flag(buffer[0], offset)
                elif offset >=8 and offset <= 15:
                    return BYTE.get_flag(buffer[1], offset - 8)
                else:
                    raise ValueError('offset is nat in valid range')
                
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int')