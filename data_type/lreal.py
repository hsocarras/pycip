from .base_datatype import BaseDatatype
import struct

class LREAL(BaseDatatype):
    """Class to implement LREAL datatype of CIP especification.

    Methods
    -------
    class Encode

    class Decode

    classmethod ValidateValue

    classmethod GetIDCode

    staticmethod Identify

    """ 

    _id_code = 0xCB
    _min_value = -1.7e+308
    _max_value = 1.7e+308

    @classmethod
    def Encode(cls, value):
        """ Encode a value in a byte array

        Parameters
        -----------
        value: double
            Value to encode

        Return
        -------
        Byte Array --  Encode value in a byte array to send trough a network

        """
        if isinstance(value, int) or isinstance(value, float):
            buffer = None
            if cls.ValidateValue(value, integer = False):
                buffer = struct.pack('<d', value)
                return buffer
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be a number')
        

    @classmethod
    def Decode(cls, buffer):
        """ Decode a value from a byte array

        Parameters
        -----------
        buffer: byte array
            buffer to decode

        Return
        -------
        value : float
            Decode value from a byte array received trough a network

        """
        if isinstance(buffer, bytes):
            value = None

            if len(buffer) == 8:
                value = struct.unpack('<d', buffer)
                return round(value[0], 10)
            else:
                raise ValueError('buffer length mitsmatch with lreal encoding')
        else:
            raise TypeError('buffer must be bytes')