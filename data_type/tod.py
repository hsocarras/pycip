from .base_datatype import BaseDatatype
from datetime import time



class TOD(BaseDatatype):
    """Class to implement Time of Date datatype of CIP especification.
     Methods
    -------
    class encode

    class decode

    classmethod validate_range

    classmethod get_id_code

    classmethod to_string

    classmethod from_string

    staticmethod identify

    """ 

    _id_code = 0xCE
    _min_value = 0
    _max_value = 86400000

    @classmethod
    def encode(cls, value):
        """ Encode a value in a byte array

        Parameters
        -----------
        value: int range from -32768 to 32767
            Value to encode

        Return
        -------
        Byte Array --  Encode value in a byte array to send trough a network

        """
        if isinstance(value, int):
            buffer = None
            if cls.validate_range(value):
                buffer = value.to_bytes(4, 'little', signed = False)
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
        buffer: byte array
            buffer to decode

        Return
        -------
        value : int
            Decode value from a byte array received trough a network

        """
        if isinstance(buffer, bytes):
            value = None

            if len(buffer) == 4:
                value = int.from_bytes(buffer, 'little', signed=False)
                return value
            else:
                raise ValueError('buffer length mitsmatch with int encoding')
        else:
            raise TypeError('buffer must be bytes')

    @classmethod
    def to_string(cls, value):
        """ Encode a date string from TOD#00:00:00.000 to TOD#23:59:59.999

        Parameters
        -----------
        value: int
            value of amount of miliseconds from 00:00:00

        Return
        -------
        str: 
            String iso format startin with TOD# identifier

        """
        if isinstance(value, int):
            
            
            if cls.validate_range(value):               
                _hours = int(value/3600000)                
                _rest = value % 3600000
                _min = int(_rest/60000)
                _rest = _rest % 60000
                _seg = int(_rest/1000)
                _miliseg = _rest % 1000
                _time = time(_hours, _min, _seg, _miliseg*1000)
                return "TOD#" + _time.isoformat('milliseconds')
            else:
                raise ValueError('value is not valid integer')
        else:
            raise TypeError('value must be int')

    @classmethod
    def from_string(cls, time_str):
        """Decode a time string from TOD#00:00:00.000 to TOD#23:59:59.999
        Parameters
        -----------
        value: string
            String iso format startin with TOD# identifier
            

        Return
        -------
        dint: 
            value of amount of miliseconds from midnight

        """
        format_str = time_str[4:]
        
        if time_str[0:4] == "TOD#":

            _time = time.fromisoformat(format_str)  
                  
            value = _time.hour*3600000 + _time.minute*60000 +  _time.second * 1000 + int(_time.microsecond/1000)

            if cls.validate_range(value):                
                return value
            else:
                raise ValueError('value is not valid integer')
        else:
            raise TypeError('argument string is not valid TOD type string')