import math
import geojson

R_EARTH = 6378160  # in meters

def make_grid(
    start_x: float = -93.56173,
    start_y: float = 41.54427,
    num_up: int = 10,
    num_over: int = 10,
    size: float = 1.0,
) -> geojson.FeatureCollection:
    
    li = []
    for j in range(num_up):
        for i in range(num_over):
            dx = i * num_over * size 
            dy = j * num_up  * size
            new_y = start_y  + (dy / R_EARTH) * (180 /math. pi);
            new_x = start_x + (dx / R_EARTH) * (180 / math.pi) / math.cos(start_y * math.pi/180);
            li.append(geojson.Feature(geometry=geojson.Point((new_x, new_y))))
    collection = geojson.FeatureCollection(li)

    return collection

collection = make_grid()
with open('dummy.geojson', 'w') as fh:
    geojson.dump(collection, fh)
