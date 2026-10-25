# Neo-Hookean solid

Neo-Hookean solid

A neo-Hookean solid is a hyperelastic material model, similar to Hooke's law, that can be used for predicting the nonlinear stress–strain behavior of materials undergoing large deformations. The model was proposed by Ronald Rivlin in 1948 using invariants, though Mooney had already described a version in stretch form in 1940, and Wall had noted the equivalence in shear with the Hooke model in 1942.
In contrast to linear elastic materials, the stress–strain curve of a neo-Hookean material is not linear. Instead, the relationship between applied stress and strain is initially linear, but at a certain point the stress–strain curve will plateau. The neo-Hookean model does not account for the dissipative release of energy as heat while straining the material, and perfect elasticity is assumed at all stages of deformation. In addition to being used to model physical materials, the stability and highly non-linear behaviour under compression has made neo-Hookean materials a popular choice for fictitious media approaches such as the third medium contact method.
The neo-Hookean model is based on the statistical thermodynamics of cross-linked polymer chains and is usable for plastics and rubber-like substances. Cross-linked polymers will act in a neo-Hookean manner because initially the polymer chains can move relative to each other when a stress is applied. However, at a certain point the polymer chains will be stretched to the maximum point that the covalent cross links will allow, and this will cause a dramatic increase in the elastic modulus of the material. The neo-Hookean material model does not predict that increase in modulus at large strains and is typically accurate only for strains less than 20%. The model is also inadequate for biaxial states of stress and has been superseded by the Mooney–Rivlin model.
The primary, and likely most widely employed, strain-energy function formulation is the Mooney–Rivlin model, which reduces to the widely known neo-Hookean model. The strain energy density function for an incompressible Mooney–Rivlin material is

        W

          C

            10

        (

          I

            1

        −
        3
        )
        +

          C

            01

        (

          I

            2

        −
        3
        )
        ;

          I

            3

        1

    {\displaystyle W=C_{10}(I_{1}-3)+C_{01}(I_{2}-3);~I_{3}=1}

Setting

          C

            01

        0

    {\displaystyle C_{01}=0}

 reduces to the (incompressible) neo-Hookean strain energy function

        W

          C

            1

        (

          I

            1

        −
        3
        )

    {\displaystyle W=C_{1}(I_{1}-3)}

where

          C

            1

    {\displaystyle C_{1}}

 is a material constant, and

          I

            1

    {\displaystyle I_{1}}

 is the first principal invariant (trace), of the left Cauchy-Green deformation tensor, i.e.,

          I

            1

          t
          r

        (

          B

        )

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

    {\displaystyle I_{1}=\mathrm {tr} (\mathbf {B} )=\lambda _{1}^{2}+\lambda _{2}^{2}+\lambda _{3}^{2}}

where

          λ

            i

    {\displaystyle \lambda _{i}}

 are the principal stretches. Similarly, the second and third principal invariants are

                  I

                    2

                    1
                    2

                    (

                  I

                    1

                    2

                −

                  t
                  r

                (

                    B

                    2

                )

                    )

                  I

                    3

                  d
                  e
                  t

                (

                  B

                )

                  d
                  e
                  t

                (

                  F

                    F

                    T

                )

                (

                  λ

                    1

                  λ

                    2

                  λ

                    3

                  )

                    2

                  J

                    2

    {\displaystyle {\begin{aligned}I_{2}&={\frac {1}{2}}{\big (}I_{1}^{2}-\mathrm {tr} (\mathbf {B} ^{2}){\big )}\I_{3}&=\mathrm {det} (\mathbf {B} )=\mathrm {det} (\mathbf {F} \mathbf {F} ^{T})=(\lambda _{1}\lambda _{2}\lambda _{3})^{2}=J^{2}\end{aligned}}}

where

          F

    {\displaystyle \mathbf {F} }

 is the deformation gradient. Relaxing the incompressible assumption (

        J

        1

    {\displaystyle J=1}

), one can add a hydrostatic work term

          W

            H

        (

          I

            3

        )

    {\displaystyle W_{H}(I_{3})}

 for a compressible material, but the first two terms must be adjusted to uncouple deviatoric and volumetric terms, resulting in

        W

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

          D

            1

        (
        J
        −
        1

          )

            2

    {\displaystyle W=C_{10}({\bar {I}}{1}-3)+C{01}({\bar {I}}{2}-3)+D{1}(J-1)^{2}}

where

                I
                ¯

            1

          I

            1

          J

            −
            2

              /

            3

        ,

                I
                ¯

            2

          I

            2

          J

            −
            4

              /

            3

    {\displaystyle {\bar {I}}{1}=I{1}J^{-2/3},~~~{\bar {I}}{2}=I{2}J^{-4/3}}

Recall that a Mooney–Rivlin material with

          C

            01

        0

    {\displaystyle C_{01}=0}

 is a neo-Hookean material, so the compressible neo-Hookean strain energy density is given by

        W

          C

            1

        (

          I

            1

          J

            −
            2

              /

            3

        −
        3
        )
        +

          D

            1

        (
        J
        −
        1

          )

            2

    {\displaystyle W=C_{1}(I_{1}J^{-2/3}-3)+D_{1}(J-1)^{2}}

where

          D

            1

    {\displaystyle D_{1}}

 is a material constant.
Note that this is one of several strain energy functions employed in hyperelasticity measurements. For example, some neo-Hookean models contain an extra

        ln
        ⁡
        J

    {\displaystyle \ln J}

 term, namely

        W

          C

            1

        (

          I

            1

        −
        3
        −
        2
        ln
        ⁡
        J
        )
        +

          D

            1

        (
        J
        −
        1

          )

            2

    {\displaystyle W=C_{1}(I_{1}-3-2\ln J)+D_{1}(J-1)^{2}}

Finally, for consistency with linear elasticity,

          C

            1

            μ
            2

        ;

          D

            1

            κ
            2

    {\displaystyle C_{1}={\frac {\mu }{2}}~;~~D_{1}={\frac {\kappa }{2}}}

where

        κ

    {\displaystyle \kappa }

 is the bulk modulus and

        μ

    {\displaystyle \mu }

 is the shear modulus or the second Lamé parameter. Alternative definitions of

          C

            1

    {\displaystyle C_{1}}

 and

          D

            1

    {\displaystyle D_{1}}

 are sometimes used, notably in commercial finite element analysis software such as Abaqus.

Cauchy stress in terms of deformation tensors

Compressible neo-Hookean material
For a compressible neo-Hookean material, the Cauchy stress is given by

        J

          σ

        −
        p

          I

        +
        2

          C

            1

        dev
        ⁡
        (

              B
              ¯

        )

        −
        p

          I

        +

              2

                C

                  1

              J

                2

                  /

                3

        dev
        ⁡
        (

          B

        )

    {\displaystyle J~{\boldsymbol {\sigma }}=-p~{\boldsymbol {I}}+2C_{1}\operatorname {dev} ({\bar {\boldsymbol {B}}})=-p~{\boldsymbol {I}}+{\frac {2C_{1}}{J^{2/3}}}\operatorname {dev} ({\boldsymbol {B}})}

where

          B

    {\displaystyle {\boldsymbol {B}}}

 is the left Cauchy–Green deformation tensor, and

        p
        :=
        −
        2

          D

            1

        J
        (
        J
        −
        1
        )

        ;

        dev
        ⁡
        (

              B
              ¯

        )

              B
              ¯

        −

              1
              3

                I
                ¯

            1

          I

        ;

              B
              ¯

          J

            −
            2

              /

            3

          B

        .

    {\displaystyle p:=-2D_{1}~J(J-1)~;~\operatorname {dev} ({\bar {\boldsymbol {B}}})={\bar {\boldsymbol {B}}}-{\tfrac {1}{3}}{\bar {I}}_{1}{\boldsymbol {I}}~;~~{\bar {\boldsymbol {B}}}=J^{-2/3}{\boldsymbol {B}}~.}

For infinitesimal strains (

          ε

    {\displaystyle {\boldsymbol {\varepsilon }}}

)

        J
        ≈
        1
        +
        tr
        ⁡
        (

          ε

        )

        ;

          B

        ≈

          I

        +
        2

          ε

    {\displaystyle J\approx 1+\operatorname {tr} ({\boldsymbol {\varepsilon }})~;~~{\boldsymbol {B}}\approx {\boldsymbol {I}}+2{\boldsymbol {\varepsilon }}}

and the Cauchy stress can be expressed as

          σ

        ≈
        4

          C

            1

          (

              ε

            −

                  1
                  3

            tr
            ⁡
            (

              ε

            )

              I

          )

        +
        2

          D

            1

        tr
        ⁡
        (

          ε

        )

          I

    {\displaystyle {\boldsymbol {\sigma }}\approx 4C_{1}\left({\boldsymbol {\varepsilon }}-{\tfrac {1}{3}}\operatorname {tr} ({\boldsymbol {\varepsilon }}){\boldsymbol {I}}\right)+2D_{1}\operatorname {tr} ({\boldsymbol {\varepsilon }}){\boldsymbol {I}}}

Comparison with Hooke's law shows that

        μ

        2

          C

            1

    {\displaystyle \mu =2C_{1}}

 and

        κ

        2

          D

            1

    {\displaystyle \kappa =2D_{1}}

, which are the shear and bulk moduli, respectively.

Incompressible neo-Hookean material
For an incompressible neo-Hookean material with

        J

        1

    {\displaystyle J=1}

          σ

        −
        p

          I

        +
        2

          C

            1

          B

    {\displaystyle {\boldsymbol {\sigma }}=-p~{\boldsymbol {I}}+2C_{1}{\boldsymbol {B}}}

where

        p

    {\displaystyle p}

 is an undetermined pressure.

Cauchy stress in terms of principal stretches

Compressible neo-Hookean material
For a compressible neo-Hookean hyperelastic material, the principal components of the Cauchy stress are given by

          σ

            i

        2

          C

            1

          J

            −
            5

              /

            3

          [

              λ

                i

                2

            −

                        I

                          1

                      3

          ]

        +
        2

          D

            1

        (
        J
        −
        1
        )

        ;

        i

        1
        ,
        2
        ,
        3

    {\displaystyle \sigma {i}=2C{1}J^{-5/3}\left[\lambda {i}^{2}-{\cfrac {I{1}}{3}}\right]+2D_{1}(J-1)~;~~i=1,2,3}

Therefore, the differences between the principal stresses are

          σ

            11

        −

          σ

            33

                  2

                    C

                      1

                    J

                      5

                        /

                      3

        (

          λ

            1

            2

        −

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

                    J

                      5

                        /

                      3

        (

          λ

            2

            2

        −

          λ

            3

            2

        )

    {\displaystyle \sigma _{11}-\sigma {33}={\cfrac {2C{1}}{J^{5/3}}}(\lambda _{1}^{2}-\lambda _{3}^{2})~;~~\sigma _{22}-\sigma {33}={\cfrac {2C{1}}{J^{5/3}}}(\lambda _{2}^{2}-\lambda _{3}^{2})}

Incompressible neo-Hookean material
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

For an incompressible neo-Hookean material,

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

        ;

          λ

            1

          λ

            2

          λ

            3

        1

    {\displaystyle W=C_{1}(\lambda _{1}^{2}+\lambda _{2}^{2}+\lambda _{3}^{2}-3)~;~~\lambda _{1}\lambda _{2}\lambda _{3}=1}

Therefore,

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

        ;

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

        ;

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

    {\displaystyle {\cfrac {\partial {W}}{\partial \lambda {1}}}=2C{1}\lambda _{1}~;{\cfrac {\partial {W}}{\partial \lambda {2}}}=2C{1}\lambda _{2}~;{\cfrac {\partial {W}}{\partial \lambda {3}}}=2C{1}\lambda _{3}}

which gives

          σ

            11

        −

          σ

            33

        2
        (

          λ

            1

            2

        −

          λ

            3

            2

        )

          C

            1

        ;

          σ

            22

        −

          σ

            33

        2
        (

          λ

            2

            2

        −

          λ

            3

            2

        )

          C

            1

    {\displaystyle \sigma _{11}-\sigma _{33}=2(\lambda _{1}^{2}-\lambda {3}^{2})C{1}~;~~\sigma _{22}-\sigma _{33}=2(\lambda _{2}^{2}-\lambda {3}^{2})C{1}}

Uniaxial extension

Compressible neo-Hookean material

For a compressible material undergoing uniaxial extension, the principal stretches are

          λ

            1

        λ

        ;

          λ

            2

          λ

            3

                J
                λ

        ;

          I

            1

          λ

            2

        +

                2
                J

              λ

    {\displaystyle \lambda _{1}=\lambda ~;\lambda _{2}=\lambda {3}={\sqrt {\tfrac {J}{\lambda }}}~;I{1}=\lambda ^{2}+{\tfrac {2J}{\lambda }}}

Hence, the true (Cauchy) stresses for a compressible neo-Hookean material are given by

                  σ

                    11

                          4

                            C

                              1

                          3

                            J

                              5

                                /

                              3

                  (

                      λ

                        2

                    −

                          J
                          λ

                  )

                +
                2

                  D

                    1

                (
                J
                −
                1
                )

                  σ

                    22

                  σ

                    33

                          2

                            C

                              1

                          3

                            J

                              5

                                /

                              3

                  (

                          J
                          λ

                    −

                      λ

                        2

                  )

                +
                2

                  D

                    1

                (
                J
                −
                1
                )

    {\displaystyle {\begin{aligned}\sigma {11}&={\cfrac {4C{1}}{3J^{5/3}}}\left(\lambda ^{2}-{\tfrac {J}{\lambda }}\right)+2D_{1}(J-1)\\sigma _{22}&=\sigma {33}={\cfrac {2C{1}}{3J^{5/3}}}\left({\tfrac {J}{\lambda }}-\lambda ^{2}\right)+2D_{1}(J-1)\end{aligned}}}

The stress differences are given by

          σ

            11

        −

          σ

            33

                  2

                    C

                      1

                    J

                      5

                        /

                      3

          (

              λ

                2

            −

                  J
                  λ

          )

        ;

          σ

            22

        −

          σ

            33

        0

    {\displaystyle \sigma _{11}-\sigma {33}={\cfrac {2C{1}}{J^{5/3}}}\left(\lambda ^{2}-{\tfrac {J}{\lambda }}\right)~;~~\sigma _{22}-\sigma _{33}=0}

If the material is unconstrained we have

          σ

            22

          σ

            33

        0

    {\displaystyle \sigma _{22}=\sigma _{33}=0}

. Then

          σ

            11

                  2

                    C

                      1

                    J

                      5

                        /

                      3

          (

              λ

                2

            −

                  J
                  λ

          )

    {\displaystyle \sigma {11}={\cfrac {2C{1}}{J^{5/3}}}\left(\lambda ^{2}-{\tfrac {J}{\lambda }}\right)}

Equating the two expressions for

          σ

            11

    {\displaystyle \sigma _{11}}

 gives a relation for

        J

    {\displaystyle J}

 as a function of

        λ

    {\displaystyle \lambda }

, i.e.,

                  4

                    C

                      1

                  3

                    J

                      5

                        /

                      3

          (

              λ

                2

            −

                  J
                  λ

          )

        +
        2

          D

            1

        (
        J
        −
        1
        )

                  2

                    C

                      1

                    J

                      5

                        /

                      3

          (

              λ

                2

            −

                  J
                  λ

          )

    {\displaystyle {\cfrac {4C_{1}}{3J^{5/3}}}\left(\lambda ^{2}-{\tfrac {J}{\lambda }}\right)+2D_{1}(J-1)={\cfrac {2C_{1}}{J^{5/3}}}\left(\lambda ^{2}-{\tfrac {J}{\lambda }}\right)}

or

          D

            1

          J

            8

              /

            3

        −

          D

            1

          J

            5

              /

            3

        +

                C

                  1

                3
                λ

        J
        −

                  C

                    1

                  λ

                    2

              3

        0

    {\displaystyle D_{1}J^{8/3}-D_{1}J^{5/3}+{\tfrac {C_{1}}{3\lambda }}J-{\tfrac {C_{1}\lambda ^{2}}{3}}=0}

The above equation can be solved numerically using a Newton–Raphson iterative root-finding procedure.

Incompressible neo-Hookean material

Under uniaxial extension,

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

. Therefore,

          σ

            22

        −

          σ

            33

        0

    {\displaystyle \sigma _{22}-\sigma _{33}=0}

where

          ε

            11

        λ
        −
        1

    {\displaystyle \varepsilon _{11}=\lambda -1}

 is the engineering strain. This equation is written as

          σ

            11

              t
              r
              u
              e

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

    {\displaystyle \sigma {11}^{\mathrm {true} }=2C{1}\left(\lambda ^{2}-{\cfrac {1}{\lambda }}\right)}

The equation above is for the true stress (ratio of the elongation force to deformed cross-section). For the engineering stress the equation is:

          σ

            11

              e
              n
              g

            1
            λ

          σ

            11

              t
              r
              u
              e

        ;

          σ

            11

              e
              n
              g

        2

          C

            1

          (

            λ
            −

                      1

                        λ

                          2

          )

    {\displaystyle \sigma _{11}^{\mathrm {eng} }={\frac {1}{\lambda }}\sigma _{11}^{\mathrm {true} };\sigma {11}^{\mathrm {eng} }=2C{1}\left(\lambda -{\cfrac {1}{\lambda ^{2}}}\right)}

For small deformations

        ε
        ≪
        1

    {\displaystyle \varepsilon \ll 1}

 we will have:

          σ

            11

        6

          C

            1

        ε

        3
        μ
        ε

    {\displaystyle \sigma {11}=6C{1}\varepsilon =3\mu \varepsilon }

Thus, the equivalent Young's modulus of a neo-Hookean solid in uniaxial extension is

        3
        μ

    {\displaystyle 3\mu }

, which is in concordance with linear elasticity (

        E

        2
        μ
        (
        1
        +
        ν
        )

    {\displaystyle E=2\mu (1+\nu )}

 with

        ν

        0.5

    {\displaystyle \nu =0.5}

 for incompressibility).

Equibiaxial extension

Compressible neo-Hookean material

In the case of equibiaxial extension

          λ

            1

          λ

            2

        λ

        ;

          λ

            3

              J

                λ

                  2

        ;

          I

            1

        2

          λ

            2

        +

                J

                  2

                λ

                  4

    {\displaystyle \lambda _{1}=\lambda _{2}=\lambda ~;\lambda {3}={\tfrac {J}{\lambda ^{2}}}~;I{1}=2\lambda ^{2}+{\tfrac {J^{2}}{\lambda ^{4}}}}

Therefore,

                  σ

                    11

                2

                  C

                    1

                  [

                                λ

                                  2

                                J

                                  5

                                    /

                                  3

                    −

                              1

                              3
                              J

                      (

                        2

                          λ

                            2

                        +

                                    J

                                      2

                                    λ

                                      4

                      )

                  ]

                +
                2

                  D

                    1

                (
                J
                −
                1
                )

                  σ

                    22

                  σ

                    33

                2

                  C

                    1

                  [

                                J

                                  1

                                    /

                                  3

                                λ

                                  4

                    −

                              1

                              3
                              J

                      (

                        2

                          λ

                            2

                        +

                                    J

                                      2

                                    λ

                                      4

                      )

                  ]

                +
                2

                  D

                    1

                (
                J
                −
                1
                )

    {\displaystyle {\begin{aligned}\sigma {11}&=2C{1}\left[{\cfrac {\lambda ^{2}}{J^{5/3}}}-{\cfrac {1}{3J}}\left(2\lambda ^{2}+{\cfrac {J^{2}}{\lambda ^{4}}}\right)\right]+2D_{1}(J-1)\&=\sigma _{22}\\sigma {33}&=2C{1}\left[{\cfrac {J^{1/3}}{\lambda ^{4}}}-{\cfrac {1}{3J}}\left(2\lambda ^{2}+{\cfrac {J^{2}}{\lambda ^{4}}}\right)\right]+2D_{1}(J-1)\end{aligned}}}

The stress differences are

          σ

            11

        −

          σ

            22

        0

        ;

          σ

            11

        −

          σ

            33

                  2

                    C

                      1

                    J

                      5

                        /

                      3

          (

              λ

                2

            −

                        J

                          2

                        λ

                          4

          )

    {\displaystyle \sigma _{11}-\sigma _{22}=0~;~~\sigma _{11}-\sigma {33}={\cfrac {2C{1}}{J^{5/3}}}\left(\lambda ^{2}-{\cfrac {J^{2}}{\lambda ^{4}}}\right)}

If the material is in a state of plane stress then

          σ

            33

        0

    {\displaystyle \sigma _{33}=0}

 and we have

          σ

            11

          σ

            22

                  2

                    C

                      1

                    J

                      5

                        /

                      3

          (

              λ

                2

            −

                        J

                          2

                        λ

                          4

          )

    {\displaystyle \sigma _{11}=\sigma {22}={\cfrac {2C{1}}{J^{5/3}}}\left(\lambda ^{2}-{\cfrac {J^{2}}{\lambda ^{4}}}\right)}

We also have a relation between

        J

    {\displaystyle J}

 and

        λ

    {\displaystyle \lambda }

:

        2

          C

            1

          [

                        λ

                          2

                        J

                          5

                            /

                          3

            −

                      1

                      3
                      J

              (

                2

                  λ

                    2

                +

                            J

                              2

                            λ

                              4

              )

          ]

        +
        2

          D

            1

        (
        J
        −
        1
        )

                  2

                    C

                      1

                    J

                      5

                        /

                      3

          (

              λ

                2

            −

                        J

                          2

                        λ

                          4

          )

    {\displaystyle 2C_{1}\left[{\cfrac {\lambda ^{2}}{J^{5/3}}}-{\cfrac {1}{3J}}\left(2\lambda ^{2}+{\cfrac {J^{2}}{\lambda ^{4}}}\right)\right]+2D_{1}(J-1)={\cfrac {2C_{1}}{J^{5/3}}}\left(\lambda ^{2}-{\cfrac {J^{2}}{\lambda ^{4}}}\right)}

or,

          (

            2

              D

                1

            −

                        C

                          1

                        λ

                          4

          )

          J

            2

        +

                  3

                    C

                      1

                    λ

                      4

          J

            4

              /

            3

        −
        3

          D

            1

        J
        −
        2

          C

            1

          λ

            2

        0

    {\displaystyle \left(2D_{1}-{\cfrac {C_{1}}{\lambda ^{4}}}\right)J^{2}+{\cfrac {3C_{1}}{\lambda ^{4}}}J^{4/3}-3D_{1}J-2C_{1}\lambda ^{2}=0}

This equation can be solved for

        J

    {\displaystyle J}

 using Newton's method.

Incompressible neo-Hookean material
For an incompressible material

        J

        1

    {\displaystyle J=1}

 and the differences between the principal Cauchy stresses take the form

          σ

            11

        −

          σ

            22

        0

        ;

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

                          4

          )

    {\displaystyle \sigma _{11}-\sigma _{22}=0~;~~\sigma _{11}-\sigma {33}=2C{1}\left(\lambda ^{2}-{\cfrac {1}{\lambda ^{4}}}\right)}

Under plane stress conditions we have

          σ

            11

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

    {\displaystyle \sigma {11}=2C{1}\left(\lambda ^{2}-{\cfrac {1}{\lambda ^{4}}}\right)}

Pure dilation
For the case of pure dilation

          λ

            1

          λ

            2

          λ

            3

        λ

        :

        J

          λ

            3

        ;

          I

            1

        3

          λ

            2

    {\displaystyle \lambda _{1}=\lambda _{2}=\lambda {3}=\lambda ~:J=\lambda ^{3}~;I{1}=3\lambda ^{2}}

Therefore, the principal Cauchy stresses for a compressible neo-Hookean material are given by

          σ

            i

        2

          C

            1

          (

                      1

                        λ

                          3

            −

                      1

                      λ

          )

        +
        2

          D

            1

        (

          λ

            3

        −
        1
        )

    {\displaystyle \sigma {i}=2C{1}\left({\cfrac {1}{\lambda ^{3}}}-{\cfrac {1}{\lambda }}\right)+2D_{1}(\lambda ^{3}-1)}

If the material is incompressible then

          λ

            3

        1

    {\displaystyle \lambda ^{3}=1}

 and the principal stresses can be arbitrary.
The figures below show that extremely high stresses are needed to achieve large triaxial extensions or compressions. Equivalently, relatively small triaxial stretch states can cause very high stresses to develop in a rubber-like material. The magnitude of the stress is quite sensitive to the bulk modulus but not to the shear modulus.

Simple shear
For the case of simple shear the deformation gradient in terms of components with respect to a reference basis is of the form

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

    {\displaystyle {\boldsymbol {F}}={\begin{bmatrix}1&\gamma &0\0&1&0\0&0&1\end{bmatrix}}}

where

        γ

    {\displaystyle \gamma }

 is the shear deformation. Therefore, the left Cauchy-Green deformation tensor is

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

    {\displaystyle {\boldsymbol {B}}={\boldsymbol {F}}\cdot {\boldsymbol {F}}^{T}={\begin{bmatrix}1+\gamma ^{2}&\gamma &0\\gamma &1&0\0&0&1\end{bmatrix}}}

Compressible neo-Hookean material
In this case

        J

        det
        (

          F

        )

        1

    {\displaystyle J=\det({\boldsymbol {F}})=1}

. Hence,

          σ

        2

          C

            1

        dev
        ⁡
        (

          B

        )

    {\displaystyle {\boldsymbol {\sigma }}=2C_{1}\operatorname {dev} ({\boldsymbol {B}})}

. Now,

        dev
        ⁡
        (

          B

        )

          B

        −

              1
              3

        tr
        ⁡
        (

          B

        )

          I

          B

        −

              1
              3

        (
        3
        +

          γ

            2

        )

          I

            [

                        2
                        3

                    γ

                      2

                  γ

                  0

                  γ

                  −

                        1
                        3

                    γ

                      2

                  0

                  0

                  0

                  −

                        1
                        3

                    γ

                      2

            ]

    {\displaystyle \operatorname {dev} ({\boldsymbol {B}})={\boldsymbol {B}}-{\tfrac {1}{3}}\operatorname {tr} ({\boldsymbol {B}}){\boldsymbol {I}}={\boldsymbol {B}}-{\tfrac {1}{3}}(3+\gamma ^{2}){\boldsymbol {I}}={\begin{bmatrix}{\tfrac {2}{3}}\gamma ^{2}&\gamma &0\\gamma &-{\tfrac {1}{3}}\gamma ^{2}&0\0&0&-{\tfrac {1}{3}}\gamma ^{2}\end{bmatrix}}}

Hence the Cauchy stress is given by

          σ

            [

                          4

                            C

                              1

                        3

                    γ

                      2

                  2

                    C

                      1

                  γ

                  0

                  2

                    C

                      1

                  γ

                  −

                          2

                            C

                              1

                        3

                    γ

                      2

                  0

                  0

                  0

                  −

                          2

                            C

                              1

                        3

                    γ

                      2

            ]

    {\displaystyle {\boldsymbol {\sigma }}={\begin{bmatrix}{\tfrac {4C_{1}}{3}}\gamma ^{2}&2C_{1}\gamma &0\2C_{1}\gamma &-{\tfrac {2C_{1}}{3}}\gamma ^{2}&0\0&0&-{\tfrac {2C_{1}}{3}}\gamma ^{2}\end{bmatrix}}}

Incompressible neo-Hookean material
Using the relation for the Cauchy stress for an incompressible neo-Hookean material we get

          σ

        −
        p

          I

        +
        2

          C

            1

          B

            [

                  2

                    C

                      1

                  (
                  1
                  +

                    γ

                      2

                  )
                  −
                  p

                  2

                    C

                      1

                  γ

                  0

                  2

                    C

                      1

                  γ

                  2

                    C

                      1

                  −
                  p

                  0

                  0

                  0

                  2

                    C

                      1

                  −
                  p

            ]

    {\displaystyle {\boldsymbol {\sigma }}=-p~{\boldsymbol {I}}+2C_{1}{\boldsymbol {B}}={\begin{bmatrix}2C_{1}(1+\gamma ^{2})-p&2C_{1}\gamma &0\2C_{1}\gamma &2C_{1}-p&0\0&0&2C_{1}-p\end{bmatrix}}}

Thus neo-Hookean solid shows linear dependence of shear stresses upon shear deformation and quadratic dependence of the normal stress difference on the shear deformation. The expressions for the Cauchy stress for a compressible and an incompressible neo-Hookean material in simple shear represent the same quantity and provide a means of determining the unknown pressure

        p

    {\displaystyle p}

.
