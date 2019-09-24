from .base_datatype import BaseDatatype
from .date import DATE
from .tod import TOD

class DT(BaseDatatype):
    """Class to implement Date and time datatype of CIP especification.

    """ 

    id_code = 0xCF

    @classmethod
    def ValidateValue(time_value, date_value):
        if(TOD.ValidateValue(time_value) and DATE.ValidateValue(date_value))
            return True
        else:
            return False

    @classmethod
    def Encode(cls, time_value, date_value):
        """ Encode a value in a byte array

        Parameters
        -----------
        time_value: int see TOD range
        date_value: int see Daterange
            

        Return
        -------
        Byte Array --  Encode value in a byte array to send trough a network

        """
        buffer = None
        if cls.ValidateValue(time_value, date_value):
            buffer_time = time_value.to_byte(4, 'litle')
            buffer_date = date_value.to_byte(2, 'litle')
            buffer = buffer_time + buffer_date
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
        time_value = None
        date_value = None

        time_buffer = None
        date_buffer = None

        if len(buffer) == 6:
            time_buffer = buffer[0:4]
            date_buffer = buffer[4:6]

            time_value = int.from_bytes(time_buffer, 'litle', signed=False)
            time_value = int.from_bytes(time_buffer, 'litle', signed=False)
            if TOD.ValidateValue(time_value) and DATE.ValidateValue(date_value):
                return [time_value, date_value]
            else:
                raise Exception('invalid value')
        else:
            raise Exception('buffer length mitsmatch with int encoding')

    @classmethod
    def EncodeString(time_value, date_value)
        """ Encode a date string 

        Parameters
        -----------
        time_value: int
        
        date_value: int

        Return
        -------
        str: 
            String iso format startin with TD# identifier

        """
        format_str = "TD#"
        
        
        if cls.ValidateValue(time_value, date_value):

            time_str = TOD.EncodeString(time_value)
            date_str = DATE.EncodeString(date_value)
            return format_str + date_str + '-' + time_str
        else:
            raise Exception('value is not valid integer')

    @classmethod
    def DecodeString(dt_str):
        """Decode a date and time string
        Parameters
        -----------
        value: string
            String iso format startin with DT# identifier
            

        Return
        -------
        dint: 
            value of amount of miliseconds from midnight

        """
        date_str = time_str[3:13]
        time_str = date_str[14:23]

        if (dt_str[0:3] == "DT#")

            try:
                _date = DATE.EncodeString(date_str)
                _time = TOD.EncodeString(time_str)        

            except e:
                raise e

        else:
            raise ValueError('time string is not valid TOD string')