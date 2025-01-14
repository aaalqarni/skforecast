# Unit test __init__ ForecasterAutoregDirect
# ==============================================================================
import re
import pytest
import numpy as np
import pandas as pd
from skforecast.ForecasterAutoregDirect import ForecasterAutoregDirect
from sklearn.linear_model import LinearRegression


def test_init_lags_when_integer():
    """
    Test creation of attribute lags when integer is passed.
    """
    forecaster = ForecasterAutoregDirect(LinearRegression(), lags=10, steps=2)
    assert (forecaster.lags == np.arange(10) + 1).all()


def test_init_lags_when_list():
    """
    Test creation of attribute lags when list is passed.
    """
    forecaster = ForecasterAutoregDirect(LinearRegression(), lags=[1, 2, 3], steps=2)
    assert (forecaster.lags == np.array([1, 2, 3])).all()


def test_init_lags_when_range():
    """
    Test creation of attribute lags when range is passed.
    """
    forecaster = ForecasterAutoregDirect(LinearRegression(), lags=range(1, 4), steps=2)
    assert (forecaster.lags == np.array(range(1, 4))).all()


def test_init_lags_when_numpy_arange():
    """
    Test creation of attribute lags when numpy arange is passed.
    """
    forecaster = ForecasterAutoregDirect(LinearRegression(), lags=np.arange(1, 10), steps=2)
    assert (forecaster.lags == np.arange(1, 10)).all()


def test_init_exception_when_lags_is_int_lower_than_1():
    """
    Test exception is raised when lags is initialized with int lower than 1.
    """
    err_msg = re.escape('Minimum value of lags allowed is 1.')
    with pytest.raises(ValueError, match = err_msg):
        ForecasterAutoregDirect(LinearRegression(), lags=-10, steps=2)


def test_init_exception_when_lags_list_or_numpy_array_with_values_not_int():
    """
    Test exception is raised when lags is list or numpy array and element(s) are not int.
    """
    lags_list = [1, 1.5, [1, 2], range(5)]
    lags_np_array = np.array([1.2, 1.5])
    err_msg = re.escape('All values in `lags` must be int.')
    
    for lags in [lags_list, lags_np_array]:
        with pytest.raises(TypeError, match = err_msg):
            ForecasterAutoregDirect(LinearRegression(), lags=lags, steps=2)

 
def test_init_exception_when_lags_has_values_lower_than_1():
    """
    Test exception is raised when lags is initialized with any value lower than 1.
    """
    err_msg = re.escape('Minimum value of lags allowed is 1.')
    for lags in [[0, 1], range(0, 2), np.arange(0, 2)]:
        with pytest.raises(ValueError, match = err_msg):
            ForecasterAutoregDirect(LinearRegression(), lags=lags, steps=2)


def test_init_exception_when_lags_is_not_valid_type():
    """
    Test exception is raised when lags is not a valid type.
    """
    lags = 'not_valid_type'
    err_msg = re.escape(
                f"`lags` argument must be int, 1d numpy ndarray, range or list. "
                f"Got {type(lags)}"
            )
    with pytest.raises(TypeError, match = err_msg):
        ForecasterAutoregDirect(LinearRegression(), lags=lags, steps=2)