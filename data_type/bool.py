from .base_datatype import BaseDatatype


class BOOL(BaseDatatype):
    """
    Class to implement BOOL datatype of CIP especification.

    ...

    Atributes:
    ----------
    class _id_code
    class _min_value
    class _max_value


    Methods
    -------
    class Encode

    class Decode
    """ 

    _id_code = 0xC1
    _min_value = 0 
    _max_value = 1

    @classmethod
    def Encode(cls, value):
        """ Encode a value in a byte array

        Parameters
        -----------
        value: int
            Value to encode

        Return
        -------
        Byte Array --  Encoded value in a byte array to send through a network

        """
        if isinstance(value, int):
            buffer = None
            if cls.ValidateValue(value):
                if value == 1:
                    buffer = bytes([1])
                else:
                    buffer = bytes([0])
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
        value : boolean
            Encoded value in the byte array received

        """
        if isinstance(buffer, bytes):

            value = None

            if len(buffer) == 1:

                if buffer[0] & 0x01 == 1:
                    value = True
                else:
                    value = False
                return value
            else:
                raise ValueError('buffer length mitsmatch with BOOL encoding')
        else:
            raise TypeError('buffer must be bytes')
    
