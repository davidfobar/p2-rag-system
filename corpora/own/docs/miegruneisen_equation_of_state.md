# Mie–Grüneisen equation of state

Mie–Grüneisen equation of state

The Mie–Grüneisen equation of state is an equation of state that relates the pressure and volume of a solid at a given temperature. It is used to determine the pressure in a shock-compressed solid. The Mie–Grüneisen relation is a special form of the Grüneisen model which describes the effect that changing the volume of a crystal lattice has on its vibrational properties. Several variations of the Mie–Grüneisen equation of state are in use.
The Grüneisen model can be expressed in the form

        Γ

        V

            (

                  d
                  p

                  d
                  e

            )

            V

    {\displaystyle \Gamma =V\left({\frac {dp}{de}}\right)_{V}}

where V is the volume, p is the pressure, e is the internal energy, and Γ is the Grüneisen parameter which represents the thermal pressure from a set of vibrating atoms. If we assume that Γ is independent of p and e, we can integrate Grüneisen's model to get

        p
        −

          p

            0

            Γ
            V

        (
        e
        −

          e

            0

        )

    {\displaystyle p-p_{0}={\frac {\Gamma }{V}}(e-e_{0})}

where

          p

            0

    {\displaystyle p_{0}}

 and

          e

            0

    {\displaystyle e_{0}}

 are the pressure and internal energy at a reference state usually assumed to be the state at which the temperature is 0K. In that case p0 and e0 are independent of temperature and the values of these quantities can be estimated from the Hugoniot equations. The Mie–Grüneisen equation of state is a special form of the above equation.

History
Gustav Mie, in 1903, developed an intermolecular potential for deriving high-temperature equations of state of solids. In 1912, Eduard Grüneisen extended Mie's model to temperatures below the Debye temperature at which quantum effects become important. Grüneisen's form of the equations is more convenient and has become the usual starting point for deriving Mie–Grüneisen equations of state.

Expressions for the Mie–Grüneisen equation of state
A temperature-corrected version that is used in computational mechanics has the form

        p

                ρ

                  0

                C

                  0

                  2

              χ

                (

                  1
                  −
                  s
                  χ

                )

                2

          [

            1
            −

                  Γ

                    0

                2

            χ

          ]

        +

          Γ

            0

        E
        ;

        χ
        :=
        1
        −

                    ρ

                      0

                  ρ

    {\displaystyle p={\frac {\rho {0}C{0}^{2}\chi }{\left(1-s\chi \right)^{2}}}\left[1-{\frac {\Gamma _{0}}{2}}\,\chi \right]+\Gamma _{0}E;\quad \chi :=1-{\cfrac {\rho _{0}}{\rho }}}

where

          C

            0

    {\displaystyle C_{0}}

 is the bulk speed of sound,

          ρ

            0

    {\displaystyle \rho _{0}}

 is the initial density,

        ρ

    {\displaystyle \rho }

 is the current density,

          Γ

            0

    {\displaystyle \Gamma _{0}}

 is Grüneisen's gamma at the reference state,

        s

        d

          U

            s

          /

        d

          U

            p

    {\displaystyle s=dU_{s}/dU_{p}}

 is a linear Hugoniot slope coefficient,

          U

            s

    {\displaystyle U_{s}}

 is the shock wave velocity,

          U

            p

    {\displaystyle U_{p}}

 is the particle velocity, and

        E

    {\displaystyle E}

 is the internal energy per unit reference volume. An alternative form is

        p

                ρ

                  0

                C

                  0

                  2

              (
              η
              −
              1
              )

                [

                  η
                  −
                  s
                  (
                  η
                  −
                  1
                  )

                ]

                2

          [

            η
            −

                  Γ

                    0

                2

            (
            η
            −
            1
            )

          ]

        +

          Γ

            0

        E
        ;

        η
        :=

                  ρ

                    ρ

                      0

        .

    {\displaystyle p={\frac {\rho {0}C{0}^{2}(\eta -1)}{\left[\eta -s(\eta -1)\right]^{2}}}\left[\eta -{\frac {\Gamma _{0}}{2}}(\eta -1)\right]+\Gamma _{0}E;\quad \eta :={\cfrac {\rho }{\rho _{0}}}\,.}

A rough estimate of the internal energy can be computed using

        E

            1

              V

                0

        ∫

          C

            v

        d
        T
        ≈

                C

                  v

              (
              T
              −

                T

                  0

              )

              V

                0

          ρ

            0

          c

            v

        (
        T
        −

          T

            0

        )

    {\displaystyle E={\frac {1}{V_{0}}}\int C_{v}dT\approx {\frac {C_{v}(T-T_{0})}{V_{0}}}=\rho {0}c{v}(T-T_{0})}

where

          V

            0

    {\displaystyle V_{0}}

 is the reference volume at temperature

        T

          T

            0

    {\displaystyle T=T_{0}}

,

          C

            v

    {\displaystyle C_{v}}

 is the heat capacity and

          c

            v

    {\displaystyle c_{v}}

 is the specific heat capacity at constant volume. In many simulations, it is assumed that

          C

            p

    {\displaystyle C_{p}}

 and

          C

            v

    {\displaystyle C_{v}}

 are equal.

Parameters for various materials

Derivation of the equation of state
From Grüneisen's model we have

where

          p

            0

    {\displaystyle p_{0}}

 and

          e

            0

    {\displaystyle e_{0}}

 are the pressure and internal energy at a reference state. The Hugoniot equations for the conservation of mass, momentum, and energy are

                  ρ

                    0

                  U

                    s

                ρ

                  (

                      U

                        s

                    −

                      U

                        p

                  )

                ,

                  p

                    H

                −

                  p

                    H
                    0

                  ρ

                    0

                  U

                    s

                  U

                    p

                ,

                  p

                    H

                  U

                    p

                  ρ

                    0

                  U

                    s

                  (

                          1
                          2

                      U

                        p

                        2

                    +

                      E

                        H

                    −

                      E

                        H
                        0

                  )

    {\displaystyle {\begin{aligned}\rho {0}U{s}&=\rho \left(U_{s}-U_{p}\right)\,,\[1ex]p_{H}-p_{H0}&=\rho {0}U{s}U_{p}\,,\[1ex]p_{H}U_{p}&=\rho {0}U{s}\left({\tfrac {1}{2}}U_{p}^{2}+E_{H}-E_{H0}\right)\end{aligned}}}

where ρ0 is the reference density, ρ is the density due to shock compression, pH is the pressure on the Hugoniot, EH is the internal energy per unit mass on the Hugoniot, Us is the shock velocity, and Up is the particle velocity. From the conservation of mass, we have

              U

                p

              U

                s

        1
        −

              ρ

                0

            ρ

        1
        −

            V

              V

                0

        =:
        χ

        .

    {\displaystyle {\frac {U_{p}}{U_{s}}}=1-{\frac {\rho {0}}{\rho }}=1-{\frac {V}{V{0}}}=:\chi \,.}

Where we defined

        V

        1

          /

        ρ

    {\displaystyle V=1/\rho }

, the specific volume (volume per unit mass).
For many materials Us and Up are linearly related, i.e., Us = C0 + s Up where C0 and s depend on the material. In that case, we have

          U

            s

          C

            0

        +
        s
        χ

          U

            s

          or

          U

            s

              C

                0

              1
              −
              s
              χ

        .

    {\displaystyle U_{s}=C_{0}+s\chi U_{s}\quad {\text{or}}\quad U_{s}={\frac {C_{0}}{1-s\chi }}\,.}

The momentum equation can then be written (for the principal Hugoniot where pH0 is zero) as

          p

            H

          ρ

            0

        χ

          U

            s

            2

                ρ

                  0

                C

                  0

                  2

              χ

                (

                  1
                  −
                  s
                  χ

                )

                2

        .

    {\displaystyle p_{H}=\rho {0}\chi U{s}^{2}={\frac {\rho {0}C{0}^{2}\chi }{\left(1-s\chi \right)^{2}}}\,.}

Similarly, from the energy equation we have

          p

            H

        χ

          U

            s

              1
              2

        ρ

          χ

            2

          U

            s

            3

        +

          ρ

            0

          U

            s

          E

            H

              1
              2

          p

            H

        χ

          U

            s

        +

          ρ

            0

          U

            s

          E

            H

        .

    {\displaystyle p_{H}\chi U_{s}={\tfrac {1}{2}}\rho \chi ^{2}U_{s}^{3}+\rho {0}U{s}E_{H}={\tfrac {1}{2}}p_{H}\chi U_{s}+\rho {0}U{s}E_{H}\,.}

Solving for eH, we have

          E

            H

              1
              2

                p

                  H

              χ

              ρ

                0

              1
              2

          p

            H

        (

          V

            0

        −
        V
        )

    {\displaystyle E_{H}={\tfrac {1}{2}}{\frac {p_{H}\chi }{\rho {0}}}={\tfrac {1}{2}}p{H}(V_{0}-V)}

With these expressions for pH and EH, the Grüneisen model on the Hugoniot becomes

          p

            H

        −

          p

            0

            Γ
            V

          (

                    p

                      H

                  χ

                    V

                      0

                2

            −

              e

                0

          )

    {\displaystyle p_{H}-p_{0}={\frac {\Gamma }{V}}\left({\frac {p_{H}\chi V_{0}}{2}}-e_{0}\right)}

or

                ρ

                  0

                C

                  0

                  2

              χ

                (

                  1
                  −
                  s
                  χ

                )

                2

          (

            1
            −

                χ
                2

                Γ
                V

              V

                0

          )

        −

          p

            0

        −

            Γ
            V

          e

            0

        .

    {\displaystyle {\frac {\rho {0}C{0}^{2}\chi }{\left(1-s\chi \right)^{2}}}\left(1-{\frac {\chi }{2}}\,{\frac {\Gamma }{V}}\,V_{0}\right)-p_{0}=-{\frac {\Gamma }{V}}e_{0}\,.}

If we assume that Γ/V = Γ0/V0 and note that

          p

            0

        −
        d

          e

            0

          /

        d
        V

    {\displaystyle p_{0}=-de_{0}/dV}

, we get

The above ordinary differential equation can be solved for e0 with the initial condition e0 = 0 when V = V0 (χ = 0). The exact solution is

                  e

                    0

                      ρ

                        C

                          0

                          2

                        V

                          0

                      2

                        s

                          4

                    [

                exp
                ⁡
                (

                  Γ

                    0

                χ
                )

                  (

                            Γ

                              0

                          s

                    −
                    3

                  )

                  s

                    2

                −

                      s

                        2

                      1
                      −
                      s
                      χ

                  [

                            Γ

                              0

                          s

                    −
                    (
                    3
                    −
                    s
                    χ
                    )

                  ]

                +

                exp
                ⁡

                  [

                    −

                            Γ

                              0

                          s

                    (
                    1
                    −
                    s
                    χ
                    )

                  ]

                  (

                      Γ

                        0

                        2

                    −
                    4

                      Γ

                        0

                    s
                    +
                    2

                      s

                        2

                  )

                  (

                      Ei

                      [

                                Γ

                                  0

                              s

                        (
                        1
                        −
                        s
                        χ
                        )

                      ]

                    −

                      Ei

                      [

                              Γ

                                0

                            s

                      ]

                  )

                    ]

    {\displaystyle {\begin{aligned}e_{0}={\frac {\rho C_{0}^{2}V_{0}}{2s^{4}}}{\Biggl [}&\exp(\Gamma _{0}\chi )\left({\tfrac {\Gamma _{0}}{s}}-3\right)s^{2}-{\frac {s^{2}}{1-s\chi }}\left[{\tfrac {\Gamma _{0}}{s}}-(3-s\chi )\right]+\&\exp \left[-{\tfrac {\Gamma _{0}}{s}}(1-s\chi )\right]\left(\Gamma _{0}^{2}-4\Gamma _{0}s+2s^{2}\right)\left({\text{Ei}}\left[{\tfrac {\Gamma _{0}}{s}}(1-s\chi )\right]-{\text{Ei}}\left[{\tfrac {\Gamma _{0}}{s}}\right]\right){\Biggr ]}\end{aligned}}}

where Ei[z] is the exponential integral. The expression for p0 is

                  p

                    0

                −

                      d

                        e

                          0

                      d
                      V

                      ρ

                        C

                          0

                          2

                      2

                        s

                          4

                      (
                      1
                      −
                      χ
                      )

                    [

                    s

                      (
                      1
                      −
                      s
                      χ

                        )

                          2

                    (

                −

                  Γ

                    0

                    2

                (
                1
                −
                χ
                )
                (
                1
                −
                s
                χ
                )
                +

                  Γ

                    0

                [
                s
                {
                4
                (
                χ
                −
                1
                )
                χ
                s
                −
                2
                χ
                +
                3
                }
                −
                1
                ]

                −
                exp
                ⁡
                (

                  Γ

                    0

                χ
                )
                [

                  Γ

                    0

                (
                χ
                −
                1
                )
                −
                1
                ]
                (
                1
                −
                s
                χ

                  )

                    2

                (

                  Γ

                    0

                −
                3
                s
                )
                +
                s
                [
                3
                −
                χ
                s
                {
                (
                χ
                −
                2
                )
                s
                +
                4
                }
                ]

                    )

                −
                exp
                ⁡

                  [

                    −

                            Γ

                              0

                          s

                    (
                    1
                    −
                    s
                    χ
                    )

                  ]

                  [

                      Γ

                        0

                    (
                    χ
                    −
                    1
                    )
                    −
                    1

                  ]

                  (

                      Γ

                        0

                        2

                    −
                    4

                      Γ

                        0

                    s
                    +
                    2

                      s

                        2

                  )

                  (

                      Ei

                      [

                                Γ

                                  0

                              s

                        (
                        1
                        −
                        s
                        χ
                        )

                      ]

                    −

                      Ei

                      [

                              Γ

                                0

                            s

                      ]

                  )

                    ]

                .

    {\displaystyle {\begin{aligned}p_{0}&=-{\frac {de_{0}}{dV}}\&={\frac {\rho C_{0}^{2}}{2s^{4}(1-\chi )}}{\Biggl [}{\frac {s}{(1-s\chi )^{2}}}{\Bigl (}-\Gamma _{0}^{2}(1-\chi )(1-s\chi )+\Gamma _{0}[s{4(\chi -1)\chi s-2\chi +3}-1]\&\quad \qquad \qquad \qquad \qquad \qquad \quad -\exp(\Gamma _{0}\chi )[\Gamma _{0}(\chi -1)-1](1-s\chi )^{2}(\Gamma _{0}-3s)+s[3-\chi s{(\chi -2)s+4}]{\Bigr )}\&\quad \qquad \qquad \qquad -\exp \left[-{\tfrac {\Gamma _{0}}{s}}(1-s\chi )\right]\left[\Gamma _{0}(\chi -1)-1\right]\left(\Gamma _{0}^{2}-4\Gamma _{0}s+2s^{2}\right)\left({\text{Ei}}\left[{\tfrac {\Gamma _{0}}{s}}(1-s\chi )\right]-{\text{Ei}}\left[{\tfrac {\Gamma _{0}}{s}}\right]\right){\Biggr ]}\,.\end{aligned}}}

For commonly encountered compression problems, an approximation to the exact solution is a power series solution of the form

          e

            0

        (
        V
        )

        A
        +
        B
        χ
        (
        V
        )
        +
        C

          χ

            2

        (
        V
        )
        +
        D

          χ

            3

        (
        V
        )
        +
        ⋯

    {\displaystyle e_{0}(V)=A+B\chi (V)+C\chi ^{2}(V)+D\chi ^{3}(V)+\cdots }

and

          p

            0

        (
        V
        )

        −

              d

                e

                  0

              d
              V

        −

              d

                e

                  0

              d
              χ

              d
              χ

              d
              V

            1

              V

                0

        (
        B
        +
        2
        C
        χ
        +
        3
        D

          χ

            2

        +
        ⋯
        )

        .

    {\displaystyle p_{0}(V)=-{\frac {de_{0}}{dV}}=-{\frac {de_{0}}{d\chi }}\,{\frac {d\chi }{dV}}={\frac {1}{V_{0}}}\,(B+2C\chi +3D\chi ^{2}+\cdots )\,.}

Substitution into the Grüneisen model gives us the Mie–Grüneisen equation of state

        p

            1

              V

                0

        (
        B
        +
        2
        C
        χ
        +
        3
        D

          χ

            2

        +
        ⋯
        )
        +

              Γ

                0

              V

                0

          [

            e
            −
            (
            A
            +
            B
            χ
            +
            C

              χ

                2

            +
            D

              χ

                3

            +
            ⋯
            )

          ]

        .

    {\displaystyle p={\frac {1}{V_{0}}}\,(B+2C\chi +3D\chi ^{2}+\cdots )+{\frac {\Gamma {0}}{V{0}}}\left[e-(A+B\chi +C\chi ^{2}+D\chi ^{3}+\cdots )\right]\,.}

If we assume that the internal energy e0 = 0 when V = V0 (χ = 0) we have A = 0. Similarly, if we assume p0 = 0 when V = V0 we have B = 0. The Mie–Grüneisen equation of state can then be written as

        p

            1

              V

                0

          [

            2
            C
            χ

              (

                1
                −

                        Γ

                          0

                      2

                χ

              )

            +
            3
            D

              χ

                2

              (

                1
                −

                        Γ

                          0

                      3

                χ

              )

            +
            ⋯

          ]

        +

          Γ

            0

        E

    {\displaystyle p={\frac {1}{V_{0}}}\left[2C\chi \left(1-{\tfrac {\Gamma _{0}}{2}}\chi \right)+3D\chi ^{2}\left(1-{\tfrac {\Gamma _{0}}{3}}\chi \right)+\cdots \right]+\Gamma _{0}E}

where E is the internal energy per unit reference volume. Several forms of this equation of state are possible.

If we take the first-order term and substitute it into equation (2), we can solve for C to get

        C

                ρ

                  0

                C

                  0

                  2

                V

                  0

              2

                  (

                    1
                    −
                    s
                    χ

                  )

                  2

        .

    {\displaystyle C={\frac {\rho {0}C{0}^{2}V_{0}}{2\left(1-s\chi \right)^{2}}}\,.}

Then we get the following expression for p:

        p

                ρ

                  0

                C

                  0

                  2

              χ

                (

                  1
                  −
                  s
                  χ

                )

                2

          (

            1
            −

                  Γ

                    0

                2

            χ

          )

        +

          Γ

            0

        E

        .

    {\displaystyle p={\frac {\rho {0}C{0}^{2}\chi }{\left(1-s\chi \right)^{2}}}\left(1-{\frac {\Gamma _{0}}{2}}\chi \right)+\Gamma _{0}E\,.}

This is the commonly used first-order Mie–Grüneisen equation of state.
