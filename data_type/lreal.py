from .base_datatype import BaseDatatype


class LREAL(BaseDatatype):
    """Class to implement LREAL datatype of CIP especification.

    """ 

    id_code = 0xCB
    min_value = -1.7e+308
    max_value = 1.7e+308

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
        buffer = None
        if cls.ValidateValue(value):
            buffer = struct.pack('<d', value)
            return buffer
        else:
            raise Exception('value is not valid number')

        

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

        if len(buffer) == 8:
            value = struct.unpack('<d', buffer)
            return value
        else:
            raise Exception('buffer length mitsmatch with lreal encoding')