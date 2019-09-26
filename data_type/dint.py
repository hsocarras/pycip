from .base_datatype import BaseDatatype


class DINT(BaseDatatype):
    """Class to implement DINT datatype of CIP especification.

    Methods
    -------
    class encode

    class decode

    classmethod validate_range

    classmethod get_id_code

    staticmethod identify

    """ 

    _id_code = 0xC4
    _min_value = -0x80000000
    _max_value = 0x7FFFFFFF - 1

    @classmethod
    def encode(cls, value):
        """ encode a value in a byte array

        Parameters
        -----------
        value: int range from -2^31 to 2^31-1
            Value to encode

        Return
        -------
        Byte Array --  encoded value in a byte array to send trough a network

        """
        if isinstance(value, int):
            buffer = None
            if cls.validate_range(value):
                buffer = value.to_bytes(4, 'little', signed = True)
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
                value = int.from_bytes(buffer, 'little', signed=True)
                return value
            else:
                raise ValueError('buffer length mitsmatch with DINT encoding')
        else:
            raise TypeError('buffer must be bytes')