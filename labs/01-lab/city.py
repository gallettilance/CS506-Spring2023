from leisure.leisure import draw_leisure
from education.education import draw_education
from infrastructure import road, power, tree, hospital

def draw_city():
    power.draw_power_plant()
    road.draw_road()
    tree.draw_tree()
    draw_education()
    road.draw_road()
    draw_leisure()
    road.draw_road()
    hospital.draw_hospital()
    return

draw_city()
