from .base_datatype import BaseDatatype


class REAL(BaseDatatype):
    """Class to implement REAL datatype of CIP especification.

    """ 

    id_code = 0xCA
    min_value = -3.4e+38
    max_value = 3.4e+38

    @classmethod
    def Encode(cls, value):
        """ Encode a value in a byte array

        Parameters
        -----------
        value: float
            Value to encode

        Return
        -------
        Byte Array --  Encode value in a byte array to send trough a network

        """
        buffer = None
        if cls.ValidateValue(value):
            buffer = struct.pack('<f', value)
            return buffer
        else:
            raise Exception('value is not valid integer')

        

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
        value = None

        if len(buffer) == 4:
            value = struct.unpack('<f', buffer)
            return value
        else:
            raise Exception('buffer length mitsmatch with dint encoding')