from .base_datatype import BaseDatatype


class UINT(BaseDatatype):
    """Class to implement UINT datatype of CIP especification.

    """ 

    id_code = 0xC7
    min_value = 0x00
    max_value = 0xFFFF

    @classmethod
    def Encode(cls, value):
        """ Encode a value in a byte array

        Parameters
        -----------
        value: int range from -2^64 to 2^64-1
            Value to encode

        Return
        -------
        Byte Array --  Encode value in a byte array to send trough a network

        """
        buffer = None
        if cls.ValidateValue(value):
            buffer = value.to_byte(2, 'litle')
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

        if len(buffer) == 2:
            value = int.from_bytes(buffer, 'litle', signed=False)
            return value
        else:
            raise Exception('buffer length mitsmatch with uint encoding')