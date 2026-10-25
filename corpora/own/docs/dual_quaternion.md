# Dual quaternion

Dual quaternion

In mathematics, the dual quaternions are an 8-dimensional real algebra isomorphic to the tensor product of the quaternions and the dual numbers. Thus, they may be constructed in the same way as the quaternions, except using dual numbers instead of real numbers as coefficients. A dual quaternion can be represented in the form A + εB, where A and B are ordinary quaternions and ε is the dual unit, which satisfies ε2 = 0 and commutes with every element of the algebra.
Unlike quaternions, the dual quaternions do not form a division algebra.
In mechanics, the dual quaternions are applied as a number system to represent rigid transformations in three dimensions. Since the space of dual quaternions is 8-dimensional and a rigid transformation has six real degrees of freedom, three for translations and three for rotations, dual quaternions obeying two algebraic constraints are used in this application. Since unit quaternions are subject to two algebraic constraints, unit quaternions are standard to represent rigid transformations.
Similar to the way that rotations in 3D space can be represented by quaternions of unit length, rigid motions in 3D space can be represented by dual quaternions of unit length. This fact is used in theoretical kinematics (see McCarthy), and in applications to 3D computer graphics, robotics and computer vision. Polynomials with coefficients given by (non-zero real norm) dual quaternions have also been used in the context of mechanical linkages design.

History
W. R. Hamilton introduced quaternions in 1843, and by 1873 W. K. Clifford obtained a broad generalization of these numbers that he called biquaternions, which is an example of what is now called a Clifford algebra.
In 1898 Alexander McAulay used Ω with Ω2 = 0 to generate the dual quaternion algebra. However, his terminology of "octonions" did not stick as today's octonions are another algebra.
In 1891 Eduard Study realized that this associative algebra was ideal for describing the group of motions of three-dimensional space. He further developed the idea in Geometrie der Dynamen in 1901.
B. L. van der Waerden called the structure "Study biquaternions", one of three eight-dimensional algebras referred to as biquaternions.
In 1895, Russian mathematician Aleksandr Kotelnikov developed dual vectors and dual quaternions for use in the study of mechanics.

Formulas
In order to describe operations with dual quaternions, it is helpful to first consider quaternions.
A quaternion is a linear combination of the basis elements 1, i, j, and k. Hamilton's rules for products of i, j, and k is

          i

            2

          j

            2

          k

            2

        i
        j
        k

        −
        1.

    {\displaystyle i^{2}=j^{2}=k^{2}=ijk=-1.}

Compute i ( i j k ) = −j k = −i, to obtain j k = i, and ( i j k ) k = −i j = −k or i j = k. Now because j ( j k ) = j i = −k, we see that this product yields i j = −j i, which shows that i, j, and k satisfy the anticommutative property.
A convenient way to work with the quaternion product is to write a quaternion as the sum of a scalar and a vector (strictly speaking a bivector), that is A = a0 + A, where a0 is a real number and A = A1 i + A2 j + A3 k is a three dimensional vector. The vector dot and cross operations can now be used to define the quaternion product of A = a0 + A and C = c0 + C as

        G

        A
        C

        (

          a

            0

        +

          A

        )
        (

          c

            0

        +

          C

        )

        (

          a

            0

          c

            0

        −

          A

        ⋅

          C

        )
        +
        (

          c

            0

          A

        +

          a

            0

          C

        +

          A

        ×

          C

        )
        .

    {\displaystyle G=AC=(a_{0}+\mathbf {A} )(c_{0}+\mathbf {C} )=(a_{0}c_{0}-\mathbf {A} \cdot \mathbf {C} )+(c_{0}\mathbf {A} +a_{0}\mathbf {C} +\mathbf {A} \times \mathbf {C} ).}

A dual quaternion is usually described as a quaternion with dual numbers as coefficients. A dual number is an ordered pair â = ( a, b ). Two dual numbers add componentwise and multiply by the rule â ĉ = ( a, b ) ( c, d ) = (a c, a d + b c). Dual numbers are often written in the form â = a + εb, where ε is the dual unit that commutes with i, j, k and has the property ε2 = 0.
The result is that a dual quaternion can be written as an ordered pair of quaternions ( A, B ). Two dual quaternions add componentwise and multiply by the rule,

              A
              ^

              C
              ^

        (
        A
        ,
        B
        )
        (
        C
        ,
        D
        )

        (
        A
        C
        ,
        A
        D
        +
        B
        C
        )
        .

    {\displaystyle {\hat {A}}{\hat {C}}=(A,B)(C,D)=(AC,AD+BC).}

It is convenient to write a dual quaternion as the sum of a dual scalar and a dual vector, Â = â0 + A, where â0 = ( a, b ) and A = ( A, B ) is the dual vector that defines a screw. This notation allows us to write the product of two dual quaternions as

              G
              ^

              A
              ^

              C
              ^

        (

                a
                ^

            0

        +

            A

        )
        (

                c
                ^

            0

        +

            C

        )

        (

                a
                ^

            0

                c
                ^

            0

        −

            A

        ⋅

            C

        )
        +
        (

                c
                ^

            0

            A

        +

                a
                ^

            0

            C

        +

            A

        ×

            C

        )
        .

    {\displaystyle {\hat {G}}={\hat {A}}{\hat {C}}=({\hat {a}}{0}+{\mathsf {A}})({\hat {c}}{0}+{\mathsf {C}})=({\hat {a}}{0}{\hat {c}}{0}-{\mathsf {A}}\cdot {\mathsf {C}})+({\hat {c}}{0}{\mathsf {A}}+{\hat {a}}{0}{\mathsf {C}}+{\mathsf {A}}\times {\mathsf {C}}).}

Addition
The addition of dual quaternions is defined componentwise so that given,

              A
              ^

        (
        A
        ,
        B
        )

          a

            0

        +

          a

            1

        i
        +

          a

            2

        j
        +

          a

            3

        k
        +

          b

            0

        ε
        +

          b

            1

        ε
        i
        +

          b

            2

        ε
        j
        +

          b

            3

        ε
        k
        ,

    {\displaystyle {\hat {A}}=(A,B)=a_{0}+a_{1}i+a_{2}j+a_{3}k+b_{0}\varepsilon +b_{1}\varepsilon i+b_{2}\varepsilon j+b_{3}\varepsilon k,}

and

              C
              ^

        (
        C
        ,
        D
        )

          c

            0

        +

          c

            1

        i
        +

          c

            2

        j
        +

          c

            3

        k
        +

          d

            0

        ε
        +

          d

            1

        ε
        i
        +

          d

            2

        ε
        j
        +

          d

            3

        ε
        k
        ,

    {\displaystyle {\hat {C}}=(C,D)=c_{0}+c_{1}i+c_{2}j+c_{3}k+d_{0}\varepsilon +d_{1}\varepsilon i+d_{2}\varepsilon j+d_{3}\varepsilon k,}

then

              A
              ^

        +

              C
              ^

        (
        A
        +
        C
        ,
        B
        +
        D
        )

        (

          a

            0

        +

          c

            0

        )
        +
        (

          a

            1

        +

          c

            1

        )
        i
        +
        (

          a

            2

        +

          c

            2

        )
        j
        +
        (

          a

            3

        +

          c

            3

        )
        k
        +
        (

          b

            0

        +

          d

            0

        )
        ε
        +
        (

          b

            1

        +

          d

            1

        )
        ε
        i
        +
        (

          b

            2

        +

          d

            2

        )
        ε
        j
        +
        (

          b

            3

        +

          d

            3

        )
        ε
        k
        ,

    {\displaystyle {\hat {A}}+{\hat {C}}=(A+C,B+D)=(a_{0}+c_{0})+(a_{1}+c_{1})i+(a_{2}+c_{2})j+(a_{3}+c_{3})k+(b_{0}+d_{0})\varepsilon +(b_{1}+d_{1})\varepsilon i+(b_{2}+d_{2})\varepsilon j+(b_{3}+d_{3})\varepsilon k,}

Multiplication
Multiplication of two dual quaternion follows from the multiplication rules for the quaternion units i, j, k and commutative multiplication by the dual unit ε. In particular, given

              A
              ^

        (
        A
        ,
        B
        )

        A
        +
        ε
        B
        ,

    {\displaystyle {\hat {A}}=(A,B)=A+\varepsilon B,}

and

              C
              ^

        (
        C
        ,
        D
        )

        C
        +
        ε
        D
        ,

    {\displaystyle {\hat {C}}=(C,D)=C+\varepsilon D,}

then

              A
              ^

              C
              ^

        (
        A
        +
        ε
        B
        )
        (
        C
        +
        ε
        D
        )

        A
        C
        +
        ε
        (
        A
        D
        +
        B
        C
        )
        .

    {\displaystyle {\hat {A}}{\hat {C}}=(A+\varepsilon B)(C+\varepsilon D)=AC+\varepsilon (AD+BC).}

Notice that there is no BD term, because the definition of dual numbers requires that ε2 = 0.
This gives us the multiplication table (note the multiplication order is row times column):

Conjugate
The conjugate of a dual quaternion is the extension of the conjugate of a quaternion, that is

                A
                ^

            ∗

        (

          A

            ∗

        ,

          B

            ∗

        )

          A

            ∗

        +
        ε

          B

            ∗

        .

    {\displaystyle {\hat {A}}^{}=(A^{},B^{})=A^{}+\varepsilon B^{*}.!}

As with quaternions, the conjugate of the product of dual quaternions, Ĝ = ÂĈ, is the product of their conjugates in reverse order,

                G
                ^

            ∗

        (

              A
              ^

              C
              ^

          )

            ∗

                C
                ^

            ∗

                A
                ^

            ∗

        .

    {\displaystyle {\hat {G}}^{}=({\hat {A}}{\hat {C}})^{}={\hat {C}}^{}{\hat {A}}^{}.}

It is useful to introduce the functions Sc(∗) and Vec(∗) that select the scalar and vector parts of a quaternion, or the dual scalar and dual vector parts of a dual quaternion. In particular, if Â = â0 + A, then

            Sc

        (

              A
              ^

        )

                a
                ^

            0

        ,

            Vec

        (

              A
              ^

        )

            A

        .

    {\displaystyle {\mbox{Sc}}({\hat {A}})={\hat {a}}_{0},{\mbox{Vec}}({\hat {A}})={\mathsf {A}}.}

This allows the definition of the conjugate of Â as

                A
                ^

            ∗

            Sc

        (

              A
              ^

        )
        −

            Vec

        (

              A
              ^

        )
        .

    {\displaystyle {\hat {A}}^{*}={\mbox{Sc}}({\hat {A}})-{\mbox{Vec}}({\hat {A}}).}

or,

        (

                a
                ^

            0

        +

            A

          )

            ∗

                a
                ^

            0

        −

            A

        .

    {\displaystyle ({\hat {a}}{0}+{\mathsf {A}})^{*}={\hat {a}}{0}-{\mathsf {A}}.}

The product of a dual quaternion with its conjugate yields

              A
              ^

                A
                ^

            ∗

        (

                a
                ^

            0

        +

            A

        )
        (

                a
                ^

            0

        −

            A

        )

                a
                ^

            0

            2

        +

            A

        ⋅

            A

        .

    {\displaystyle {\hat {A}}{\hat {A}}^{*}=({\hat {a}}{0}+{\mathsf {A}})({\hat {a}}{0}-{\mathsf {A}})={\hat {a}}_{0}^{2}+{\mathsf {A}}\cdot {\mathsf {A}}.}

This is a dual scalar which is the magnitude squared of the dual quaternion.

Dual number conjugate
A second type of conjugate of a dual quaternion is given by taking the dual number conjugate, given by

                A
                ^

            ¯

        (
        A
        ,
        −
        B
        )

        A
        −
        ε
        B
        .

    {\displaystyle {\overline {\hat {A}}}=(A,-B)=A-\varepsilon B.!}

The quaternion and dual number conjugates can be combined into a third form of conjugate given by

                    A
                    ^

                ∗

            ¯

        (

          A

            ∗

        ,
        −

          B

            ∗

        )

          A

            ∗

        −
        ε

          B

            ∗

        .

    {\displaystyle {\overline {{\hat {A}}^{}}}=(A^{},-B^{})=A^{}-\varepsilon B^{*}.!}

In the context of dual quaternions, the term "conjugate" can be used to mean the quaternion conjugate, dual number conjugate, or both.

Norm
The norm of a dual quaternion |Â| is computed using the conjugate to compute |Â| = √Â Â*. This is a dual number called the magnitude of the dual quaternion. Dual quaternions with |Â| = 1 are unit dual quaternions.
Dual quaternions of magnitude 1 are used to represent spatial Euclidean displacements. Notice that the requirement that Â Â* = 1, introduces two algebraic constraints on the components of Â, that is

              A
              ^

                A
                ^

            ∗

        (
        A
        ,
        B
        )
        (

          A

            ∗

        ,

          B

            ∗

        )

        (
        A

          A

            ∗

        ,
        A

          B

            ∗

        +
        B

          A

            ∗

        )

        (
        1
        ,
        0
        )
        .

    {\displaystyle {\hat {A}}{\hat {A}}^{}=(A,B)(A^{},B^{})=(AA^{},AB^{}+BA^{})=(1,0).}

The first of these constraints,

        A

          A

            ∗

        1
        ,

    {\displaystyle AA^{*}=1,}

 implies that

        A

    {\displaystyle A}

 has magnitude 1, while the second constraint,

        A

          B

            ∗

        +
        B

          A

            ∗

        0
        ,

    {\displaystyle AB^{}+BA^{}=0,}

 implies that

        A

    {\displaystyle A}

 and

        B

    {\displaystyle B}

 are orthogonal.

Inverse
If p + ε q is a dual quaternion, and p is not zero, then the inverse dual quaternion is given by

p−1 (1 − ε q p−1).
Thus the elements of the subspace { ε q : q ∈ H } do not have inverses. This subspace is called an ideal in ring theory. It happens to be the unique maximal ideal of the ring of dual numbers.
The group of units of the dual number ring then consists of numbers not in the ideal. The dual numbers form a local ring since there is a unique maximal ideal. The group of units is a Lie group and can be studied using the exponential mapping. Dual quaternions have been used to exhibit transformations in the Euclidean group. A typical element can be written as a screw transformation.

Dual quaternions and spatial displacements
A benefit of the dual quaternion formulation of the composition of two spatial displacements DB = ([RB], b) and DA = ([RA], a) is that the resulting dual quaternion yields directly the screw axis and dual angle of the composite displacement DC = DBDA.
In general, the dual quaternion associated with a spatial displacement D = ([A], d) is constructed from its screw axis S = (S, V) and the dual angle (φ, d) where φ is the rotation about and d the slide along this axis, which defines the displacement D. The associated dual quaternion is given by,

              S
              ^

        cos
        ⁡

                ϕ
                ^

            2

        +
        sin
        ⁡

                ϕ
                ^

            2

            S

        .

    {\displaystyle {\hat {S}}=\cos {\frac {\hat {\phi }}{2}}+\sin {\frac {\hat {\phi }}{2}}{\mathsf {S}}.}

Let the composition of the displacement DB with DA be the displacement DC = DBDA. The screw axis and dual angle of DC is obtained from the product of the dual quaternions of DA and DB, given by

              A
              ^

        cos
        ⁡
        (

              α
              ^

          /

        2
        )
        +
        sin
        ⁡
        (

              α
              ^

          /

        2
        )

            A

          and

              B
              ^

        cos
        ⁡
        (

              β
              ^

          /

        2
        )
        +
        sin
        ⁡
        (

              β
              ^

          /

        2
        )

            B

        .

    {\displaystyle {\hat {A}}=\cos({\hat {\alpha }}/2)+\sin({\hat {\alpha }}/2){\mathsf {A}}\quad {\text{and}}\quad {\hat {B}}=\cos({\hat {\beta }}/2)+\sin({\hat {\beta }}/2){\mathsf {B}}.}

That is, the composite displacement DC=DBDA has the associated dual quaternion given by

              C
              ^

        cos
        ⁡

                γ
                ^

            2

        +
        sin
        ⁡

                γ
                ^

            2

            C

          (

            cos
            ⁡

                    β
                    ^

                2

            +
            sin
            ⁡

                    β
                    ^

                2

                B

          )

          (

            cos
            ⁡

                    α
                    ^

                2

            +
            sin
            ⁡

                    α
                    ^

                2

                A

          )

        .

    {\displaystyle {\hat {C}}=\cos {\frac {\hat {\gamma }}{2}}+\sin {\frac {\hat {\gamma }}{2}}{\mathsf {C}}=\left(\cos {\frac {\hat {\beta }}{2}}+\sin {\frac {\hat {\beta }}{2}}{\mathsf {B}}\right)\left(\cos {\frac {\hat {\alpha }}{2}}+\sin {\frac {\hat {\alpha }}{2}}{\mathsf {A}}\right).}

Expand this product in order to obtain

        cos
        ⁡

                γ
                ^

            2

        +
        sin
        ⁡

                γ
                ^

            2

            C

          (

            cos
            ⁡

                    β
                    ^

                2

            cos
            ⁡

                    α
                    ^

                2

            −
            sin
            ⁡

                    β
                    ^

                2

            sin
            ⁡

                    α
                    ^

                2

                B

            ⋅

                A

          )

        +

          (

            sin
            ⁡

                    β
                    ^

                2

            cos
            ⁡

                    α
                    ^

                2

                B

            +
            sin
            ⁡

                    α
                    ^

                2

            cos
            ⁡

                    β
                    ^

                2

                A

            +
            sin
            ⁡

                    β
                    ^

                2

            sin
            ⁡

                    α
                    ^

                2

                B

            ×

                A

          )

        .

    {\displaystyle \cos {\frac {\hat {\gamma }}{2}}+\sin {\frac {\hat {\gamma }}{2}}{\mathsf {C}}=\left(\cos {\frac {\hat {\beta }}{2}}\cos {\frac {\hat {\alpha }}{2}}-\sin {\frac {\hat {\beta }}{2}}\sin {\frac {\hat {\alpha }}{2}}{\mathsf {B}}\cdot {\mathsf {A}}\right)+\left(\sin {\frac {\hat {\beta }}{2}}\cos {\frac {\hat {\alpha }}{2}}{\mathsf {B}}+\sin {\frac {\hat {\alpha }}{2}}\cos {\frac {\hat {\beta }}{2}}{\mathsf {A}}+\sin {\frac {\hat {\beta }}{2}}\sin {\frac {\hat {\alpha }}{2}}{\mathsf {B}}\times {\mathsf {A}}\right).}

Divide both sides of this equation by the identity

        cos
        ⁡

                γ
                ^

            2

        cos
        ⁡

                β
                ^

            2

        cos
        ⁡

                α
                ^

            2

        −
        sin
        ⁡

                β
                ^

            2

        sin
        ⁡

                α
                ^

            2

            B

        ⋅

            A

    {\displaystyle \cos {\frac {\hat {\gamma }}{2}}=\cos {\frac {\hat {\beta }}{2}}\cos {\frac {\hat {\alpha }}{2}}-\sin {\frac {\hat {\beta }}{2}}\sin {\frac {\hat {\alpha }}{2}}{\mathsf {B}}\cdot {\mathsf {A}}}

to obtain

        tan
        ⁡

                γ
                ^

            2

            C

              tan
              ⁡

                      β
                      ^

                  2

                  B

              +
              tan
              ⁡

                      α
                      ^

                  2

                  A

              +
              tan
              ⁡

                      β
                      ^

                  2

              tan
              ⁡

                      α
                      ^

                  2

                  B

              ×

                  A

              1
              −
              tan
              ⁡

                      β
                      ^

                  2

              tan
              ⁡

                      α
                      ^

                  2

                  B

              ⋅

                  A

        .

    {\displaystyle \tan {\frac {\hat {\gamma }}{2}}{\mathsf {C}}={\frac {\tan {\frac {\hat {\beta }}{2}}{\mathsf {B}}+\tan {\frac {\hat {\alpha }}{2}}{\mathsf {A}}+\tan {\frac {\hat {\beta }}{2}}\tan {\frac {\hat {\alpha }}{2}}{\mathsf {B}}\times {\mathsf {A}}}{1-\tan {\frac {\hat {\beta }}{2}}\tan {\frac {\hat {\alpha }}{2}}{\mathsf {B}}\cdot {\mathsf {A}}}}.}

This is Rodrigues' formula for the screw axis of a composite displacement defined in terms of the screw axes of the two displacements. He derived this formula in 1840.
The three screw axes A, B, and C form a spatial triangle and the dual angles at these vertices between the common normals that form the sides of this triangle are directly related to the dual angles of the three spatial displacements.

Matrix form of dual quaternion multiplication
The matrix representation of the quaternion product is convenient for programming quaternion computations using matrix algebra, which is true for dual quaternion operations as well.
The quaternion product AC is a linear transformation by the operator A of the components of the quaternion C, therefore there is a matrix representation of A operating on the vector formed from the components of C.
Assemble the components of the quaternion C = c0 + C into the array C = (C1, C2, C3, c0). Notice that the components of the vector part of the quaternion are listed first and the scalar is listed last. This is an arbitrary choice, but once this convention is selected we must abide by it.
The quaternion product AC can now be represented as the matrix product

        A
        C

        [

          A

            +

        ]
        C

            [

                    a

                      0

                    A

                      3

                  −

                    A

                      2

                    A

                      1

                  −

                    A

                      3

                    a

                      0

                    A

                      1

                    A

                      2

                    A

                      2

                  −

                    A

                      1

                    a

                      0

                    A

                      3

                  −

                    A

                      1

                  −

                    A

                      2

                  −

                    A

                      3

                    a

                      0

            ]

            {

                    C

                      1

                    C

                      2

                    C

                      3

                    c

                      0

            }

        .

    {\displaystyle AC=[A^{+}]C={\begin{bmatrix}a_{0}&A_{3}&-A_{2}&A_{1}\-A_{3}&a_{0}&A_{1}&A_{2}\A_{2}&-A_{1}&a_{0}&A_{3}\-A_{1}&-A_{2}&-A_{3}&a_{0}\end{bmatrix}}{\begin{Bmatrix}C_{1}\C_{2}\C_{3}\c_{0}\end{Bmatrix}}.}

The product AC can also be viewed as an operation by C on the components of A, in which case we have

        A
        C

        [

          C

            −

        ]
        A

            [

                    c

                      0

                  −

                    C

                      3

                    C

                      2

                    C

                      1

                    C

                      3

                    c

                      0

                  −

                    C

                      1

                    C

                      2

                  −

                    C

                      2

                    C

                      1

                    c

                      0

                    C

                      3

                  −

                    C

                      1

                  −

                    C

                      2

                  −

                    C

                      3

                    c

                      0

            ]

            {

                    A

                      1

                    A

                      2

                    A

                      3

                    a

                      0

            }

        .

    {\displaystyle AC=[C^{-}]A={\begin{bmatrix}c_{0}&-C_{3}&C_{2}&C_{1}\C_{3}&c_{0}&-C_{1}&C_{2}\-C_{2}&C_{1}&c_{0}&C_{3}\-C_{1}&-C_{2}&-C_{3}&c_{0}\end{bmatrix}}{\begin{Bmatrix}A_{1}\A_{2}\A_{3}\a_{0}\end{Bmatrix}}.}

The dual quaternion product ÂĈ = (A, B)(C, D) = (AC, AD+BC) can be formulated as a matrix operation as follows. Assemble the components of Ĉ into the eight dimensional array Ĉ = (C1, C2, C3, c0, D1, D2, D3, d0), then ÂĈ is given by the 8x8 matrix product

              A
              ^

              C
              ^

        [

                A
                ^

            +

        ]

              C
              ^

            [

                    A

                      +

                  0

                    B

                      +

                    A

                      +

            ]

            {

                  C

                  D

            }

        .

    {\displaystyle {\hat {A}}{\hat {C}}=[{\hat {A}}^{+}]{\hat {C}}={\begin{bmatrix}A^{+}&0\B^{+}&A^{+}\end{bmatrix}}{\begin{Bmatrix}C\D\end{Bmatrix}}.}

As we saw for quaternions, the product ÂĈ can be viewed as the operation of Ĉ on the coordinate vector Â, which means ÂĈ can also be formulated as,

              A
              ^

              C
              ^

        [

                C
                ^

            −

        ]

              A
              ^

            [

                    C

                      −

                  0

                    D

                      −

                    C

                      −

            ]

            {

                  A

                  B

            }

        .

    {\displaystyle {\hat {A}}{\hat {C}}=[{\hat {C}}^{-}]{\hat {A}}={\begin{bmatrix}C^{-}&0\D^{-}&C^{-}\end{bmatrix}}{\begin{Bmatrix}A\B\end{Bmatrix}}.}

More on spatial displacements
The dual quaternion of a displacement D = ([A], d) can be constructed from the quaternion S = cos(φ/2) + sin(φ/2)S that defines the rotation [A] and the vector quaternion constructed from the translation vector d, given by D = d1i + d2j + d3k. Using this notation, the dual quaternion for the displacement D = ([A], d) is given by

              S
              ^

        S
        +
        ε

            1
            2

        D
        S
        .

    {\displaystyle {\hat {S}}=S+\varepsilon {\frac {1}{2}}DS.}

Let the Plücker coordinates of a line in the direction x through a point p in a moving body and its coordinates in the fixed frame which is in the direction X through the point P be given by,

              x
              ^

          x

        +
        ε

          p

        ×

          x

          and

              X
              ^

          X

        +
        ε

          P

        ×

          X

        .

    {\displaystyle {\hat {x}}=\mathbf {x} +\varepsilon \mathbf {p} \times \mathbf {x} \quad {\text{and}}\quad {\hat {X}}=\mathbf {X} +\varepsilon \mathbf {P} \times \mathbf {X} .}

Then the dual quaternion of the displacement of this body transforms Plücker coordinates in the moving frame to Plücker coordinates in the fixed frame by the formula

              X
              ^

              S
              ^

              x
              ^

                    S
                    ^

                ∗

            ¯

        .

    {\displaystyle {\hat {X}}={\hat {S}}{\hat {x}}{\overline {{\hat {S}}^{*}}}.}

Using the matrix form of the dual quaternion product this becomes,

              X
              ^

        [

                S
                ^

            +

        ]
        [

                S
                ^

            −

          ]

            ∗

              x
              ^

        .

    {\displaystyle {\hat {X}}=[{\hat {S}}^{+}][{\hat {S}}^{-}]^{*}{\hat {x}}.}

This calculation is easily managed using matrix operations.

Dual quaternions and 4×4 homogeneous transforms
It might be helpful, especially in rigid body motion, to represent unit dual quaternions as homogeneous matrices. As given above a dual quaternion can be written as:

              q
              ^

        r
        +
        d
        ε
        r

    {\displaystyle {\hat {q}}=r+d\varepsilon r}

 where r and d are both quaternions. The r quaternion is known as the real or rotational part and the

        d

    {\displaystyle d}

 quaternion is known as the dual or displacement part.
The rotation part can be given by

        r

          r

            w

        +

          r

            x

        i
        +

          r

            y

        j
        +

          r

            z

        k

        cos
        ⁡

          (

              θ
              2

          )

        +
        sin
        ⁡

          (

              θ
              2

          )

          (

                  a
                  →

            ⋅
            (
            i
            ,
            j
            ,
            k
            )

          )

    {\displaystyle r=r_{w}+r_{x}i+r_{y}j+r_{z}k=\cos \left({\frac {\theta }{2}}\right)+\sin \left({\frac {\theta }{2}}\right)\left({\vec {a}}\cdot (i,j,k)\right)}

where

        θ

    {\displaystyle \theta }

 is the angle of rotation about the direction given by unit vector

              a
              →

    {\displaystyle {\vec {a}}}

. The displacement part can be written as

        d

        0
        +

              Δ
              x

            2

        i
        +

              Δ
              y

            2

        j
        +

              Δ
              z

            2

        k

    {\displaystyle d=0+{\frac {\Delta x}{2}}i+{\frac {\Delta y}{2}}j+{\frac {\Delta z}{2}}k}

.
The dual-quaternion equivalent of a 3D-vector is

              v
              ^

        :=
        1
        +
        ε
        (

          v

            x

        i
        +

          v

            y

        j
        +

          v

            z

        k
        )

    {\displaystyle {\hat {v}}:=1+\varepsilon (v_{x}i+v_{y}j+v_{z}k)}

and its transformation by

              q
              ^

    {\displaystyle {\hat {q}}}

 is given by

                v
                ^

          ′

              q
              ^

        ⋅

              v
              ^

        ⋅

                    q
                    ^

                ∗

            ¯

        .

    {\displaystyle {\hat {v}}'={\hat {q}}\cdot {\hat {v}}\cdot {\overline {{\hat {q}}^{*}}}.}

These dual quaternions (or actually their transformations on 3D-vectors) can be represented by the homogeneous transformation matrix

        T

            (

                  1

                  0

                  0

                  0

                  Δ
                  x

                  Δ
                  y

                  R

                  Δ
                  z

            )

    {\displaystyle T={\begin{pmatrix}1&0&0&0&\\Delta x&&&\\Delta y&&R&\\Delta z&&&\\end{pmatrix}}}

where the 3×3 orthogonal matrix is given by

        R

            (

                    r

                      w

                      2

                  +

                    r

                      x

                      2

                  −

                    r

                      y

                      2

                  −

                    r

                      z

                      2

                  2

                    r

                      x

                    r

                      y

                  −
                  2

                    r

                      w

                    r

                      z

                  2

                    r

                      x

                    r

                      z

                  +
                  2

                    r

                      w

                    r

                      y

                  2

                    r

                      x

                    r

                      y

                  +
                  2

                    r

                      w

                    r

                      z

                    r

                      w

                      2

                  −

                    r

                      x

                      2

                  +

                    r

                      y

                      2

                  −

                    r

                      z

                      2

                  2

                    r

                      y

                    r

                      z

                  −
                  2

                    r

                      w

                    r

                      x

                  2

                    r

                      x

                    r

                      z

                  −
                  2

                    r

                      w

                    r

                      y

                  2

                    r

                      y

                    r

                      z

                  +
                  2

                    r

                      w

                    r

                      x

                    r

                      w

                      2

                  −

                    r

                      x

                      2

                  −

                    r

                      y

                      2

                  +

                    r

                      z

                      2

            )

        .

    {\displaystyle R={\begin{pmatrix}r_{w}^{2}+r_{x}^{2}-r_{y}^{2}-r_{z}^{2}&2r_{x}r_{y}-2r_{w}r_{z}&2r_{x}r_{z}+2r_{w}r_{y}\2r_{x}r_{y}+2r_{w}r_{z}&r_{w}^{2}-r_{x}^{2}+r_{y}^{2}-r_{z}^{2}&2r_{y}r_{z}-2r_{w}r_{x}\2r_{x}r_{z}-2r_{w}r_{y}&2r_{y}r_{z}+2r_{w}r_{x}&r_{w}^{2}-r_{x}^{2}-r_{y}^{2}+r_{z}^{2}\\end{pmatrix}}.}

For the 3D-vector

        v

            (

                  1

                    v

                      x

                    v

                      y

                    v

                      z

            )

    {\displaystyle v={\begin{pmatrix}1\v_{x}\v_{y}\v_{z}\\end{pmatrix}}}

the transformation by T is given by

                v
                →

          ′

        T
        ⋅

              v
              →

    {\displaystyle {\vec {v}}'=T\cdot {\vec {v}}}

Connection to Clifford algebras
Besides being the tensor product of two Clifford algebras, the quaternions and the dual numbers, the dual quaternions have two other formulations in terms of Clifford algebras.
First, dual quaternions are isomorphic to the Clifford algebra generated by 3 anticommuting elements

        i

    {\displaystyle i}

,

        j

    {\displaystyle j}

,

        e

    {\displaystyle e}

 with

          i

            2

          j

            2

        −
        1

    {\displaystyle i^{2}=j^{2}=-1}

 and

          e

            2

        0

    {\displaystyle e^{2}=0}

. If we define

        k

        i
        j

    {\displaystyle k=ij}

 and

        ε

        e
        k

    {\displaystyle \varepsilon =ek}

, then the relations defining the dual quaternions are implied by these and vice versa. Second, the dual quaternions are isomorphic to the even part of the Clifford algebra generated by 4 anticommuting elements

          e

            1

        ,

          e

            2

        ,

          e

            3

        ,

          e

            4

    {\displaystyle e_{1},e_{2},e_{3},e_{4}}

 with

          e

            1

            2

          e

            2

            2

          e

            3

            2

        −
        1
        ,

          e

            4

            2

        0.

    {\displaystyle e_{1}^{2}=e_{2}^{2}=e_{3}^{2}=-1,\,\,e_{4}^{2}=0.}

For details, see Clifford algebras: dual quaternions.

Eponyms
Since both Eduard Study and William Kingdon Clifford used and wrote about dual quaternions, at times authors refer to dual quaternions as "Study biquaternions" or "Clifford biquaternions". The latter eponym has also been used to refer to split-biquaternions. Read the article by Joe Rooney linked below for view of a supporter of W.K. Clifford's claim. Since the claims of Clifford and Study are in contention, it is convenient to use the current designation dual quaternion to avoid conflict.
