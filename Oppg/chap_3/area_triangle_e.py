def area(vertices):
    x1 = vertices[0][1]; y1 = vertices[0][1]
    x2 = vertices[1][0]; y2 = vertices[1][1]
    x3 = vertices[2][0]; y3 = vertices[2][1]

    A = 0.5*abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
    return A

v1 = (0,0); v2 = (1,0); v3 = (0,2)
vertices = [v1,v2,v3]
triangle1 = area(vertices)

print 'Area of triangle is %.2f' % triangle1


def test_area():
    v1 = (15,15); v2 = (50,25); v3 = (23,30)
    vertices = [v1,v2,v3]
    exact_result = 222.5
    computed_result = area(vertices)
    tol = 1E-14    
    success = abs(exact_result - computed_result) < tol
    msg_if_failure = 'got %.3f, should have %.3f' % (computed_result, exact_result)
    assert success, msg_if_failure
test_area()
"""
Terminal> python area_triangle.py
Area of triangle is 1.00
"""

