from .base_datatype import BaseDatatype


class ULINT(BaseDatatype):
    """Class to implement ULINT datatype of CIP especification.

    Methods
    -------
    class Encode

    class Decode

    classmethod ValidateValue

    classmethod GetIDCode

    staticmethod Identify

    """ 

    _id_code = 0xC9
    _min_value = 0x00
    _max_value = 0xFFFFFFFFFFFFFFFF

    @classmethod
    def Encode(cls, value):
        """ Encode a value in a byte array

        Parameters
        -----------
        value: int range from 0 to 2^64
            Value to encode

        Return
        -------
        Byte Array --  Encode value in a byte array to send trough a network
        """
        if isinstance(value, int):
            buffer = None
            if cls.ValidateValue(value):
                buffer = value.to_bytes(8, 'little')
                return buffer
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int')

        

    @classmethod
    def Decode(cls, buffer):
        """ Decode a value from a byte array

        Parameters
        -----------
        buffer: bytes
            buffer to decode

        Return
        -------
        value : int
            Encoded value in the byte array received

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