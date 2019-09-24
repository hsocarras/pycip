from .base_datatype import BaseDatatype
from datetime import time



class TOD(BaseDatatype):
    """Class to implement Time of Date datatype of CIP especification.

    """ 

    id_code = 0xCE
    min_value = 0
    max_value = 86400000

    @classmethod
    def Encode(cls, value):
        """ Encode a value in a byte array

        Parameters
        -----------
        value: int range from -32768 to 32767
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
            raise Exception('value is not in valid range')
        

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
            value = int.from_bytes(buffer, 'litle', signed=False)
            return value
        else:
            raise Exception('buffer length mitsmatch with int encoding')

    @classmethod
    def EncodeString(value)
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
        format_str = "TOD#"
        
        
        if cls.ValidateValue(value):

            _hours = int(value/3600)
            _rest = value % 3600
            _min = int(_rest/60)
            _rest = _rest % 60
            _seg = int(_rest/60)
            _miliseg = _rest % 60
            _time = time(_hours, _min, _seg, _miliseg*1000)
            return format_str + time.toisoformat()
        else:
            raise Exception('value is not valid integer')

    @classmethod
    def DecodeString(time_str):
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

        if (time_str[0:4] == "TOD#")

        _time = time.fromisoformat(format_str)        
        value = _time.hour*3600 + _time.minute*60 + _time.second * 60 + int(_time.microsecond/1000)

            if cls.ValidateValue(value):                
                return value
            else:
                raise ValueError('value is not valid integer')
        else:
            raise ValueError('time string is not valid TOD string')