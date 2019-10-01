
from .base_datatype import BaseDatatype
from .bool import BOOL
from .sint import SINT
from .int  import INT
from .dint import DINT
from .lint import LINT
from .usint import USINT
from .uint import UINT
from .udint import UDINT
from .ulint import ULINT
from .real import REAL
from .lreal import LREAL
from .date import DATE
from .tod import TOD
from .dt import DT
from .string import STRING
from .byte import BYTE
from .word import WORD
from .dword import DWORD
from .lword import LWORD
from .ftime import FTIME
from .ltime import LTIME
from .itime import ITIME

class DataType:
    BOOL = BOOL
    SINT = SINT 
    INT = INT
    DINT = DINT 
    LINT = LINT 
    USINT = USINT 
    UINT = UINT 
    UDINT = UDINT 
    ULINT = ULINT 
    REAL = REAL 
    LREAL = LREAL 

    DATE = DATE 
    TOD = TOD
    DT = DT 
    STRING = STRING
    BYTE = BYTE 
    WORD = WORD 
    DWORD = DWORD
    LWORD = LWORD 
    
    FTIME = FTIME
    LTIME = LTIME 
    ITIME = ITIME # not ready yet

    identify = BaseDatatype.identify
