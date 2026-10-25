# Rotation of axes in two dimensions

Rotation of axes in two dimensions

In mathematics, a rotation of axes in two dimensions is a mapping from an

        x
        y

    {\displaystyle xy}

-Cartesian coordinate system to an

          x
          ′

          y
          ′

    {\displaystyle x'y'}

-Cartesian coordinate system in which the origin is kept fixed and the

          x
          ′

    {\displaystyle x'}

 and

          y
          ′

    {\displaystyle y'}

 axes are obtained by rotating the

        x

    {\displaystyle x}

 and

        y

    {\displaystyle y}

 axes counterclockwise through an angle

        θ

    {\displaystyle \theta }

. A point

        P

    {\displaystyle P}

 has coordinates

        (
        x
        ,
        y
        )

    {\displaystyle (x,y)}

 with respect to the original system and coordinates

        (

          x
          ′

        ,

          y
          ′

        )

    {\displaystyle (x',y')}

 with respect to the new system. In the new coordinate system, the point

        P

    {\displaystyle P}

 will appear to have been rotated in the opposite direction, that is, clockwise through the angle

        θ

    {\displaystyle \theta }

. A rotation of axes in more than two dimensions is defined similarly. A rotation of axes is a linear map and a rigid transformation.

Motivation
Coordinate systems are essential for studying the equations of curves using the methods of analytic geometry. To use the method of coordinate geometry, the axes are placed at a convenient position with respect to the curve under consideration. For example, to study the equations of ellipses and hyperbolas, the foci are usually located on one of the axes and are situated symmetrically with respect to the origin. If the curve (hyperbola, parabola, ellipse, etc.) is not situated conveniently with respect to the axes, the coordinate system should be changed to place the curve at a convenient and familiar location and orientation. The process of making this change is called a transformation of coordinates.
The solutions to many problems can be simplified by rotating the coordinate axes to obtain new axes through the same origin.

Derivation
The equations defining the transformation in two dimensions, which rotates the

        x
        y

    {\displaystyle xy}

 axes counterclockwise through an angle

        θ

    {\displaystyle \theta }

 into the

          x
          ′

          y
          ′

    {\displaystyle x'y'}

 axes, are derived as follows.
In the

        x
        y

    {\displaystyle xy}

 system, let the point

        P

    {\displaystyle P}

 have polar coordinates

        (
        r
        ,
        α
        )

    {\displaystyle (r,\alpha )}

. Then, in the

          x
          ′

          y
          ′

    {\displaystyle x'y'}

 system,

        P

    {\displaystyle P}

 will have polar coordinates

        (
        r
        ,
        α
        −
        θ
        )

    {\displaystyle (r,\alpha -\theta )}

.
Using trigonometric functions, we have

and using the standard trigonometric formulae for differences, we have

Substituting equations (1) and (2) into equations (3) and (4), we obtain

Equations (5) and (6) can be represented in matrix form as

            [

                    x
                    ′

                    y
                    ′

            ]

            [

                  cos
                  ⁡
                  θ

                  sin
                  ⁡
                  θ

                  −
                  sin
                  ⁡
                  θ

                  cos
                  ⁡
                  θ

            ]

            [

                  x

                  y

            ]

        ,

    {\displaystyle {\begin{bmatrix}x'\y'\end{bmatrix}}={\begin{bmatrix}\cos \theta &\sin \theta \-\sin \theta &\cos \theta \end{bmatrix}}{\begin{bmatrix}x\y\end{bmatrix}},}

which is the standard matrix equation of a rotation of axes in two dimensions.
The inverse transformation is

or

            [

                  x

                  y

            ]

            [

                  cos
                  ⁡
                  θ

                  −
                  sin
                  ⁡
                  θ

                  sin
                  ⁡
                  θ

                  cos
                  ⁡
                  θ

            ]

            [

                    x
                    ′

                    y
                    ′

            ]

        .

    {\displaystyle {\begin{bmatrix}x\y\end{bmatrix}}={\begin{bmatrix}\cos \theta &-\sin \theta \\sin \theta &\cos \theta \end{bmatrix}}{\begin{bmatrix}x'\y'\end{bmatrix}}.}

Examples in two dimensions

Example 1
Find the coordinates of the point

          P

            1

        (
        x
        ,
        y
        )

        (

            3

        ,
        1
        )

    {\displaystyle P_{1}=(x,y)=({\sqrt {3}},1)}

 after the axes have been rotated through the angle

          θ

            1

        π

          /

        6

    {\displaystyle \theta _{1}=\pi /6}

, or 30°.
Solution:

          x
          ′

            3

        cos
        ⁡
        (
        π

          /

        6
        )
        +
        1
        sin
        ⁡
        (
        π

          /

        6
        )

        (

            3

        )
        (

            3

          /

        2
        )
        +
        (
        1
        )
        (
        1

          /

        2
        )

        2

    {\displaystyle x'={\sqrt {3}}\cos(\pi /6)+1\sin(\pi /6)=({\sqrt {3}})({\sqrt {3}}/2)+(1)(1/2)=2}

          y
          ′

        1
        cos
        ⁡
        (
        π

          /

        6
        )
        −

            3

        sin
        ⁡
        (
        π

          /

        6
        )

        (
        1
        )
        (

            3

          /

        2
        )
        −
        (

            3

        )
        (
        1

          /

        2
        )

        0.

    {\displaystyle y'=1\cos(\pi /6)-{\sqrt {3}}\sin(\pi /6)=(1)({\sqrt {3}}/2)-({\sqrt {3}})(1/2)=0.}

The axes have been rotated counterclockwise through an angle of

          θ

            1

        π

          /

        6

    {\displaystyle \theta _{1}=\pi /6}

 and the new coordinates are

          P

            1

        (

          x
          ′

        ,

          y
          ′

        )

        (
        2
        ,
        0
        )

    {\displaystyle P_{1}=(x',y')=(2,0)}

. Note that the point appears to have been rotated clockwise through

        π

          /

        6

    {\displaystyle \pi /6}

 with respect to fixed axes so it now coincides with the (new)

          x
          ′

    {\displaystyle x'}

 axis.

Example 2
Find the coordinates of the point

          P

            2

        (
        x
        ,
        y
        )

        (
        7
        ,
        7
        )

    {\displaystyle P_{2}=(x,y)=(7,7)}

 after the axes have been rotated clockwise 90°, that is, through the angle

          θ

            2

        −
        π

          /

        2

    {\displaystyle \theta _{2}=-\pi /2}

, or −90°.
Solution:

            [

                    x
                    ′

                    y
                    ′

            ]

            [

                  cos
                  ⁡
                  (
                  −
                  π

                    /

                  2
                  )

                  sin
                  ⁡
                  (
                  −
                  π

                    /

                  2
                  )

                  −
                  sin
                  ⁡
                  (
                  −
                  π

                    /

                  2
                  )

                  cos
                  ⁡
                  (
                  −
                  π

                    /

                  2
                  )

            ]

            [

                  7

                  7

            ]

            [

                  0

                  −
                  1

                  1

                  0

            ]

            [

                  7

                  7

            ]

            [

                  −
                  7

                  7

            ]

        .

    {\displaystyle {\begin{bmatrix}x'\y'\end{bmatrix}}={\begin{bmatrix}\cos(-\pi /2)&\sin(-\pi /2)\-\sin(-\pi /2)&\cos(-\pi /2)\end{bmatrix}}{\begin{bmatrix}7\7\end{bmatrix}}={\begin{bmatrix}0&-1\1&0\end{bmatrix}}{\begin{bmatrix}7\7\end{bmatrix}}={\begin{bmatrix}-7\7\end{bmatrix}}.}

The axes have been rotated through an angle of

          θ

            2

        −
        π

          /

        2

    {\displaystyle \theta _{2}=-\pi /2}

, which is in the clockwise direction and the new coordinates are

          P

            2

        (

          x
          ′

        ,

          y
          ′

        )

        (
        −
        7
        ,
        7
        )

    {\displaystyle P_{2}=(x',y')=(-7,7)}

. Again, note that the point appears to have been rotated counterclockwise through

        π

          /

        2

    {\displaystyle \pi /2}

 with respect to fixed axes.

Rotation of conic sections

The most general equation of the second degree has the form

Through a change of coordinates (a rotation of axes and a translation of axes), equation (9) can be put into a standard form, which is usually easier to work with. It is always possible to rotate the coordinates at a specific angle so as to eliminate the

          x
          ′

          y
          ′

    {\displaystyle x'y'}

 term. Substituting equations (7) and (8) into equation (9), we obtain

where

If

        θ

    {\displaystyle \theta }

 is selected so that

        cot
        ⁡
        2
        θ

        (
        A
        −
        C
        )

          /

        B

    {\displaystyle \cot 2\theta =(A-C)/B}

 we will have

          B
          ′

        0

    {\displaystyle B'=0}

 and the

          x
          ′

          y
          ′

    {\displaystyle x'y'}

 term in equation (10) will vanish.
When a problem arises with

        B

    {\displaystyle B}

,

        D

    {\displaystyle D}

 and

        E

    {\displaystyle E}

 all different from zero, they can be eliminated by performing in succession a rotation (eliminating

        B

    {\displaystyle B}

) and a translation (eliminating the

        D

    {\displaystyle D}

 and

        E

    {\displaystyle E}

 terms).

Identifying rotated conic sections
A non-degenerate conic section given by equation (9) can be identified by evaluating

          B

            2

        −
        4
        A
        C

    {\displaystyle B^{2}-4AC}

. The conic section is:

an ellipse or a circle, if

          B

            2

        −
        4
        A
        C
        <
        0

    {\displaystyle B^{2}-4AC<0}

;
a parabola, if

          B

            2

        −
        4
        A
        C

        0

    {\displaystyle B^{2}-4AC=0}

;
a hyperbola, if

          B

            2

        −
        4
        A
        C

        0

    {\displaystyle B^{2}-4AC>0}

.

Generalization to several dimensions
Suppose a rectangular

        x
        y
        z

    {\displaystyle xyz}

-coordinate system is rotated around its

        z

    {\displaystyle z}

 axis counterclockwise (looking down the positive

        z

    {\displaystyle z}

 axis) through an angle

        θ

    {\displaystyle \theta }

, that is, the positive

        x

    {\displaystyle x}

 axis is rotated immediately into the positive

        y

    {\displaystyle y}

 axis. The

        z

    {\displaystyle z}

 coordinate of each point is unchanged and the

        x

    {\displaystyle x}

  and

        y

    {\displaystyle y}

 coordinates transform as above. The old coordinates

        (
        x
        ,
        y
        ,
        z
        )

    {\displaystyle (x,y,z)}

 of a point

        Q

    {\displaystyle Q}

 are related to its new coordinates

        (

          x
          ′

        ,

          y
          ′

        ,

          z
          ′

        )

    {\displaystyle (x',y',z')}

 by

            [

                    x
                    ′

                    y
                    ′

                    z
                    ′

            ]

            [

                  cos
                  ⁡
                  θ

                  sin
                  ⁡
                  θ

                  0

                  −
                  sin
                  ⁡
                  θ

                  cos
                  ⁡
                  θ

                  0

                  0

                  0

                  1

            ]

            [

                  x

                  y

                  z

            ]

        .

    {\displaystyle {\begin{bmatrix}x'\y'\z'\end{bmatrix}}={\begin{bmatrix}\cos \theta &\sin \theta &0\-\sin \theta &\cos \theta &0\0&0&1\end{bmatrix}}{\begin{bmatrix}x\y\z\end{bmatrix}}.}

Generalizing to any finite number of dimensions, a rotation matrix

        A

    {\displaystyle A}

 is an orthogonal matrix that differs from the identity matrix in at most four elements. These four elements are of the form

          a

            i
            i

          a

            j
            j

        cos
        ⁡
        θ

    {\displaystyle a_{ii}=a_{jj}=\cos \theta }

      and

          a

            i
            j

        −

          a

            j
            i

        sin
        ⁡
        θ
        ,

    {\displaystyle a_{ij}=-a_{ji}=\sin \theta ,}

for some

        θ

    {\displaystyle \theta }

 and some

        i
        ≠
        j

    {\displaystyle i\neq j}

.

Example in several dimensions

Example 3
Find the coordinates of the point

          P

            3

        (
        w
        ,
        x
        ,
        y
        ,
        z
        )

        (
        1
        ,
        1
        ,
        1
        ,
        1
        )

    {\displaystyle P_{3}=(w,x,y,z)=(1,1,1,1)}

 after the positive w axis has been rotated through the angle

          θ

            3

        π

          /

        12

    {\displaystyle \theta _{3}=\pi /12}

, or 15°, into the positive

        z

    {\displaystyle z}

 axis.
Solution:

                    [

                            w
                            ′

                            x
                            ′

                            y
                            ′

                            z
                            ′

                    ]

                    [

                          cos
                          ⁡
                          (
                          π

                            /

                          12
                          )

                          0

                          0

                          sin
                          ⁡
                          (
                          π

                            /

                          12
                          )

                          0

                          1

                          0

                          0

                          0

                          0

                          1

                          0

                          −
                          sin
                          ⁡
                          (
                          π

                            /

                          12
                          )

                          0

                          0

                          cos
                          ⁡
                          (
                          π

                            /

                          12
                          )

                    ]

                    [

                          w

                          x

                          y

                          z

                    ]

                ≈

                    [

                          0.96593

                          0.0

                          0.0

                          0.25882

                          0.0

                          1.0

                          0.0

                          0.0

                          0.0

                          0.0

                          1.0

                          0.0

                          −
                          0.25882

                          0.0

                          0.0

                          0.96593

                    ]

                    [

                          1.0

                          1.0

                          1.0

                          1.0

                    ]

                    [

                          1.22475

                          1.00000

                          1.00000

                          0.70711

                    ]

                .

    {\displaystyle {\begin{aligned}{\begin{bmatrix}w'\x'\y'\z'\end{bmatrix}}&={\begin{bmatrix}\cos(\pi /12)&0&0&\sin(\pi /12)\0&1&0&0\0&0&1&0\-\sin(\pi /12)&0&0&\cos(\pi /12)\end{bmatrix}}{\begin{bmatrix}w\x\y\z\end{bmatrix}}\[4pt]&\approx {\begin{bmatrix}0.96593&0.0&0.0&0.25882\0.0&1.0&0.0&0.0\0.0&0.0&1.0&0.0\-0.25882&0.0&0.0&0.96593\end{bmatrix}}{\begin{bmatrix}1.0\1.0\1.0\1.0\end{bmatrix}}={\begin{bmatrix}1.22475\1.00000\1.00000\0.70711\end{bmatrix}}.\end{aligned}}}
