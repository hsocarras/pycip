from .base_datatype import BaseDatatype


class STRING(BaseDatatype):
    """Class to implement STRING datatype of CIP especification.

    Methods
    -------
    class encode

    class decode

    classmethod validate_range

    classmethod GetIDCode

    staticmethod Identify

    """ 

    _id_code = 0xD0

    @classmethod
    def validate_range(cls, value):
        if len(value) <= 0xFFFF:
            return True
        else:
            return False
    

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
        if isinstance(value, str):
            buffer = None
            char_count = len(value)
            
            if cls.validate_range(value):
                buffer = char_count.to_bytes(2, 'little', signed = False) + bytes(value, 'ascii')
                return buffer
            else:
                raise ValueError('the string is to long')
        else:
            raise TypeError('value must be str')

        

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
            char_count = int.from_bytes(buffer[0:1], 'little', signed=False)
            
            if len(buffer[2:]) == char_count:
                value = buffer[2:].decode('ascii')
                return value
            else:
                raise ValueError('buffer length mitsmatch with USINT encoding')
        else:
            raise TypeError('buffer must be bytes')