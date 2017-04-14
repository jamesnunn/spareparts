RIVER_STATIONS_TYPES = {'town': str, 'river_name': str, 'label': str,
                        'lat': float, 'lon': float, 'stage_scale_url': str,
                        'typical_low': float , 'typical_high': float,
                        'url': str}

def map_redis_response(response_dict, response_types):
    """Casts binary strings returned from Redis to the types intended.

    Both dict keys must match. response_types values must be a type or a
    callable.
    """
    out_dict = {}
    for k, v in response_dict.items():
        val = v.decode('ascii')
        if val == 'None':
            converted_val = None
        else:
            converted_val = response_types[k.decode('ascii')](val)

        out_dict[k.decode('ascii')] = converted_val
    return out_dict
