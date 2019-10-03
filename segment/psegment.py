class PortSegment:
    def __init__(self, port_identifier = 1, link_address = 0):

        self.type = 0x00

        self._extended_link_address_size = False
        
        self._port_identifier = 1
        self._extended_port_identifier = None
        self._set_port_identifier(port_identifier)

        self._link_address_size = None
        self._link_address = bytes([0])
        self._set_link_address(link_address)

       

    def _set_link_address(self, value):
        """ Set the logical segment's value

        Parameters
        -----------

        value: integer or bytes 
            int for 0 to 255
            bytes for other values       

        """
        if isinstance(value, int):
            if value <= 255:
                self._extended_link_address_size = False
                self._link_address_size = None
                self._link_address = value.to_bytes(1, 'little')
            else:
                raise ValueError('value should be a bytes if value are higer than 255')
        elif isinstance(value, bytes):
            if len(value) > 1:
                self._extended_link_address_size = True
                self._link_address_size = len(value)
                self._link_address = value
            else:
                self._extended_link_address_size = False
                self._link_address_size = None
                self._link_address = value
        else:
            raise TypeError('arguments should be a int or bytes')


    def _get_link_address(self):
        """ get the logical segment's value

        Return
        -----------

        logical_value: bytes                   

        """
        return self._link_address

    def _del_link_address(self):
        pass

    link_address = property(_get_link_address, _set_link_address, _del_link_address)

    def _set_port_identifier(self, value):

        if isinstance(value, int):
            if value > 0 and value <= 0xFFFF:
                if value <= 14:
                   self._port_identifier = value
                   self._extended_port_identifier = None
                else:
                    self._port_identifier = 15
                    self._extended_port_identifier = value
            else:
                raise ValueError('port should be 1 to 0xFFFF')
        else:
            raise TypeError('argument should be a int or str')

    def _get_port_identifier(self):
        if self._port_identifier == 15:
            return self._extended_port_identifier
        else:
            return self._port_identifier

    def _del_port_identifier(self):
        pass

    port_identifier = property(_get_port_identifier, _set_port_identifier, _del_port_identifier)

    def encode(self):
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
        if self._extended_link_address_size:
            format_byte = 0x10
        else:
            format_byte = 0x00
        format_byte = format_byte | (self._port_identifier & 0x0F)

        buffer = format_byte.to_bytes(1, 'little')

        if self._extended_link_address_size:
            buffer = buffer + self._link_address_size.to_bytes(1, 'little')

        if self._port_identifier == 15:
            buffer = buffer + self._extended_port_identifier.to_bytes(2, 'little')

        buffer = buffer + self._link_address

        if len(buffer) & 0x01: #testing odd
            buffer = buffer + bytes([0])

        return buffer

    @classmethod
    def decode(cls, buffer):
        """ encode the logical segment

        Parameters
        -----------

        buffer: bytes or bytesarray 
             

        Return
        ------------

        segment: a port segment instance   

        """
        segment_class = buffer[0] & 0xE0
        if segment_class == 0x00:
            
            port_identifier = buffer[0] & 0x0F
            
            if buffer[0] & 0x10 == 0x10:
                extended = True
            else:
                extended = False
                           

            if extended:
                link_length = buffer[1]

                if port_identifier == 15:
                    port_identifier = int.from_bytes(buffer[2:4], 'little')
                    link_address = buffer[4: 4+link_length]
                else:
                    link_address = buffer[2: 2 + link_length]
            else:
                if port_identifier == 15:
                    port_identifier = int.from_bytes(buffer[1:3], 'little')
                    link_address = buffer[3]
                else:
                    link_address = buffer[1]

            segment = cls(port_identifier, link_address)
            
            return segment
        else:
            raise ValueError('buffer is not a port segment')
        
    @classmethod
    def calc_len(cls, buffer):
        """ calculate the expected size of a encoded segment from firs byte

        Parameters
        -----------

        buffer: bytes or bytesarray or int
                 

        Return
        ------------

        len: int with the expected len value   

        """
        segment_class = buffer[0] & 0xE0
        if segment_class == 0x00:
            
            port_identifier = buffer[0] & 0x0F
            
            if buffer[0] & 0x10 == 0x10:
                extended = True
            else:
                extended = False
                           

            if extended:            
                link_length = buffer[1]
                if port_identifier == 15:
                    length = 4 + link_length
                else:
                    length = 2 + link_length
                if length & 0x01: #if length is odd
                    length = length +1
            else:
                if port_identifier == 15:
                    length = 4
                else:
                    length = 2

            return length
        else:
            raise ValueError('buffer is not a port segment')

    def __eq__(self, port_segment):
        return self.port_identifier == port_segment.port_identifier and self.link_address == port_segment.link_address