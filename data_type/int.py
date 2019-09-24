from .base_datatype import BaseDatatype


class INT(BaseDatatype):
    """Class to implement INT datatype of CIP especification.

    """ 

    _id_code = 0xC3
    _min_value = -32768
    _max_value = 32767

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
                buffer = value.to_bytes(2, 'little', signed = True)
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
        value : int
            Encoded value in the byte array received

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