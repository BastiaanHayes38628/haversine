"""Core haversine distance implementation.

The haversine formula computes the great-circle distance between two points
on a sphere given their longitudes and latitudes. This is the shortest path
over the sphere's surface, ignoring ellipsoidal flattening of the Earth.

All angles are in degrees, but the trigonometric functions require radians,
so conversion happens at the boundary of the public function. The Earth's
radius is taken as the mean radius 6371.0088 km, which is the convention used
by the IUGG and is accurate to about 0.5% compared to a reference ellipsoid.
"""

import math

EARTH_RADIUS_KM = 6371.0088


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Return the great-circle distance in kilometers between two points.

    Args:
        lat1: Latitude of the first point in degrees.
        lon1: Longitude of the first point in degrees.
        lat2: Latitude of the second point in degrees.
        lon2: Longitude of the second point in degrees.

    Returns:
        The distance in kilometers as a non-negative float.

    Raises:
        ValueError: If any latitude is outside [-90, 90] or any longitude
            is outside [-180, 180].

    Notes:
        The haversine formula is numerically stable for small distances
        compared to the spherical law of cosines, which loses precision
        when the central angle is small.
    """
    if not (-90.0 <= lat1 <= 90.0):
        raise ValueError(f"lat1 must be between -90 and 90 degrees, got {lat1}")
    if not (-90.0 <= lat2 <= 90.0):
        raise ValueError(f"lat2 must be between -90 and 90 degrees, got {lat2}")
    if not (-180.0 <= lon1 <= 180.0):
        raise ValueError(f"lon1 must be between -180 and 180 degrees, got {lon1}")
    if not (-180.0 <= lon2 <= 180.0):
        raise ValueError(f"lon2 must be between -180 and 180 degrees, got {lon2}")

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (
        math.sin(delta_phi / 2.0) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    )
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

    return EARTH_RADIUS_KM * c
