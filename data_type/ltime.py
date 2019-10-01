from .base_datatype import BaseDatatype




class LTIME(BaseDatatype):
    """Class to implement LTIME datatype of CIP especification.
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

    _id_code = 0xD7
    _min_value = -0x8000000000000000
    _max_value = 0x7FFFFFFFFFFFFFFF - 1

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
                buffer = value.to_bytes(8, 'little', signed = True)
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

            if len(buffer) == 8:
                value = int.from_bytes(buffer, 'little', signed=True)
                return value
            else:
                raise ValueError('buffer length mitsmatch with LINT encoding')
        else:
            raise TypeError('buffer must be bytes')

    @classmethod
    def to_string(cls, value):
        """ Encode a date string from  T#-106751991d04h00m54.775808s to T#106751991d04h00m54.775807s.

        Parameters
        -----------
        value: int
            value of amount of microseconds
        Return
        -------
        str: 
            String iso format starting with T# identifier

        """
        if isinstance(value, int):
            
            
            if cls.validate_range(value):               
                
                _days = int(value/86400000000)
                _rest = int(value%86400000000)
                _hours = int(_rest/3600000000)
                _rest = int(_rest%3600000000)
                _min = int(_rest/60000000)
                _rest = _rest % 60000000
                _seconds = int(_rest/1000000)                
                _micro_seconds = _rest % 1000000

                str_hours = str(_hours)
                if len(str_hours) < 2:
                    str_hours = "0" + str_hours
                
                str_min = str(_min)
                if len(str_min) < 2:
                    str_min = "0" + str_min

                str_seconds = str(_seconds)
                if len(str_seconds) < 2:
                    str_seconds = "0" + str_seconds

                str_microseconds = str(_micro_seconds)
                if len(str_microseconds) < 6:
                    pad_str = {
                        1:"00000",
                        2:"0000",
                        3:"000",
                        4:"00",
                        5:"0"
                    }
                    str_microseconds = pad_str.get(len(str_microseconds)) + str_microseconds

                return "T#" + str(_days) + 'd' + str_hours + 'h' + str_min +'m' + str_seconds + '.' + str_microseconds + 's'
            else:
                raise ValueError('value is not valid integer')
        else:
            raise TypeError('value must be int')

    @classmethod
    def from_string(cls, time_str):
        """Decode a time string from T#-106751991d04h00m54.775808s to T#106751991d04h00m54.775807s.
        Parameters
        -----------
        value: string
            String iso format startin with T# identifier
            

        Return
        -------
        dint: 
            value of amount of miliseconds from midnight

        """
        format_str = time_str[2:-1]
        
        if time_str[0:2] == "T#":

            index_days = format_str.find('d') 
            _days = int(format_str[0:index_days])

            index_hours = format_str.find('h')
            _hours = int(format_str[index_days+1:index_hours])

            index_minutes = format_str.find('m')
            _minutes = int(format_str[index_hours+1:index_minutes])

            _seconds = float(format_str[index_minutes + 1:])
            if _days < 0:
                value = _days*86400000000 - _hours*3600000000 - _minutes * 60000000 - int(_seconds*1000000)
            else:
                value = _days*86400000000 + _hours*3600000000 + _minutes * 60000000 + int(_seconds*1000000)

            if cls.validate_range(value):                
                return value
            else:
                raise ValueError('value is not valid integer')
        else:
            raise TypeError('argument string is not valid TOD type string')