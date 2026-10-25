# Mooney–Rivlin solid

Mooney–Rivlin solid

In continuum mechanics, a Mooney–Rivlin solid is a hyperelastic material model where the strain energy density function

        W

    {\displaystyle W\,}

 is a linear combination of two invariants of the left Cauchy–Green deformation tensor

          B

    {\displaystyle {\boldsymbol {B}}}

. The model was proposed by Melvin Mooney in 1940 and expressed in terms of invariants by Ronald Rivlin in 1948.
The strain energy density function for an incompressible Mooney–Rivlin material is

        W

          C

            1

        (

                I
                ¯

            1

        −
        3
        )
        +

          C

            2

        (

                I
                ¯

            2

        −
        3
        )
        ,

    {\displaystyle W=C_{1}({\bar {I}}{1}-3)+C{2}({\bar {I}}_{2}-3),\,}

where

          C

            1

    {\displaystyle C_{1}}

 and

          C

            2

    {\displaystyle C_{2}}

 are empirically determined material constants, and

                I
                ¯

            1

    {\displaystyle {\bar {I}}_{1}}

 and

                I
                ¯

            2

    {\displaystyle {\bar {I}}_{2}}

 are the first and the second invariant of

              B
              ¯

        (
        det

          B

          )

            −
            1

              /

            3

          B

    {\displaystyle {\bar {\boldsymbol {B}}}=(\det {\boldsymbol {B}})^{-1/3}{\boldsymbol {B}}}

 (the unimodular component of

          B

    {\displaystyle {\boldsymbol {B}}}

):

                        I
                        ¯

                    1

                  J

                    −
                    2

                      /

                    3

                  I

                    1

                ,

                  I

                    1

                  λ

                    1

                    2

                +

                  λ

                    2

                    2

                +

                  λ

                    3

                    2

                ,

                        I
                        ¯

                    2

                  J

                    −
                    4

                      /

                    3

                  I

                    2

                ,

                  I

                    2

                  λ

                    1

                    2

                  λ

                    2

                    2

                +

                  λ

                    2

                    2

                  λ

                    3

                    2

                +

                  λ

                    3

                    2

                  λ

                    1

                    2

    {\displaystyle {\begin{aligned}{\bar {I}}{1}&=J^{-2/3}~I{1},\quad I_{1}=\lambda _{1}^{2}+\lambda _{2}^{2}+\lambda {3}^{2},\{\bar {I}}{2}&=J^{-4/3}~I_{2},\quad I_{2}=\lambda _{1}^{2}\lambda _{2}^{2}+\lambda _{2}^{2}\lambda _{3}^{2}+\lambda _{3}^{2}\lambda _{1}^{2}\end{aligned}}}

where

          F

    {\displaystyle {\boldsymbol {F}}}

 is the deformation gradient and

        J

        det
        (

          F

        )

          λ

            1

          λ

            2

          λ

            3

    {\displaystyle J=\det({\boldsymbol {F}})=\lambda _{1}\lambda _{2}\lambda _{3}}

. For an incompressible material,

        J

        1

    {\displaystyle J=1}

.

Derivation
The Mooney–Rivlin model is a special case of the generalized Rivlin model (also called polynomial hyperelastic model) which has the form

        W

          ∑

            p
            ,
            q

            0

            N

          C

            p
            q

        (

                I
                ¯

            1

        −
        3

          )

            p

        (

                I
                ¯

            2

        −
        3

          )

            q

        +

          ∑

            m

            1

            M

            1

              D

                m

        (
        J
        −
        1

          )

            2
            m

    {\displaystyle W=\sum {p,q=0}^{N}C{pq}({\bar {I}}{1}-3)^{p}~({\bar {I}}{2}-3)^{q}+\sum {m=1}^{M}{\frac {1}{D{m}}}~(J-1)^{2m}}

with

          C

            00

        0

    {\displaystyle C_{00}=0}

 where

          C

            p
            q

    {\displaystyle C_{pq}}

 are material constants related to the distortional response and

          D

            m

    {\displaystyle D_{m}}

 are material constants related to the volumetric response. For a compressible Mooney–Rivlin material

        N

        1
        ,

          C

            01

          C

            2

        ,

          C

            11

        0
        ,

          C

            10

          C

            1

        ,
        M

        1

    {\displaystyle N=1,C_{01}=C_{2},C_{11}=0,C_{10}=C_{1},M=1}

 and we have

        W

          C

            01

        (

                I
                ¯

            2

        −
        3
        )
        +

          C

            10

        (

                I
                ¯

            1

        −
        3
        )
        +

            1

              D

                1

        (
        J
        −
        1

          )

            2

    {\displaystyle W=C_{01}~({\bar {I}}{2}-3)+C{10}~({\bar {I}}{1}-3)+{\frac {1}{D{1}}}~(J-1)^{2}}

If

          C

            01

        0

    {\displaystyle C_{01}=0}

 we obtain a neo-Hookean solid, a special case of a Mooney–Rivlin solid.
For consistency with linear elasticity in the limit of small strains, it is necessary that

        κ

        2

          /

          D

            1

        ;

        μ

        2

        (

          C

            01

        +

          C

            10

        )

    {\displaystyle \kappa =2/D_{1}~;~~\mu =2~(C_{01}+C_{10})}

where

        κ

    {\displaystyle \kappa }

 is the bulk modulus and

        μ

    {\displaystyle \mu }

 is the shear modulus.

Cauchy stress in terms of strain invariants and deformation tensors
The Cauchy stress in a compressible hyperelastic material with a stress free reference configuration is given by

          σ

                  2

                  J

          [

                      1

                        J

                          2

                            /

                          3

              (

                          ∂

                            W

                          ∂

                                  I
                                  ¯

                              1

                +

                        I
                        ¯

                    1

                          ∂

                            W

                          ∂

                                  I
                                  ¯

                              2

              )

              B

            −

                      1

                        J

                          4

                            /

                          3

                      ∂

                        W

                      ∂

                              I
                              ¯

                          2

              B

            ⋅

              B

          ]

        +

          [

                      ∂

                        W

                      ∂
                      J

            −

                      2

                      3
                      J

              (

                        I
                        ¯

                    1

                          ∂

                            W

                          ∂

                                  I
                                  ¯

                              1

                +
                2

                        I
                        ¯

                    2

                          ∂

                            W

                          ∂

                                  I
                                  ¯

                              2

              )

          ]

          I

    {\displaystyle {\boldsymbol {\sigma }}={\cfrac {2}{J}}\left[{\cfrac {1}{J^{2/3}}}\left({\cfrac {\partial {W}}{\partial {\bar {I}}{1}}}+{\bar {I}}{1}~{\cfrac {\partial {W}}{\partial {\bar {I}}{2}}}\right){\boldsymbol {B}}-{\cfrac {1}{J^{4/3}}}~{\cfrac {\partial {W}}{\partial {\bar {I}}{2}}}~{\boldsymbol {B}}\cdot {\boldsymbol {B}}\right]+\left[{\cfrac {\partial {W}}{\partial J}}-{\cfrac {2}{3J}}\left({\bar {I}}{1}~{\cfrac {\partial {W}}{\partial {\bar {I}}{1}}}+2~{\bar {I}}{2}~{\cfrac {\partial {W}}{\partial {\bar {I}}{2}}}\right)\right]~{\boldsymbol {I}}}

For a compressible Mooney–Rivlin material,

                  ∂

                    W

                  ∂

                          I
                          ¯

                      1

          C

            1

        ;

                  ∂

                    W

                  ∂

                          I
                          ¯

                      2

          C

            2

        ;

                  ∂

                    W

                  ∂
                  J

            2

              D

                1

        (
        J
        −
        1
        )

    {\displaystyle {\cfrac {\partial {W}}{\partial {\bar {I}}{1}}}=C{1}~;{\cfrac {\partial {W}}{\partial {\bar {I}}{2}}}=C{2}~;{\cfrac {\partial {W}}{\partial J}}={\frac {2}{D_{1}}}(J-1)}

Therefore, the Cauchy stress in a compressible Mooney–Rivlin material is given by

          σ

                  2

                  J

          [

                      1

                        J

                          2

                            /

                          3

              (

                  C

                    1

                +

                        I
                        ¯

                    1

                  C

                    2

              )

              B

            −

                      1

                        J

                          4

                            /

                          3

              C

                2

              B

            ⋅

              B

          ]

        +

          [

                2

                  D

                    1

            (
            J
            −
            1
            )
            −

                      2

                      3
                      J

              (

                  C

                    1

                        I
                        ¯

                    1

                +
                2

                  C

                    2

                        I
                        ¯

                    2

              )

          ]

          I

    {\displaystyle {\boldsymbol {\sigma }}={\cfrac {2}{J}}\left[{\cfrac {1}{J^{2/3}}}\left(C_{1}+{\bar {I}}{1}~C{2}\right){\boldsymbol {B}}-{\cfrac {1}{J^{4/3}}}~C_{2}~{\boldsymbol {B}}\cdot {\boldsymbol {B}}\right]+\left[{\frac {2}{D_{1}}}(J-1)-{\cfrac {2}{3J}}\left(C_{1}{\bar {I}}{1}+2C{2}{\bar {I}}_{2}~\right)\right]{\boldsymbol {I}}}

It can be shown, after some algebra, that the pressure is given by

        p
        :=
        −

              1
              3

          tr

        (

          σ

        )

        −

              ∂
              W

              ∂
              J

        −

            2

              D

                1

        (
        J
        −
        1
        )

        .

    {\displaystyle p:=-{\tfrac {1}{3}}\,{\text{tr}}({\boldsymbol {\sigma }})=-{\frac {\partial W}{\partial J}}=-{\frac {2}{D_{1}}}(J-1)\,.}

The stress can then be expressed in the form

          σ

        −
        p

          I

        +

                  1

                  J

          [

                      2

                        J

                          2

                            /

                          3

              (

                  C

                    1

                +

                        I
                        ¯

                    1

                  C

                    2

              )

              B

            −

                      2

                        J

                          4

                            /

                          3

              C

                2

              B

            ⋅

              B

            −

                      2

                      3

              (

                  C

                    1

                        I
                        ¯

                    1

                +
                2

                  C

                    2

                        I
                        ¯

                    2

              )

              I

          ]

        .

    {\displaystyle {\boldsymbol {\sigma }}=-p~{\boldsymbol {I}}+{\cfrac {1}{J}}\left[{\cfrac {2}{J^{2/3}}}\left(C_{1}+{\bar {I}}{1}~C{2}\right){\boldsymbol {B}}-{\cfrac {2}{J^{4/3}}}~C_{2}~{\boldsymbol {B}}\cdot {\boldsymbol {B}}-{\cfrac {2}{3}}\left(C_{1}\,{\bar {I}}{1}+2C{2}\,{\bar {I}}_{2}\right){\boldsymbol {I}}\right]\,.}

The above equation is often written using the unimodular tensor

              B
              ¯

          J

            −
            2

              /

            3

          B

    {\displaystyle {\bar {\boldsymbol {B}}}=J^{-2/3}\,{\boldsymbol {B}}}

 :

          σ

        −
        p

          I

        +

                  1

                  J

          [

            2

              (

                  C

                    1

                +

                        I
                        ¯

                    1

                  C

                    2

              )

                  B
                  ¯

            −
            2

              C

                2

                  B
                  ¯

            ⋅

                  B
                  ¯

            −

                      2

                      3

              (

                  C

                    1

                        I
                        ¯

                    1

                +
                2

                  C

                    2

                        I
                        ¯

                    2

              )

              I

          ]

        .

    {\displaystyle {\boldsymbol {\sigma }}=-p~{\boldsymbol {I}}+{\cfrac {1}{J}}\left[2\left(C_{1}+{\bar {I}}{1}~C{2}\right){\bar {\boldsymbol {B}}}-2~C_{2}~{\bar {\boldsymbol {B}}}\cdot {\bar {\boldsymbol {B}}}-{\cfrac {2}{3}}\left(C_{1}\,{\bar {I}}{1}+2C{2}\,{\bar {I}}_{2}\right){\boldsymbol {I}}\right]\,.}

For an incompressible Mooney–Rivlin material with

        J

        1

    {\displaystyle J=1}

 there holds

        p

        0

    {\displaystyle p=0}

 and

              B
              ¯

          B

    {\displaystyle {\bar {\boldsymbol {B}}}={\boldsymbol {B}}}

 . Thus

          σ

        2

          (

              C

                1

            +

              I

                1

              C

                2

          )

          B

        −
        2

          C

            2

          B

        ⋅

          B

        −

                  2

                  3

          (

              C

                1

              I

                1

            +
            2

              C

                2

              I

                2

          )

          I

        .

    {\displaystyle {\boldsymbol {\sigma }}=2\left(C_{1}+I_{1}~C_{2}\right){\boldsymbol {B}}-2C_{2}~{\boldsymbol {B}}\cdot {\boldsymbol {B}}-{\cfrac {2}{3}}\left(C_{1}\,I_{1}+2C_{2}\,I_{2}\right){\boldsymbol {I}}\,.}

Since

        det
        J

        1

    {\displaystyle \det J=1}

 the Cayley–Hamilton theorem implies

            B

            −
            1

          B

        ⋅

          B

        −

          I

            1

          B

        +

          I

            2

          I

        .

    {\displaystyle {\boldsymbol {B}}^{-1}={\boldsymbol {B}}\cdot {\boldsymbol {B}}-I_{1}~{\boldsymbol {B}}+I_{2}~{\boldsymbol {I}}.}

Hence, the Cauchy stress can be expressed as

          σ

        −

          p

            ∗

          I

        +
        2

          C

            1

          B

        −
        2

          C

            2

            B

            −
            1

    {\displaystyle {\boldsymbol {\sigma }}=-p^{*}~{\boldsymbol {I}}+2C_{1}~{\boldsymbol {B}}-2C_{2}~{\boldsymbol {B}}^{-1}}

where

          p

            ∗

        :=

              2
              3

        (

          C

            1

          I

            1

        −

          C

            2

          I

            2

        )
        .

    {\displaystyle p^{*}:={\tfrac {2}{3}}(C_{1}~I_{1}-C_{2}~I_{2}).\,}

Cauchy stress in terms of principal stretches
In terms of the principal stretches, the Cauchy stress differences for an incompressible hyperelastic material are given by

          σ

            11

        −

          σ

            33

          λ

            1

                  ∂

                    W

                  ∂

                    λ

                      1

        −

          λ

            3

                  ∂

                    W

                  ∂

                    λ

                      3

        ;

          σ

            22

        −

          σ

            33

          λ

            2

                  ∂

                    W

                  ∂

                    λ

                      2

        −

          λ

            3

                  ∂

                    W

                  ∂

                    λ

                      3

    {\displaystyle \sigma _{11}-\sigma _{33}=\lambda _{1}~{\cfrac {\partial {W}}{\partial \lambda _{1}}}-\lambda _{3}~{\cfrac {\partial {W}}{\partial \lambda _{3}}}~;~~\sigma _{22}-\sigma _{33}=\lambda _{2}~{\cfrac {\partial {W}}{\partial \lambda _{2}}}-\lambda _{3}~{\cfrac {\partial {W}}{\partial \lambda _{3}}}}

For an incompressible Mooney-Rivlin material,

        W

          C

            1

        (

          λ

            1

            2

        +

          λ

            2

            2

        +

          λ

            3

            2

        −
        3
        )
        +

          C

            2

        (

          λ

            1

            2

          λ

            2

            2

        +

          λ

            2

            2

          λ

            3

            2

        +

          λ

            3

            2

          λ

            1

            2

        −
        3
        )

        ;

          λ

            1

          λ

            2

          λ

            3

        1

    {\displaystyle W=C_{1}(\lambda _{1}^{2}+\lambda _{2}^{2}+\lambda {3}^{2}-3)+C{2}(\lambda _{1}^{2}\lambda _{2}^{2}+\lambda _{2}^{2}\lambda _{3}^{2}+\lambda _{3}^{2}\lambda _{1}^{2}-3)~;~~\lambda _{1}\lambda _{2}\lambda _{3}=1}

Therefore,

          λ

            1

                  ∂

                    W

                  ∂

                    λ

                      1

        2

          C

            1

          λ

            1

            2

        +
        2

          C

            2

          λ

            1

            2

        (

          λ

            2

            2

        +

          λ

            3

            2

        )

        ;

          λ

            2

                  ∂

                    W

                  ∂

                    λ

                      2

        2

          C

            1

          λ

            2

            2

        +
        2

          C

            2

          λ

            2

            2

        (

          λ

            1

            2

        +

          λ

            3

            2

        )

        ;

          λ

            3

                  ∂

                    W

                  ∂

                    λ

                      3

        2

          C

            1

          λ

            3

            2

        +
        2

          C

            2

          λ

            3

            2

        (

          λ

            1

            2

        +

          λ

            2

            2

        )

    {\displaystyle \lambda _{1}{\cfrac {\partial {W}}{\partial \lambda {1}}}=2C{1}\lambda {1}^{2}+2C{2}\lambda _{1}^{2}(\lambda _{2}^{2}+\lambda _{3}^{2})~;\lambda _{2}{\cfrac {\partial {W}}{\partial \lambda {2}}}=2C{1}\lambda {2}^{2}+2C{2}\lambda _{2}^{2}(\lambda _{1}^{2}+\lambda _{3}^{2})~;\lambda _{3}{\cfrac {\partial {W}}{\partial \lambda {3}}}=2C{1}\lambda {3}^{2}+2C{2}\lambda _{3}^{2}(\lambda _{1}^{2}+\lambda _{2}^{2})}

Since

          λ

            1

          λ

            2

          λ

            3

        1

    {\displaystyle \lambda _{1}\lambda _{2}\lambda _{3}=1}

. we can write

                  λ

                    1

                          ∂

                            W

                          ∂

                            λ

                              1

                2

                  C

                    1

                  λ

                    1

                    2

                +
                2

                  C

                    2

                  (

                              1

                                λ

                                  3

                                  2

                    +

                              1

                                λ

                                  2

                                  2

                  )

                ;

                  λ

                    2

                          ∂

                            W

                          ∂

                            λ

                              2

                2

                  C

                    1

                  λ

                    2

                    2

                +
                2

                  C

                    2

                  (

                              1

                                λ

                                  3

                                  2

                    +

                              1

                                λ

                                  1

                                  2

                  )

                  λ

                    3

                          ∂

                            W

                          ∂

                            λ

                              3

                2

                  C

                    1

                  λ

                    3

                    2

                +
                2

                  C

                    2

                  (

                              1

                                λ

                                  2

                                  2

                    +

                              1

                                λ

                                  1

                                  2

                  )

    {\displaystyle {\begin{aligned}\lambda _{1}{\cfrac {\partial {W}}{\partial \lambda {1}}}&=2C{1}\lambda {1}^{2}+2C{2}\left({\cfrac {1}{\lambda _{3}^{2}}}+{\cfrac {1}{\lambda _{2}^{2}}}\right)~;~~\lambda _{2}{\cfrac {\partial {W}}{\partial \lambda {2}}}=2C{1}\lambda {2}^{2}+2C{2}\left({\cfrac {1}{\lambda _{3}^{2}}}+{\cfrac {1}{\lambda _{1}^{2}}}\right)\\lambda _{3}{\cfrac {\partial {W}}{\partial \lambda {3}}}&=2C{1}\lambda {3}^{2}+2C{2}\left({\cfrac {1}{\lambda _{2}^{2}}}+{\cfrac {1}{\lambda _{1}^{2}}}\right)\end{aligned}}}

Then the expressions for the Cauchy stress differences become

          σ

            11

        −

          σ

            33

        2

          C

            1

        (

          λ

            1

            2

        −

          λ

            3

            2

        )
        −
        2

          C

            2

          (

                      1

                        λ

                          1

                          2

            −

                      1

                        λ

                          3

                          2

          )

        ;

          σ

            22

        −

          σ

            33

        2

          C

            1

        (

          λ

            2

            2

        −

          λ

            3

            2

        )
        −
        2

          C

            2

          (

                      1

                        λ

                          2

                          2

            −

                      1

                        λ

                          3

                          2

          )

    {\displaystyle \sigma _{11}-\sigma {33}=2C{1}(\lambda _{1}^{2}-\lambda {3}^{2})-2C{2}\left({\cfrac {1}{\lambda _{1}^{2}}}-{\cfrac {1}{\lambda _{3}^{2}}}\right)~;~~\sigma _{22}-\sigma {33}=2C{1}(\lambda _{2}^{2}-\lambda {3}^{2})-2C{2}\left({\cfrac {1}{\lambda _{2}^{2}}}-{\cfrac {1}{\lambda _{3}^{2}}}\right)}

Uniaxial extension
For the case of an incompressible Mooney–Rivlin material under uniaxial elongation,

          λ

            1

        λ

    {\displaystyle \lambda _{1}=\lambda \,}

 and

          λ

            2

          λ

            3

        1

          /

            λ

    {\displaystyle \lambda _{2}=\lambda _{3}=1/{\sqrt {\lambda }}}

. Then the true stress (Cauchy stress) differences can be calculated as:

                  σ

                    11

                −

                  σ

                    33

                2

                  C

                    1

                  (

                      λ

                        2

                    −

                              1

                              λ

                  )

                −
                2

                  C

                    2

                  (

                              1

                                λ

                                  2

                    −
                    λ

                  )

                  σ

                    22

                −

                  σ

                    33

                0

    {\displaystyle {\begin{aligned}\sigma _{11}-\sigma {33}&=2C{1}\left(\lambda ^{2}-{\cfrac {1}{\lambda }}\right)-2C_{2}\left({\cfrac {1}{\lambda ^{2}}}-\lambda \right)\\sigma _{22}-\sigma _{33}&=0\end{aligned}}}

Simple tension

In the case of simple tension,

          σ

            22

          σ

            33

        0

    {\displaystyle \sigma _{22}=\sigma _{33}=0}

. Then we can write

          σ

            11

          (

            2

              C

                1

            +

                      2

                        C

                          2

                      λ

          )

          (

              λ

                2

            −

                      1

                      λ

          )

    {\displaystyle \sigma {11}=\left(2C{1}+{\cfrac {2C_{2}}{\lambda }}\right)\left(\lambda ^{2}-{\cfrac {1}{\lambda }}\right)}

In alternative notation, where the Cauchy stress is written as

          T

    {\displaystyle {\boldsymbol {T}}}

 and the stretch as

        α

    {\displaystyle \alpha }

, we can write

          T

            11

          (

            2

              C

                1

            +

                  2

                    C

                      2

                α

          )

          (

              α

                2

            −

              α

                −
                1

          )

    {\displaystyle T_{11}=\left(2C_{1}+{\frac {2C_{2}}{\alpha }}\right)\left(\alpha ^{2}-\alpha ^{-1}\right)}

and the engineering stress (force per unit reference area) for an incompressible Mooney–Rivlin material under simple tension can be calculated using

          T

            11

              e
              n
              g

          T

            11

          α

            2

          α

            3

                    T

                      11

                  α

    {\displaystyle T_{11}^{\mathrm {eng} }=T_{11}\alpha _{2}\alpha {3}={\cfrac {T{11}}{\alpha }}}

. Hence

          T

            11

              e
              n
              g

          (

            2

              C

                1

            +

                  2

                    C

                      2

                α

          )

          (

            α
            −

              α

                −
                2

          )

    {\displaystyle T_{11}^{\mathrm {eng} }=\left(2C_{1}+{\frac {2C_{2}}{\alpha }}\right)\left(\alpha -\alpha ^{-2}\right)}

If we define

          T

            11

            ∗

        :=

                    T

                      11

                        e
                        n
                        g

                  α
                  −

                    α

                      −
                      2

        ;

        β
        :=

                  1

                  α

    {\displaystyle T_{11}^{*}:={\cfrac {T_{11}^{\mathrm {eng} }}{\alpha -\alpha ^{-2}}}~;~~\beta :={\cfrac {1}{\alpha }}}

then

          T

            11

            ∗

        2

          C

            1

        +
        2

          C

            2

        β

        .

    {\displaystyle T_{11}^{*}=2C_{1}+2C_{2}\beta ~.}

The slope of the

          T

            11

            ∗

    {\displaystyle T_{11}^{*}}

 versus

        β

    {\displaystyle \beta }

 line gives the value of

          C

            2

    {\displaystyle C_{2}}

 while the intercept with the

          T

            11

            ∗

    {\displaystyle T_{11}^{*}}

 axis gives the value of

          C

            1

    {\displaystyle C_{1}}

. The Mooney–Rivlin solid model usually fits experimental data better than Neo-Hookean solid does, but requires an additional empirical constant.

Equibiaxial tension
In the case of equibiaxial tension, the principal stretches are

          λ

            1

          λ

            2

        λ

    {\displaystyle \lambda _{1}=\lambda _{2}=\lambda }

. If, in addition, the material is incompressible then

          λ

            3

        1

          /

          λ

            2

    {\displaystyle \lambda _{3}=1/\lambda ^{2}}

. The Cauchy stress differences may therefore be expressed as

          σ

            11

        −

          σ

            33

          σ

            22

        −

          σ

            33

        2

          C

            1

          (

              λ

                2

            −

                      1

                        λ

                          4

          )

        −
        2

          C

            2

          (

                      1

                        λ

                          2

            −

              λ

                4

          )

    {\displaystyle \sigma _{11}-\sigma _{33}=\sigma _{22}-\sigma {33}=2C{1}\left(\lambda ^{2}-{\cfrac {1}{\lambda ^{4}}}\right)-2C_{2}\left({\cfrac {1}{\lambda ^{2}}}-\lambda ^{4}\right)}

The equations for equibiaxial tension are equivalent to those governing uniaxial compression.

Pure shear
A pure shear deformation can be achieved by applying stretches of the form

          λ

            1

        λ

        ;

          λ

            2

                  1

                  λ

        ;

          λ

            3

        1

    {\displaystyle \lambda _{1}=\lambda ~;\lambda _{2}={\cfrac {1}{\lambda }}~;\lambda _{3}=1}

The Cauchy stress differences for pure shear may therefore be expressed as

          σ

            11

        −

          σ

            33

        2

          C

            1

        (

          λ

            2

        −
        1
        )
        −
        2

          C

            2

          (

                      1

                        λ

                          2

            −
            1

          )

        ;

          σ

            22

        −

          σ

            33

        2

          C

            1

          (

                      1

                        λ

                          2

            −
            1

          )

        −
        2

          C

            2

        (

          λ

            2

        −
        1
        )

    {\displaystyle \sigma _{11}-\sigma {33}=2C{1}(\lambda ^{2}-1)-2C_{2}\left({\cfrac {1}{\lambda ^{2}}}-1\right)~;~~\sigma _{22}-\sigma {33}=2C{1}\left({\cfrac {1}{\lambda ^{2}}}-1\right)-2C_{2}(\lambda ^{2}-1)}

Therefore

          σ

            11

        −

          σ

            22

        2
        (

          C

            1

        +

          C

            2

        )

          (

              λ

                2

            −

                      1

                        λ

                          2

          )

    {\displaystyle \sigma _{11}-\sigma {22}=2(C{1}+C_{2})\left(\lambda ^{2}-{\cfrac {1}{\lambda ^{2}}}\right)}

For a pure shear deformation

          I

            1

          λ

            1

            2

        +

          λ

            2

            2

        +

          λ

            3

            2

          λ

            2

        +

                  1

                    λ

                      2

        +
        1

        ;

          I

            2

                  1

                    λ

                      1

                      2

        +

                  1

                    λ

                      2

                      2

        +

                  1

                    λ

                      3

                      2

                  1

                    λ

                      2

        +

          λ

            2

        +
        1

    {\displaystyle I_{1}=\lambda _{1}^{2}+\lambda _{2}^{2}+\lambda {3}^{2}=\lambda ^{2}+{\cfrac {1}{\lambda ^{2}}}+1~;~~I{2}={\cfrac {1}{\lambda _{1}^{2}}}+{\cfrac {1}{\lambda _{2}^{2}}}+{\cfrac {1}{\lambda _{3}^{2}}}={\cfrac {1}{\lambda ^{2}}}+\lambda ^{2}+1}

Therefore

          I

            1

          I

            2

    {\displaystyle I_{1}=I_{2}}

.

Simple shear
The deformation gradient for a simple shear deformation has the form

          F

          1

        +
        γ

            e

            1

        ⊗

            e

            2

    {\displaystyle {\boldsymbol {F}}={\boldsymbol {1}}+\gamma ~\mathbf {e} _{1}\otimes \mathbf {e} _{2}}

where

            e

            1

        ,

            e

            2

    {\displaystyle \mathbf {e} _{1},\mathbf {e} _{2}}

 are reference orthonormal basis vectors in the plane of deformation and the shear deformation is given by

        γ

        λ
        −

                  1

                  λ

        ;

          λ

            1

        λ

        ;

          λ

            2

                  1

                  λ

        ;

          λ

            3

        1

    {\displaystyle \gamma =\lambda -{\cfrac {1}{\lambda }}~;\lambda _{1}=\lambda ~;\lambda _{2}={\cfrac {1}{\lambda }}~;~~\lambda _{3}=1}

In matrix form, the deformation gradient and the left Cauchy-Green deformation tensor may then be expressed as

          F

            [

                  1

                  γ

                  0

                  0

                  1

                  0

                  0

                  0

                  1

            ]

        ;

          B

          F

        ⋅

            F

            T

            [

                  1
                  +

                    γ

                      2

                  γ

                  0

                  γ

                  1

                  0

                  0

                  0

                  1

            ]

    {\displaystyle {\boldsymbol {F}}={\begin{bmatrix}1&\gamma &0\0&1&0\0&0&1\end{bmatrix}}~;~~{\boldsymbol {B}}={\boldsymbol {F}}\cdot {\boldsymbol {F}}^{T}={\begin{bmatrix}1+\gamma ^{2}&\gamma &0\\gamma &1&0\0&0&1\end{bmatrix}}}

Therefore,

            B

            −
            1

            [

                  1

                  −
                  γ

                  0

                  −
                  γ

                  1
                  +

                    γ

                      2

                  0

                  0

                  0

                  1

            ]

    {\displaystyle {\boldsymbol {B}}^{-1}={\begin{bmatrix}1&-\gamma &0\-\gamma &1+\gamma ^{2}&0\0&0&1\end{bmatrix}}}

The Cauchy stress is given by

          σ

            [

                  −

                    p

                      ∗

                  +
                  2
                  (

                    C

                      1

                  −

                    C

                      2

                  )
                  +
                  2

                    C

                      1

                    γ

                      2

                  2
                  (

                    C

                      1

                  +

                    C

                      2

                  )
                  γ

                  0

                  2
                  (

                    C

                      1

                  +

                    C

                      2

                  )
                  γ

                  −

                    p

                      ∗

                  +
                  2
                  (

                    C

                      1

                  −

                    C

                      2

                  )
                  −
                  2

                    C

                      2

                    γ

                      2

                  0

                  0

                  0

                  −

                    p

                      ∗

                  +
                  2
                  (

                    C

                      1

                  −

                    C

                      2

                  )

            ]

    {\displaystyle {\boldsymbol {\sigma }}={\begin{bmatrix}-p^{}+2(C_{1}-C_{2})+2C_{1}\gamma ^{2}&2(C_{1}+C_{2})\gamma &0\2(C_{1}+C_{2})\gamma &-p^{}+2(C_{1}-C_{2})-2C_{2}\gamma ^{2}&0\0&0&-p^{*}+2(C_{1}-C_{2})\end{bmatrix}}}

For consistency with linear elasticity, clearly

        μ

        2
        (

          C

            1

        +

          C

            2

        )

    {\displaystyle \mu =2(C_{1}+C_{2})}

 where

        μ

    {\displaystyle \mu }

 is the shear modulus.

Rubber
Elastic response of rubber-like materials are often modeled based on the Mooney–Rivlin model. The constants

          C

            1

        ,

          C

            2

    {\displaystyle C_{1},C_{2}}

 are determined by fitting the predicted stress from the above equations to the experimental data. The recommended tests are uniaxial tension, equibiaxial compression, equibiaxial tension, uniaxial compression, and for shear, planar tension and planar compression. The two parameter Mooney–Rivlin model is usually valid for strains less than 100%.

Notes and references
