
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

    identify = BaseDatatype.identify
