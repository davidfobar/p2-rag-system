# Minimal coupling

Minimal coupling

In analytical mechanics and quantum field theory, minimal coupling refers to a coupling between fields which involves only the charge distribution and not higher multipole moments of the charge distribution. This minimal coupling is in contrast to, for example, Pauli coupling, which includes the magnetic moment of an electron directly in the Lagrangian.

Electrodynamics
In electrodynamics, minimal coupling is adequate to account for all electromagnetic interactions. Higher moments of particles are consequences of minimal coupling and non-zero spin.

Non-relativistic charged particle in an electromagnetic field
In Cartesian coordinates, the Lagrangian of a non-relativistic classical particle in an electromagnetic field is (in SI Units):

            L

          ∑

            i

              1
              2

        m

                x
                ˙

            i

            2

        +

          ∑

            i

        q

                x
                ˙

            i

          A

            i

        −
        q
        φ

    {\displaystyle {\mathcal {L}}=\sum {i}{\tfrac {1}{2}}m{\dot {x}}{i}^{2}+\sum {i}q{\dot {x}}{i}A_{i}-q\varphi }

where q is the electric charge of the particle, φ is the electric scalar potential, and the Ai, i = 1, 2, 3, are the components of the magnetic vector potential that may all explicitly depend on

          x

            i

    {\displaystyle x_{i}}

 and

        t

    {\displaystyle t}

.
This Lagrangian, combined with Euler–Lagrange equation, produces the Lorentz force law

        m

                x

              ¨

        q

          E

        +
        q

                x

              ˙

        ×

          B

        ,

    {\displaystyle m{\ddot {\mathbf {x} }}=q\mathbf {E} +q{\dot {\mathbf {x} }}\times \mathbf {B} \,,}

and is called minimal coupling.
Note that the values of scalar potential and vector potential would change during a gauge transformation, and the Lagrangian itself will pick up extra terms as well, but the extra terms in the Lagrangian add up to a total time derivative of a scalar function, and therefore still produce the same Euler–Lagrange equation.
The canonical momenta are given by

          p

            i

              ∂

                  L

              ∂

                      x
                      ˙

                  i

        m

                x
                ˙

            i

        +
        q

          A

            i

    {\displaystyle p_{i}={\frac {\partial {\mathcal {L}}}{\partial {\dot {x}}{i}}}=m{\dot {x}}{i}+qA_{i}}

Note that canonical momenta are not gauge invariant, and are not physically measurable. However, the kinetic momenta

          P

            i

        ≡
        m

                x
                ˙

            i

          p

            i

        −
        q

          A

            i

    {\displaystyle P_{i}\equiv m{\dot {x}}{i}=p{i}-qA_{i}}

are gauge invariant and physically measurable.
The Hamiltonian, as the Legendre transformation of the Lagrangian, is therefore

            H

          {

              ∑

                i

                    x
                    ˙

                i

              p

                i

          }

        −

            L

          ∑

            i

                (

                    p

                      i

                  −
                  q

                    A

                      i

                )

                2

              2
              m

        +
        q
        φ

    {\displaystyle {\mathcal {H}}=\left{\sum {i}{\dot {x}}{i}p_{i}\right}-{\mathcal {L}}=\sum {i}{\frac {\left(p{i}-qA_{i}\right)^{2}}{2m}}+q\varphi }

This equation is used frequently in quantum mechanics.
Under a gauge transformation,

          A

        →

          A

        +
        ∇
        f

        ,

        φ
        →
        φ
        −

              f
              ˙

        ,

    {\displaystyle \mathbf {A} \rightarrow \mathbf {A} +\nabla f\,,\quad \varphi \rightarrow \varphi -{\dot {f}}\,,}

where f(r,t) is any scalar function of space and time, the aforementioned Lagrangian, canonical momenta and Hamiltonian transform like

        L
        →

          L
          ′

        L
        +
        q

              d
              f

              d
              t

        ,

          p

        →

            p
            ′

          p

        +
        q
        ∇
        f

        ,

        H
        →

          H
          ′

        H
        −
        q

              ∂
              f

              ∂
              t

        ,

    {\displaystyle L\rightarrow L'=L+q{\frac {df}{dt}}\,,\quad \mathbf {p} \rightarrow \mathbf {p'} =\mathbf {p} +q\nabla f\,,\quad H\rightarrow H'=H-q{\frac {\partial f}{\partial t}}\,,}

which still produces the same Hamilton's equation:

                          ∂

                            H
                            ′

                          ∂

                              x

                                i

                      p

                        i

                      ′

                        ∂

                          ∂

                              x

                                i

                      p

                        i

                      ′

                (

                        x
                        ˙

                    i

                  p

                    i

                  ′

                −

                  L
                  ′

                )

                −

                          ∂

                            L
                            ′

                          ∂

                              x

                                i

                      p

                        i

                      ′

                −

                          ∂
                          L

                          ∂

                              x

                                i

                      p

                        i

                      ′

                −
                q

                        ∂

                          ∂

                              x

                                i

                      p

                        i

                      ′

                      d
                      f

                      d
                      t

                −

                    d

                      d
                      t

                  (

                              ∂
                              L

                              ∂

                                        x
                                        ˙

                                    i

                          p

                            i

                          ′

                    +
                    q

                              ∂
                              f

                              ∂

                                  x

                                    i

                          p

                            i

                          ′

                  )

                −

                        p
                        ˙

                    i

                  ′

    {\displaystyle {\begin{aligned}\left.{\frac {\partial H'}{\partial {x_{i}}}}\right|{p'{i}}&=\left.{\frac {\partial }{\partial {x_{i}}}}\right|{p'{i}}({\dot {x}}{i}p'{i}-L')=-\left.{\frac {\partial L'}{\partial {x_{i}}}}\right|{p'{i}}\&=-\left.{\frac {\partial L}{\partial {x_{i}}}}\right|{p'{i}}-q\left.{\frac {\partial }{\partial {x_{i}}}}\right|{p'{i}}{\frac {df}{dt}}\&=-{\frac {d}{dt}}\left(\left.{\frac {\partial L}{\partial {{\dot {x}}{i}}}}\right|{p'{i}}+q\left.{\frac {\partial f}{\partial {x{i}}}}\right|{p'{i}}\right)\&=-{\dot {p}}'_{i}\end{aligned}}}

In quantum mechanics, the wave function will also undergo a local U(1) group transformation during the gauge transformation, which implies that all physical results must be invariant under local U(1) transformations.

Relativistic charged particle in an electromagnetic field
The relativistic Lagrangian for a particle (rest mass m and charge q) is given by:

            L

        (
        t
        )

        −
        m

          c

            2

            1
            −

                            x

                          ˙

                    (
                    t
                    )

                    2

                  c

                    2

        +
        q

                x

              ˙

        (
        t
        )
        ⋅

          A

          (

              x

            (
            t
            )
            ,
            t

          )

        −
        q
        φ

          (

              x

            (
            t
            )
            ,
            t

          )

    {\displaystyle {\mathcal {L}}(t)=-mc^{2}{\sqrt {1-{\frac {{{\dot {\mathbf {x} }}(t)}^{2}}{c^{2}}}}}+q{\dot {\mathbf {x} }}(t)\cdot \mathbf {A} \left(\mathbf {x} (t),t\right)-q\varphi \left(\mathbf {x} (t),t\right)}

Thus the particle's canonical momentum is

          p

        (
        t
        )

              ∂

                  L

              ∂

                      x

                    ˙

              m

                      x

                    ˙

              1
              −

                            x

                          ˙

                      2

                    c

                      2

        +
        q

          A

    {\displaystyle \mathbf {p} (t)={\frac {\partial {\mathcal {L}}}{\partial {\dot {\mathbf {x} }}}}={\frac {m{\dot {\mathbf {x} }}}{\sqrt {1-{\frac {{\dot {\mathbf {x} }}^{2}}{c^{2}}}}}}+q\mathbf {A} }

that is, the sum of the kinetic momentum and the potential momentum.
Solving for the velocity, we get

                x

              ˙

        (
        t
        )

                p

              −
              q

                A

                m

                  2

              +

                  1

                    c

                      2

                    (

                        p

                      −
                      q

                        A

                    )

                  2

    {\displaystyle {\dot {\mathbf {x} }}(t)={\frac {\mathbf {p} -q\mathbf {A} }{\sqrt {m^{2}+{\frac {1}{c^{2}}}{\left(\mathbf {p} -q\mathbf {A} \right)}^{2}}}}}

So the Hamiltonian is

            H

        (
        t
        )

                x

              ˙

        ⋅

          p

        −

            L

        c

              m

                2

              c

                2

            +

                  (

                      p

                    −
                    q

                      A

                  )

                2

        +
        q
        φ

    {\displaystyle {\mathcal {H}}(t)={\dot {\mathbf {x} }}\cdot \mathbf {p} -{\mathcal {L}}=c{\sqrt {m^{2}c^{2}+{\left(\mathbf {p} -q\mathbf {A} \right)}^{2}}}+q\varphi }

This results in the force equation (equivalent to the Euler–Lagrange equation)

                p

              ˙

        −

              ∂

                  H

              ∂

                x

        q

                x

              ˙

        ⋅
        (

          ∇

          A

        )
        −
        q

          ∇

        φ

        q

          ∇

        (

                x

              ˙

        ⋅

          A

        )
        −
        q

          ∇

        φ

    {\displaystyle {\dot {\mathbf {p} }}=-{\frac {\partial {\mathcal {H}}}{\partial \mathbf {x} }}=q{\dot {\mathbf {x} }}\cdot ({\boldsymbol {\nabla }}\mathbf {A} )-q{\boldsymbol {\nabla }}\varphi =q{\boldsymbol {\nabla }}({\dot {\mathbf {x} }}\cdot \mathbf {A} )-q{\boldsymbol {\nabla }}\varphi }

from which one can derive

                      d

                        d

                      t

                  (

                        m

                                x

                              ˙

                        1
                        −

                                      x

                                    ˙

                                2

                              c

                                2

                  )

                      d

                        d

                      t

                (

                  p

                −
                q

                  A

                )

                        p

                      ˙

                −
                q

                      ∂
                      A

                      ∂
                      t

                −
                q
                (

                        x

                      ˙

                ⋅
                ∇
                )

                  A

                q

                  ∇

                (

                        x

                      ˙

                ⋅

                  A

                )
                −
                q

                  ∇

                φ
                −
                q

                      ∂
                      A

                      ∂
                      t

                −
                q
                (

                        x

                      ˙

                ⋅
                ∇
                )

                  A

                q

                  E

                +
                q

                        x

                      ˙

                ×

                  B

    {\displaystyle {\begin{aligned}{\frac {\mathrm {d} }{\mathrm {d} t}}\left({\frac {m{\dot {\mathbf {x} }}}{\sqrt {1-{\frac {{\dot {\mathbf {x} }}^{2}}{c^{2}}}}}}\right)&={\frac {\mathrm {d} }{\mathrm {d} t}}(\mathbf {p} -q\mathbf {A} )={\dot {\mathbf {p} }}-q{\frac {\partial A}{\partial t}}-q({\dot {\mathbf {x} }}\cdot \nabla )\mathbf {A} \&=q{\boldsymbol {\nabla }}({\dot {\mathbf {x} }}\cdot \mathbf {A} )-q{\boldsymbol {\nabla }}\varphi -q{\frac {\partial A}{\partial t}}-q({\dot {\mathbf {x} }}\cdot \nabla )\mathbf {A} \&=q\mathbf {E} +q{\dot {\mathbf {x} }}\times \mathbf {B} \end{aligned}}}

The above derivation makes use of the vector calculus identity:

              1
              2

        ∇

          (

              A

            ⋅

              A

          )

          A

        ⋅

            J

              A

          A

        ⋅
        (
        ∇

          A

        )

        (

          A

          ⋅

        ∇
        )

          A

        +

          A

          ×

        (
        ∇

          ×

          A

        )
        .

    {\displaystyle {\tfrac {1}{2}}\nabla \left(\mathbf {A} \cdot \mathbf {A} \right)\ =\ \mathbf {A} \cdot \mathbf {J} _{\mathbf {A} }\ =\ \mathbf {A} \cdot (\nabla \mathbf {A} )\ =\ (\mathbf {A} {\cdot }\nabla )\mathbf {A} \,+\,\mathbf {A} {\times }(\nabla {\times }\mathbf {A} ).}

An equivalent expression for the Hamiltonian as function of the relativistic (kinetic) momentum, P = γmẋ(t) = p - qA, is

            H

        (
        t
        )

                x

              ˙

        (
        t
        )
        ⋅

          P

        (
        t
        )
        +

              m

                c

                  2

            γ

        +
        q
        φ
        (

          x

        (
        t
        )
        ,
        t
        )

        γ
        m

          c

            2

        +
        q
        φ
        (

          x

        (
        t
        )
        ,
        t
        )

        E
        +
        V

    {\displaystyle {\mathcal {H}}(t)={\dot {\mathbf {x} }}(t)\cdot \mathbf {P} (t)+{\frac {mc^{2}}{\gamma }}+q\varphi (\mathbf {x} (t),t)=\gamma mc^{2}+q\varphi (\mathbf {x} (t),t)=E+V}

This has the advantage that kinetic momentum P can be measured experimentally whereas canonical momentum p cannot. Notice that the Hamiltonian (total energy) can be viewed as the sum of the relativistic energy (kinetic+rest), E = γmc2, plus the potential energy, V = eφ.

Inflation
In studies of cosmological inflation, minimal coupling of a scalar field usually refers to minimal coupling to gravity. This means that the action for the inflaton field

        φ

    {\displaystyle \varphi }

 is not coupled to the scalar curvature. Its only coupling to gravity is the coupling to the Lorentz invariant measure

            g

          d

            4

        x

    {\displaystyle {\sqrt {g}}\,d^{4}x}

 constructed from the metric (in Planck units):

        S

        ∫

          d

            4

        x

            g

          (

            −

                1
                2

            R
            +

                1
                2

              ∇

                μ

            φ

              ∇

                μ

            φ
            −
            V
            (
            φ
            )

          )

    {\displaystyle S=\int d^{4}x\,{\sqrt {g}}\,\left(-{\frac {1}{2}}R+{\frac {1}{2}}\nabla _{\mu }\varphi \nabla ^{\mu }\varphi -V(\varphi )\right)}

where

        g
        :=
        det

          g

            μ
            ν

    {\displaystyle g:=\det g_{\mu \nu }}

, and utilizing the gauge covariant derivative.
