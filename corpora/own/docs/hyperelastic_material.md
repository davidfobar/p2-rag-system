# Hyperelastic material

Hyperelastic material

A hyperelastic or Green elastic material is a type of constitutive model for ideally elastic material for which the stress–strain relationship derives from a strain energy density function. The hyperelastic material is a special case of a Cauchy elastic material.
For many materials, linear elastic models do not accurately describe the observed material behaviour. The most common example of this kind of material is rubber, whose stress-strain relationship can be defined as non-linearly elastic, isotropic and incompressible. Hyperelasticity provides a means of modeling the stress–strain behavior of such materials. The behavior of unfilled, vulcanized elastomers often conforms closely to the hyperelastic ideal. Filled elastomers and biological tissues are also often modeled via the hyperelastic idealization. In addition to being used to model physical materials, hyperelastic materials are also used as fictitious media, e.g. in the third medium contact method.
Ronald Rivlin and Melvin Mooney developed the first hyperelastic models, the Neo-Hookean and Mooney–Rivlin solids. Many other hyperelastic models have since been developed. Other widely used hyperelastic material models include the Ogden model and the Arruda–Boyce model.

Hyperelastic material models

Saint Venant–Kirchhoff model
The simplest hyperelastic material model is the Saint Venant–Kirchhoff model which is just an extension of the geometrically linear elastic material model to the geometrically nonlinear regime. This model has the general form and the isotropic form respectively

                  S

                  C

                :

                  E

                  S

                λ

                  tr

                (

                  E

                )

                    I

                +
                2
                μ

                  E

                  .

    {\displaystyle {\begin{aligned}{\boldsymbol {S}}&={\boldsymbol {C}}:{\boldsymbol {E}}\{\boldsymbol {S}}&=\lambda ~{\text{tr}}({\boldsymbol {E}}){\boldsymbol {\mathit {I}}}+2\mu {\boldsymbol {E}}{\text{.}}\end{aligned}}}

where

          :

    {\displaystyle \mathbin {:} }

 is tensor contraction,

          S

    {\displaystyle {\boldsymbol {S}}}

 is the second Piola–Kirchhoff stress,

          C

        ∈

            R

            3
            ×
            3
            ×
            3
            ×
            3

    {\displaystyle {\boldsymbol {C}}\in \mathbb {R} ^{3\times 3\times 3\times 3}}

 is a fourth order stiffness tensor and

          E

    {\displaystyle {\boldsymbol {E}}}

 is the Lagrangian Green strain given by

          E

            1
            2

          [

            (

              ∇

                  X

              u

              )

                  T

            +

              ∇

                  X

              u

            +
            (

              ∇

                  X

              u

              )

                  T

            ⋅

              ∇

                  X

              u

          ]

    {\displaystyle \mathbf {E} ={\frac {1}{2}}\left[(\nabla _{\mathbf {X} }\mathbf {u} )^{\textsf {T}}+\nabla _{\mathbf {X} }\mathbf {u} +(\nabla _{\mathbf {X} }\mathbf {u} )^{\textsf {T}}\cdot \nabla _{\mathbf {X} }\mathbf {u} \right]\,!}

        λ

    {\displaystyle \lambda }

 and

        μ

    {\displaystyle \mu }

 are the Lamé constants, and

            I

    {\displaystyle {\boldsymbol {\mathit {I}}}}

 is the second order unit tensor.
The strain-energy density per unit volume (of the reference configuration) function for the Saint Venant–Kirchhoff model is

        W
        (

          E

        )

            λ
            2

        [

          tr

        (

          E

        )

          ]

            2

        +
        μ

          tr

              (

                  E

                  2

              )

    {\displaystyle W({\boldsymbol {E}})={\frac {\lambda }{2}}[{\text{tr}}({\boldsymbol {E}})]^{2}+\mu {\text{tr}}{\mathord {\left({\boldsymbol {E}}^{2}\right)}}}

and the second Piola–Kirchhoff stress can be derived from the relation

          S

              ∂
              W

              ∂

                E

        .

    {\displaystyle {\boldsymbol {S}}={\frac {\partial W}{\partial {\boldsymbol {E}}}}~.}

Classification of hyperelastic material models
Hyperelastic material models can be classified as:

phenomenological descriptions of observed behavior
Fung
Mooney–Rivlin
Ogden
Polynomial
Saint Venant–Kirchhoff
Yeoh
Marlow
mechanistic models deriving from arguments about the underlying structure of the material
Arruda–Boyce model
Neo–Hookean model
Buche–Silberstein model
hybrids of phenomenological and mechanistic models
Gent
Van der Waals
Generally, a hyperelastic model should satisfy the Drucker stability criterion.
Some hyperelastic models satisfy the Valanis-Landel hypothesis which states that the strain energy function can be separated into the sum of separate functions of the principal stretches

        (

          λ

            1

        ,

          λ

            2

        ,

          λ

            3

        )

    {\displaystyle (\lambda _{1},\lambda _{2},\lambda _{3})}

:

        W

        f
        (

          λ

            1

        )
        +
        f
        (

          λ

            2

        )
        +
        f
        (

          λ

            3

        )

        .

    {\displaystyle W=f(\lambda _{1})+f(\lambda _{2})+f(\lambda _{3})\,.}

Stress–strain relations

Compressible hyperelastic materials

First Piola–Kirchhoff stress
If

        W
        (

          F

        )

    {\displaystyle W({\boldsymbol {F}})}

 is the strain energy density function, the 1st Piola–Kirchhoff stress tensor can be calculated for a hyperelastic material as

          P

              ∂
              W

              ∂

                F

          or

          P

            i
            K

              ∂
              W

              ∂

                F

                  i
                  K

        .

    {\displaystyle {\boldsymbol {P}}={\frac {\partial W}{\partial {\boldsymbol {F}}}}\qquad {\text{or}}\qquad P_{iK}={\frac {\partial W}{\partial F_{iK}}}.}

where

          F

    {\displaystyle {\boldsymbol {F}}}

 is the deformation gradient. In terms of the Lagrangian Green strain (

          E

    {\displaystyle {\boldsymbol {E}}}

)

          P

          F

        ⋅

              ∂
              W

              ∂

                E

          or

          P

            i
            K

          F

            i
            L

              ∂
              W

              ∂

                E

                  L
                  K

        .

    {\displaystyle {\boldsymbol {P}}={\boldsymbol {F}}\cdot {\frac {\partial W}{\partial {\boldsymbol {E}}}}\qquad {\text{or}}\qquad P_{iK}=F_{iL}~{\frac {\partial W}{\partial E_{LK}}}~.}

In terms of the right Cauchy–Green deformation tensor (

          C

    {\displaystyle {\boldsymbol {C}}}

)

          P

        2

          F

        ⋅

              ∂
              W

              ∂

                C

          or

          P

            i
            K

        2

          F

            i
            L

              ∂
              W

              ∂

                C

                  L
                  K

        .

    {\displaystyle {\boldsymbol {P}}=2~{\boldsymbol {F}}\cdot {\frac {\partial W}{\partial {\boldsymbol {C}}}}\qquad {\text{or}}\qquad P_{iK}=2~F_{iL}~{\frac {\partial W}{\partial C_{LK}}}~.}

Second Piola–Kirchhoff stress
If

          S

    {\displaystyle {\boldsymbol {S}}}

 is the second Piola–Kirchhoff stress tensor then

          S

            F

            −
            1

        ⋅

              ∂
              W

              ∂

                F

          or

          S

            I
            J

          F

            I
            k

            −
            1

              ∂
              W

              ∂

                F

                  k
                  J

        .

    {\displaystyle {\boldsymbol {S}}={\boldsymbol {F}}^{-1}\cdot {\frac {\partial W}{\partial {\boldsymbol {F}}}}\qquad {\text{or}}\qquad S_{IJ}=F_{Ik}^{-1}{\frac {\partial W}{\partial F_{kJ}}}~.}

In terms of the Lagrangian Green strain

          S

              ∂
              W

              ∂

                E

          or

          S

            I
            J

              ∂
              W

              ∂

                E

                  I
                  J

        .

    {\displaystyle {\boldsymbol {S}}={\frac {\partial W}{\partial {\boldsymbol {E}}}}\qquad {\text{or}}\qquad S_{IJ}={\frac {\partial W}{\partial E_{IJ}}}~.}

In terms of the right Cauchy–Green deformation tensor

          S

        2

              ∂
              W

              ∂

                C

          or

          S

            I
            J

        2

              ∂
              W

              ∂

                C

                  I
                  J

        .

    {\displaystyle {\boldsymbol {S}}=2~{\frac {\partial W}{\partial {\boldsymbol {C}}}}\qquad {\text{or}}\qquad S_{IJ}=2~{\frac {\partial W}{\partial C_{IJ}}}~.}

The above relation is also known as the Doyle-Ericksen formula in the material configuration.

Cauchy stress
Similarly, the Cauchy stress is given by

          σ

            1
            J

              ∂
              W

              ∂

                F

        ⋅

            F

              T

        ;

        J
        :=
        det

          F

          or

          σ

            i
            j

            1
            J

              ∂
              W

              ∂

                F

                  i
                  K

          F

            j
            K

        .

    {\displaystyle {\boldsymbol {\sigma }}={\frac {1}{J}}~{\frac {\partial W}{\partial {\boldsymbol {F}}}}\cdot {\boldsymbol {F}}^{\textsf {T}}~;~~J:=\det {\boldsymbol {F}}\qquad {\text{or}}\qquad \sigma {ij}={\frac {1}{J}}~{\frac {\partial W}{\partial F{iK}}}~F_{jK}~.}

In terms of the Lagrangian Green strain

          σ

            1
            J

          F

        ⋅

              ∂
              W

              ∂

                E

        ⋅

            F

              T

          or

          σ

            i
            j

            1
            J

          F

            i
            K

              ∂
              W

              ∂

                E

                  K
                  L

          F

            j
            L

        .

    {\displaystyle {\boldsymbol {\sigma }}={\frac {1}{J}}~{\boldsymbol {F}}\cdot {\frac {\partial W}{\partial {\boldsymbol {E}}}}\cdot {\boldsymbol {F}}^{\textsf {T}}\qquad {\text{or}}\qquad \sigma {ij}={\frac {1}{J}}~F{iK}~{\frac {\partial W}{\partial E_{KL}}}~F_{jL}~.}

In terms of the right Cauchy–Green deformation tensor

          σ

            2
            J

          F

        ⋅

              ∂
              W

              ∂

                C

        ⋅

            F

              T

          or

          σ

            i
            j

            2
            J

          F

            i
            K

              ∂
              W

              ∂

                C

                  K
                  L

          F

            j
            L

        .

    {\displaystyle {\boldsymbol {\sigma }}={\frac {2}{J}}~{\boldsymbol {F}}\cdot {\frac {\partial W}{\partial {\boldsymbol {C}}}}\cdot {\boldsymbol {F}}^{\textsf {T}}\qquad {\text{or}}\qquad \sigma {ij}={\frac {2}{J}}~F{iK}~{\frac {\partial W}{\partial C_{KL}}}~F_{jL}~.}

The above expressions are valid even for anisotropic media (in which case, the potential function is understood to depend implicitly on reference directional quantities such as initial fiber orientations). In the special case of isotropy, the Cauchy stress can be expressed in terms of the left Cauchy-Green deformation tensor as follows:

          σ

            2
            J

              ∂
              W

              ∂

                B

        ⋅

          B

          or

          σ

            i
            j

            2
            J

          B

            i
            k

              ∂
              W

              ∂

                B

                  k
                  j

        .

    {\displaystyle {\boldsymbol {\sigma }}={\frac {2}{J}}{\frac {\partial W}{\partial {\boldsymbol {B}}}}\cdot ~{\boldsymbol {B}}\qquad {\text{or}}\qquad \sigma {ij}={\frac {2}{J}}~B{ik}~{\frac {\partial W}{\partial B_{kj}}}~.}

Incompressible hyperelastic materials
For an incompressible material

        J
        :=
        det

          F

        1

    {\displaystyle J:=\det {\boldsymbol {F}}=1}

. The incompressibility constraint is therefore

        J
        −
        1

        0

    {\displaystyle J-1=0}

. To ensure incompressibility of a hyperelastic material, the strain-energy function can be written in form:

        W

        W
        (

          F

        )
        −
        p

        (
        J
        −
        1
        )

    {\displaystyle W=W({\boldsymbol {F}})-p~(J-1)}

where the hydrostatic pressure

        p

    {\displaystyle p}

 functions as a Lagrangian multiplier to enforce the incompressibility constraint. The 1st Piola–Kirchhoff stress now becomes

          P

        −
        p

        J

            F

            −

                T

        +

              ∂
              W

              ∂

                F

        −
        p

            F

            −

                T

        +

          F

        ⋅

              ∂
              W

              ∂

                E

        −
        p

            F

            −

                T

        +
        2

          F

        ⋅

              ∂
              W

              ∂

                C

        .

    {\displaystyle {\boldsymbol {P}}=-p~J{\boldsymbol {F}}^{-{\textsf {T}}}+{\frac {\partial W}{\partial {\boldsymbol {F}}}}=-p~{\boldsymbol {F}}^{-{\textsf {T}}}+{\boldsymbol {F}}\cdot {\frac {\partial W}{\partial {\boldsymbol {E}}}}=-p~{\boldsymbol {F}}^{-{\textsf {T}}}+2~{\boldsymbol {F}}\cdot {\frac {\partial W}{\partial {\boldsymbol {C}}}}~.}

This stress tensor can subsequently be converted into any of the other conventional stress tensors, such as the Cauchy stress tensor which is given by

          σ

          P

        ⋅

            F

              T

        −
        p

            1

        +

              ∂
              W

              ∂

                F

        ⋅

            F

              T

        −
        p

            1

        +

          F

        ⋅

              ∂
              W

              ∂

                E

        ⋅

            F

              T

        −
        p

            1

        +
        2

          F

        ⋅

              ∂
              W

              ∂

                C

        ⋅

            F

              T

        .

    {\displaystyle {\boldsymbol {\sigma }}={\boldsymbol {P}}\cdot {\boldsymbol {F}}^{\textsf {T}}=-p~{\boldsymbol {\mathit {1}}}+{\frac {\partial W}{\partial {\boldsymbol {F}}}}\cdot {\boldsymbol {F}}^{\textsf {T}}=-p~{\boldsymbol {\mathit {1}}}+{\boldsymbol {F}}\cdot {\frac {\partial W}{\partial {\boldsymbol {E}}}}\cdot {\boldsymbol {F}}^{\textsf {T}}=-p~{\boldsymbol {\mathit {1}}}+2~{\boldsymbol {F}}\cdot {\frac {\partial W}{\partial {\boldsymbol {C}}}}\cdot {\boldsymbol {F}}^{\textsf {T}}~.}

Expressions for the Cauchy stress

Compressible isotropic hyperelastic materials
For isotropic hyperelastic materials, the Cauchy stress can be expressed in terms of the invariants of the left Cauchy–Green deformation tensor (or right Cauchy–Green deformation tensor). If the strain energy density function is

        W
        (

          F

        )

              W
              ^

        (

          I

            1

        ,

          I

            2

        ,

          I

            3

        )

              W
              ¯

        (

                I
                ¯

            1

        ,

                I
                ¯

            2

        ,
        J
        )

              W
              ~

        (

          λ

            1

        ,

          λ

            2

        ,

          λ

            3

        )
        ,

    {\displaystyle W({\boldsymbol {F}})={\hat {W}}(I_{1},I_{2},I_{3})={\bar {W}}({\bar {I}}{1},{\bar {I}}{2},J)={\tilde {W}}(\lambda _{1},\lambda _{2},\lambda _{3}),}

 then

                  σ

                    2

                        I

                          3

                  [

                      (

                              ∂

                                    W
                                    ^

                              ∂

                                I

                                  1

                        +

                          I

                            1

                              ∂

                                    W
                                    ^

                              ∂

                                I

                                  2

                      )

                      B

                    −

                          ∂

                                W
                                ^

                          ∂

                            I

                              2

                      B

                    ⋅

                      B

                  ]

                +
                2

                      I

                        3

                      ∂

                            W
                            ^

                      ∂

                        I

                          3

                    1

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
                                    ¯

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
                                    ¯

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
                                ¯

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
                                ¯

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
                                    ¯

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
                                    ¯

                              ∂

                                      I
                                      ¯

                                  2

                      )

                  ]

                    1

                    2
                    J

                  [

                      (

                              ∂

                                    W
                                    ¯

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
                                    ¯

                              ∂

                                      I
                                      ¯

                                  2

                      )

                          B
                          ¯

                    −

                          ∂

                                W
                                ¯

                          ∂

                                  I
                                  ¯

                              2

                          B
                          ¯

                    ⋅

                          B
                          ¯

                  ]

                +

                  [

                          ∂

                                W
                                ¯

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
                                    ¯

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
                                    ¯

                              ∂

                                      I
                                      ¯

                                  2

                      )

                  ]

                    1

                      λ

                        1

                        λ

                          1

                        λ

                          2

                        λ

                          3

                      ∂

                            W
                            ~

                      ∂

                        λ

                          1

                    n

                    1

                ⊗

                    n

                    1

                +

                      λ

                        2

                        λ

                          1

                        λ

                          2

                        λ

                          3

                      ∂

                            W
                            ~

                      ∂

                        λ

                          2

                    n

                    2

                ⊗

                    n

                    2

                +

                      λ

                        3

                        λ

                          1

                        λ

                          2

                        λ

                          3

                      ∂

                            W
                            ~

                      ∂

                        λ

                          3

                    n

                    3

                ⊗

                    n

                    3

    {\displaystyle {\begin{aligned}{\boldsymbol {\sigma }}&={\frac {2}{\sqrt {I_{3}}}}\left[\left({\frac {\partial {\hat {W}}}{\partial I_{1}}}+I_{1}~{\frac {\partial {\hat {W}}}{\partial I_{2}}}\right){\boldsymbol {B}}-{\frac {\partial {\hat {W}}}{\partial I_{2}}}~{\boldsymbol {B}}\cdot {\boldsymbol {B}}\right]+2{\sqrt {I_{3}}}~{\frac {\partial {\hat {W}}}{\partial I_{3}}}~{\boldsymbol {\mathit {1}}}\[5pt]&={\frac {2}{J}}\left[{\frac {1}{J^{2/3}}}\left({\frac {\partial {\bar {W}}}{\partial {\bar {I}}{1}}}+{\bar {I}}{1}~{\frac {\partial {\bar {W}}}{\partial {\bar {I}}{2}}}\right){\boldsymbol {B}}-{\frac {1}{J^{4/3}}}~{\frac {\partial {\bar {W}}}{\partial {\bar {I}}{2}}}~{\boldsymbol {B}}\cdot {\boldsymbol {B}}\right]+\left[{\frac {\partial {\bar {W}}}{\partial J}}-{\frac {2}{3J}}\left({\bar {I}}{1}~{\frac {\partial {\bar {W}}}{\partial {\bar {I}}{1}}}+2~{\bar {I}}{2}~{\frac {\partial {\bar {W}}}{\partial {\bar {I}}{2}}}\right)\right]~{\boldsymbol {\mathit {1}}}\[5pt]&={\frac {2}{J}}\left[\left({\frac {\partial {\bar {W}}}{\partial {\bar {I}}{1}}}+{\bar {I}}{1}~{\frac {\partial {\bar {W}}}{\partial {\bar {I}}{2}}}\right){\bar {\boldsymbol {B}}}-{\frac {\partial {\bar {W}}}{\partial {\bar {I}}{2}}}~{\bar {\boldsymbol {B}}}\cdot {\bar {\boldsymbol {B}}}\right]+\left[{\frac {\partial {\bar {W}}}{\partial J}}-{\frac {2}{3J}}\left({\bar {I}}{1}~{\frac {\partial {\bar {W}}}{\partial {\bar {I}}{1}}}+2~{\bar {I}}{2}~{\frac {\partial {\bar {W}}}{\partial {\bar {I}}{2}}}\right)\right]~{\boldsymbol {\mathit {1}}}\[5pt]&={\frac {\lambda _{1}}{\lambda _{1}\lambda _{2}\lambda _{3}}}~{\frac {\partial {\tilde {W}}}{\partial \lambda _{1}}}~\mathbf {n} _{1}\otimes \mathbf {n} _{1}+{\frac {\lambda _{2}}{\lambda _{1}\lambda _{2}\lambda _{3}}}~{\frac {\partial {\tilde {W}}}{\partial \lambda _{2}}}~\mathbf {n} _{2}\otimes \mathbf {n} _{2}+{\frac {\lambda _{3}}{\lambda _{1}\lambda _{2}\lambda _{3}}}~{\frac {\partial {\tilde {W}}}{\partial \lambda _{3}}}~\mathbf {n} _{3}\otimes \mathbf {n} _{3}\end{aligned}}}

(See the page on the left Cauchy–Green deformation tensor for the definitions of these symbols).

Incompressible isotropic hyperelastic materials
For incompressible isotropic hyperelastic materials, the strain energy density function is

        W
        (

          F

        )

              W
              ^

        (

          I

            1

        ,

          I

            2

        )

    {\displaystyle W({\boldsymbol {F}})={\hat {W}}(I_{1},I_{2})}

. The Cauchy stress is then given by

                  σ

                −
                p

                    1

                +
                2

                  [

                      (

                              ∂

                                    W
                                    ^

                              ∂

                                I

                                  1

                        +

                          I

                            1

                              ∂

                                    W
                                    ^

                              ∂

                                I

                                  2

                      )

                      B

                    −

                          ∂

                                W
                                ^

                          ∂

                            I

                              2

                      B

                    ⋅

                      B

                  ]

                −
                p

                    1

                +
                2

                  [

                      (

                              ∂
                              W

                              ∂

                                      I
                                      ¯

                                  1

                        +

                          I

                            1

                              ∂
                              W

                              ∂

                                      I
                                      ¯

                                  2

                      )

                          B
                          ¯

                    −

                          ∂
                          W

                          ∂

                                  I
                                  ¯

                              2

                          B
                          ¯

                    ⋅

                          B
                          ¯

                  ]

                −
                p

                    1

                +

                  λ

                    1

                      ∂
                      W

                      ∂

                        λ

                          1

                    n

                    1

                ⊗

                    n

                    1

                +

                  λ

                    2

                      ∂
                      W

                      ∂

                        λ

                          2

                    n

                    2

                ⊗

                    n

                    2

                +

                  λ

                    3

                      ∂
                      W

                      ∂

                        λ

                          3

                    n

                    3

                ⊗

                    n

                    3

    {\displaystyle {\begin{aligned}{\boldsymbol {\sigma }}&=-p~{\boldsymbol {\mathit {1}}}+2\left[\left({\frac {\partial {\hat {W}}}{\partial I_{1}}}+I_{1}~{\frac {\partial {\hat {W}}}{\partial I_{2}}}\right){\boldsymbol {B}}-{\frac {\partial {\hat {W}}}{\partial I_{2}}}~{\boldsymbol {B}}\cdot {\boldsymbol {B}}\right]\&=-p~{\boldsymbol {\mathit {1}}}+2\left[\left({\frac {\partial W}{\partial {\bar {I}}{1}}}+I{1}~{\frac {\partial W}{\partial {\bar {I}}{2}}}\right)~{\bar {\boldsymbol {B}}}-{\frac {\partial W}{\partial {\bar {I}}{2}}}~{\bar {\boldsymbol {B}}}\cdot {\bar {\boldsymbol {B}}}\right]\&=-p~{\boldsymbol {\mathit {1}}}+\lambda _{1}~{\frac {\partial W}{\partial \lambda _{1}}}~\mathbf {n} _{1}\otimes \mathbf {n} _{1}+\lambda _{2}~{\frac {\partial W}{\partial \lambda _{2}}}~\mathbf {n} _{2}\otimes \mathbf {n} _{2}+\lambda _{3}~{\frac {\partial W}{\partial \lambda _{3}}}~\mathbf {n} _{3}\otimes \mathbf {n} _{3}\end{aligned}}}

where

        p

    {\displaystyle p}

 is an undetermined pressure. In terms of stress differences

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

    {\displaystyle \sigma _{11}-\sigma _{33}=\lambda _{1}~{\frac {\partial W}{\partial \lambda _{1}}}-\lambda _{3}~{\frac {\partial W}{\partial \lambda _{3}}}~;~~\sigma _{22}-\sigma _{33}=\lambda _{2}~{\frac {\partial W}{\partial \lambda _{2}}}-\lambda _{3}~{\frac {\partial W}{\partial \lambda _{3}}}}

If in addition

          I

            1

          I

            2

    {\displaystyle I_{1}=I_{2}}

, then

          σ

        2

              ∂
              W

              ∂

                I

                  1

          B

        −
        p

            1

        .

    {\displaystyle {\boldsymbol {\sigma }}=2{\frac {\partial W}{\partial I_{1}}}~{\boldsymbol {B}}-p~{\boldsymbol {\mathit {1}}}~.}

If

          λ

            1

          λ

            2

    {\displaystyle \lambda _{1}=\lambda _{2}}

, then

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

    {\displaystyle \sigma _{11}-\sigma _{33}=\sigma _{22}-\sigma _{33}=\lambda _{1}~{\frac {\partial W}{\partial \lambda _{1}}}-\lambda _{3}~{\frac {\partial W}{\partial \lambda _{3}}}}

Consistency with linear elasticity
Consistency with linear elasticity is often used to determine some of the parameters of hyperelastic material models. These consistency conditions can be found by comparing Hooke's law with linearized hyperelasticity at small strains.

Consistency conditions for isotropic hyperelastic models
For isotropic hyperelastic materials to be consistent with isotropic linear elasticity, the stress–strain relation should have the following form in the infinitesimal strain limit:

          σ

        λ

          t
          r

        (

          ε

        )

            1

        +
        2
        μ

          ε

    {\displaystyle {\boldsymbol {\sigma }}=\lambda ~\mathrm {tr} ({\boldsymbol {\varepsilon }})~{\boldsymbol {\mathit {1}}}+2\mu {\boldsymbol {\varepsilon }}}

where

        λ
        ,
        μ

    {\displaystyle \lambda ,\mu }

 are the Lamé constants. The strain energy density function that corresponds to the above relation is

        W

              1
              2

        λ

        [

          t
          r

        (

          ε

        )

          ]

            2

        +
        μ

          t
          r

              (

                  ε

                  2

              )

    {\displaystyle W={\tfrac {1}{2}}\lambda ~[\mathrm {tr} ({\boldsymbol {\varepsilon }})]^{2}+\mu ~\mathrm {tr} {\mathord {\left({\boldsymbol {\varepsilon }}^{2}\right)}}}

For an incompressible material

          t
          r

        (

          ε

        )

        0

    {\displaystyle \mathrm {tr} ({\boldsymbol {\varepsilon }})=0}

 and we have

        W

        μ

          t
          r

              (

                  ε

                  2

              )

    {\displaystyle W=\mu ~\mathrm {tr} {\mathord {\left({\boldsymbol {\varepsilon }}^{2}\right)}}}

For any strain energy density function

        W
        (

          λ

            1

        ,

          λ

            2

        ,

          λ

            3

        )

    {\displaystyle W(\lambda _{1},\lambda _{2},\lambda _{3})}

 to reduce to the above forms for small strains the following conditions have to be met

                W
                (
                1
                ,
                1
                ,
                1
                )

                0

                ;

                      ∂
                      W

                      ∂

                        λ

                          i

                (
                1
                ,
                1
                ,
                1
                )

                0

                        ∂

                          2

                      W

                      ∂

                        λ

                          i

                      ∂

                        λ

                          j

                (
                1
                ,
                1
                ,
                1
                )

                λ
                +
                2
                μ

                  δ

                    i
                    j

    {\displaystyle {\begin{aligned}&W(1,1,1)=0~;~~{\frac {\partial W}{\partial \lambda _{i}}}(1,1,1)=0\&{\frac {\partial ^{2}W}{\partial \lambda _{i}\partial \lambda _{j}}}(1,1,1)=\lambda +2\mu \delta _{ij}\end{aligned}}}

If the material is incompressible, then the above conditions may be expressed in the following form.

                W
                (
                1
                ,
                1
                ,
                1
                )

                0

                      ∂
                      W

                      ∂

                        λ

                          i

                (
                1
                ,
                1
                ,
                1
                )

                      ∂
                      W

                      ∂

                        λ

                          j

                (
                1
                ,
                1
                ,
                1
                )

                ;

                        ∂

                          2

                      W

                      ∂

                        λ

                          i

                          2

                (
                1
                ,
                1
                ,
                1
                )

                        ∂

                          2

                      W

                      ∂

                        λ

                          j

                          2

                (
                1
                ,
                1
                ,
                1
                )

                        ∂

                          2

                      W

                      ∂

                        λ

                          i

                      ∂

                        λ

                          j

                (
                1
                ,
                1
                ,
                1
                )

                  i
                  n
                  d
                  e
                  p
                  e
                  n
                  d
                  e
                  n
                  t
                  o
                  f

                i
                ,
                j
                ≠
                i

                        ∂

                          2

                      W

                      ∂

                        λ

                          i

                          2

                (
                1
                ,
                1
                ,
                1
                )
                −

                        ∂

                          2

                      W

                      ∂

                        λ

                          i

                      ∂

                        λ

                          j

                (
                1
                ,
                1
                ,
                1
                )
                +

                      ∂
                      W

                      ∂

                        λ

                          i

                (
                1
                ,
                1
                ,
                1
                )

                2
                μ

                (
                i
                ≠
                j
                )

    {\displaystyle {\begin{aligned}&W(1,1,1)=0\&{\frac {\partial W}{\partial \lambda _{i}}}(1,1,1)={\frac {\partial W}{\partial \lambda _{j}}}(1,1,1)~;~~{\frac {\partial ^{2}W}{\partial \lambda _{i}^{2}}}(1,1,1)={\frac {\partial ^{2}W}{\partial \lambda _{j}^{2}}}(1,1,1)\&{\frac {\partial ^{2}W}{\partial \lambda _{i}\partial \lambda _{j}}}(1,1,1)=\mathrm {independentof} ~i,j\neq i\&{\frac {\partial ^{2}W}{\partial \lambda _{i}^{2}}}(1,1,1)-{\frac {\partial ^{2}W}{\partial \lambda _{i}\partial \lambda _{j}}}(1,1,1)+{\frac {\partial W}{\partial \lambda _{i}}}(1,1,1)=2\mu ~~(i\neq j)\end{aligned}}}

These conditions can be used to find relations between the parameters of a given hyperelastic model and shear and bulk moduli.

Consistency conditions for incompressible I1 based rubber materials
Many elastomers are modeled adequately by a strain energy density function that depends only on

          I

            1

    {\displaystyle I_{1}}

. For such materials we have

        W

        W
        (

          I

            1

        )

    {\displaystyle W=W(I_{1})}

.
The consistency conditions for incompressible materials for

          I

            1

        3
        ,

          λ

            i

          λ

            j

        1

    {\displaystyle I_{1}=3,\lambda _{i}=\lambda _{j}=1}

 may then be expressed as

              W
              (

                I

                  1

              )

              I

                1

            3

        0

          and

                  ∂
                  W

                  ∂

                    I

                      1

              I

                1

            3

            μ
            2

        .

    {\displaystyle \left.W(I_{1})\right|{I{1}=3}=0\quad {\text{and}}\quad \left.{\frac {\partial W}{\partial I_{1}}}\right|{I{1}=3}={\frac {\mu }{2}}\,.}

The second consistency condition above can be derived by noting that

              ∂
              W

              ∂

                λ

                  i

              ∂
              W

              ∂

                I

                  1

              ∂

                I

                  1

              ∂

                λ

                  i

        2

          λ

            i

              ∂
              W

              ∂

                I

                  1

          and

                ∂

                  2

              W

              ∂

                λ

                  i

              ∂

                λ

                  j

        2

          δ

            i
            j

              ∂
              W

              ∂

                I

                  1

        +
        4

          λ

            i

          λ

            j

                ∂

                  2

              W

              ∂

                I

                  1

                  2

        .

    {\displaystyle {\frac {\partial W}{\partial \lambda {i}}}={\frac {\partial W}{\partial I{1}}}{\frac {\partial I_{1}}{\partial \lambda _{i}}}=2\lambda {i}{\frac {\partial W}{\partial I{1}}}\quad {\text{and}}\quad {\frac {\partial ^{2}W}{\partial \lambda _{i}\partial \lambda _{j}}}=2\delta {ij}{\frac {\partial W}{\partial I{1}}}+4\lambda _{i}\lambda {j}{\frac {\partial ^{2}W}{\partial I{1}^{2}}}\,.}

These relations can then be substituted into the consistency condition for isotropic incompressible hyperelastic materials.
