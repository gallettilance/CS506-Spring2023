import io
import sys

from city import draw_city

expected = """fire station not found
hospital not found
police station not found
road not found
power plant not found
road not found
museum not found
restaurant not found
mall not found
gym not found
market not found
road not found
lake not found
park not found
tree not found
road not found
library not found
school not found
"""

def test_draw_city():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    draw_city()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == expected

