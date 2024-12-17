import line_equation

prefix_forward_command = 'G1'

def point_connect(point_number, created_point, commands):
    commands.insert(point_number + 1, prefix_forward_command + created_point.x + created_point.y)
    
