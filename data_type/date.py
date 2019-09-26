from .base_datatype import BaseDatatype
from datetime import date
from datetime import timedelta


class DATE(BaseDatatype):
    """Class to implement DATE datatype of CIP especification.

    Methods
    -------
    class Encode

    class Decode

    classmethod ValidateValue

    classmethod GetIDCode

    classmethod ToString

    classmethod FromString

    staticmethod Identify

    """ 

    _id_code = 0xCD
    _min_value = 0
    _max_value = 0xFFFF

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
        if isinstance(value, int):
            buffer = None
            if cls.ValidateValue(value):
                buffer = value.to_bytes(2, 'little', signed = False)
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
        buffer: byte array
            buffer to decode

        Return
        -------
        value : int
            Decode value from a byte array received trough a network

        """
        if isinstance(buffer, bytes):
            value = None
            
            if len(buffer) == 2:
                value = int.from_bytes(buffer, 'little', signed=False)
                return value
            else:
                raise ValueError('buffer length mitsmatch with UINT encoding')
        else:
            raise TypeError('buffer must be bytes')

    @classmethod
    def ToString(cls, value):
        """ Encode a date string from D#1972-01-01 to D#2151-06-06

        Parameters
        -----------
        value: int
            value of amount of day from 1972

        Return
        -------
        str: 
            String iso format startin with D# identifier

        """
        if isinstance(value, int):
            format_str = "D#"
            init_date = date(1972, 1, 1)
            if cls.ValidateValue(value):
                d = timedelta(days = value)
                _date = init_date + d
                return format_str + _date.isoformat()
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int')

    @classmethod
    def FromString(cls, date_str):
        """Decode a date string from D#1972-01-01 to D#2151-06-06

        Parameters
        -----------
        value: int
            value of amount of day from 1972

        Return
        -------
        str: 
            String iso format startin with D# identifier

        """
        format_str = "D#"
        init_date = date(1972, 1, 1)
        _date = date.fromisoformat(date_str[2:])
        diff = _date - init_date
        value = int(diff.total_seconds()/86400)

        if cls.ValidateValue(value):            
            return value
        else:
            raise ValueError('value is not in valid cip range')