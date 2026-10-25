# Stress resultants

Stress resultants

Stress resultants are simplified representations of the stress state in structural elements such as beams, plates, or shells. The geometry of typical structural elements allows the internal stress state to be simplified because of the existence of a "thickness'" direction in which the size of the element is much smaller than in other directions. As a consequence the three traction components that vary from point to point in a cross-section can be replaced with a set of resultant forces and resultant moments. These are the stress resultants (also called membrane forces, shear forces, and bending moment) that may be used to determine the detailed stress state in the structural element. A three-dimensional problem can then be reduced to a one-dimensional problem (for beams) or a two-dimensional problem (for plates and shells).
Stress resultants are defined as integrals of stress over the thickness of a structural element. The integrals are weighted by integer powers the thickness coordinate z (or x3). Stress resultants are so defined to represent the effect of stress as a membrane force N (zero power in z), bending moment M (power 1) on a beam or shell (structure). Stress resultants are necessary to eliminate the z dependency of the stress from the equations of the theory of plates and shells.

Stress resultants in beams

Consider the element shown in the adjacent figure. Assume that the thickness direction is x3. If the element has been extracted from a beam, the width and thickness are comparable in size. Let x2 be the width direction. Then x1 is the length direction.

Membrane and shear forces
The resultant force vector due to the traction in the cross-section (A) perpendicular to the x1 axis is

            F

            1

          ∫

            A

        (

          σ

            11

            e

            1

        +

          σ

            12

            e

            2

        +

          σ

            13

            e

            3

        )

        d
        A

    {\displaystyle \mathbf {F} _{1}=\int _{A}(\sigma _{11}\mathbf {e} _{1}+\sigma _{12}\mathbf {e} _{2}+\sigma _{13}\mathbf {e} _{3})\,dA}

where e1, e2, e3 are the unit vectors along x1, x2, and x3, respectively. We define the stress resultants such that

            F

            1

        =:

          N

            11

            e

            1

        +

          V

            2

            e

            2

        +

          V

            3

            e

            3

    {\displaystyle \mathbf {F} {1}=:N{11}\mathbf {e} {1}+V{2}\mathbf {e} {2}+V{3}\mathbf {e} _{3}}

where N11 is the membrane force and V2, V3 are the shear forces. More explicitly, for a beam of height t and width b,

          N

            11

          ∫

            −
            b

              /

            2

            b

              /

            2

          ∫

            −
            t

              /

            2

            t

              /

            2

          σ

            11

        d

          x

            3

        d

          x

            2

        .

    {\displaystyle N_{11}=\int _{-b/2}^{b/2}\int _{-t/2}^{t/2}\sigma {11}\,dx{3}\,dx_{2}\,.}

Similarly the shear force resultants are

            [

                    V

                      2

                    V

                      3

            ]

          ∫

            −
            b

              /

            2

            b

              /

            2

          ∫

            −
            t

              /

            2

            t

              /

            2

            [

                    σ

                      12

                    σ

                      13

            ]

        d

          x

            3

        d

          x

            2

        .

    {\displaystyle {\begin{bmatrix}V_{2}\V_{3}\end{bmatrix}}=\int _{-b/2}^{b/2}\int _{-t/2}^{t/2}{\begin{bmatrix}\sigma _{12}\\sigma {13}\end{bmatrix}}\,dx{3}\,dx_{2}\,.}

Bending moments
The bending moment vector due to stresses in the cross-section A perpendicular to the x1-axis is given by

            M

            1

          ∫

            A

          r

        ×
        (

          σ

            11

            e

            1

        +

          σ

            12

            e

            2

        +

          σ

            13

            e

            3

        )

        d
        A

          where

          r

          x

            2

            e

            2

        +

          x

            3

            e

            3

        .

    {\displaystyle \mathbf {M} _{1}=\int _{A}\mathbf {r} \times (\sigma _{11}\mathbf {e} _{1}+\sigma _{12}\mathbf {e} _{2}+\sigma _{13}\mathbf {e} {3})\,dA\quad {\text{where}}\quad \mathbf {r} =x{2}\,\mathbf {e} {2}+x{3}\,\mathbf {e} _{3}\,.}

Expanding this expression we have,

            M

            1

          ∫

            A

          (

            −

              x

                2

              σ

                11

                e

                3

            +

              x

                2

              σ

                13

                e

                1

            +

              x

                3

              σ

                11

                e

                2

            −

              x

                3

              σ

                12

                e

                1

          )

        d
        A
        =:

          M

            11

            e

            1

        +

          M

            12

            e

            2

        +

          M

            13

            e

            3

        .

    {\displaystyle \mathbf {M} _{1}=\int {A}\left(-x{2}\sigma _{11}\mathbf {e} {3}+x{2}\sigma _{13}\mathbf {e} {1}+x{3}\sigma _{11}\mathbf {e} {2}-x{3}\sigma _{12}\mathbf {e} {1}\right)dA=:M{11}\,\mathbf {e} {1}+M{12}\,\mathbf {e} {2}+M{13}\,\mathbf {e} _{3}\,.}

We can write the bending moment resultant components as

            [

                    M

                      11

                    M

                      12

                    M

                      13

            ]

        :=

          ∫

            −
            b

              /

            2

            b

              /

            2

          ∫

            −
            t

              /

            2

            t

              /

            2

            [

                    x

                      2

                    σ

                      13

                  −

                    x

                      3

                    σ

                      12

                    x

                      3

                    σ

                      11

                  −

                    x

                      2

                    σ

                      11

            ]

        d

          x

            3

        d

          x

            2

        .

    {\displaystyle {\begin{bmatrix}M_{11}\M_{12}\M_{13}\end{bmatrix}}:=\int _{-b/2}^{b/2}\int {-t/2}^{t/2}{\begin{bmatrix}x{2}\sigma {13}-x{3}\sigma {12}\x{3}\sigma {11}\-x{2}\sigma {11}\end{bmatrix}}\,dx{3}\,dx_{2}\,.}

Stress resultants in plates and shells
For plates and shells, the x1 and x2 dimensions are much larger than the size in the x3 direction. Integration over the area of cross-section would have to include one of the larger dimensions and would lead to a model that is too simple for practical calculations. For this reason the stresses are only integrated through the thickness and the stress resultants are typically expressed in units of force per unit length (or moment per unit length) instead of the true force and moment as is the case for beams.

Membrane and shear forces
For plates and shells we have to consider two cross-sections. The first is perpendicular to the x1 axis and the second is perpendicular to the x2 axis. Following the same procedure as for beams, and keeping in mind that the resultants are now per unit length, we have

            F

            1

          ∫

            −
            t

              /

            2

            t

              /

            2

        (

          σ

            11

            e

            1

        +

          σ

            12

            e

            2

        +

          σ

            13

            e

            3

        )

        d

          x

            3

          and

            F

            2

          ∫

            −
            t

              /

            2

            t

              /

            2

        (

          σ

            12

            e

            1

        +

          σ

            22

            e

            2

        +

          σ

            23

            e

            3

        )

        d

          x

            3

    {\displaystyle \mathbf {F} _{1}=\int _{-t/2}^{t/2}(\sigma _{11}\mathbf {e} _{1}+\sigma _{12}\mathbf {e} _{2}+\sigma _{13}\mathbf {e} {3})\,dx{3}\quad {\text{and}}\quad \mathbf {F} _{2}=\int _{-t/2}^{t/2}(\sigma _{12}\mathbf {e} _{1}+\sigma _{22}\mathbf {e} _{2}+\sigma _{23}\mathbf {e} {3})\,dx{3}}

We can write the above as

            F

            1

          N

            11

            e

            1

        +

          N

            12

            e

            2

        +

          V

            1

            e

            3

          and

            F

            2

          N

            12

            e

            1

        +

          N

            22

            e

            2

        +

          V

            2

            e

            3

    {\displaystyle \mathbf {F} {1}=N{11}\mathbf {e} {1}+N{12}\mathbf {e} {2}+V{1}\mathbf {e} _{3}\quad {\text{and}}\quad \mathbf {F} {2}=N{12}\mathbf {e} {1}+N{22}\mathbf {e} {2}+V{2}\mathbf {e} _{3}}

where the membrane forces are defined as

            [

                    N

                      11

                    N

                      22

                    N

                      12

            ]

        :=

          ∫

            −
            t

              /

            2

            t

              /

            2

            [

                    σ

                      11

                    σ

                      22

                    σ

                      12

            ]

        d

          x

            3

    {\displaystyle {\begin{bmatrix}N_{11}\N_{22}\N_{12}\end{bmatrix}}:=\int _{-t/2}^{t/2}{\begin{bmatrix}\sigma _{11}\\sigma _{22}\\sigma {12}\end{bmatrix}}\,dx{3}}

and the shear forces are defined as

            [

                    V

                      1

                    V

                      2

            ]

          ∫

            −
            t

              /

            2

            t

              /

            2

            [

                    σ

                      13

                    σ

                      23

            ]

        d

          x

            3

        .

    {\displaystyle {\begin{bmatrix}V_{1}\V_{2}\end{bmatrix}}=\int _{-t/2}^{t/2}{\begin{bmatrix}\sigma _{13}\\sigma {23}\end{bmatrix}}\,dx{3}\,.}

Bending moments
For the bending moment resultants, we have

            M

            1

          ∫

            −
            t

              /

            2

            t

              /

            2

          r

        ×
        (

          σ

            11

            e

            1

        +

          σ

            12

            e

            2

        +

          σ

            13

            e

            3

        )

        d

          x

            3

          and

            M

            2

          ∫

            −
            t

              /

            2

            t

              /

            2

          r

        ×
        (

          σ

            12

            e

            1

        +

          σ

            22

            e

            2

        +

          σ

            23

            e

            3

        )

        d

          x

            3

    {\displaystyle \mathbf {M} _{1}=\int _{-t/2}^{t/2}\mathbf {r} \times (\sigma _{11}\mathbf {e} _{1}+\sigma _{12}\mathbf {e} _{2}+\sigma _{13}\mathbf {e} {3})\,dx{3}\quad {\text{and}}\quad \mathbf {M} _{2}=\int _{-t/2}^{t/2}\mathbf {r} \times (\sigma _{12}\mathbf {e} _{1}+\sigma _{22}\mathbf {e} _{2}+\sigma _{23}\mathbf {e} {3})\,dx{3}}

where r = x3 e3.
Expanding these expressions we have,

            M

            1

          ∫

            −
            t

              /

            2

            t

              /

            2

        [
        −

          x

            3

          σ

            12

            e

            1

        +

          x

            3

          σ

            11

            e

            2

        ]

        d

          x

            3

          and

            M

            2

          ∫

            −
            t

              /

            2

            t

              /

            2

        [
        −

          x

            3

          σ

            22

            e

            1

        +

          x

            3

          σ

            12

            e

            2

        ]

        d

          x

            3

    {\displaystyle \mathbf {M} _{1}=\int {-t/2}^{t/2}[-x{3}\sigma _{12}\mathbf {e} {1}+x{3}\sigma _{11}\mathbf {e} {2}]\,dx{3}\quad {\text{and}}\quad \mathbf {M} _{2}=\int {-t/2}^{t/2}[-x{3}\sigma _{22}\mathbf {e} {1}+x{3}\sigma _{12}\mathbf {e} {2}]\,dx{3}}

Define the bending moment resultants such that

            M

            1

        =:
        −

          M

            12

            e

            1

        +

          M

            11

            e

            2

          and

            M

            2

        =:
        −

          M

            22

            e

            1

        +

          M

            12

            e

            2

        .

    {\displaystyle \mathbf {M} {1}=:-M{12}\mathbf {e} {1}+M{11}\mathbf {e} _{2}\quad {\text{and}}\quad \mathbf {M} {2}=:-M{22}\mathbf {e} {1}+M{12}\mathbf {e} _{2}\,.}

Then, the bending moment resultants are given by

            [

                    M

                      11

                    M

                      22

                    M

                      12

            ]

        :=

          ∫

            −
            t

              /

            2

            t

              /

            2

          x

            3

            [

                    σ

                      11

                    σ

                      22

                    σ

                      12

            ]

        d

          x

            3

        .

    {\displaystyle {\begin{bmatrix}M_{11}\M_{22}\M_{12}\end{bmatrix}}:=\int {-t/2}^{t/2}x{3}\,{\begin{bmatrix}\sigma _{11}\\sigma _{22}\\sigma {12}\end{bmatrix}}\,dx{3}\,.}

These are the resultants that are often found in the literature but care has to be taken to make sure that the signs are correctly interpreted.
