import numpy as np

def swing_door_trending(x, y, e, m=(25, 75)):
    _x = np.array(x)
    _y = np.array(y)
    _upper = _y[0] + e
    _lower = _y[0] - e
    max_angle_upper = 0
    max_angle_lower = 0
    keep = [0]
    for i in range(1, len(_y)):
        x_dist = _x[i] - _x[keep[-1]]
        angle_upper = 90 + np.arctan( (_y[i] - _upper)/x_dist )*180/np.pi
        angle_lower = 90 - np.arctan( (_y[i] - _lower)/x_dist )*180/np.pi
        max_angle_upper = max(max_angle_upper, angle_upper)
        max_angle_lower = max(max_angle_lower, angle_lower)
        if ((max_angle_upper + max_angle_lower >= 180) 
            | (i == (len(_y)-1))
            | (_y[i] < np.percentile(_y, m[0]))
            | (_y[i] > np.percentile(_y, m[1]))
            ):
            max_angle_upper = 0
            max_angle_lower = 0
            _upper = _y[i] + e
            _lower = _y[i] - e
            keep.append(i)
    return keep, _x[keep], _y[keep]