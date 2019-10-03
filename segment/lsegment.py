

class LogicalSegment:
    def __init__(self, logical_type = 0, logical_format = 0):

        self.type = 0x01

        self.logical_type = 0
        self.set_logical_type(logical_type)

        self.logical_format = 0
        self.set_logical_format(logical_format)

        #bytes type for segment value
        self._logical_value = 0

    def _set_value(self, value):
        """ Set the logical segment's value

        Parameters
        -----------

        value: integer or bytes 
            int for ids
            bytes for electronic-key         

        """
        if isinstance(value, int):
            if self.logical_type != 5:
                if self.logical_format == 0:
                    self._logical_value = value.to_bytes(1, 'little')
                elif self.logical_format == 1:
                    self._logical_value = value.to_bytes(2, 'little')
                else:
                    self._logical_value = value.to_bytes(4, 'little')
            else:
                raise TypeError('invalid electronic-key')
        elif isinstance(value, bytes):
            if len(value) == 9 and value[0] == 4:
                self._logical_value = value
            else:
                raise ValueError('invalid electronic-key')
        else:
            raise TypeError('arguments should be a int or bytes')


    def _get_value(self):
        """ get the logical segment's value

        Return
        -----------

        logical_value: bytes                   

        """
        if self.logical_type != 5:            
            return int.from_bytes(self._logical_value, 'little', signed=False)            
        else:
            electronic_key = {}
            if self._logical_value == 0:
                return electronic_key
            else:
                electronic_key = {
                 'vendor_id': int.from_bytes(self._logical_value[1:3], 'little', signed=False),
                 'device_type': int.from_bytes(self._logical_value[3:5], 'little', signed=False),
                 'product_code': int.from_bytes(self._logical_value[5:7], 'little', signed=False),
                 'major_revision': self._logical_value[7],
                 'minor_revision': int.from_bytes(self._logical_value[8:], 'little', signed=False)
                 }
                return electronic_key

    def _del_value(self):
        del self._logical_value

    logical_value = property(_get_value, _set_value, _del_value)

    def set_logical_type(self, type):

        if isinstance(type, int):
            if type >= 0 and type <= 6:
                self.logical_type = type
            else:
                raise ValueError("logical type should be 0 to 6")
        elif isinstance(type, str):
            repo = {
                'class_id': 0,
                'instance_id' : 1,
                'member_id' : 2,
                'connection_point': 3,
                'alttribute_id': 4,
                'special': 5,
                'service_id': 6
            }
            
            if repo.get(type) != None:
                self.logical_type = repo.get(type)
            else:
                raise ValueError("Not a valid string")
        else:
            raise TypeError('argument should be a int or str')

    def set_logical_format(self, format):
        if isinstance(format, int):
            if format >= 0 and format < 3:
                if self.logical_type == 6:
                    if format == 0:
                        self.logical_format = format
                    else:
                        raise ValueError('format not allowed')
                elif self.logical_type == 5:
                    if format == 0:
                        self.logical_format = format
                    else:
                        raise ValueError('format not allowed')
                else:
                    if format == 2:                        
                        if self.logical_type == 1 or self.logical_type == 3:
                            self.logical_format = format
                        else:
                            raise ValueError('32-bits not supported')
                    else:
                        self.logical_format = format
            else:
                raise ValueError("format should be 0 to 2")
        elif isinstance(type, str):
            repo = {
                '8-bit': 0,
                'electronic-key': 0,
                '16-bit' : 1,
                '32-bit' : 2               
            }
            if repo.get(type) != None:
                if self.logical_type == 6:
                    if repo.get(format) == 0:
                        self.logical_format = repo.get(format)
                    else:
                        raise ValueError('format not allowed')
                elif self.logical_type == 5:
                    if repo.get(format) == 0:
                        self.logical_format = repo.get(format)
                    else:
                        raise ValueError('format not allowed')
                else:
                    if repo.get(format) == 2:
                        if self.logical_type == 1 and self.logical_type == 3:
                            self.logical_format = repo.get(format)
                        else:
                            raise ValueError('32-bits not supported')
                    else:
                        self.logical_format = repo.get(format)              
            else:
                raise ValueError("Not a valid string")
        else:
            raise TypeError('argument should be a int or str')

    def encode(self, padded = True):
        """ encode the logical segment

        Parameters
        -----------

        padded: boolean 
            true for padded encode
            false for packed encode     

        Return
        ------------

        buffer: bytes    

        """
        format_byte = 0x20 | ((self.logical_type << 2) & 0x1C) | (self.logical_format & 0x03)

        if self.logical_type == 5:
            buffer = format_byte.to_bytes(1, 'little') + self._logical_value
        else:
            if self.logical_format == 0:
                buffer = format_byte.to_bytes(1, 'little') + self._logical_value
            else:
                if padded:
                    padd = bytes([0])
                    buffer = format_byte.to_bytes(1, 'little') + padd + self._logical_value
                else:
                    buffer = format_byte.to_bytes(1, 'little') + self._logical_value
        return buffer

    @classmethod
    def decode(cls, buffer):
        """ encode the logical segment

        Parameters
        -----------

        buffer: bytes or bytesarray 
            true for padded encode
            false for packed encode     

        Return
        ------------

        segment: a logical segment instance   

        """
        segment_class = buffer[0] & 0xE0
        if segment_class == 0x20:
            type = (buffer[0] & 0x1C) >> 2
            format = buffer[0] & 0x03

            if type == 5:
                if buffer[0] == 0x34 and len(buffer) == 10:
                    value = buffer[1:]
                else:
                    raise ValueError('invalid segment')
            else:
                if format == 0:
                    if len(buffer) == 2:
                        value = buffer[1]
                    else:
                        raise ValueError('invalid segment')
                elif format == 1:
                    if len(buffer) == 3:
                        value = buffer[1:]
                    elif len(buffer) == 4:
                        value = buffer[2:]
                    else:
                        raise ValueError('invalid segment')
                else:
                    if len(buffer) == 5:
                        value = buffer[1:]
                    elif len(buffer) == 6:
                        value = buffer[2:]
                    else:
                        raise ValueError('invalid segment')

            segment = cls(type, format)

            if isinstance(buffer, bytes):
                segment._logical_value = value
            else:
                segment._logical_value = bytes(value)
            return segment
        else:
            raise ValueError('buffer is not a logical segment')

    @classmethod
    def calc_len(cls, buffer, padded = True):
        """ calculate the expected size of a encoded segment from firs byte

        Parameters
        -----------

        buffer: bytes or bytesarray or int
                 

        Return
        ------------

        len: int with the expected len value   

        """
        segment_class = buffer[0] & 0xE0
        if segment_class == 0x20:
            type = (buffer[0] & 0x1C) >> 2
            format = buffer[0] & 0x03

            if type == 5:
                if buffer[0] == 0x34:
                    length = 10                
            else:
                if format == 0:
                    length = 2
                elif format == 1:
                    if padded:
                        length = 4                    
                    else:
                        length = 3
                else:
                    if padded:
                        length = 6                   
                    else:
                        length = 5
            
            return length
        else:
            raise ValueError('buffer is not a logical segment')