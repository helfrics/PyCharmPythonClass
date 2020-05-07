import math  # Allow use of constants like math.pi.
# These are dimensions of a torus.
r_inner = 3  # Radius of torus hole.
r_outer = 4  # Radius from center to outer edge of torus.
r_minor = (r_outer - r_inner) / 2
r_major = r_outer - r_minor
volume = math.pi * r_minor * r_minor * 2 * math.pi * r_major
print(volume)
