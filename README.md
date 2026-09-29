# Haversine

Compute the great-circle distance between two points on Earth given their latitude and longitude in degrees.

```python
from haversine import haversine_distance

# Distance from Paris to London in kilometers
d = haversine_distance(48.8566, 2.3522, 51.5074, -0.1278)
print(d)  # ~343.5
```

## Why this exists

Geographic coordinates are angular measurements on a sphere. Simple Euclidean distance on latitude/longitude values is meaningless because a degree of longitude shrinks toward the poles. The haversine formula gives the correct shortest path over the sphere's surface using only trigonometry, and it remains numerically stable for very small distances where the spherical law of cosines loses precision.

The implementation uses the Earth's mean radius of 6371.0088 km. This treats the Earth as a perfect sphere, which is accurate to about 0.5% compared to a reference ellipsoid. That trade-off keeps the code simple and dependency-free while being sufficient for most non-surveying applications.

## Edge cases

Latitudes must be in [-90, 90] and longitudes in [-180, 180]. Values outside these ranges raise a `ValueError`. The distance between identical points is exactly `0.0`.

## API

### `haversine_distance(lat1, lon1, lat2, lon2)`

Returns the distance in kilometers as a non-negative float.

- `lat1`, `lon1`: coordinates of the first point in degrees.
- `lat2`, `lon2`: coordinates of the second point in degrees.

## Performance

The window keeps a bounded buffer, so `push` is constant time and memory does not
grow with the length of the stream. `peak` and `trough` are linear in the window
size, which is the trade that keeps `push` cheap.

## Limitations

Values are coerced to floats, so very large integers lose precision. If you need
exact integer aggregates over a window, this is the wrong tool.

