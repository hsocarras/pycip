from .base_datatype import BaseDatatype


class UDINT(BaseDatatype):
    """Class to implement UDINT datatype of CIP especification.

    Methods
    -------
    class encode

    class decode

    classmethod validate_range

    classmethod GetIDCode

    staticmethod Identify

    """ 

    _id_code = 0xC8
    _min_value = 0x00
    _max_value = 0xFFFFFFFF

    @classmethod
    def encode(cls, value):
        """ encode a value in a byte array

        Parameters
        -----------
        value: int range from 0 to 2^32
            Value to encode

        Return
        -------
        Byte Array --  encode value in a byte array to send trough a network

        """
        if isinstance(value, int):
            buffer = None
            if cls.validate_range(value):
                buffer = value.to_bytes(4, 'little')
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

            if len(buffer) == 4:
                value = int.from_bytes(buffer, 'little', signed=False)
                return value
            else:
                raise ValueError('buffer length mitsmatch with UDINT encoding')
        else:
            raise TypeError('buffer must be bytes')