from .base_datatype import BaseDatatype
from datetime import date
from datetime import timedelta


class DATE(BaseDatatype):
    """Class to implement DATE datatype of CIP especification.

    """ 

    id_code = 0xCD
    min_value = 0
    max_value = 0xFFFF

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
            raise Exception('buffer length mitsmatch with int encoding')

    @classmethod
    def EncodeString(value)
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
        format_str = "D#"
        init_date = date(1972, 1, 1)
        if cls.ValidateValue(value):
            d = timedelta(days = value)
            date = init_date + d
            return format_str + date.toisoformat()
        else:
            raise Exception('value is not valid integer')

    @classmethod
    def DecodeString(date_str):
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
        _date = date.fromisoformat(format_str)
        diff = _date - init_date
        value = int(diff.total_seconds()/86400)

        if cls.ValidateValue(value):
            
            return value
        else:
            raise Exception('value is not valid integer')