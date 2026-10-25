# Rigid transformation

Rigid transformation

In mathematics, a rigid transformation (also called Euclidean transformation or Euclidean isometry) is a geometric transformation of a Euclidean space that preserves the Euclidean distance between every pair of points.
The rigid transformations include rotations, translations, reflections, or any sequence of these. Reflections are sometimes excluded from the definition of a rigid transformation by requiring that the transformation also preserve the handedness of objects in the Euclidean space. (A reflection would not preserve handedness; for instance, it would transform a left hand into a right hand.) To avoid ambiguity, a transformation that preserves handedness is known as a rigid motion, a Euclidean motion, or a proper rigid transformation.
In dimension two, a rigid motion is either a translation or a rotation. In dimension three, every rigid motion can be decomposed as the composition of a rotation and a translation, and is thus sometimes called a rototranslation. In dimension three, all rigid motions are also screw motions (this is Chasles' theorem).
In dimension at most three, any improper rigid transformation can be decomposed into an improper rotation followed by a translation, or into a sequence of reflections.
Any object will keep the same shape and size after a proper rigid transformation.
All rigid transformations are examples of affine transformations. The set of all (proper and improper) rigid transformations is a mathematical group called the Euclidean group, denoted E(n) for n-dimensional Euclidean spaces. The set of rigid motions is called the special Euclidean group, and denoted SE(n).
In kinematics, rigid motions in a 3-dimensional Euclidean space are used to represent displacements of rigid bodies. According to Chasles' theorem, every rigid transformation can be expressed as a screw motion.

Formal definition
A rigid transformation is formally defined as a transformation that, when acting on any vector v, produces a transformed vector T(v) of the form

where RT = R−1 (i.e., R is an orthogonal transformation), and t is a vector giving the translation of the origin.
A proper rigid transformation has, in addition,

which means that R does not produce a reflection, and hence it represents a rotation (an orientation-preserving orthogonal transformation). Indeed, when an orthogonal transformation matrix produces a reflection, its determinant is −1.

Distance formula
A measure of distance between points, or metric, is needed in order to confirm that a transformation is rigid. The Euclidean distance formula for Rn is the generalization of the Pythagorean theorem. The formula gives the distance squared between two points X and Y as the sum of the squares of the distances along the coordinate axes, that is

        d

            (

                X

              ,

                Y

            )

            2

            (

                X

                  1

              −

                Y

                  1

            )

            2

        +

            (

                X

                  2

              −

                Y

                  2

            )

            2

        +
        ⋯
        +

            (

                X

                  n

              −

                Y

                  n

            )

            2

          (

              X

            −

              Y

          )

        ⋅

          (

              X

            −

              Y

          )

        .

    {\displaystyle d\left(\mathbf {X} ,\mathbf {Y} \right)^{2}=\left(X_{1}-Y_{1}\right)^{2}+\left(X_{2}-Y_{2}\right)^{2}+\dots +\left(X_{n}-Y_{n}\right)^{2}=\left(\mathbf {X} -\mathbf {Y} \right)\cdot \left(\mathbf {X} -\mathbf {Y} \right).}

where X = (X1, X2, ..., Xn) and Y = (Y1, Y2, ..., Yn), and the dot denotes the scalar product.
Using this distance formula, a rigid transformation g : Rn → Rn has the property,

        d
        (
        g
        (

          X

        )
        ,
        g
        (

          Y

        )

          )

            2

        d
        (

          X

        ,

          Y

          )

            2

        .

    {\displaystyle d(g(\mathbf {X} ),g(\mathbf {Y} ))^{2}=d(\mathbf {X} ,\mathbf {Y} )^{2}.}

Translations and linear transformations
A translation of a vector space adds a vector d to every vector in the space, which means it is the transformation

It is easy to show that this is a rigid transformation by showing that the distance between translated vectors equal the distance between the original vectors:

        d
        (

          v

        +

          d

        ,

          w

        +

          d

          )

            2

        (

          v

        +

          d

        −

          w

        −

          d

        )
        ⋅
        (

          v

        +

          d

        −

          w

        −

          d

        )

        (

          v

        −

          w

        )
        ⋅
        (

          v

        −

          w

        )

        d
        (

          v

        ,

          w

          )

            2

        .

    {\displaystyle d(\mathbf {v} +\mathbf {d} ,\mathbf {w} +\mathbf {d} )^{2}=(\mathbf {v} +\mathbf {d} -\mathbf {w} -\mathbf {d} )\cdot (\mathbf {v} +\mathbf {d} -\mathbf {w} -\mathbf {d} )=(\mathbf {v} -\mathbf {w} )\cdot (\mathbf {v} -\mathbf {w} )=d(\mathbf {v} ,\mathbf {w} )^{2}.}

A linear transformation of a vector space, L : Rn → Rn, preserves linear combinations,

        L
        (

          V

        )

        L
        (
        a

          v

        +
        b

          w

        )

        a
        L
        (

          v

        )
        +
        b
        L
        (

          w

        )
        .

    {\displaystyle L(\mathbf {V} )=L(a\mathbf {v} +b\mathbf {w} )=aL(\mathbf {v} )+bL(\mathbf {w} ).}

A linear transformation L can be represented by a matrix, which means

where [L] is an n×n matrix.
A linear transformation is a rigid transformation if it satisfies the condition,

        d
        (
        [
        L
        ]

          v

        ,
        [
        L
        ]

          w

          )

            2

        d
        (

          v

        ,

          w

          )

            2

        ,

    {\displaystyle d([L]\mathbf {v} ,[L]\mathbf {w} )^{2}=d(\mathbf {v} ,\mathbf {w} )^{2},}

that is

        d
        (
        [
        L
        ]

          v

        ,
        [
        L
        ]

          w

          )

            2

        (
        [
        L
        ]

          v

        −
        [
        L
        ]

          w

        )
        ⋅
        (
        [
        L
        ]

          v

        −
        [
        L
        ]

          w

        )

        (
        [
        L
        ]
        (

          v

        −

          w

        )
        )
        ⋅
        (
        [
        L
        ]
        (

          v

        −

          w

        )
        )
        .

    {\displaystyle d([L]\mathbf {v} ,[L]\mathbf {w} )^{2}=([L]\mathbf {v} -[L]\mathbf {w} )\cdot ([L]\mathbf {v} -[L]\mathbf {w} )=([L](\mathbf {v} -\mathbf {w} ))\cdot ([L](\mathbf {v} -\mathbf {w} )).}

Now use the fact that the scalar product of two vectors v.w can be written as the matrix operation vTw, where the T denotes the matrix transpose, we have

        d
        (
        [
        L
        ]

          v

        ,
        [
        L
        ]

          w

          )

            2

        (

          v

        −

          w

          )

              T

        [
        L

          ]

              T

        [
        L
        ]
        (

          v

        −

          w

        )
        .

    {\displaystyle d([L]\mathbf {v} ,[L]\mathbf {w} )^{2}=(\mathbf {v} -\mathbf {w} )^{\mathsf {T}}[L]^{\mathsf {T}}[L](\mathbf {v} -\mathbf {w} ).}

Thus, the linear transformation L is rigid if its matrix satisfies the condition

        [
        L

          ]

              T

        [
        L
        ]

        [
        I
        ]
        ,

    {\displaystyle [L]^{\mathsf {T}}[L]=[I],}

where [I] is the identity matrix. Matrices that satisfy this condition are called orthogonal matrices. This condition actually requires the columns of these matrices to be orthogonal unit vectors.
Matrices that satisfy this condition form a mathematical group under the operation of matrix multiplication called the orthogonal group of n×n matrices and denoted O(n).
Compute the determinant of the condition for an orthogonal matrix to obtain

        det

          (

            [
            L

              ]

                  T

            [
            L
            ]

          )

        det
        [
        L

          ]

            2

        det
        [
        I
        ]

        1
        ,

    {\displaystyle \det \left([L]^{\mathsf {T}}[L]\right)=\det[L]^{2}=\det[I]=1,}

which shows that the matrix [L] can have a determinant of either +1 or −1. Orthogonal matrices with determinant −1 are reflections, and those with determinant +1 are rotations. Notice that the set of orthogonal matrices can be viewed as consisting of two manifolds in Rn×n separated by the set of singular matrices.
The set of rotation matrices is called the special orthogonal group, and denoted SO(n). It is an example of a Lie group because it has the structure of a manifold.
