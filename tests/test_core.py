"""Tests for the haversine core module."""

import math
import unittest

from haversine import haversine_distance


class TestHaversineDistance(unittest.TestCase):
    """Test cases for haversine_distance function."""

    def test_same_point_returns_zero(self):
        """Distance between identical coordinates is exactly zero."""
        self.assertEqual(haversine_distance(0.0, 0.0, 0.0, 0.0), 0.0)

    def test_known_distance_paris_london(self):
        """Paris to London is approximately 343.5 km (within 0.5 km)."""
        distance = haversine_distance(48.8566, 2.3522, 51.5074, -0.1278)
        self.assertAlmostEqual(distance, 343.5, delta=0.5)

    def test_known_distance_new_york_los_angeles(self):
        """NYC to LA is approximately 3940 km (within 10 km)."""
        distance = haversine_distance(40.7128, -74.0060, 34.0522, -118.2437)
        self.assertAlmostEqual(distance, 3940.0, delta=10.0)

    def test_distance_is_symmetric(self):
        """Order of arguments does not affect the distance."""
        d1 = haversine_distance(40.0, -73.0, 35.0, 135.0)
        d2 = haversine_distance(35.0, 135.0, 40.0, -73.0)
        self.assertAlmostEqual(d1, d2, places=12)

    def test_antipodal_points(self):
        """Half the circumference of the Earth (about 20015 km)."""
        distance = haversine_distance(0.0, 0.0, 0.0, 180.0)
        self.assertAlmostEqual(distance, math.pi * 6371.0088, delta=0.01)

    def test_poles_distance(self):
        """North Pole to South Pole is half the circumference."""
        distance = haversine_distance(90.0, 0.0, -90.0, 0.0)
        self.assertAlmostEqual(distance, math.pi * 6371.0088, delta=0.01)

    def test_equator_quarter_circumference(self):
        """Quarter turn along equator: 90 degrees of longitude."""
        distance = haversine_distance(0.0, 0.0, 0.0, 90.0)
        self.assertAlmostEqual(distance, (math.pi / 2.0) * 6371.0088, delta=0.01)

    def test_invalid_latitude_above_range(self):
        """Latitude greater than 90 raises ValueError."""
        with self.assertRaises(ValueError):
            haversine_distance(91.0, 0.0, 0.0, 0.0)

    def test_invalid_latitude_below_range(self):
        """Latitude less than -90 raises ValueError."""
        with self.assertRaises(ValueError):
            haversine_distance(-91.0, 0.0, 0.0, 0.0)

    def test_invalid_longitude_above_range(self):
        """Longitude greater than 180 raises ValueError."""
        with self.assertRaises(ValueError):
            haversine_distance(0.0, 181.0, 0.0, 0.0)

    def test_invalid_longitude_below_range(self):
        """Longitude less than -180 raises ValueError."""
        with self.assertRaises(ValueError):
            haversine_distance(0.0, -181.0, 0.0, 0.0)

    def test_valid_boundary_values(self):
        """Boundary latitude/longitude values are accepted."""
        # Should not raise
        haversine_distance(90.0, 180.0, -90.0, -180.0)

    def test_small_distance_positive(self):
        """A very small but nonzero separation yields a positive distance."""
        distance = haversine_distance(0.0, 0.0, 0.0, 0.0001)
        self.assertGreater(distance, 0.0)
        self.assertLess(distance, 0.02)  # about 11.1 m at equator

    def test_float_returns_float(self):
        """The return type is float."""
        result = haversine_distance(10.0, 20.0, 30.0, 40.0)
        self.assertIsInstance(result, float)
