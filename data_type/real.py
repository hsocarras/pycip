from .base_datatype import BaseDatatype
import struct

class REAL(BaseDatatype):
    """Class to implement REAL datatype of CIP especification.

    Methods
    -------
    class encode

    class decode

    classmethod validate_range

    classmethod get_id_code

    staticmethod identify

    """ 

    _id_code = 0xCA
    _min_value = -3.4e+38
    _max_value = 3.4e+38

    @classmethod
    def encode(cls, value):
        """ encode a value in a byte array

        Parameters
        -----------
        value: float
            Value to encode

        Return
        -------
        Byte Array --  encode value in a byte array to send trough a network

        """
        if isinstance(value, int) or isinstance(value, float):
            buffer = None
            if cls.validate_range(value, integer = False):
                buffer = struct.pack('<f', value)
                return buffer
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be a number')

        

    @classmethod
    def decode(cls, buffer):
        """ decode a value from a byte array

        Parameters
        -----------
        buffer: byte array
            buffer to decode

        Return
        -------
        value : float
            decode value from a byte array received trough a network

        """
        if isinstance(buffer, bytes):
            value = None

            if len(buffer) == 4:
                value = struct.unpack('<f', buffer)
                return round(value[0], 5)
            else:
                raise ValueError('buffer length mitsmatch with REAL encoding')
        else:
            raise TypeError('buffer must be bytes')