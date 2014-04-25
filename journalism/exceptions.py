#!/usr/bin/env python

class NullComputationError(Exception):
    """
    Exception raised if an illogical computation is
    attempted on a Column containing nulls.
    """
    pass

class UnsupportedOperationError(Exception):
    """
    Exception raised when an operation is applied
    to an invalid column type.
    """
    pass

class ColumnValidationError(Exception):
    """
    Exception raised in a column value can not be
    validated.

    TODO: details of what failed
    """
    pass
