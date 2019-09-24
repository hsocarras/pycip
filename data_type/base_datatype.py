
class BaseDatatype:
    """
    Base class of all datatype.

    ...

    Atributes:
    ----------

    none

    Methods
    -------
    classmethod ValidateValue

    classmethod GetIdCode

    staticmethod Identify
    """ 
    
    @classmethod
    def ValidateValue(cls, value, integer = True):
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
    def GetIDCode(cls):
        """ Return de id code for primitive datatype on CIP

        Return
        -------
        integer -- Datatype identification code.

        """
        return cls._id_code

    @staticmethod
    def Identify(id_code):
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
            0xCA : "",
            0xCB : "",
            0xCC : "",
            0xCD : "",
            0xCE : "",
            0xCF : "",
            0xD0 : ""
        }

        return repo.get(key)

    