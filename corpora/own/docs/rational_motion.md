# Rational motion

Rational motion

In kinematics, the motion of a rigid body is defined as a continuous set of displacements. One-parameter motions can be defined
as a continuous displacement of moving object with respect to a fixed frame in Euclidean three-space (E3), where the displacement depends on one parameter, mostly identified as time.
Rational motions are defined by rational functions (ratio of two polynomial functions) of time. They produce rational trajectories, and therefore they integrate well with the existing NURBS (Non-Uniform Rational B-Spline) based industry standard CAD/CAM systems. They are readily amenable to the applications of existing computer-aided geometric design (CAGD) algorithms. By combining kinematics of rigid body motions with NURBS geometry of curves and surfaces, methods have been developed for computer-aided design of rational motions.
These CAD methods for motion design find applications in animation in computer graphics (key frame interpolation), trajectory planning in robotics (taught-position interpolation), spatial navigation in virtual reality, computer-aided geometric design of motion via interactive interpolation, CNC tool path planning, and task specification in mechanism synthesis.

Background
There has been a great deal of research in applying the principles of computer-aided geometric design (CAGD) to the problem of computer-aided motion design.
In recent years, it has been well established that rational Bézier and rational B-spline based curve representation schemes can be combined with dual quaternion representation of spatial displacements to obtain rational Bézier and B-spline
motions. Ge and Ravani, developed a new framework for geometric constructions
of spatial motions by combining the concepts from kinematics and CAGD. Their work was built upon the seminal paper of Shoemake, in which he
used the concept of a quaternion for rotation interpolation. A detailed list of references on this topic can be found in and.

Rational Bézier and B-spline motions
Let

                q

              ^

            q

        +
        ε

              q

            0

    {\displaystyle {\hat {\textbf {q}}}={\textbf {q}}+\varepsilon {\textbf {q}}^{0}}

denote a unit dual quaternion. A homogeneous dual quaternion may be
written as a pair of quaternions,

                Q

              ^

            Q

        +
        ε

              Q

            0

    {\displaystyle {\hat {\textbf {Q}}}={\textbf {Q}}+\varepsilon {\textbf {Q}}^{0}}

; where

            Q

        w

            q

        ,

              Q

            0

        w

              q

            0

        +

          w

            0

            q

    {\displaystyle {\textbf {Q}}=w{\textbf {q}},{\textbf {Q}}^{0}=w{\textbf {q}}^{0}+w^{0}{\textbf {q}}}

. This is obtained by
expanding

                Q

              ^

              w
              ^

                q

              ^

    {\displaystyle {\hat {\textbf {Q}}}={\hat {w}}{\hat {\textbf {q}}}}

 using
dual number algebra (here,

              w
              ^

        w
        +
        ε

          w

            0

    {\displaystyle {\hat {w}}=w+\varepsilon w^{0}}

).
In terms of dual quaternions and the homogeneous coordinates of a point

            P

        :
        (

          P

            1

        ,

          P

            2

        ,

          P

            3

        ,

          P

            4

        )

    {\displaystyle {\textbf {P}}:(P_{1},P_{2},P_{3},P_{4})}

 of the object, the transformation equation in terms of quaternions is given by

                P

              ~

            Q

            P

              Q

            ∗

        +

          P

            4

        [
        (

              Q

            0

        )

              Q

            ∗

        −

            Q

        (

              Q

            0

          )

            ∗

        ]
        ,

    {\displaystyle {\tilde {\textbf {P}}}={\textbf {Q}}{\textbf {P}}{\textbf {Q}}^{\ast }+P_{4}[({\textbf {Q}}^{0}){\textbf {Q}}^{\ast }-{\textbf {Q}}({\textbf {Q}}^{0})^{\ast }],}

where

              Q

            ∗

    {\displaystyle {\textbf {Q}}^{\ast }}

 and

        (

              Q

            0

          )

            ∗

    {\displaystyle ({\textbf {Q}}^{0})^{\ast }}

 are
conjugates of

            Q

    {\displaystyle {\textbf {Q}}}

 and

              Q

            0

    {\displaystyle {\textbf {Q}}^{0}}

, respectively and

                P

              ~

    {\displaystyle {\tilde {\textbf {P}}}}

 denotes homogeneous coordinates of the point after the displacement.
Given a set of unit dual quaternions and dual weights

                  q

                ^

            i

        ,

                w
                ^

            i

        ;
        i

        0...
        n

    {\displaystyle {\hat {\textbf {q}}}{i},{\hat {w}}{i};i=0...n}

 respectively, the
following represents a rational Bézier curve in the space of
dual quaternions.

                Q

              ^

        (
        t
        )

          ∑

            i

            0

            n

            B

              i

              n

          (
          t
          )

                    Q

                  ^

              i

          ∑

            i

            0

            n

            B

              i

              n

          (
          t
          )

                  w
                  ^

              i

                    q

                  ^

              i

    {\displaystyle {\hat {\textbf {Q}}}(t)=\sum \limits {i=0}^{n}{B{i}^{n}(t){\hat {\textbf {Q}}}_{i}}=\sum \limits {i=0}^{n}{B{i}^{n}(t){\hat {w}}{i}{\hat {\textbf {q}}}{i}}}

where

          B

            i

            n

        (
        t
        )

    {\displaystyle B_{i}^{n}(t)}

 are the Bernstein polynomials. The Bézier dual quaternion curve given by above equation defines a rational Bézier motion of
degree

        2
        n

    {\displaystyle 2n}

.
Similarly, a B-spline dual quaternion curve, which defines a NURBS
motion of degree 2p, is given by,

                Q

              ^

        (
        t
        )

          ∑

            i

            0

            n

            N

              i
              ,
              p

          (
          t
          )

                    Q

                  ^

              i

          ∑

            i

            0

            n

            N

              i
              ,
              p

          (
          t
          )

                  w
                  ^

              i

                    q

                  ^

              i

    {\displaystyle {\hat {\textbf {Q}}}(t)=\sum \limits {i=0}^{n}{N{i,p}(t){\hat {\textbf {Q}}}_{i}}=\sum \limits {i=0}^{n}{N{i,p}(t){\hat {w}}{i}{\hat {\textbf {q}}}{i}}}

where

          N

            i
            ,
            p

        (
        t
        )

    {\displaystyle N_{i,p}(t)}

 are the pth-degree B-spline basis functions.
A representation for the rational Bézier motion and rational B-spline motion in the Cartesian space can be obtained by substituting either of the above two preceding expressions for

                Q

              ^

        (
        t
        )

    {\displaystyle {\hat {\textbf {Q}}}(t)}

 in the equation for point transform. In what follows, we deal with the case of rational Bézier motion. The trajectory of a point undergoing rational Bézier motion is given by,

                  P

                ~

            2
            n

        (
        t
        )

        [

          H

            2
            n

        (
        t
        )
        ]

            P

        ,

    {\displaystyle {\tilde {\textbf {P}}}^{2n}(t)=[H^{2n}(t)]{\textbf {P}},}

          H

            2
            n

        (
        t
        )
        ]

          ∑

            k

            0

            2
            n

            B

              k

              2
              n

          (
          t
          )
          [

            H

              k

          ]

        ,

    {\displaystyle H^{2n}(t)]=\sum \limits {k=0}^{2n}{B{k}^{2n}(t)[H_{k}]},}

where

        [

          H

            2
            n

        (
        t
        )
        ]

    {\displaystyle [H^{2n}(t)]}

 is the matrix
representation of the rational Bézier motion of degree

        2
        n

    {\displaystyle 2n}

 in Cartesian space. The following matrices

        [

          H

            k

        ]

    {\displaystyle [H_{k}]}

 (also referred to as Bézier Control
Matrices) define the affine control structure of the motion:

        [

          H

            k

        ]

            1

              C

                k

                2
                n

          ∑

            i
            +
            j

            k

            C

              i

              n

            C

              j

              n

            w

              i

            w

              j

          [

            H

              i
              j

              ∗

          ]

        ,

    {\displaystyle [H_{k}]={\frac {1}{C_{k}^{2n}}}\sum \limits {i+j=k}{C{i}^{n}C_{j}^{n}w_{i}w_{j}[H_{ij}^{\ast }]},}

where

        [

          H

            i
            j

            ∗

        ]

        [

          H

            i

            +

        ]
        [

          H

            j

            −

        ]
        +
        [

          H

            j

            −

        ]
        [

          H

            i

            0
            +

        ]
        −
        [

          H

            i

            +

        ]
        [

          H

            j

            0
            −

        ]
        +
        (

          α

            i

        −

          α

            j

        )
        [

          H

            j

            −

        ]
        [

          Q

            i

            +

        ]

    {\displaystyle [H_{ij}^{\ast }]=[H_{i}^{+}][H_{j}^{-}]+[H_{j}^{-}][H_{i}^{0+}]-[H_{i}^{+}][H_{j}^{0-}]+(\alpha _{i}-\alpha {j})[H{j}^{-}][Q_{i}^{+}]}

.
In the above equations,

          C

            i

            n

    {\displaystyle C_{i}^{n}}

 and

          C

            j

            n

    {\displaystyle C_{j}^{n}}

are binomial coefficients and

          α

            i

          w

            i

            0

          /

          w

            i

        ,

          α

            j

          w

            j

            0

          /

          w

            j

    {\displaystyle \alpha {i}=w{i}^{0}/w_{i},\alpha {j}=w{j}^{0}/w_{j}}

 are the weight ratios and

        [

          H

            j

            −

        ]

          [

                    q

                      j
                      ,
                      4

                  −

                    q

                      j
                      ,
                      3

                    q

                      j
                      ,
                      2

                  −

                    q

                      j
                      ,
                      1

                    q

                      j
                      ,
                      3

                    q

                      j
                      ,
                      4

                  −

                    q

                      j
                      ,
                      1

                  −

                    q

                      j
                      ,
                      2

                  −

                    q

                      j
                      ,
                      2

                    q

                      j
                      ,
                      1

                    q

                      j
                      ,
                      4

                  −

                    q

                      j
                      ,
                      3

                    q

                      j
                      ,
                      1

                    q

                      j
                      ,
                      2

                    q

                      j
                      ,
                      3

                    q

                      j
                      ,
                      4

          ]

        ,

    {\displaystyle [H_{j}^{-}]=\left[{\begin{array}{rrrr}q_{j,4}&-q_{j,3}&q_{j,2}&-q_{j,1}\q_{j,3}&q_{j,4}&-q_{j,1}&-q_{j,2}\-q_{j,2}&q_{j,1}&q_{j,4}&-q_{j,3}\q_{j,1}&q_{j,2}&q_{j,3}&q_{j,4}\\end{array}}\right],}

        [

          Q

            i

            +

        ]

          [

                  0

                  0

                  0

                    q

                      i
                      ,
                      1

                  0

                  0

                  0

                    q

                      i
                      ,
                      2

                  0

                  0

                  0

                    q

                      i
                      ,
                      3

                  0

                  0

                  0

                    q

                      i
                      ,
                      4

          ]

        ,

    {\displaystyle [Q_{i}^{+}]=\left[{\begin{array}{rrrr}0&0&0&q_{i,1}\0&0&0&q_{i,2}\0&0&0&q_{i,3}\0&0&0&q_{i,4}\\end{array}}\right],}

        [

          H

            i

            0
            +

        ]

          [

                  0

                  0

                  0

                    q

                      i
                      ,
                      1

                      0

                  0

                  0

                  0

                    q

                      i
                      ,
                      2

                      0

                  0

                  0

                  0

                    q

                      i
                      ,
                      3

                      0

                  0

                  0

                  0

                    q

                      i
                      ,
                      4

                      0

          ]

        ,

    {\displaystyle [H_{i}^{0+}]=\left[{\begin{array}{rrrr}0&0&0&q_{i,1}^{0}\0&0&0&q_{i,2}^{0}\0&0&0&q_{i,3}^{0}\0&0&0&q_{i,4}^{0}\\end{array}}\right],}

        [

          H

            j

            0
            −

        ]

          [

                  0

                  0

                  0

                  −

                    q

                      j
                      ,
                      1

                      0

                  0

                  0

                  0

                  −

                    q

                      j
                      ,
                      2

                      0

                  0

                  0

                  0

                  −

                    q

                      j
                      ,
                      3

                      0

                  0

                  0

                  0

                    q

                      j
                      ,
                      4

                      0

          ]

        ,

    {\displaystyle [H_{j}^{0-}]=\left[{\begin{array}{rrrr}0&0&0&-q_{j,1}^{0}\0&0&0&-q_{j,2}^{0}\0&0&0&-q_{j,3}^{0}\0&0&0&q_{j,4}^{0}\\end{array}}\right],}

        [

          H

            i

            +

        ]

          [

                    q

                      i
                      ,
                      4

                  −

                    q

                      i
                      ,
                      3

                    q

                      i
                      ,
                      2

                    q

                      i
                      ,
                      1

                    q

                      i
                      ,
                      3

                    q

                      i
                      ,
                      4

                  −

                    q

                      i
                      ,
                      1

                    q

                      i
                      ,
                      2

                  −

                    q

                      i
                      ,
                      2

                    q

                      i
                      ,
                      1

                    q

                      i
                      ,
                      4

                    q

                      i
                      ,
                      3

                  −

                    q

                      i
                      ,
                      1

                  −

                    q

                      i
                      ,
                      2

                  −

                    q

                      i
                      ,
                      3

                    q

                      i
                      ,
                      4

          ]

        .

    {\displaystyle [H_{i}^{+}]=\left[{\begin{array}{rrrr}q_{i,4}&-q_{i,3}&q_{i,2}&q_{i,1}\q_{i,3}&q_{i,4}&-q_{i,1}&q_{i,2}\-q_{i,2}&q_{i,1}&q_{i,4}&q_{i,3}\-q_{i,1}&-q_{i,2}&-q_{i,3}&q_{i,4}\\end{array}}\right].}

In above matrices,

        (

          q

            i
            ,
            1

        ,

          q

            i
            ,
            2

        ,

          q

            i
            ,
            3

        ,

          q

            i
            ,
            4

        )

    {\displaystyle (q_{i,1},q_{i,2},q_{i,3},q_{i,4})}

are four components of the real part

        (

              q

            i

        )

    {\displaystyle ({\textbf {q}}_{i})}

 and

        (

          q

            i
            ,
            1

            0

        ,

          q

            i
            ,
            2

            0

        ,

          q

            i
            ,
            3

            0

        ,

          q

            i
            ,
            4

            0

        )

    {\displaystyle (q_{i,1}^{0},q_{i,2}^{0},q_{i,3}^{0},q_{i,4}^{0})}

 are four
components of the dual part

        (

              q

            i

            0

        )

    {\displaystyle ({\textbf {q}}_{i}^{0})}

 of the unit
dual quaternion

        (

                  q

                ^

            i

        )

    {\displaystyle ({\hat {\textbf {q}}}_{i})}

.

Example
