# Chasles' theorem (kinematics)

Chasles' theorem (kinematics)

In kinematics, Chasles' theorem, or Mozzi–Chasles' theorem, says that the most general rigid body displacement can be produced by a screw displacement or screw motion. A direct Euclidean isometry in three dimensions involves a translation and a rotation. The screw displacement representation of the isometry decomposes the translation into two components, one parallel to the axis of rotation associated with the isometry and the other component perpendicular to that axis. The Chasles theorem states that the axis of rotation can be selected to provide the second component of the original translation as a result of the rotation. This theorem in three dimensions extends a similar representation of planar isometries as rotation. Once the screw axis is selected, the screw displacement rotates about it and a translation parallel to the axis is included in the screw displacement.

Planar isometries with complex numbers
Euclidean geometry is expressed in the complex plane by points

        p

        x
        +
        y
        i

    {\displaystyle p=x+yi}

 where i squared is −1. Rotations result from multiplications by

        ω

        cos
        ⁡
        t
        +
        i
        sin
        ⁡
        t

    {\displaystyle \omega =\cos t+i\sin t}

.
Note that a rotation about complex point p is obtained by complex arithmetic with

        z
        ↦
        ω
        (
        z
        −
        p
        )
        +
        p

        ω
        z
        +
        p
        (
        1
        −
        ω
        )

    {\displaystyle z\mapsto \omega (z-p)+p=\omega z+p(1-\omega )}

where the last expression shows the mapping equivalent to rotation at 0 and a translation.
Therefore, given direct isometry

        z
        ↦
        ω
        z
        +
        a
        ,

    {\displaystyle z\mapsto \omega z+a,}

 one can solve

        p
        (
        1
        −
        ω
        )

        a

    {\displaystyle p(1-\omega )=a}

 to obtain

        p

        a

          /

        (
        1
        −
        ω
        )

    {\displaystyle p=a/(1-\omega )}

 as the center for an equivalent rotation, provided that

        ω
        ≠
        1

    {\displaystyle \omega \neq 1}

, that is, provided the direct isometry is not a pure translation. As stated by Cederberg, "A direct isometry is either a rotation or a translation."

History
The proof that a spatial displacement can be decomposed into a rotation and slide around and along a line is attributed to the astronomer and mathematician Giulio Giuseppe Mozzi (1763), in fact the screw axis is traditionally called asse di Mozzi in Italy. However, most textbooks refer to a subsequent similar work by Michel Chasles dating from 1830. Several other contemporaries of M. Chasles obtained the same or similar results around that time, including Gaetano Giorgini, Augustin-Louis Cauchy, Louis Poinsot, Siméon Denis Poisson and Olinde Rodrigues. An account of the 1763 proof by Giulio Mozzi and some of its history can be found here.

Proof
Mozzi considers a rigid body undergoing first a rotation about an axis passing through the center of mass and then a translation of displacement D in an arbitrary direction. Any rigid motion can be accomplished in this way due to a theorem by Euler on the existence of an axis of rotation.
The displacement D of the center of mass can be decomposed into components parallel and perpendicular to the axis. The perpendicular (and parallel) component acts on all points of the rigid body but Mozzi shows that for some points the previous rotation acted exactly with an opposite displacement, so those points are translated parallel to the axis of rotation. These points lie on the Mozzi axis through which the rigid motion can be accomplished through a screw motion.
Another elementary proof of Mozzi–Chasles' theorem was given by E. T. Whittaker in 1904. Suppose A is to be transformed into B. Whittaker suggests that line AK be selected parallel to the axis of the given rotation, with K the foot of a perpendicular from B. The appropriate screw displacement is about an axis parallel to AK such that K is moved to B. In Whittaker's terms, "A rotation about any axis is equivalent to a rotation through the same angle about any axis parallel to it, together with a simple translation in a direction perpendicular to the axis."

Calculation
The calculation of the commuting translation and rotation from a screw motion can be performed using 3DPGA (

            R

            3
            ,
            0
            ,
            1

    {\displaystyle \mathbb {R} _{3,0,1}}

), the geometric algebra of 3D Euclidean space. It has three Euclidean basis vectors

            e

            i

    {\displaystyle \mathbf {e} _{i}}

 satisfying

            e

            i

            2

        1

    {\displaystyle \mathbf {e} _{i}^{2}=1}

 representing orthogonal planes through the origin, and one Grassmannian basis vector

            e

            0

    {\displaystyle \mathbf {e} _{0}}

 satisfying

            e

            0

            2

        0

    {\displaystyle \mathbf {e} _{0}^{2}=0}

 to represent the plane at infinity. Any plane a distance

        δ

    {\displaystyle \delta }

 from the origin can then be formed as a linear combination

        a

          ∑

            i

            1

            3

          a

            i

            e

            i

        −
        δ

            e

            0

    {\displaystyle a=\sum _{i=1}^{3}a^{i}\mathbf {e} _{i}-\delta \mathbf {e} _{0}}

which is normalized such that

          a

            2

        1

    {\displaystyle a^{2}=1}

. Because reflections can be represented by the plane in which the reflection occurs, the product of two planes

        a

    {\displaystyle a}

 and

        b

    {\displaystyle b}

 is the bireflection

        a
        b

    {\displaystyle ab}

. The result is a rotation around their intersection line

        a
        ∧
        b

    {\displaystyle a\wedge b}

, which could also lie on the plane at infinity when the two reflections are parallel, in which case the bireflection

        a
        b

    {\displaystyle ab}

 is a translation.
A screw motion

        S

    {\displaystyle S}

 is the product of four non-collinear reflections, and thus

        S

        a
        b
        c
        d

    {\displaystyle S=abcd}

. But according to the Mozzi-Chasles' theorem a screw motion can be decomposed into a commuting translation

        T

          e

            α

              B

                1

        1
        +
        α

          B

            1

    {\displaystyle T=e^{\alpha B_{1}}=1+\alpha B_{1}}

where

          B

            1

    {\displaystyle B_{1}}

 is the axis of translation satisfying

          B

            1

            2

        0

    {\displaystyle B_{1}^{2}=0}

, and rotation

        R

          e

            β

              B

                2

        cos
        ⁡
        (
        β
        )
        +

          B

            2

        sin
        ⁡
        (
        β
        )

    {\displaystyle R=e^{\beta B_{2}}=\cos(\beta )+B_{2}\sin(\beta )}

where

          B

            2

    {\displaystyle B_{2}}

 is the axis of rotation satisfying

          B

            2

            2

        −
        1

    {\displaystyle B_{2}^{2}=-1}

. The two bivector lines

          B

            1

    {\displaystyle B_{1}}

 and

          B

            2

    {\displaystyle B_{2}}

 are orthogonal and commuting. To find

        T

    {\displaystyle T}

 and

        R

    {\displaystyle R}

 from

        S

    {\displaystyle S}

, we simply write out

        S

    {\displaystyle S}

 and consider the result grade-by-grade:

                S

                T
                R

                  e

                    α

                      B

                        1

                  e

                    β

                      B

                        2

                        cos
                        ⁡
                        β

                      ⏟

                    scalar

                +

                        sin
                        ⁡
                        β

                          B

                            2

                        +
                        α
                        cos
                        ⁡
                        β

                          B

                            1

                      ⏟

                    bivector

                +

                        α
                        sin
                        ⁡
                        β

                          B

                            1

                          B

                            2

                      ⏟

                    quadrivector

    {\displaystyle {\begin{aligned}S&=TR\&=e^{\alpha B_{1}}e^{\beta B_{2}}\&=\underbrace {\cos \beta } {\text{scalar}}+\underbrace {\sin \beta B{2}+\alpha \cos \beta B_{1}} {\text{bivector}}+\underbrace {\alpha \sin \beta B{1}B_{2}} _{\text{quadrivector}}\end{aligned}}}

Because the quadrivector part

        ⟨
        S

          ⟩

            4

        ⟨
        T

          ⟩

            2

        ⟨
        R

          ⟩

            2

    {\displaystyle \langle S\rangle _{4}=\langle T\rangle _{2}\langle R\rangle _{2}}

 and

          B

            1

            2

        0

    {\displaystyle B_{1}^{2}=0}

,

        T

    {\displaystyle T}

 is directly found to be

        T

        1
        +

              ⟨
              S

                ⟩

                  4

              ⟨
              S

                ⟩

                  2

    {\displaystyle T=1+{\frac {\langle S\rangle _{4}}{\langle S\rangle _{2}}}}

and thus

        R

        S

          T

            −
            1

          T

            −
            1

        S

            S
            T

    {\displaystyle R=ST^{-1}=T^{-1}S={\frac {S}{T}}}

Thus, for a given screw motion

        S

    {\displaystyle S}

 the commuting translation and rotation can be found using the two formulae above, after which the lines

          B

            1

    {\displaystyle B_{1}}

 and

          B

            2

    {\displaystyle B_{2}}

 are found to be proportional to

        ⟨
        T

          ⟩

            2

    {\displaystyle \langle T\rangle _{2}}

 and

        ⟨
        R

          ⟩

            2

    {\displaystyle \langle R\rangle _{2}}

 respectively.

Other dimensions and fields
The Chasles' theorem is a special case of the Invariant decomposition.
