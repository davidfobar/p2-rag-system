# Simple shear

Simple shear

Simple shear is a deformation in which parallel planes in a material remain parallel and maintain a constant distance, while translating relative to each other.

In fluid mechanics
In fluid mechanics, simple shear is a special case of deformation where only one component of velocity vectors has a non-zero value:

          V

            x

        f
        (
        x
        ,
        y
        )

    {\displaystyle V_{x}=f(x,y)}

          V

            y

          V

            z

        0

    {\displaystyle V_{y}=V_{z}=0}

And the gradient of velocity is constant and perpendicular to the velocity itself:

              ∂

                V

                  x

              ∂
              y

              γ
              ˙

    {\displaystyle {\frac {\partial V_{x}}{\partial y}}={\dot {\gamma }}}

,
where

              γ
              ˙

    {\displaystyle {\dot {\gamma }}}

 is the shear rate and:

              ∂

                V

                  x

              ∂
              x

              ∂

                V

                  x

              ∂
              z

        0

    {\displaystyle {\frac {\partial V_{x}}{\partial x}}={\frac {\partial V_{x}}{\partial z}}=0}

The displacement gradient tensor Γ for this deformation has only one nonzero term:

        Γ

            [

                  0

                        γ
                        ˙

                  0

                  0

                  0

                  0

                  0

                  0

                  0

            ]

    {\displaystyle \Gamma ={\begin{bmatrix}0&{\dot {\gamma }}&0\0&0&0\0&0&0\end{bmatrix}}}

Simple shear with the rate

              γ
              ˙

    {\displaystyle {\dot {\gamma }}}

 is the combination of pure shear strain with the rate of 1/2

              γ
              ˙

    {\displaystyle {\dot {\gamma }}}

 and rotation with the rate of 1/2

              γ
              ˙

    {\displaystyle {\dot {\gamma }}}

:

        Γ

                      [

                            0

                                  γ
                                  ˙

                            0

                            0

                            0

                            0

                            0

                            0

                            0

                      ]

                    ⏟

                    simple shear

                      [

                            0

                                    1
                                    2

                                    γ
                                    ˙

                            0

                                    1
                                    2

                                    γ
                                    ˙

                            0

                            0

                            0

                            0

                            0

                      ]

                    ⏟

                    pure shear

        +

                      [

                            0

                                    1
                                    2

                                    γ
                                    ˙

                            0

                              −

                                      1
                                      2

                                      γ
                                      ˙

                            0

                            0

                            0

                            0

                            0

                      ]

                    ⏟

                    solid rotation

    {\displaystyle \Gamma ={\begin{matrix}\underbrace {\begin{bmatrix}0&{\dot {\gamma }}&0\0&0&0\0&0&0\end{bmatrix}} \{\mbox{simple shear}}\end{matrix}}={\begin{matrix}\underbrace {\begin{bmatrix}0&{{\tfrac {1}{2}}{\dot {\gamma }}}&0\{{\tfrac {1}{2}}{\dot {\gamma }}}&0&0\0&0&0\end{bmatrix}} \{\mbox{pure shear}}\end{matrix}}+{\begin{matrix}\underbrace {\begin{bmatrix}0&{{\tfrac {1}{2}}{\dot {\gamma }}}&0\{-{{\tfrac {1}{2}}{\dot {\gamma }}}}&0&0\0&0&0\end{bmatrix}} \{\mbox{solid rotation}}\end{matrix}}}

The mathematical model representing simple shear is a shear mapping restricted to the physical limits. It is an elementary linear transformation represented by a matrix. The model may represent laminar flow velocity at varying depths of a long channel with constant cross-section. Limited shear deformation is also used in vibration control, for instance base isolation of buildings for limiting earthquake damage.

In solid mechanics

In solid mechanics, a simple shear deformation is defined as an isochoric plane deformation in which there are a set of line elements with a given reference orientation that do not change length and orientation during the deformation. This deformation is differentiated from a pure shear by virtue of the presence of a rigid rotation of the material. When rubber deforms under simple shear, its stress-strain behavior is approximately linear. A rod under torsion is a practical example for a body under simple shear.
If e1 is the fixed reference orientation in which line elements do not deform during the deformation and e1 − e2 is the plane of deformation, then the deformation gradient in simple shear can be expressed as

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

        .

    {\displaystyle {\boldsymbol {F}}={\begin{bmatrix}1&\gamma &0\0&1&0\0&0&1\end{bmatrix}}.}

We can also write the deformation gradient as

          F

            1

        +
        γ

            e

            1

        ⊗

            e

            2

        .

    {\displaystyle {\boldsymbol {F}}={\boldsymbol {\mathit {1}}}+\gamma \mathbf {e} _{1}\otimes \mathbf {e} _{2}.}

Simple shear stress–strain relation
In linear elasticity, shear stress, denoted

        τ

    {\displaystyle \tau }

, is related to shear strain, denoted

        γ

    {\displaystyle \gamma }

, by the following equation:

        τ

        γ
        G

    {\displaystyle \tau =\gamma G\,}

where

        G

    {\displaystyle G}

 is the shear modulus of the material, given by

        G

            E

              2
              (
              1
              +
              ν
              )

    {\displaystyle G={\frac {E}{2(1+\nu )}}}

Here

        E

    {\displaystyle E}

 is Young's modulus and

        ν

    {\displaystyle \nu }

 is Poisson's ratio. Combining gives

        τ

              γ
              E

              2
              (
              1
              +
              ν
              )

    {\displaystyle \tau ={\frac {\gamma E}{2(1+\nu )}}}
