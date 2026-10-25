# Bertrand's theorem

Bertrand's theorem

In classical mechanics, Bertrand's theorem states that among central-force potentials with bound orbits, there are only two types of central-force (radial) scalar potentials with the property that all bound orbits are also closed orbits. The theorem is named after its discoverer, Joseph Bertrand who published it in 1873.
The first such potential is an inverse-square central force such as the gravitational or electrostatic potential:

        V
        (
        r
        )

        −

            k
            r

    {\displaystyle V(r)=-{\frac {k}{r}}}

 with force

          F

        (
        r
        )

        −
        ∇
        V

        −

            k

              r

                2

                r

              ^

        .

    {\displaystyle \mathbf {F} (r)=-\nabla V=-{\frac {k}{r^{2}}}{\hat {\mathbf {r} }}.}

The second is the radial harmonic oscillator potential:

        V
        (
        r
        )

            1
            2

        k

          r

            2

    {\displaystyle V(r)={\frac {1}{2}}kr^{2}}

 with force

          F

        (

          r

        )

        −
        ∇
        V

        −
        k
        r

                r

              ^

        .

    {\displaystyle \mathbf {F} (\mathbf {r} )=-\nabla V=-kr\,{\hat {\mathbf {r} }}.}

Derivation

All attractive central forces can produce circular orbits, which are naturally closed orbits. The only requirement is that the central force exactly equals the centripetal force, which determines the required angular velocity for a given circular radius. Non-central forces (i.e., those that depend on the angular variables as well as the radius) are ignored here, since they do not produce circular orbits in general.
The equation of motion for the radius

        r

    {\displaystyle r}

 of a particle of mass

        m

    {\displaystyle m}

 moving in a central potential

        V
        (
        r
        )

    {\displaystyle V(r)}

 is given by motion equations

        m

                d

                  2

              r

              d

                t

                  2

        −
        m
        r

          ω

            2

        m

                d

                  2

              r

              d

                t

                  2

        −

              L

                2

              m

                r

                  3

        −

              d
              V

              d
              r

        ,

    {\displaystyle m{\frac {d^{2}r}{dt^{2}}}-mr\omega ^{2}=m{\frac {d^{2}r}{dt^{2}}}-{\frac {L^{2}}{mr^{3}}}=-{\frac {dV}{dr}},}

where

        ω
        ≡

              d
              θ

              d
              t

    {\displaystyle \omega \equiv {\frac {d\theta }{dt}}}

, and the angular momentum

        L

        m

          r

            2

        ω

    {\displaystyle L=mr^{2}\omega }

 is conserved. For illustration, the first term on the left is zero for circular orbits, and the applied inwards force

              d
              V

              d
              r

    {\displaystyle {\frac {dV}{dr}}}

 equals the centripetal force requirement

        m

          r

            2

        ω

    {\displaystyle mr^{2}\omega }

, as expected.
The definition of angular momentum allows a change of independent variable from

        t

    {\displaystyle t}

 to

        θ

    {\displaystyle \theta }

:

            d

              d
              t

            L

              m

                r

                  2

            d

              d
              θ

        ,

    {\displaystyle {\frac {d}{dt}}={\frac {L}{mr^{2}}}{\frac {d}{d\theta }},}

giving the new equation of motion that is independent of time:

            L

              r

                2

            d

              d
              θ

          (

                L

                  m

                    r

                      2

                  d
                  r

                  d
                  θ

          )

        −

              L

                2

              m

                r

                  3

        −

              d
              V

              d
              r

        .

    {\displaystyle {\frac {L}{r^{2}}}{\frac {d}{d\theta }}\left({\frac {L}{mr^{2}}}{\frac {dr}{d\theta }}\right)-{\frac {L^{2}}{mr^{3}}}=-{\frac {dV}{dr}}.}

This equation becomes quasilinear on making the change of variables

        u
        ≡

            1
            r

    {\displaystyle u\equiv {\frac {1}{r}}}

 and multiplying both sides by

              m

                r

                  2

              L

                2

    {\displaystyle {\frac {mr^{2}}{L^{2}}}}

 (see also Binet equation):

                d

                  2

              u

              d

                θ

                  2

        +
        u

        −

            m

              L

                2

            d

              d
              u

        V

            (

                1
                u

            )

        .

    {\displaystyle {\frac {d^{2}u}{d\theta ^{2}}}+u=-{\frac {m}{L^{2}}}{\frac {d}{du}}V{\left({\frac {1}{u}}\right)}.}

As noted above, all central forces can produce circular orbits given an appropriate initial velocity. However, if some radial velocity is introduced, these orbits need not be stable (i.e., remain in orbit indefinitely) nor closed (repeatedly returning to exactly the same path). Here we show that a necessary condition for stable, exactly closed non-circular orbits is an inverse-square force or radial harmonic oscillator potential. In the following sections, we show that those two force laws produce stable, exactly closed orbits.
Define

        J
        (
        u
        )

    {\displaystyle J(u)}

 as

                d

                  2

              u

              d

                θ

                  2

        +
        u

        J
        (
        u
        )
        ≡
        −

            m

              L

                2

            d

              d
              u

        V

            (

                1
                u

            )

        −

            m

                L

                  2

                u

                  2

        f

            (

                1
                u

            )

        ,

    {\displaystyle {\frac {d^{2}u}{d\theta ^{2}}}+u=J(u)\equiv -{\frac {m}{L^{2}}}{\frac {d}{du}}V{\left({\frac {1}{u}}\right)}=-{\frac {m}{L^{2}u^{2}}}f{\left({\frac {1}{u}}\right)},}

where

        f

    {\displaystyle f}

 represents the radial force. The criterion for perfectly circular motion at a radius

          r

            0

    {\displaystyle r_{0}}

 is that the first term on the left be zero:

where

          u

            0

        ≡
        1

          /

          r

            0

    {\displaystyle u_{0}\equiv 1/r_{0}}

.
The next step is to consider the equation for

        u

    {\displaystyle u}

 under small perturbations

        η
        ≡
        u
        −

          u

            0

    {\displaystyle \eta \equiv u-u_{0}}

 from perfectly circular orbits. On the right, the

        J

    {\displaystyle J}

 function can be expanded in a standard Taylor series:

        J
        (
        u
        )
        ≈
        J
        (

          u

            0

        )
        +
        η

          J
          ′

        (

          u

            0

        )
        +

            1
            2

          η

            2

          J
          ″

        (

          u

            0

        )
        +

            1
            6

          η

            3

          J
          ‴

        (

          u

            0

        )
        +
        ⋯

    {\displaystyle J(u)\approx J(u_{0})+\eta J'(u_{0})+{\frac {1}{2}}\eta ^{2}J''(u_{0})+{\frac {1}{6}}\eta ^{3}J'''(u_{0})+\cdots }

Substituting this expansion into the equation for

        u

    {\displaystyle u}

 and subtracting the constant terms yields

                d

                  2

              η

              d

                θ

                  2

        +
        η

        η

          J
          ′

        (

          u

            0

        )
        +

            1
            2

          η

            2

          J
          ″

        (

          u

            0

        )
        +

            1
            6

          η

            3

          J
          ‴

        (

          u

            0

        )
        +
        ⋯
        ,

    {\displaystyle {\frac {d^{2}\eta }{d\theta ^{2}}}+\eta =\eta J'(u_{0})+{\frac {1}{2}}\eta ^{2}J''(u_{0})+{\frac {1}{6}}\eta ^{3}J'''(u_{0})+\cdots ,}

which can be written as

where

          β

            2

        ≡
        1
        −

          J
          ′

        (

          u

            0

        )

    {\displaystyle \beta ^{2}\equiv 1-J'(u_{0})}

 is a constant.

          β

            2

    {\displaystyle \beta ^{2}}

 must be non-negative; otherwise, the radius of the orbit would vary exponentially away from its initial radius. (The solution

        β

        0

    {\displaystyle \beta =0}

 corresponds to a perfectly circular orbit.) If the right side may be neglected (i.e., for small perturbations), the solutions are

        η
        (
        θ
        )

          h

            1

        cos
        ⁡
        (
        β
        θ
        )
        ,

    {\displaystyle \eta (\theta )=h_{1}\cos(\beta \theta ),}

where the amplitude

          h

            1

    {\displaystyle h_{1}}

 is a constant of integration. For the orbits to be closed,

        β

    {\displaystyle \beta }

 must be a rational number. What's more, it must be the same rational number for all radii, since

        β

    {\displaystyle \beta }

 cannot change continuously; the rational numbers are totally disconnected from one another. Using the definition of

        J

    {\displaystyle J}

 along with equation 1,

                  J
                  ′

                (

                  u

                    0

                )

                    2

                      u

                        0

                  [

                        m

                            L

                              2

                            u

                              0

                              2

                    f

                        (

                            1

                              u

                                0

                        )

                  ]

                −

                  [

                        m

                            L

                              2

                            u

                              0

                              2

                    f

                        (

                            1

                              u

                                0

                        )

                  ]

                    1

                      f

                          (

                              1

                                u

                                  0

                          )

                    d

                      d

                        u

                          0

                f

                    (

                        1

                          u

                            0

                    )

                −
                2
                +

                      u

                        0

                      f

                          (

                              1

                                u

                                  0

                          )

                    d

                      d

                        u

                          0

                f

                    (

                        1

                          u

                            0

                    )

                1
                −

                  β

                    2

                .

    {\displaystyle {\begin{aligned}J'(u_{0})&={\frac {2}{u_{0}}}\left[{\frac {m}{L^{2}u_{0}^{2}}}f{\left({\frac {1}{u_{0}}}\right)}\right]-\left[{\frac {m}{L^{2}u_{0}^{2}}}f{\left({\frac {1}{u_{0}}}\right)}\right]{\frac {1}{f{\left({\frac {1}{u_{0}}}\right)}}}{\frac {d}{du_{0}}}f{\left({\frac {1}{u_{0}}}\right)}\[1ex]&=-2+{\frac {u_{0}}{f{\left({\frac {1}{u_{0}}}\right)}}}{\frac {d}{du_{0}}}f{\left({\frac {1}{u_{0}}}\right)}=1-\beta ^{2}.\end{aligned}}}

Since this must hold for any value of

          u

            0

    {\displaystyle u_{0}}

,

              d
              f

              d
              r

          (

              β

                2

            −
            3

          )

            f
            r

        ,

    {\displaystyle {\frac {df}{dr}}=\left(\beta ^{2}-3\right){\frac {f}{r}},}

which implies that the force must follow a power law

        f
        (
        r
        )

        −

            k

              r

                3
                −

                  β

                    2

        .

    {\displaystyle f(r)=-{\frac {k}{r^{3-\beta ^{2}}}}.}

Hence,

        J

    {\displaystyle J}

 must have the general form

For more general deviations from circularity (i.e., when we cannot neglect the higher-order terms in the Taylor expansion of

        J

    {\displaystyle J}

 ),

        η

    {\displaystyle \eta }

 may be expanded in a Fourier series, e.g.,

        η
        (
        θ
        )

          h

            0

        +

          h

            1

        cos
        ⁡
        β
        θ
        +

          h

            2

        cos
        ⁡
        2
        β
        θ
        +

          h

            3

        cos
        ⁡
        3
        β
        θ
        +
        ⋯

    {\displaystyle \eta (\theta )=h_{0}+h_{1}\cos \beta \theta +h_{2}\cos 2\beta \theta +h_{3}\cos 3\beta \theta +\cdots }

We substitute this into equation 2 and equate the coefficients belonging to the same frequency, keeping only the lowest-order terms. As we show below,

          h

            0

    {\displaystyle h_{0}}

 and

          h

            2

    {\displaystyle h_{2}}

 are smaller than

          h

            1

    {\displaystyle h_{1}}

, being of order

          h

            1

            2

    {\displaystyle h_{1}^{2}}

.

          h

            3

    {\displaystyle h_{3}}

, and all further coefficients, are at least of order

          h

            1

            3

    {\displaystyle h_{1}^{3}}

. This makes sense, since

          h

            0

        ,

          h

            2

        ,

          h

            3

        ,
        …

    {\displaystyle h_{0},h_{2},h_{3},\ldots }

 must all vanish faster than

          h

            1

    {\displaystyle h_{1}}

 as a circular orbit is approached.

                  h

                    0

                  h

                    1

                    2

                        J
                        ″

                      (

                        u

                          0

                      )

                      4

                        β

                          2

                ,

                  h

                    2

                −

                  h

                    1

                    2

                        J
                        ″

                      (

                        u

                          0

                      )

                      12

                        β

                          2

                ,

                  h

                    3

                −

                    1

                      8

                        β

                          2

                  [

                      h

                        1

                      h

                        2

                            J
                            ″

                          (

                            u

                              0

                          )

                        2

                    +

                      h

                        1

                        3

                            J
                            ‴

                          (

                            u

                              0

                          )

                        24

                  ]

                .

    {\displaystyle {\begin{aligned}h_{0}&=h_{1}^{2}{\frac {J''(u_{0})}{4\beta ^{2}}},\h_{2}&=-h_{1}^{2}{\frac {J''(u_{0})}{12\beta ^{2}}},\h_{3}&=-{\frac {1}{8\beta ^{2}}}\left[h_{1}h_{2}{\frac {J''(u_{0})}{2}}+h_{1}^{3}{\frac {J'''(u_{0})}{24}}\right].\end{aligned}}}

From the

        cos
        ⁡
        β
        θ

    {\displaystyle \cos \beta \theta }

 term, we get

                0

                  (

                    2

                      h

                        1

                      h

                        0

                    +

                      h

                        1

                      h

                        2

                  )

                        J
                        ″

                      (

                        u

                          0

                      )

                    2

                +

                  h

                    1

                    3

                        J
                        ‴

                      (

                        u

                          0

                      )

                    8

                      h

                        1

                        3

                      24

                        β

                          2

                  (

                    3

                      β

                        2

                      J
                      ‴

                    (

                      u

                        0

                    )
                    +
                    5

                      J
                      ″

                    (

                      u

                        0

                      )

                        2

                  )

                ,

    {\displaystyle {\begin{aligned}0&=\left(2h_{1}h_{0}+h_{1}h_{2}\right){\frac {J''(u_{0})}{2}}+h_{1}^{3}{\frac {J'''(u_{0})}{8}}\&={\frac {h_{1}^{3}}{24\beta ^{2}}}\left(3\beta ^{2}J'''(u_{0})+5J''(u_{0})^{2}\right),\end{aligned}}}

where in the last step we substituted in the values of

          h

            0

    {\displaystyle h_{0}}

 and

          h

            2

    {\displaystyle h_{2}}

.
Using equations (3) and (1), we can calculate the second and third derivatives of

        J

    {\displaystyle J}

 evaluated at

          u

            0

    {\displaystyle u_{0}}

:

                  J
                  ″

                (

                  u

                    0

                )

                −

                        β

                          2

                        (

                          1
                          −

                            β

                              2

                        )

                      u

                        0

                ,

                  J
                  ‴

                (

                  u

                    0

                )

                        β

                          2

                        (

                          1
                          −

                            β

                              2

                        )

                        (

                          1
                          +

                            β

                              2

                        )

                      u

                        0

                        2

                .

    {\displaystyle {\begin{aligned}J''(u_{0})&=-{\frac {\beta ^{2}\left(1-\beta ^{2}\right)}{u_{0}}},\J'''(u_{0})&={\frac {\beta ^{2}\left(1-\beta ^{2}\right)\left(1+\beta ^{2}\right)}{u_{0}^{2}}}.\end{aligned}}}

Substituting these values into the last equation yields the main result of Bertrand's theorem:

          β

            2

          (

            1
            −

              β

                2

          )

          (

            4
            −

              β

                2

          )

        0.

    {\displaystyle \beta ^{2}\left(1-\beta ^{2}\right)\left(4-\beta ^{2}\right)=0.}

Hence, the only potentials that can produce stable closed non-circular orbits are the inverse-square force law (

        β

        1

    {\displaystyle \beta =1}

) and the radial harmonic-oscillator potential (

        β

        2

    {\displaystyle \beta =2}

). The solution

        β

        0

    {\displaystyle \beta =0}

 corresponds to perfectly circular orbits, as noted above.

Classical field potentials
For an inverse-square force law such as the gravitational or electrostatic potential, the potential can be written

        V
        (

          r

        )

              −
              k

            r

        −
        k
        u
        .

    {\displaystyle V(\mathbf {r} )={\frac {-k}{r}}=-ku.}

The orbit u(θ) can be derived from the general equation

                d

                  2

              u

              d

                θ

                  2

        +
        u

        −

            m

              L

                2

            d

              d
              u

        V

            (

                1
                u

            )

              k
              m

              L

                2

        ,

    {\displaystyle {\frac {d^{2}u}{d\theta ^{2}}}+u=-{\frac {m}{L^{2}}}{\frac {d}{du}}V{\left({\frac {1}{u}}\right)}={\frac {km}{L^{2}}},}

whose solution is the constant

              k
              m

              L

                2

    {\displaystyle {\frac {km}{L^{2}}}}

 plus a simple sinusoid:

        u
        ≡

            1
            r

              k
              m

              L

                2

        [
        1
        +
        e
        cos
        ⁡
        (
        θ
        −

          θ

            0

        )
        ]
        ,

    {\displaystyle u\equiv {\frac {1}{r}}={\frac {km}{L^{2}}}[1+e\cos(\theta -\theta _{0})],}

where e (the eccentricity), and θ0 (the phase offset) are constants of integration.
This is the general formula for a conic section that has one focus at the origin; e = 0 corresponds to a circle, 0 < e < 1 corresponds to an ellipse, e = 1 corresponds to a parabola, and e > 1 corresponds to a hyperbola. The eccentricity e is related to the total energy E (see Laplace–Runge–Lenz vector):

        e

            1
            +

                  2
                  E

                    L

                      2

                    k

                      2

                  m

        .

    {\displaystyle e={\sqrt {1+{\frac {2EL^{2}}{k^{2}m}}}}.}

Comparing these formulae shows that E < 0 corresponds to an ellipse, E = 0 corresponds to a parabola, and E > 0 corresponds to a hyperbola. In particular,

        E

        −

                k

                  2

              m

              2

                L

                  2

    {\displaystyle E=-{\frac {k^{2}m}{2L^{2}}}}

 for perfectly circular orbits.

Harmonic oscillator
To solve for the orbit under a radial harmonic-oscillator potential, it's easier to work in components r = (x, y, z). The potential can be written as

        V
        (

          r

        )

            1
            2

        k

          r

            2

            1
            2

        k
        (

          x

            2

        +

          y

            2

        +

          z

            2

        )
        .

    {\displaystyle V(\mathbf {r} )={\frac {1}{2}}kr^{2}={\frac {1}{2}}k(x^{2}+y^{2}+z^{2}).}

The equation of motion for a particle of mass m is given by three independent Euler equations:

                        d

                          2

                      x

                      d

                        t

                          2

                +

                  ω

                    0

                    2

                x

                0
                ,

                        d

                          2

                      y

                      d

                        t

                          2

                +

                  ω

                    0

                    2

                y

                0
                ,

                        d

                          2

                      z

                      d

                        t

                          2

                +

                  ω

                    0

                    2

                z

                0
                ,

    {\displaystyle {\begin{aligned}{\frac {d^{2}x}{dt^{2}}}+\omega _{0}^{2}x&=0,\{\frac {d^{2}y}{dt^{2}}}+\omega _{0}^{2}y&=0,\{\frac {d^{2}z}{dt^{2}}}+\omega _{0}^{2}z&=0,\end{aligned}}}

where the constant

          ω

            0

            2

        ≡

            k
            m

    {\displaystyle \omega _{0}^{2}\equiv {\frac {k}{m}}}

 must be positive (i.e., k > 0) to ensure bounded, closed orbits; otherwise, the particle will fly off to infinity. The solutions of these simple harmonic oscillator equations are all similar:

                x

                  A

                    x

                cos
                ⁡
                (

                  ω

                    0

                t
                +

                  ϕ

                    x

                )
                ,

                y

                  A

                    y

                cos
                ⁡
                (

                  ω

                    0

                t
                +

                  ϕ

                    y

                )
                ,

                z

                  A

                    z

                cos
                ⁡
                (

                  ω

                    0

                t
                +

                  ϕ

                    z

                )
                ,

    {\displaystyle {\begin{aligned}x&=A_{x}\cos(\omega _{0}t+\phi {x}),\y&=A{y}\cos(\omega _{0}t+\phi {y}),\z&=A{z}\cos(\omega _{0}t+\phi _{z}),\end{aligned}}}

where the positive constants Ax, Ay and Az represent the amplitudes of the oscillations, and the angles φx, φy and φz represent their phases. The resulting orbit r(t) = [x(t), y(y), z(t)] is closed because it repeats exactly after one period

        T
        ≡

              2
              π

              ω

                0

        .

    {\displaystyle T\equiv {\frac {2\pi }{\omega _{0}}}.}

The system is also stable because small perturbations in the amplitudes and phases cause correspondingly small changes in the overall orbit.
