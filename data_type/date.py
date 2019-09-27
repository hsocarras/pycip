from .base_datatype import BaseDatatype
from datetime import date
from datetime import timedelta


class DATE(BaseDatatype):
    """Class to implement DATE datatype of CIP especification.

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

    _id_code = 0xCD
    _min_value = 0
    _max_value = 0xFFFF

    @classmethod
    def encode(cls, value):
        """ encode a value in a byte array

        Parameters
        -----------
        value: int range from -32768 to 32767
            Value to encode

        Return
        -------
        Byte Array --  encode value in a byte array to send trough a network

        """
        if isinstance(value, int):
            buffer = None
            if cls.validate_range(value):
                buffer = value.to_bytes(2, 'little', signed = False)
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
        buffer: byte array
            buffer to decode

        Return
        -------
        value : int
            decode value from a byte array received trough a network

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
    def to_string(cls, value):
        """ encode a date string from D#1972-01-01 to D#2151-06-06

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
            
            init_date = date(1972, 1, 1)
            if cls.validate_range(value):
                d = timedelta(days = value)
                _date = init_date + d
                return "D#" + _date.isoformat()
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('value must be int')

    @classmethod
    def from_string(cls, date_str):
        """decode a date string from D#1972-01-01 to D#2151-06-06

        Parameters
        -----------
        value: int
            value of amount of day from 1972

        Return
        -------
        str: 
            String iso format startin with D# identifier

        """
        format_str = date_str[2:] #String whithout prefixes

        if date_str[0:2] == "D#":

            init_date = date(1972, 1, 1)
            _date = date.fromisoformat(format_str)
            diff = _date - init_date
            value = int(diff.total_seconds()/86400)

            if cls.validate_range(value):            
                return value
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('argument string is not valid DATE type string')