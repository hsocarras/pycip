from .base_datatype import BaseDatatype


class INT(BaseDatatype):
    """Class to implement INT datatype of CIP especification.

    Methods
    -------
    class encode

    class decode

    classmethod validate_range

    classmethod get_id_code

    staticmethod identify

    """ 

    _id_code = 0xC3
    _min_value = -32768
    _max_value = 32767

    @classmethod
    def encode(cls, value):
        """ encode a value in a byte array
        
        Parameters
        -----------
        value: int
            Value to encode

        Return
        -------
        Byte Array --  encoded value in a byte array to send through a network

        """
        if isinstance(value, int):
            buffer = None
            if cls.validate_range(value):
                buffer = value.to_bytes(2, 'little', signed = True)
                return buffer
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int') 

        

    @classmethod
    def decode(cls, buffer):
        """ Decode a value from a byte array

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
            
            if len(buffer) == 2:
                value = int.from_bytes(buffer, 'little', signed=True)
                return value
            else:
                raise ValueError('buffer length mitsmatch with INT encoding')
        else:
            raise TypeError('buffer must be bytes')