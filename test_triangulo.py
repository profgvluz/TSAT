from triangulo import calcular_area_triangulo
import pytest
@pytest.mark.parametrize( "a, b, c, d, e,f, expected",  
    [  
        (1, 2, 4, 5, 7, 1, 10.5), 
        (0, 0, 0, 0, 0, 0, 0),  
        (1, 2, 1, 5, 1, 1, 0),  
        (1, 2, 4, 6, 7, 8, 3),
        (1, 2, 4, 6, 7, 8, 4),
    ],)  
def test_triangulo (a, b, c, d, e,f, expected):    
    assert calcular_area_triangulo(a, b, c, d, e, f) == expected 