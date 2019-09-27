from .base_datatype import BaseDatatype
from .date import DATE
from .tod import TOD

class DT(BaseDatatype):
    """Class to implement Date and time datatype of CIP especification.

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

    _id_code = 0xCF

    @classmethod
    def validate_range(cls, time_value, date_value):
        if TOD.validate_range(time_value) and DATE.validate_range(date_value):
            return True
        else:
            return False

    @classmethod
    def encode(cls, time_value, date_value):
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
        try:           
            buffer_time = TOD.encode(time_value)
            buffer_date = DATE.encode(date_value)
            buffer = buffer_time + buffer_date
            return buffer
        except TypeError:
            raise TypeError('values must be int')
        except ValueError:
            raise ValueError('value is not in valid cip range')
            
        

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
            time_value = None
            date_value = None

            time_buffer = None
            date_buffer = None

            if len(buffer) == 6:

                time_buffer = buffer[0:4]
                date_buffer = buffer[4:6]

                time_value = int.from_bytes(time_buffer, 'little', signed=False)
                date_value = int.from_bytes(date_buffer, 'little', signed=False)
                
                return (time_value, date_value)
               
            else:
                raise ValueError('buffer length mitsmatch with int encoding')
        else:
            raise TypeError('buffer must be bytes')

    @classmethod
    def to_string(cls, time_value, date_value):
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
        if isinstance(date_value, int) and isinstance(time_value, int):

                        
            
            if cls.validate_range(time_value, date_value):

                time_str = TOD.to_string(time_value)
                date_str = DATE.to_string(date_value)
                return "DT#" + date_str[2:] + '-' + time_str[4:]
            else:
                raise ValueError('value is not in valid cip range')
        else:
            raise TypeError('values must be int')


    @classmethod
    def from_string(cls, dt_str):
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
        format_date_str = dt_str[3:13]
        format_time_str = dt_str[14:26]
        

        if (dt_str[0:3] == "DT#"):

            try:
                _date = DATE.from_string("D#" + format_date_str)
                _time = TOD.from_string("TOD#" + format_time_str)        
                return (_time, _date)

            except TypeError:
                raise TypeError('DATE or TOD string are not valid type')
            except ValueError:
                raise ValueError('values are not valid range')

        else:
            raise TypeError('argument string is not valid DT string')