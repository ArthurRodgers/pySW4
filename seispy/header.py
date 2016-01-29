"""
- dictionaries_and_dtypes.py-

Some dictionaries and data_types for WPP and SW4 image files

By: Omri Volk & Shahar Shani-Kadmiel, June 2015, kadmiel@post.bgu.ac.il

"""
import numpy as np

# image header is 61 bytes
SW4_IMAGE_HEADER_DTYPE = np.dtype([
    ('precision', np.int32),
    ('number of patches', np.int32),
    ('time', np.float64),
    ('plane', np.int32),
    ('coordinate', np.float64),
    ('mode', np.int32),
    ('gridinfo', np.int32),
    ('creation time', 'S25')])

# patch header is 32 bytes
SW4_PATCH_HEADER_DTYPE = np.dtype([
    ('h', np.float64),
    ('zmin', np.float64),
    ('ib', np.int32),
    ('ni', np.int32),
    ('jb', np.int32),
    ('nj', np.int32)])

SW4_IMAGE_MODE_COMMON = {
    4: {'name': 'Density',
        'symbol': 'rho',
        'cmap_type': "sequential",
        'unit': 'kg/m^3'},
    5: {'name': 'Lambda',
        'symbol': 'lambda',
        'cmap_type': "sequential",
        'unit': 'Pa'},
    6: {'name': 'Mu',
        'symbol': 'mu',
        'cmap_type': "sequential",
        'unit': 'Pa'},
    7: {'name': 'P Wave Velocity',
        'symbol': 'Vp',
        'cmap_type': "sequential",
        'unit': 'm/s'},
    8: {'name': 'S Wave Velocity',
        'symbol': 'Vs',
        'cmap_type': "sequential",
        'unit': 'm/s'},
    16: {'name': 'Latitude',
         'symbol': 'lat',
         'cmap_type': "sequential",
         'unit': 'degrees'},
    17: {'name': 'Longitude',
         'symbol': 'lon',
         'cmap_type': "sequential",
         'unit': 'degrees'},
    18: {'name': 'Topography',
         'symbol': 'topo',
         'cmap_type': "sequential",
         'unit': 'm'},
    19: {'name': 'X',
         'symbol': 'x',
         'cmap_type': "sequential",
         'unit': 'm'},
    20: {'name': 'X',
         'symbol': 'y',
         'cmap_type': "sequential",
         'unit': 'm'},
    21: {'name': 'Z',
         'symbol': 'z',
         'cmap_type': "sequential",
         'unit': 'm'},
    }
SW4_IMAGE_MODE_DISPLACEMENT = {
    1: {'name': 'X Displacement',
        'symbol': 'ux',
        'cmap_type': "divergent",
        'unit': 'm'},
    2: {'name': 'Y Displacement',
        'symbol': 'uy',
        'cmap_type': "divergent",
        'unit': 'm'},
    3: {'name': 'Z Displacement',
        'symbol': 'uz',
        'cmap_type': "divergent",
        'unit': 'm'},
    9: {'name': 'X Displacement (exact)',
        'symbol': 'ux ex',
        'cmap_type': "divergent",
        'unit': 'm'},
    10: {'name': 'Y Displacement (exact)',
         'symbol': 'uy ex',
         'cmap_type': "divergent",
         'unit': 'm'},
    11: {'name': 'Z Displacement (exact)',
         'symbol': 'uz ex',
         'cmap_type': "divergent",
         'unit': 'm'},
    12: {'name': 'Divergence of Displacement',
         'symbol': 'div(u)',
         'cmap_type': "divergent",
         'unit': '<no unit>'},
    13: {'name': 'Curl of Displacement',
         'symbol': 'curl(u)',
         'cmap_type': "divergent",
         'unit': '<no unit>'},
    14: {'name': 'Divergence of Velocity',
         'symbol': 'div(du/dt)',
         'cmap_type': "divergent",
         'unit': 's^-1'},
    15: {'name': 'Curl of Velocity',
         'symbol': 'curl(du/dt)',
         'cmap_type': "divergent",
         'unit': 's^-1'},
    22: {'name': 'X Displacement Error',
         'symbol': 'ux error',
         'cmap_type': "sequential",
         'unit': '<no unit>'},
    23: {'name': 'Y Displacement Error',
         'symbol': 'uy error',
         'cmap_type': "sequential",
         'unit': '<no unit>'},
    24: {'name': 'Z Displacement Error',
         'symbol': 'uz error',
         'cmap_type': "sequential",
         'unit': '<no unit>'},
    25: {'name': 'Velocity Magnitude',
         'symbol': '|du/dt|',
         'cmap_type': "sequential",
         'unit': 'm/s'},
    26: {'name': 'Horizontal Velocity Magnitude',
         'symbol': 'sqrt((dux/dt)^2 + (duy/dt)^2)',
         'cmap_type': "sequential",
         'unit': 'm/s'},
    27: {'name': 'Peak Horizontal Velocity Magnitude',
         'symbol': 'max_t (sqrt((dux/dt)^2 + (duy/dt)^2))',
         'cmap_type': "sequential",
         'unit': 'm/s'},
    28: {'name': 'Peak Vertical Velocity',
         'symbol': 'max_t |duz/dt|',
         'cmap_type': "sequential",
         'unit': 'm/s'},
    29: {'name': 'Displacement Magnitude',
         'symbol': '|u|',
         'cmap_type': "sequential",
         'unit': 'm'},
    30: {'name': 'Horizontal Displacement Magnitude',
         'symbol': 'sqrt(ux^2 + uy^2)',
         'cmap_type': "sequential",
         'unit': 'm'},
    31: {'name': 'Peak Horizontal Displacement Magnitude',
         'symbol': 'max_t sqrt(ux^2 + uy^2)',
         'cmap_type': "sequential",
         'unit': 'm'},
    32: {'name': 'Peak Vertical Displacement',
         'symbol': 'max_t |uz|',
         'cmap_type': "sequential",
         'unit': 'm'},
    }
SW4_IMAGE_MODE_DISPLACEMENT.update(SW4_IMAGE_MODE_COMMON)
SW4_IMAGE_MODE_VELOCITY = {
    1: {'name': 'X Velocity',
        'symbol': 'ux',
        'cmap_type': "divergent",
        'unit': 'm/s'},
    2: {'name': 'Y Velocity',
        'symbol': 'uy',
        'cmap_type': "divergent",
        'unit': 'm/s'},
    3: {'name': 'Z Velocity',
        'symbol': 'uz',
        'cmap_type': "divergent",
        'unit': 'm/s'},
    9: {'name': 'X Velocity (exact)',
        'symbol': 'ux ex',
        'cmap_type': "divergent",
        'unit': 'm/s'},
    10: {'name': 'Y Velocity (exact)',
         'symbol': 'uy ex',
         'cmap_type': "divergent",
         'unit': 'm/s'},
    11: {'name': 'Z Velocity (exact)',
         'symbol': 'uz ex',
         'cmap_type': "divergent",
         'unit': 'm/s'},
    12: {'name': 'Divergence of Velocity',
         'symbol': 'div(u)',
         'cmap_type': "sequential",
         'unit': 's^-1'},
    13: {'name': 'Curl of Velocity',
         'symbol': 'curl(u)',
         'cmap_type': "sequential",
         'unit': 's^-1'},
    14: {'name': 'Divergence of Acceleration',
         'symbol': 'div(du/dt)',
         'cmap_type': "sequential",
         'unit': 's^-2'},
    15: {'name': 'Curl of Acceleration',
         'symbol': 'curl(du/dt)',
         'cmap_type': "sequential",
         'unit': 's^-2'},
    22: {'name': 'X Velocity Error',
         'symbol': 'ux error',
         'cmap_type': "sequential",
         'unit': '<no unit>'},
    23: {'name': 'Y Velocity Error',
         'symbol': 'uy error',
         'cmap_type': "sequential",
         'unit': '<no unit>'},
    24: {'name': 'Z Velocity Error',
         'symbol': 'uz error',
         'cmap_type': "sequential",
         'unit': '<no unit>'},
    25: {'name': 'Acceleration Magnitude',
         'symbol': '|du/dt|',
         'cmap_type': "sequential",
         'unit': 'm/s^2'},
    26: {'name': 'Horizontal Acceleration Magnitude',
         'symbol': 'sqrt((dux/dt)^2 + (duy/dt)^2)',
         'cmap_type': "sequential",
         'unit': 'm/s^2'},
    27: {'name': 'Peak Horizontal Acceleration Magnitude',
         'symbol': 'max_t (sqrt((dux/dt)^2 + (duy/dt)^2))',
         'cmap_type': "sequential",
         'unit': 'm/s^2'},
    28: {'name': 'Peak Vertical Acceleration',
         'symbol': 'max_t |duz/dt|',
         'cmap_type': "sequential",
         'unit': 'm/s^2'},
    29: {'name': 'Velocity Magnitude',
         'symbol': '|u|',
         'cmap_type': "sequential",
         'unit': 'm/s'},
    30: {'name': 'Horizontal Velocity Magnitude',
         'symbol': 'sqrt(ux^2 + uy^2)',
         'cmap_type': "sequential",
         'unit': 'm/s'},
    31: {'name': 'Peak Horizontal Velocity Magnitude',
         'symbol': 'max_t sqrt(ux^2 + uy^2)',
         'cmap_type': "sequential",
         'unit': 'm/s'},
    32: {'name': 'Peak Vertical Velocity',
         'symbol': 'max_t |uz|',
         'cmap_type': "sequential",
         'unit': 'm/s'},
    }
SW4_IMAGE_MODE_VELOCITY.update(SW4_IMAGE_MODE_COMMON)

SW4_IMAGE_PLANE = {0: 'x', 1: 'y', 2: 'z'}

SW4_IMAGE_PRECISION = {4: np.float32, 8: np.float64}
