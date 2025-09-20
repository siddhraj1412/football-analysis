def get_center_of_bbox(bbox):
    """Get the center coordinates of a bounding box"""
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int((y1+y2)/2)

# Get the width of a bounding box
def get_bbox_width(bbox):
    return bbox[2]-bbox[0]

# Get the height of a bounding box
def measure_distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

# Get the x and y distance between two points
def measure_xy_distance(p1,p2):
    return p1[0]-p2[0],p1[1]-p2[1]

# Get the foot position of a bounding box
def get_foot_position(bbox):
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int(y2)