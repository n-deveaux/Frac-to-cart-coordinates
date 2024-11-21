# `Frac-to-cart-coordinates`

The `Frac-to-cart-coordinates` package allows users to easily convert atomic coordinates from Cartesian to fractional format and vice versa, based on the unit cell parameters.

## Overview
### Coordinate Transformation in Crystallography

In crystallography, atomic positions within a crystal's unit cell can be described using:
- **Fractional coordinates** $(x/a, y/b, z/c)$, which refer to the natural axes \(a, b, c\), scaled by their respective unit cell lengths.
- **Orthogonal coordinates** $(X, Y, Z)$, which use a right-angled Cartesian system with distances measured in Ångstroms.

For triclinic unit cells, the relationship between these coordinate systems involves a transformation matrix with non-trivial elements, derived using spherical trigonometry.

### Implementation details

This implementation follows the methodology described on John Cooper's website, [fractorth](https://ic50.org/fractorth/). It relies on the fundamental principles of spherical trigonometry, particularly the cosine rule for reciprocal angles:

$$
\cos(\alpha^*) = \frac{\cos(\beta)\cos(\gamma) - \cos(\alpha)}{\sin(\beta)\sin(\gamma)}
$$

Using this, the transformation matrix to convert Cartesian orthogonal coordinates $(X, Y, Z)$ to fractional ones $(x, y, z)$ aliging $a$ with the $X$-axis, is:

$$
\begin{pmatrix}
X \\
Y \\
Z
\end{pmatrix}
=
\begin{pmatrix}
a & b\cos(\gamma) & c\cos(\beta) \\
0 & b\sin(\gamma) & -c\sin(\beta)\cos(\alpha^*) \\
0 & 0 & c\sin(\beta)\sin(\alpha^*)
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
$$

where:
- $a, b, c$ are the unit cell lengths,
- $\alpha, \beta, \gamma$ are the angles of the unit cell (in radians),
- $\alpha^*$ is the reciprocal angle, calculated using the cosine rule above.

## Installation

You can clone the repository and install the package using:

```bash
git clone <https://github.com/n-deveaux/Frac-to-cart-coordinates.git>
cd Frac-to-cart-coordinates
```

Make sure you have numpy installed and Python 3.6 or higher.

## Usage

### Importing the Module

```python
from Fractocart import convert_to_fractional_coordinates, convert_to_cartesian_coordinates
```

### Functions

1. **Convert to Fractional Coordinates**

   ```python
   fractional_coords = convert_to_fractional_coordinates(cartesian_coords, unit_cell)
   ````

2. **Convert to Cartesian Coordinates**

    ```python
    cartesian_coords = convert_to_cartesian_coordinates(fractional_coords, unit_cell)
    ````

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


    