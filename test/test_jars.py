from co.deability.jars.service import analytics_service


def test_r_script_validator():
    assert analytics_service.validate("x<-0; print(x);") == True
    assert analytics_service.validate("foobarFIZZBUZZ") == False
