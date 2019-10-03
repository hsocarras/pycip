
from .lsegment import LogicalSegment

class Segment:
    """
    Base class of all segment.

    ...

    Atributes:
    ----------

    none

    Methods
    -------
    classmethod validate_reange

    classmethod get_id_code

    staticmethod identify
    """ 
    

    @classmethod
    def get_segment(cls, buffer):
        """ get the segment fom a buffer

        Parameters
        -----------

        buffer: bytes or bytesarray 
                 

        Return
        ------------

        segment: a segment type instance   

        """
        segment_class = {
            0: 'Port',
            1: LogicalSegment,
            2: 'Network',
            3: 'Symbolic',
            4: 'Data',
            5: 'DataType C',
            6: 'DataType E',
            7: 'Reserved'
        }

        buffer_class = (buffer[0] & 0xE0) >> 5

        if buffer_class >= 7:
            raise TypeError('Invalid segment ')
        else:
            return segment_class.get(buffer_class).decode(buffer)
