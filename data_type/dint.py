from .base_datatype import BaseDatatype


class DINT(BaseDatatype):
    """Class to implement DINT datatype of CIP especification.

    """ 

    id_code = 0xC4
    min_value = -0x80000000
    max_value = 0x7FFFFFFF - 1

    @classmethod
    def Encode(cls, value):
        """ Encode a value in a byte array

        Parameters
        -----------
        value: int range from -2^31 to 2^31-1
            Value to encode

        Return
        -------
        Byte Array --  Encode value in a byte array to send trough a network

        """
        buffer = None
        if cls.ValidateValue(value):
            buffer = value.to_byte(4, 'litle')
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
        value : int
            Decode value from a byte array received trough a network

        """
        value = None

        if len(buffer) == 4:
            value = int.from_bytes(buffer, 'litle', signed=True)
            return value
        else:
            raise Exception('buffer length mitsmatch with dint encoding')