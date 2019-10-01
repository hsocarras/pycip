from .base_datatype import BaseDatatype
from .dword import DWORD


class LWORD(BaseDatatype):
    """Class to implement LWORD datatype of CIP especification.

    Methods
    -------
    class encode

    class decode

    classmethod validate_range

    classmethod get_id_code
    
    staticmethod Identify

    classmethod set_flag

    classmethod get_flag

    """ 

    _id_code = 0xD4
    _min_value = 0x00
    _max_value = 0xFFFFFFFFFFFFFFFF

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
                buffer = value.to_bytes(8, 'little')
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

            if len(buffer) == 8:
                value = int.from_bytes(buffer, 'little', signed=False)
                return value
            else:
                raise ValueError('buffer length mitsmatch with ULINT encoding')
        else:
            raise TypeError('buffer must be bytes')

    @classmethod
    def set_flag(cls, value, offset = 0, flag = True):
        """ set the boolean flag value in a byte's offset position 
        Parameters
        -----------
        value: int range from 0 to 0xFFFFFFFFFFFFFFFF
        offset: int range 0 to 63
        flag : boolean
                    

        Return
        -------
        return int

        """
        if isinstance(value, int) and isinstance(offset, int) and isinstance(flag, bool):
            
            if cls.validate_range(value):

                buffer = bytearray(value.to_bytes(8, 'little'))
               
                if offset >=0 and offset <= 31:
                    value_low = int.from_bytes(buffer[0:4], 'little', signed=False)                    
                    value_low = DWORD.set_flag(value_low, offset, flag)
                    buffer[0:4] = value_low.to_bytes(4, 'little')
                    return int.from_bytes(buffer, 'little', signed=False)
                elif offset >=32 and offset <= 63:
                    value_hight = int.from_bytes(buffer[4:], 'little', signed=False)
                    value_hight = DWORD.set_flag(value_hight, offset-32, flag)                                    
                    buffer[4:] = value_hight.to_bytes(4, 'little')                        
                    return int.from_bytes(buffer, 'little', signed=False)
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
        offset: int range 0 to 63
                 

        Return
        -------
        return int

        """
        if isinstance(value, int) and isinstance(offset, int):
            
            if cls.validate_range(value):  

                buffer = value.to_bytes(8, 'little')

                if offset >=0 and offset <= 31:
                    value_low = int.from_bytes(buffer[0:4], 'little', signed=False)
                    return DWORD.get_flag(value_low, offset)
                elif offset >=32 and offset <= 63:
                    value_hight = int.from_bytes(buffer[4:], 'little', signed=False)
                    return DWORD.get_flag(value_hight, offset - 32)
                else:
                    raise ValueError('offset is not in valid range')
                
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int')