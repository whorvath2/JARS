import pytest
from co.deability.jars.error.r_script_error import RScriptError
from co.deability.jars.service import analytics_service


def test_r_script_validator():
    assert analytics_service.validate("x<-0; print(x);") == True
    assert analytics_service.validate("foobar%FIZZBUZZ") == False


def test_r_script_runner():
    with pytest.raises(RScriptError):
        analytics_service.run("foobar%FIZZBUZZ")
    expected = "[1] 0\n"
    actual = analytics_service.run("x<-0; print(x);")
    assert actual == expected
