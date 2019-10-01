
class BaseDatatype:
    """
    Base class of all datatype.

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
    def validate_range(cls, value, integer = True):
        """ Check if value are in allowable range

        Parameters
        -----------

        value: number
            Value to check that fit the datatype range

        Return
        -------

        Bolean
            True if is a valid value otherwise false

        """
        if integer and isinstance(value, int):
            if value >= cls._min_value and value <= cls._max_value:
                return True
            else:
                return False
        elif integer and isinstance(value, int) == False:
            return False
        else:
            if value >= cls._min_value and value <= cls._max_value:
                return True
            else:
                return False

    @classmethod
    def get_id_code(cls):
        """ Return de id code for primitive datatype on CIP

        Return
        -------
        integer -- Datatype identification code.

        """
        return cls._id_code

    @staticmethod
    def identify(id_code):
        """ Get de datatype from identification code

        Parameters
        -----------

        id_code: integer or string representing a integer
            A datatype's identification code 

        Return
        -------

        string:
            Datatype's name

        """

        #acepting string as argument
        if(isinstance(id_code, str)):
            key = int(id_code)
        elif(isinstance(id_code, int)):
            key = id_code
        else:
            raise TypeError()
        

        repo = {
            0xC1 : "BOOL",
            0xC2 : "SINT",
            0xC3 : "INT",
            0xC4 : "DINT",
            0xC5 : "LINT",
            0xC6 : "USINT",
            0xC7 : "UINT",
            0xC8 : "UDINT",
            0xC9 : "ULINT",
            0xCA : "REAL",
            0xCB : "LREAL",
            0xCC : "STIME",
            0xCD : "DATE",
            0xCE : "TOD",
            0xCF : "DT",
            0xD0 : "STRING",
            0xD1 : "BYTE",
            0xD2 : "WORD",
            0xD3 : "DWORD",
            0xD4 : "LWORD",
            0xD6 : "FTIME",
            0xD7 : "LTIME",
            0xD8 : "ITIME",
            0xDA : "SHORT_STRING",
            0xDB : "TIME",
            0xDC : "EPATH",
            0xDD : "ENGUNIT"
        }

        return repo.get(key)

    