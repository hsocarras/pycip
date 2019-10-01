from .base_datatype import BaseDatatype


class ITIME(BaseDatatype):
    """Class to implement ITIME datatype of CIP especification.
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

    _id_code = 0xD8
    _min_value = -32768
    _max_value = 32767

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
                value = int.from_bytes(buffer, 'little', signed=True)
                return value
            else:
                raise ValueError('buffer length mitsmatch with INT encoding')
        else:
            raise TypeError('buffer must be bytes')

    @classmethod
    def to_string(cls, value):
        """ Encode a date string from  T#-32s768ms to T#32s767ms.

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
                
                _seconds = int(value/1000)                
                _miliseconds = value % 1000

                
                str_seconds = str(_seconds)
                if len(str_seconds) < 2:
                    str_seconds = "0" + str_seconds

                str_miliseconds = str(_miliseconds)
                if len(str_miliseconds) < 3:
                    pad_str = {                       
                        1:"00",
                        2:"0"
                    }
                    str_miliseconds = pad_str.get(len(str_miliseconds)) + str_miliseconds

                return "T#" + str_seconds + 's' + str_miliseconds + 'ms'
            else:
                raise ValueError('value is not valid integer')
        else:
            raise TypeError('value must be int')

    @classmethod
    def from_string(cls, time_str):
        """Decode a time string from T#-32s768ms to T#32s767ms.
        Parameters
        -----------
        value: string
            String iso format startin with T# identifier
            

        Return
        -------
        dint: 
            value of amount of miliseconds from midnight

        """
        format_str = time_str[2:-2]
        
        if time_str[0:2] == "T#":
            
            index_seconds = format_str.find('s')
            _seconds = int(format_str[0:index_seconds])
            _miliseconds = int(format_str[index_seconds + 1:])

            if _seconds < 0:
                value = _seconds*1000 - _miliseconds
            else:
                value = _seconds*1000 + _miliseconds

            if cls.validate_range(value):                
                return value
            else:
                raise ValueError('value is not valid integer')
        else:
            raise TypeError('argument string is not valid TOD type string')