# Screw theory

Screw theory

Screw theory is the algebraic calculation of pairs of vectors, also known as dual vectors – such as angular and linear velocity, or forces and moments – that arise in the kinematics and dynamics of rigid bodies.
Screw theory provides a mathematical formulation for the geometry of lines which is central to rigid body dynamics, where lines form the screw axes of spatial movement and the lines of action of forces. The pair of vectors that form the Plücker coordinates of a line define a unit screw, and general screws are obtained by multiplication by a pair of real numbers and addition of vectors.
Important theorems of screw theory include: the transfer principle proves that geometric calculations for points using vectors have parallel geometric calculations for lines obtained by replacing vectors with screws;
Chasles' theorem proves that any change between two rigid object poses can be performed by a single screw; the intermediate axis theorem proves that rotations about a rigid object's major and minor – but not intermediate – axes are stable.
Screw theory is an important tool in robot mechanics, mechanical design, computational geometry and multibody dynamics.
This is in part because of the relationship between screws and dual quaternions which have been used to interpolate rigid-body motions. Based on screw theory, an efficient approach has also been developed for the type synthesis of parallel mechanisms (parallel manipulators or parallel robots).

Basic concepts

A spatial displacement of a rigid body can be defined by a rotation about a line and a translation along the same line, called a screw motion; this is known as Chasles' theorem. The six parameters that define a screw motion are the four independent components of the Plücker vector that defines the screw axis, together with the rotation angle about and linear slide along this line, and form a pair of vectors called a screw. For comparison, the six parameters that define a spatial displacement can also be given by three Euler angles that define the rotation and the three components of the translation vector.

Screw
A screw is a six-dimensional vector constructed from a pair of three-dimensional vectors, such as forces and torques and linear and angular velocity, that arise in the study of spatial rigid body movement. The components of the screw define the Plücker coordinates of a line in space and the magnitudes of the vector along the line and moment about this line.

Twist
A twist is a screw used to represent the velocity of a rigid body as an angular velocity around an axis and a linear velocity along this axis. All points in the body have the same component of the velocity along the axis, however the greater the distance from the axis the greater the velocity in the plane perpendicular to this axis. Thus, the helicoidal field formed by the velocity vectors in a moving rigid body flattens out the further the points are radially from the twist axis.
The points in a body undergoing a constant twist motion trace helices in the fixed frame. If this screw motion has zero pitch then the trajectories trace circles, and the movement is a pure rotation. If the screw motion has infinite pitch then the trajectories are all straight lines in the same direction.

Wrench
The force and torque vectors that arise in applying Newton's laws to a rigid body can be assembled into a screw called a wrench. A force has a point of application and a line of action, therefore it defines the Plücker coordinates of a line in space and has zero pitch. A torque, on the other hand, is a pure moment that is not bound to a line in space and is an infinite pitch screw. The ratio of these two magnitudes defines the pitch of the screw.

Algebra of screws
Let a screw be an ordered pair

            S

        (

          S

        ,

          V

        )
        ,

    {\displaystyle {\mathsf {S}}=(\mathbf {S} ,\mathbf {V} ),}

where S and V are three-dimensional real vectors. The sum and difference of these ordered pairs are computed componentwise. Screws are often called dual vectors.
Now, introduce the ordered pair of real numbers â = (a, b), called a dual scalar. Let the addition and subtraction of these numbers be componentwise, and define multiplication as

                a

              ^

                c

              ^

        (
        a
        ,
        b
        )
        (
        c
        ,
        d
        )

        (
        a
        c
        ,
        a
        d
        +
        b
        c
        )
        .

    {\displaystyle {\hat {\mathsf {a}}}{\hat {\mathsf {c}}}=(a,b)(c,d)=(ac,ad+bc).}

The multiplication of a screw S = (S, V) by the dual scalar â = (a, b) is computed componentwise to be,

                a

              ^

            S

        (
        a
        ,
        b
        )
        (

          S

        ,

          V

        )

        (
        a

          S

        ,
        a

          V

        +
        b

          S

        )
        .

    {\displaystyle {\hat {\mathsf {a}}}{\mathsf {S}}=(a,b)(\mathbf {S} ,\mathbf {V} )=(a\mathbf {S} ,a\mathbf {V} +b\mathbf {S} ).}

Finally, introduce the dot and cross products of screws by the formulas:

            S

        ⋅

            T

        (

          S

        ,

          V

        )
        ⋅
        (

          T

        ,

          W

        )

        (

          S

        ⋅

          T

        ,

          S

        ⋅

          W

        +

          V

        ⋅

          T

        )
        ,

    {\displaystyle {\mathsf {S}}\cdot {\mathsf {T}}=(\mathbf {S} ,\mathbf {V} )\cdot (\mathbf {T} ,\mathbf {W} )=(\mathbf {S} \cdot \mathbf {T} ,\,\,\mathbf {S} \cdot \mathbf {W} +\mathbf {V} \cdot \mathbf {T} ),}

which is a dual scalar, and

            S

        ×

            T

        (

          S

        ,

          V

        )
        ×
        (

          T

        ,

          W

        )

        (

          S

        ×

          T

        ,

          S

        ×

          W

        +

          V

        ×

          T

        )
        ,

    {\displaystyle {\mathsf {S}}\times {\mathsf {T}}=(\mathbf {S} ,\mathbf {V} )\times (\mathbf {T} ,\mathbf {W} )=(\mathbf {S} \times \mathbf {T} ,\,\,\mathbf {S} \times \mathbf {W} +\mathbf {V} \times \mathbf {T} ),}

which is a screw. The dot and cross products of screws satisfy the identities of vector algebra, and allow computations that directly parallel computations in the algebra of vectors.
Let the dual scalar ẑ = (φ, d) define a dual angle, then the infinite series definitions of sine and cosine yield the relations

        sin
        ⁡

                z

              ^

        (
        sin
        ⁡
        φ
        ,
        d
        cos
        ⁡
        φ
        )
        ,

        cos
        ⁡

                z

              ^

        (
        cos
        ⁡
        φ
        ,
        −
        d
        sin
        ⁡
        φ
        )
        ,

    {\displaystyle \sin {\hat {\mathsf {z}}}=(\sin \varphi ,d\cos \varphi ),\,\,\,\cos {\hat {\mathsf {z}}}=(\cos \varphi ,-d\sin \varphi ),}

which are also dual scalars. In general, the function of a dual variable is defined to be f(ẑ) = (f(φ), df′(φ)), where f′(φ) is the derivative of f(φ).
These definitions allow the following results:

Unit screws are Plücker coordinates of a line and satisfy the relation

            S

                S

            ⋅

                S

        1
        ;

    {\displaystyle |{\mathsf {S}}|={\sqrt {{\mathsf {S}}\cdot {\mathsf {S}}}}=1;}

Let ẑ = (φ, d) be the dual angle, where φ is the angle between the axes of S and T around their common normal, and d is the distance between these axes along the common normal, then

            S

        ⋅

            T

              S

              T

        cos
        ⁡

                z

              ^

        ;

    {\displaystyle {\mathsf {S}}\cdot {\mathsf {T}}=\left|{\mathsf {S}}\right|\left|{\mathsf {T}}\right|\cos {\hat {\mathsf {z}}};}

Let N be the unit screw that defines the common normal to the axes of S and T, and ẑ = (φ, d) is the dual angle between these axes, then

            S

        ×

            T

              S

              T

        sin
        ⁡

                z

              ^

            N

        .

    {\displaystyle {\mathsf {S}}\times {\mathsf {T}}=\left|{\mathsf {S}}\right|\left|{\mathsf {T}}\right|\sin {\hat {\mathsf {z}}}{\mathsf {N}}.}

Wrench
A common example of a screw is the wrench associated with a force acting on a rigid body. Let P be the point of application of the force F and let P be the vector locating this point in a fixed frame. The wrench W = (F, P × F) is a screw. The resultant force and moment obtained from all the forces Fi, i = 1, ..., n, acting on a rigid body is simply the sum of the individual wrenches Wi, that is

            R

          ∑

            i

            1

            n

              W

            i

          ∑

            i

            1

            n

        (

            F

            i

        ,

            P

            i

        ×

            F

            i

        )
        .

    {\displaystyle {\mathsf {R}}=\sum {i=1}^{n}{\mathsf {W}}{i}=\sum _{i=1}^{n}(\mathbf {F} _{i},\mathbf {P} _{i}\times \mathbf {F} _{i}).}

Notice that the case of two equal but opposite forces F and −F acting at points A and B respectively, yields the resultant

            R

        (

          F

        −

          F

        ,

          A

        ×

          F

        −

          B

        ×

          F

        )

        (
        0
        ,
        (

          A

        −

          B

        )
        ×

          F

        )
        .

    {\displaystyle {\mathsf {R}}=(\mathbf {F} -\mathbf {F} ,\mathbf {A} \times \mathbf {F} -\mathbf {B} \times \mathbf {F} )=(0,(\mathbf {A} -\mathbf {B} )\times \mathbf {F} ).}

This shows that screws of the form

            M

        (
        0
        ,

          M

        )
        ,

    {\displaystyle {\mathsf {M}}=(0,\mathbf {M} ),}

can be interpreted as pure moments.

Twist
In order to define the twist of a rigid body, we must consider its movement defined by the parameterized set of spatial displacements, D(t) = ([A(t)], d(t)), where [A] is a rotation matrix and d is a translation vector. This causes a point p that is fixed in moving body coordinates to trace a curve P(t) in the fixed frame given by

          P

        (
        t
        )

        [
        A
        (
        t
        )
        ]

          p

        +

          d

        (
        t
        )
        .

    {\displaystyle \mathbf {P} (t)=[A(t)]\mathbf {p} +\mathbf {d} (t).}

The velocity of P is

            V

            P

        (
        t
        )

          [

                d
                A
                (
                t
                )

                d
                t

          ]

          p

        +

          v

        (
        t
        )
        ,

    {\displaystyle \mathbf {V} _{P}(t)=\left[{\frac {dA(t)}{dt}}\right]\mathbf {p} +\mathbf {v} (t),}

where v is velocity of the origin of the moving frame, that is dd/dt. Now substitute p = [AT](P − d) into this equation to obtain,

            V

            P

        (
        t
        )

        [
        Ω
        ]

          P

        +

          v

        −
        [
        Ω
        ]

          d

          or

            V

            P

        (
        t
        )

          ω

        ×

          P

        +

          v

        +

          d

        ×

          ω

        ,

    {\displaystyle \mathbf {V} _{P}(t)=[\Omega ]\mathbf {P} +\mathbf {v} -[\Omega ]\mathbf {d} \quad {\text{or}}\quad \mathbf {V} _{P}(t)=\mathbf {\omega } \times \mathbf {P} +\mathbf {v} +\mathbf {d} \times \mathbf {\omega } ,}

where [Ω] = [dA/dt][AT] is the angular velocity matrix and ω is the angular velocity vector.
The screw

            T

        (

              ω
              →

        ,

          v

        +

          d

        ×

              ω
              →

        )
        ,

    {\displaystyle {\mathsf {T}}=({\vec {\omega }},\mathbf {v} +\mathbf {d} \times {\vec {\omega }}),!}

is the twist of the moving body. The vector V = v + d × ω is the velocity of the point in the body that corresponds with the origin of the fixed frame.
There are two important special cases: (i) when d is constant, that is v = 0, then the twist is a pure rotation about a line, then the twist is

            T

        (
        ω
        ,

          d

        ×
        ω
        )
        ,

    {\displaystyle {\mathsf {T}}=(\omega ,\mathbf {d} \times \omega ),}

and (ii) when [Ω] = 0, that is the body does not rotate but only slides in the direction v, then the twist is a pure slide given by

            T

        (
        0
        ,

          v

        )
        .

    {\displaystyle {\mathsf {T}}=(0,\mathbf {v} ).}

Revolute joints
For a revolute joint, let the axis of rotation pass through the point q and be directed along the vector ω, then the twist for the joint is given by,

        ξ

            {

                    ω

                  q
                  ×

                    ω

            }

        .

    {\displaystyle \xi ={\begin{Bmatrix}{\boldsymbol {\omega }}\q\times {\boldsymbol {\omega }}\end{Bmatrix}}.}

Prismatic joints
For a prismatic joint, let the vector v pointing define the direction of the slide, then the twist for the joint is given by,

        ξ

            {

                  0

                  v

            }

        .

    {\displaystyle \xi ={\begin{Bmatrix}0\v\end{Bmatrix}}.}

Coordinate transformation of screws
The coordinate transformations for screws are easily understood by beginning with the coordinate transformations of the Plücker vector of line, which in turn are obtained from the transformations of the coordinate of points on the line.
Let the displacement of a body be defined by D = ([A], d), where [A] is the rotation matrix and d is the translation vector. Consider the line in the body defined by the two points p and q, which has the Plücker coordinates,

            q

        (

          q

        −

          p

        ,

          p

        ×

          q

        )
        ,

    {\displaystyle {\mathsf {q}}=(\mathbf {q} -\mathbf {p} ,\mathbf {p} \times \mathbf {q} ),}

then in the fixed frame we have the transformed point coordinates P = [A]p + d and Q = [A]q + d, which yield.

            Q

        (

          Q

        −

          P

        ,

          P

        ×

          Q

        )

        (
        [
        A
        ]
        (

          q

        −

          p

        )
        ,
        [
        A
        ]
        (

          p

        ×

          q

        )
        +

          d

        ×
        [
        A
        ]
        (

          q

        −

          p

        )
        )

    {\displaystyle {\mathsf {Q}}=(\mathbf {Q} -\mathbf {P} ,\mathbf {P} \times \mathbf {Q} )=([A](\mathbf {q} -\mathbf {p} ),[A](\mathbf {p} \times \mathbf {q} )+\mathbf {d} \times [A](\mathbf {q} -\mathbf {p} ))}

Thus, a spatial displacement defines a transformation for Plücker coordinates of lines given by

            {

                    Q

                  −

                    P

                    P

                  ×

                    Q

            }

            [

                  A

                  0

                  D
                  A

                  A

            ]

            {

                    q

                  −

                    p

                    p

                  ×

                    q

            }

        .

    {\displaystyle {\begin{Bmatrix}\mathbf {Q} -\mathbf {P} \\mathbf {P} \times \mathbf {Q} \end{Bmatrix}}={\begin{bmatrix}A&0\DA&A\end{bmatrix}}{\begin{Bmatrix}\mathbf {q} -\mathbf {p} \\mathbf {p} \times \mathbf {q} \end{Bmatrix}}.}

The matrix [D] is the skew-symmetric matrix that performs the cross product operation, that is [D]y = d × y.
The 6×6 matrix obtained from the spatial displacement D = ([A], d) can be assembled into the dual matrix

        [

                A

              ^

        ]

        (
        [
        A
        ]
        ,
        [
        D
        A
        ]
        )
        ,

    {\displaystyle [{\hat {\mathsf {A}}}]=([A],[DA]),}

which operates on a screw s = (s.v) to obtain,

            S

        [

                A

              ^

        ]

            s

        ,

        (

          S

        ,

          V

        )

        (
        [
        A
        ]
        ,
        [
        D
        A
        ]
        )
        (

          s

        ,

          v

        )

        (
        [
        A
        ]

          s

        ,
        [
        A
        ]

          v

        +
        [
        D
        A
        ]

          s

        )
        .

    {\displaystyle {\mathsf {S}}=[{\hat {\mathsf {A}}}]{\mathsf {s}},\quad (\mathbf {S} ,\mathbf {V} )=([A],[DA])(\mathbf {s} ,\mathbf {v} )=([A]\mathbf {s} ,[A]\mathbf {v} +[DA]\mathbf {s} ).}

The dual matrix [Â] = ([A], [DA]) has determinant 1 and is called a dual orthogonal matrix.

Twists as elements of a Lie algebra
Consider the movement of a rigid body defined by the parameterized 4x4 homogeneous transform,

            P

        (
        t
        )

        [
        T
        (
        t
        )
        ]

            p

            {

                      P

                  1

            }

            [

                  A
                  (
                  t
                  )

                      d

                  (
                  t
                  )

                  0

                  1

            ]

            {

                      p

                  1

            }

        .

    {\displaystyle {\textbf {P}}(t)=[T(t)]{\textbf {p}}={\begin{Bmatrix}{\textbf {P}}\1\end{Bmatrix}}={\begin{bmatrix}A(t)&{\textbf {d}}(t)\0&1\end{bmatrix}}{\begin{Bmatrix}{\textbf {p}}\1\end{Bmatrix}}.}

This notation does not distinguish between P = (X, Y, Z, 1), and P = (X, Y, Z), which is hopefully clear in context.
The velocity of this movement is defined by computing the velocity of the trajectories of the points in the body,

              V

            P

        [

              T
              ˙

        (
        t
        )
        ]

            p

            {

                        V

                      P

                  0

            }

            [

                        A
                        ˙

                  (
                  t
                  )

                          d

                        ˙

                  (
                  t
                  )

                  0

                  0

            ]

            {

                      p

                  1

            }

        .

    {\displaystyle {\textbf {V}}{P}=[{\dot {T}}(t)]{\textbf {p}}={\begin{Bmatrix}{\textbf {V}}{P}\0\end{Bmatrix}}={\begin{bmatrix}{\dot {A}}(t)&{\dot {\textbf {d}}}(t)\0&0\end{bmatrix}}{\begin{Bmatrix}{\textbf {p}}\1\end{Bmatrix}}.}

The dot denotes the derivative with respect to time, and because p is constant its derivative is zero.
Substitute the inverse transform for p into the velocity equation to obtain the velocity of P by operating on its trajectory P(t), that is

              V

            P

        [

              T
              ˙

        (
        t
        )
        ]
        [
        T
        (
        t
        )

          ]

            −
            1

            P

        (
        t
        )

        [
        S
        ]

            P

        ,

    {\displaystyle {\textbf {V}}_{P}=[{\dot {T}}(t)][T(t)]^{-1}{\textbf {P}}(t)=[S]{\textbf {P}},}

where

        [
        S
        ]

            [

                  Ω

                  −
                  Ω

                      d

                  +

                          d

                        ˙

                  0

                  0

            ]

            [

                  Ω

                    d

                  ×
                  ω
                  +

                    v

                  0

                  0

            ]

        .

    {\displaystyle [S]={\begin{bmatrix}\Omega &-\Omega {\textbf {d}}+{\dot {\textbf {d}}}\0&0\end{bmatrix}}={\begin{bmatrix}\Omega &\mathbf {d} \times \omega +\mathbf {v} \0&0\end{bmatrix}}.}

Recall that [Ω] is the angular velocity matrix. The matrix [S] is an element of the Lie algebra se(3) of the Lie group SE(3) of homogeneous transforms. The components of [S] are the components of the twist screw, and for this reason [S] is also often called a twist.
From the definition of the matrix [S], we can formulate the ordinary differential equation,

        [

              T
              ˙

        (
        t
        )
        ]

        [
        S
        ]
        [
        T
        (
        t
        )
        ]
        ,

    {\displaystyle [{\dot {T}}(t)]=[S][T(t)],}

and ask for the movement [T(t)] that has a constant twist matrix [S]. The solution is the matrix exponential

        [
        T
        (
        t
        )
        ]

          e

            [
            S
            ]
            t

        .

    {\displaystyle [T(t)]=e^{[S]t}.}

This formulation can be generalized such that given an initial configuration g(0) in SE(n), and a twist ξ in se(n), the homogeneous transformation to a new location and orientation can be computed with the formula,

        g
        (
        θ
        )

        exp
        ⁡
        (
        ξ
        θ
        )
        g
        (
        0
        )
        ,

    {\displaystyle g(\theta )=\exp(\xi \theta )g(0),}

where θ represents the parameters of the transformation.

Screws by reflection
In transformation geometry, the elemental concept of transformation is the reflection (mathematics). In planar transformations a translation is obtained by reflection in parallel lines, and rotation is obtained by reflection in a pair of intersecting lines. To produce a screw transformation from similar concepts one must use planes in space: the parallel planes must be perpendicular to the screw axis, which is the line of intersection of the intersecting planes that generate the rotation of the screw. Thus four reflections in planes effect a screw transformation. The tradition of inversive geometry borrows some of the ideas of projective geometry and provides a language of transformation that does not depend on analytic geometry.

Homography
The combination of a translation with a rotation effected by a screw displacement can be illustrated with the exponential mapping.
Since ε2 = 0 for dual numbers, exp(aε) = 1 + aε, all other terms of the exponential series vanishing.
Let F = {1 + εr : r ∈ H}, ε2 = 0.
Note that F is stable under the rotation q → p−1qp and under the translation (1 + εr)(1 + εs) = 1 + ε(r + s) for any vector quaternions r and s.
F is a 3-flat in the eight-dimensional space of dual quaternions. This 3-flat F represents space, and the homography constructed, restricted to F, is a screw displacement of space.
Let a be half the angle of the desired turn about axis r, and br half the displacement on the screw axis. Then form z = exp((a + bε)r) and z* = exp((a − bε)r). Now the homography is

        [
        q
        :
        1
        ]

            (

                  z

                  0

                  0

                    z

                      ∗

            )

        [
        q
        z
        :

          z

            ∗

        ]
        ∼
        [
        (

          z

            ∗

          )

            −
            1

        q
        z
        :
        1
        ]
        .

    {\displaystyle [q:1]{\begin{pmatrix}z&0\0&z^{}\end{pmatrix}}=[qz:z^{}]\thicksim [(z^{*})^{-1}qz:1].}

The inverse for z* is

            1

              exp
              ⁡
              (
              a
              r
              −
              b
              ε
              r
              )

        (

          e

            a
            r

          e

            −
            b
            r
            ε

          )

            −
            1

          e

            b
            r
            ε

          e

            −
            a
            r

        ,

    {\displaystyle {\frac {1}{\exp(ar-b\varepsilon r)}}=(e^{ar}e^{-br\varepsilon })^{-1}=e^{br\varepsilon }e^{-ar},}

so, the homography sends q to

        (

          e

            b
            ε

          e

            −
            a
            r

        )
        q
        (

          e

            a
            r

          e

            b
            ε
            r

        )

          e

            b
            ε
            r

        (

          e

            −
            a
            r

        q

          e

            a
            r

        )

          e

            b
            ε
            r

          e

            2
            b
            ε
            r

        (

          e

            −
            a
            r

        q

          e

            a
            r

        )
        .

    {\displaystyle (e^{b\varepsilon }e^{-ar})q(e^{ar}e^{b\varepsilon r})=e^{b\varepsilon r}(e^{-ar}qe^{ar})e^{b\varepsilon r}=e^{2b\varepsilon r}(e^{-ar}qe^{ar}).}

Now for any quaternion vector p, p* = −p, let q = 1 + pε ∈ F, where the required rotation and translation are effected.
Evidently the group of units of the ring of dual quaternions is a Lie group. A subgroup has Lie algebra generated by the parameters a r and b s, where a, b ∈ R, and r, s ∈ H. These six parameters generate a subgroup of the units, the unit sphere. Of course it includes F and the 3-sphere of versors.

Work of forces acting on a rigid body
Consider the set of forces F1, F2 ... Fn act on the points X1, X2 ... Xn in a rigid body. The trajectories of Xi, i = 1,...,n are defined by the movement of the rigid body with rotation [A(t)] and the translation d(t) of a reference point in the body, given by

            X

            i

        (
        t
        )

        [
        A
        (
        t
        )
        ]

            x

            i

        +

          d

        (
        t
        )

        i

        1
        ,
        …
        ,
        n
        ,

    {\displaystyle \mathbf {X} _{i}(t)=[A(t)]\mathbf {x} _{i}+\mathbf {d} (t)\quad i=1,\ldots ,n,}

where xi are coordinates in the moving body.
The velocity of each point Xi is

            V

            i

              ω
              →

        ×
        (

            X

            i

        −

          d

        )
        +

          v

        ,

    {\displaystyle \mathbf {V} _{i}={\vec {\omega }}\times (\mathbf {X} _{i}-\mathbf {d} )+\mathbf {v} ,}

where ω is the angular velocity vector and v is the derivative of d(t).
The work by the forces over the displacement δri=viδt of each point is given by

        δ
        W

            F

            1

        ⋅

            V

            1

        δ
        t
        +

            F

            2

        ⋅

            V

            2

        δ
        t
        +
        ⋯
        +

            F

            n

        ⋅

            V

            n

        δ
        t
        .

    {\displaystyle \delta W=\mathbf {F} _{1}\cdot \mathbf {V} _{1}\delta t+\mathbf {F} _{2}\cdot \mathbf {V} _{2}\delta t+\cdots +\mathbf {F} _{n}\cdot \mathbf {V} _{n}\delta t.}

Define the velocities of each point in terms of the twist of the moving body to obtain

        δ
        W

          ∑

            i

            1

            n

            F

            i

        ⋅
        (

              ω
              →

        ×
        (

            X

            i

        −

          d

        )
        +

          v

        )
        δ
        t
        .

    {\displaystyle \delta W=\sum _{i=1}^{n}\mathbf {F} _{i}\cdot ({\vec {\omega }}\times (\mathbf {X} _{i}-\mathbf {d} )+\mathbf {v} )\delta t.}

Expand this equation and collect coefficients of ω and v to obtain

                δ
                W

                  (

                      ∑

                        i

                        1

                        n

                        F

                        i

                  )

                ⋅

                  d

                ×

                      ω
                      →

                δ
                t
                +

                  (

                      ∑

                        i

                        1

                        n

                        F

                        i

                  )

                ⋅

                  v

                δ
                t
                +

                  (

                      ∑

                        i

                        1

                        n

                        X

                        i

                    ×

                        F

                        i

                  )

                ⋅

                      ω
                      →

                δ
                t

                  (

                      ∑

                        i

                        1

                        n

                        F

                        i

                  )

                ⋅
                (

                  v

                +

                  d

                ×

                      ω
                      →

                )
                δ
                t
                +

                  (

                      ∑

                        i

                        1

                        n

                        X

                        i

                    ×

                        F

                        i

                  )

                ⋅

                      ω
                      →

                δ
                t
                .

    {\displaystyle {\begin{aligned}\delta W&=\left(\sum _{i=1}^{n}\mathbf {F} _{i}\right)\cdot \mathbf {d} \times {\vec {\omega }}\delta t+\left(\sum _{i=1}^{n}\mathbf {F} _{i}\right)\cdot \mathbf {v} \delta t+\left(\sum _{i=1}^{n}\mathbf {X} _{i}\times \mathbf {F} _{i}\right)\cdot {\vec {\omega }}\delta t\[4pt]&=\left(\sum _{i=1}^{n}\mathbf {F} _{i}\right)\cdot (\mathbf {v} +\mathbf {d} \times {\vec {\omega }})\delta t+\left(\sum _{i=1}^{n}\mathbf {X} _{i}\times \mathbf {F} _{i}\right)\cdot {\vec {\omega }}\delta t.\end{aligned}}}

Introduce the twist of the moving body and the wrench acting on it given by

            T

        (

              ω
              →

        ,

          d

        ×

              ω
              →

        +

          v

        )

        (

          T

        ,

            T

            ∘

        )
        ,

            W

          (

              ∑

                i

                1

                n

                F

                i

            ,

              ∑

                i

                1

                n

                X

                i

            ×

                F

                i

          )

        (

          W

        ,

            W

            ∘

        )
        ,

    {\displaystyle {\mathsf {T}}=({\vec {\omega }},\mathbf {d} \times {\vec {\omega }}+\mathbf {v} )=(\mathbf {T} ,\mathbf {T} ^{\circ }),\quad {\mathsf {W}}=\left(\sum _{i=1}^{n}\mathbf {F} _{i},\sum _{i=1}^{n}\mathbf {X} _{i}\times \mathbf {F} _{i}\right)=(\mathbf {W} ,\mathbf {W} ^{\circ }),}

then work takes the form

        δ
        W

        (

          W

        ⋅

            T

            ∘

        +

            W

            ∘

        ⋅

          T

        )
        δ
        t
        .

    {\displaystyle \delta W=(\mathbf {W} \cdot \mathbf {T} ^{\circ }+\mathbf {W} ^{\circ }\cdot \mathbf {T} )\delta t.}

The 6×6 matrix [Π] is used to simplify the calculation of work using screws, so that

        δ
        W

        (

          W

        ⋅

            T

            ∘

        +

            W

            ∘

        ⋅

          T

        )
        δ
        t

            W

        [
        Π
        ]

            T

        δ
        t
        ,

    {\displaystyle \delta W=(\mathbf {W} \cdot \mathbf {T} ^{\circ }+\mathbf {W} ^{\circ }\cdot \mathbf {T} )\delta t={\mathsf {W}}[\Pi ]{\mathsf {T}}\delta t,}

where

        [
        Π
        ]

            [

                  0

                  I

                  I

                  0

            ]

        ,

    {\displaystyle [\Pi ]={\begin{bmatrix}0&I\I&0\end{bmatrix}},}

and [I] is the 3×3 identity matrix.

Reciprocal screws
If the virtual work of a wrench on a twist is zero, then the forces and torque of the wrench are constraint forces relative to the twist. The wrench and twist are said to be reciprocal, that is if

        δ
        W

            W

        [
        Π
        ]

            T

        δ
        t

        0
        ,

    {\displaystyle \delta W={\mathsf {W}}[\Pi ]{\mathsf {T}}\delta t=0,}

then the screws W and T are reciprocal.

Twists in robotics
In the study of robotic systems the components of the twist are often transposed to eliminate the need for the 6×6 matrix [Π] in the calculation of work. In this case the twist is defined to be

                T

              ˇ

        (

          d

        ×

              ω
              →

        +

          v

        ,

              ω
              →

        )
        ,

    {\displaystyle {\check {\mathsf {T}}}=(\mathbf {d} \times {\vec {\omega }}+\mathbf {v} ,{\vec {\omega }}),}

so the calculation of work takes the form

        δ
        W

            W

        ⋅

                T

              ˇ

        δ
        t
        .

    {\displaystyle \delta W={\mathsf {W}}\cdot {\check {\mathsf {T}}}\delta t.}

In this case, if

        δ
        W

            W

        ⋅

                T

              ˇ

        δ
        t

        0
        ,

    {\displaystyle \delta W={\mathsf {W}}\cdot {\check {\mathsf {T}}}\delta t=0,}

then the wrench W is reciprocal to the twist T.

History
In 1763, Giulio Giuseppe Mozzi showed that every rigid-body motion can be represented as a “twist”. This result was also associated with Michel Chasles and it became known as Chasles' theorem. In his Élements de Statique (1803), Louis Poinsot introduced many modern concepts of statics. He introduced what become known in English as "wrench". Julius Plücker in 1846 introduced the concept of a dyname, a 6-dimensional vector whose first three components represent the force, while the last three represent the couple.
A complete mathematical framework was developed by Sir Robert Stawell Ball in 1876 for application in kinematics and statics of mechanisms (rigid body mechanics). Screw theory was introduced to France by Paul Émile Appell in his Traité de Mécanique Rationnelle (1893) which became a standard topic in engineering in France (French: théorie de torseurs).
Felix Klein saw screw theory as an application of elliptic geometry and his Erlangen program. He also worked out elliptic geometry, and a fresh view of Euclidean geometry, with the Cayley–Klein metric. The use of a symmetric matrix for a von Staudt conic and metric, applied to screws, has been described by Harvey Lipkin. Other prominent contributors include August Ferdinand Möbius, Edward Routh, Eduard Study, Richard von Mises, W. K. Clifford, F. M. Dimentberg, Kenneth H. Hunt, J. R. Phillips.
The homography idea in transformation geometry was advanced by Sophus Lie more than a century ago. Even earlier, William Rowan Hamilton displayed the versor form of unit quaternions as

        exp
        ⁡
        (
        a
        r
        )

        cos
        ⁡
        a
        +
        r
        sin
        ⁡
        a

    {\textstyle \exp(ar)=\cos a+r\sin a}

. The idea is also in Euler's formula parametrizing the unit circle in the complex plane.
William Kingdon Clifford initiated the use of dual quaternions for kinematics, followed by Aleksandr Kotelnikov, Eduard Study (Geometrie der Dynamen), and Wilhelm Blaschke. However, the point of view of Sophus Lie has recurred.
In 1940, Julian Coolidge described the use of dual quaternions for screw displacements on page 261 of A History of Geometrical Methods. He notes the 1885 contribution of Arthur Buchheim. Coolidge based his description simply on the tools Hamilton had used for real quaternions.
