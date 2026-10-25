# Ponderomotive force

Ponderomotive force

In physics, a ponderomotive force is a nonlinear force that a charged particle experiences in an inhomogeneous oscillating electromagnetic field. It causes the particle to move towards the area of the weaker field strength, rather than oscillating around an initial point as happens in a homogeneous field. This occurs because the particle sees a greater magnitude of force during the half of the oscillation period while it is in the area with the stronger field. The net force during its period in the weaker area in the second half of the oscillation does not offset the net force of the first half, and so over a complete cycle this makes the particle accelerate towards the area of lesser force.
The classical expression for the ponderomotive force Fp is

            F

            p

    {\displaystyle \mathbf {F} _{\text{p}}=}

        −

              e

                2

              4
              m

                ω

                  2

    {\displaystyle -{\frac {e^{2}}{4m\omega ^{2}}}}

        ∇

    {\displaystyle \nabla }

        (

                E
                ^

            2

        )

    {\displaystyle ({\hat {E}}^{2})}

which has units of newtons (in SI units) and where e is the electrical charge of the particle, m is its mass, ω is the angular frequency of oscillation of the field, and

              E
              ^

    {\displaystyle {\hat {E}}}

 is the amplitude of the electric field. At non-relativistic particle velocities the magnetic field exerts very little force and can be disregarded.
This equation means that a charged particle in an inhomogeneous oscillating field not only oscillates at the frequency of ω of the field, but is also accelerated by Fp toward the weak field direction. This is a rare case in which the direction of the force does not depend on whether the particle is positively or negatively charged.

Etymology
The term ponderomotive comes from the Latin ponder- (meaning weight) and the English motive (having to do with motion).

1D Classical Derivation
A simplified derivation of the ponderomotive force expression proceeds in the one-dimensional case as follows.
Consider a particle under the action of a non-uniform electric field oscillating at frequency

        ω

    {\displaystyle \omega }

 in the x-direction, and assume that the particle moves only in the x-direction. Further, also assume the particle always moves at non-relativistic velocities, letting us neglect the magnetic force. The equation of motion is then given by:

              x
              ¨

            e
            m

                E
                ^

            x

        (
        x
        )
        cos
        ⁡
        (
        ω
        t
        )
        .

    {\displaystyle {\ddot {x}}={\frac {e}{m}}{\hat {E}}_{x}(x)\cos(\omega t).}

If the length scale

        ∼
        L

    {\displaystyle \sim L}

 of variation of

                E
                ^

            x

        (
        x
        )

    {\displaystyle {\hat {E}}_{x}(x)}

 is large enough, then the particle trajectory can be divided into a slow time (secular) motion and a fast time (micro)motion:

        x

          x

            0

        +

          x

            1

    {\displaystyle x=x_{0}+x_{1}}

where

          x

            0

    {\displaystyle x_{0}}

 is the slow drift motion and

          x

            1

    {\displaystyle x_{1}}

 represents fast oscillations. Now, let us also assume that

          x

            1

        ≪
        L

    {\displaystyle x_{1}\ll L}

. Under this assumption, we can use Taylor expansion on the force equation about

          x

            0

    {\displaystyle x_{0}}

, to get:

                x
                ¨

            0

        +

                x
                ¨

            1

        ≈

            e
            m

          [

                    E
                    ^

                x

            (

              x

                0

            )
            +

              x

                1

                    E
                    ^

                x

              ′

            (

              x

                0

            )

          ]

        cos
        ⁡
        (
        ω
        t
        )

    {\displaystyle {\ddot {x}}{0}+{\ddot {x}}{1}\approx {\frac {e}{m}}\left[{\hat {E}}{x}(x{0})+x_{1}{\hat {E}}{x}'(x{0})\right]\cos(\omega t)}

because the oscillation is high frequency

                x
                ¨

            0

        ≪

                x
                ¨

            1

    {\displaystyle {\ddot {x}}{0}\ll {\ddot {x}}{1}}

, and because

          x

            1

    {\displaystyle x_{1}}

 is small,

          x

            1

                E
                ^

            x

          ′

        (

          x

            0

        )

    {\displaystyle x_{1}{\hat {E}}{x}'(x{0})}

 can be neglected, so

                x
                ¨

            1

        ≈

            e
            m

                E
                ^

            x

        (

          x

            0

        )
        cos
        ⁡
        (
        ω
        t
        )

    {\displaystyle {\ddot {x}}{1}\approx {\frac {e}{m}}{\hat {E}}{x}(x_{0})\cos(\omega t)}

On the time scale on which

          x

            1

    {\displaystyle x_{1}}

 oscillates,

          x

            0

    {\displaystyle x_{0}}

 is essentially a constant. Thus, the above can be integrated to get:

          x

            1

        ≈
        −

            e
            m

                      E
                      ^

                  x

              (

                x

                  0

              )

              ω

                2

        cos
        ⁡
        (
        ω
        t
        )

    {\displaystyle x_{1}\approx -{\frac {e}{m}}{\frac {{\hat {E}}{x}(x{0})}{\omega ^{2}}}\cos(\omega t)}

Substituting this in the Taylor expanded force equation and averaging over the

        2
        π

          /

        ω

    {\displaystyle 2\pi /\omega }

 timescale, we get,

                x
                ¨

            0

        ≈
        −

              e

                2

              m

                2

                      E
                      ^

                  x

              (

                x

                  0

              )

                      E
                      ^

                  x

                ′

              (

                x

                  0

              )

              2

                ω

                  2

        −

              e

                2

              4

                m

                  2

                ω

                  2

        (

                E
                ^

            x

            2

          )
          ′

    {\displaystyle {\ddot {x}}{0}\approx -{\frac {e^{2}}{m^{2}}}{\frac {{\hat {E}}{x}(x_{0}){\hat {E}}{x}'(x{0})}{2\omega ^{2}}}=-{\frac {e^{2}}{4m^{2}\omega ^{2}}}({\hat {E}}_{x}^{2})'}

        ⇒

          F

            p

        m

                x
                ¨

            0

        −

              e

                2

              4
              m

                ω

                  2

        (

                E
                ^

            x

            2

          )
          ′

        ,

    {\displaystyle \Rightarrow F_{p}=m{\ddot {x}}{0}=-{\frac {e^{2}}{4m\omega ^{2}}}({\hat {E}}{x}^{2})',}

as sinusoids average to 0 and squared sinusoids average to

            1
            2

    {\displaystyle {\frac {1}{2}}}

. This at least hints at the form of the classical 3D expression.

General expression
Including the magnetic field in the analysis and allowing relativistic velocities and slightly more general fields, the starting point is the exact equations, in four-vector notation:

        m

              d

                u

                  μ

              d
              τ

          R
          e

          [

            f

              μ

          ]

          R
          e

          [

                    f
                    ^

                μ

            (
            x
            ,
            u
            )

              e

                −
                i

                  k

                    ν

                  x

                    ν

          ]

        .

    {\displaystyle m{\frac {du^{\mu }}{d\tau }}=\mathrm {Re} \left[f^{\mu }\right]=\mathrm {Re} \left[{\hat {f}}^{\mu }(x,u)e^{-ik_{\nu }x^{\nu }}\right].}

Here

        m

    {\displaystyle m}

 is the mass of the particle,

        u

    {\displaystyle u}

 is the four-velocity,

        τ

    {\displaystyle \tau }

 is the proper time,

        f

    {\displaystyle f}

 is the Lorentz force (see four-force),

        x

    {\displaystyle x}

 is the four-position, and

        k

    {\displaystyle k}

 is the wave four-vector. The force is allowed to be complex so that, for example, circularly polarized fields are included.
From these assumptions, the perturbative analysis yields the following ponderomotive force:

        m

              d

                      u
                      ¯

                  μ

              d
              τ

        ≈
        −

                ∂

                    x

                      μ

                [

                          f
                          ^

                      ν

                      ∗

                          f
                          ^

                      ν

                ]

              4
              m
              (

                k

                  λ

                u

                  λ

                )

                  2

    {\displaystyle m{\frac {d{\bar {u}}^{\mu }}{d\tau }}\approx -{\frac {\partial ^{x^{\mu }}\left[{\hat {f}}{\nu }^{*}{\hat {f}}^{\nu }\right]}{4m(k{\lambda }u^{\lambda })^{2}}}}

,

where

              u
              ¯

    {\displaystyle {\bar {u}}}

 is the time-averaged four-velocity,

          ∂

              x

                μ

    {\displaystyle \partial ^{x^{\mu }}}

 are the contravariant components of the four-gradient and

            ∗

    {\displaystyle \ ^{*}}

 denotes complex conjugation. The force is a proper four-vector, being the four-gradient of a Lorentz scalar. This can be translated to regular 3-vector notation:

              d

                p

              d
              t

        ≈

              −
              ∇

                  [

                    f
                    ^

                  2

              −

                    f
                    ^

              ⋅

                β

                  2

                  ]

              4
              m

                  γ
                  ¯

                  (

                    ω
                    −

                      k

                    ⋅

                      v

                  )

                  2

    {\displaystyle {\frac {d{\boldsymbol {p}}}{dt}}\approx {\frac {-\nabla {\Big [}||{\hat {\boldsymbol {f}}}||^{2}-|{\hat {\boldsymbol {f}}}\cdot {\boldsymbol {\beta }}|^{2}{\Big ]}}{4m{\overline {\gamma }}\left(\omega -{\boldsymbol {k}}\cdot {\boldsymbol {v}}\right)^{2}}}}

where

          β

          v

          /

        c

    {\displaystyle {\boldsymbol {\beta }}={\boldsymbol {v}}/c}

,

              γ
              ¯

    {\displaystyle {\bar {\gamma }}}

 is the time-averaged particle energy in the units of the rest mass, and

        ω
        −

          k

        ⋅

          v

    {\displaystyle \omega -{\boldsymbol {k}}\cdot {\boldsymbol {v}}}

 can be interpreted as a Doppler-shifted angular frequency. Note that

        k

    {\displaystyle k}

 and

        ω

    {\displaystyle \omega }

 do not have to follow any particular dispersion relation. For example, in a magnetic undulator,

        ω

    {\displaystyle \omega }

 is zero, and in a standing wave

          k

    {\displaystyle {\boldsymbol {k}}}

 is 0, as the spatial variation must be included in the envelope of

              f
              ^

    {\displaystyle {\hat {\boldsymbol {f}}}}

.
This expression predicts behaviour that can be significantly different from those predicted by the classical expression. The ponderomotive force can even have a completely opposite direction to that of the classical expression for relativistic particle velocities or for strongly focused fields. Taking

        β

            v
            c

    {\displaystyle \beta ={\frac {v}{c}}}

 to be very small, the general expression reduces to the classical one. In the limit where the electromagnetic fields are very similar to those of a plane wave, it reduces to an earlier relativistic generalisation found by (among others) Quesnel and Mora in 1998:

              d

                p

              d
              t

        ≈

              −

                e

                  2

              ∇

                  [

                    E
                    ^

                  2

                  ]

              4
              m

                  γ
                  ¯

                ω

                  2

    {\displaystyle {\frac {d{\boldsymbol {p}}}{dt}}\approx {\frac {-e^{2}\nabla {\Big [}||{\hat {\boldsymbol {E}}}||^{2}{\Big ]}}{4m{\overline {\gamma }}\omega ^{2}}}}

.

Time averaged density
Instead of a single charged particle, there could be a gas of charged particles confined by the action of such a force. Such a gas of charged particles is called plasma. The distribution function and density of the plasma will fluctuate at the applied oscillating frequency and to obtain an exact solution, we need to solve the Vlasov Equation. But, it is usually assumed that the time averaged density of the plasma can be directly obtained from the expression for the force expression for the drift motion of individual charged particles:

              n
              ¯

        (
        x
        )

          n

            0

        exp
        ⁡

          [

            −

                e

                  κ
                  T

              Φ

                P

            (
            x
            )

          ]

    {\displaystyle {\bar {n}}(x)=n_{0}\exp \left[-{\frac {e}{\kappa T}}\Phi _{\text{P}}(x)\right]}

where

          Φ

            P

    {\displaystyle \Phi _{\text{P}}}

 is the ponderomotive potential and is given by

          Φ

            P

        (
        x
        )

            m

              4

                ω

                  2

            [

              g
              (
              x
              )

            ]

            2

    {\displaystyle \Phi _{\text{P}}(x)={\frac {m}{4\omega ^{2}}}\left[g(x)\right]^{2}}

Applications
The idea of a ponderomotive description of particles under the action of a time-varying field has applications in areas like:

High harmonic generation
Plasma acceleration of particles
Plasma propulsion engine especially the Electrodeless plasma thruster
Quadrupole ion trap
Terahertz time-domain spectroscopy as a source of high energy THz radiation in laser-induced air plasmas
The quadrupole ion trap uses a linear function

        g
        (
        x
        )

        x

    {\displaystyle g(x)=x}

 along its principal axes. This gives rise to a harmonic oscillator in the secular motion with the so-called trapping frequency

        Ω
        ∝

              q
              V

              m
              ω

                d

                  0

                  2

    {\displaystyle \Omega \propto {\frac {qV}{m\omega d_{0}^{2}}}}

, where

        q
        ,
        m
        ,
        V
        ,
        ω
        ,

          d

            0

    {\displaystyle q,m,V,\omega ,d_{0}}

 are the charge and mass of the ion, the peak amplitude and the frequency of the radiofrequency (rf) trapping field, and the ion-to-electrode distance respectively. Note that a larger rf frequency lowers the trapping frequency.
The ponderomotive force also plays an important role in laser induced plasmas as a major density lowering factor.
Often, however, the assumed slow-time independency of

          Φ

            P

    {\displaystyle \Phi _{P}}

 is too restrictive, an example being the
ultra-short, intense laser pulse-plasma(target) interaction. Here a new ponderomotive effect comes into play,
the ponderomotive memory effect. The result is a weakening of the ponderomotive force and the generation of wake fields and ponderomotive streamers. In this case the fast-time averaged density becomes for a Maxwellian plasma:

              n
              ¯

        (
        x
        ,
        t
        )

          n

            0

          e

            −
            Ψ

        [
        1
        +

            1

              2
              π

          ∫

            −
            ∞

            +
            ∞

        d
        v

          e

            −

              v

                2

              /

            2

        M
        (
        x
        ,
        v
        ,
        t
        )
        ]

    {\displaystyle {\bar {n}}(x,t)=n_{0}e^{-\Psi }[1+{\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{+\infty }dve^{-v^{2}/2}M(x,v,t)]}

,
where

        M
        (
        x
        ,
        v
        ,
        t
        )
        :=

          ∫

            −
            ∞

            t

        d
        τ

          ∂

            τ

        Ψ
        (
        x
        −
        v
        (
        t
        −
        τ
        )
        ,
        τ
        )

    {\displaystyle M(x,v,t):=\int _{-\infty }^{t}d\tau \partial _{\tau }\Psi (x-v(t-\tau ),\tau )}

 and

        Ψ
        (
        x
        ,
        t
        )
        :=

            e

              κ
              T

          Φ

            P

        (
        x
        ,
        t
        )

    {\displaystyle \Psi (x,t):={\frac {e}{\kappa T}}\Phi _{P}(x,t)}

.

Journals
Cary, J. R.; Kaufman, A. N. (1981). "Ponderomotive effects in collisionless plasma: A Lie transform approach". Phys. Fluids. 24 (7): 1238. Bibcode:1981PhFl...24.1238C. doi:10.1063/1.863527. OSTI 1149513. S2CID 56314589.
Grebogi, C.; Littlejohn, R. G. (1984). "Relativistic ponderomotive Hamiltonian". Phys. Fluids. 27 (8): 1996. Bibcode:1984PhFl...27.1996G. doi:10.1063/1.864855.
Morales, G. J.; Lee, Y. C. (1974). "Ponderomotive-Force Effects in a Nonuniform Plasma". Phys. Rev. Lett. 33 (17): 1016–1019. Bibcode:1974PhRvL..33.1016M. doi:10.1103/physrevlett.33.1016.
Lamb, B. M.; Morales, G. J. (1983). "Ponderomotive effects in nonneutral plasmas". Phys. Fluids. 26 (12): 3488. Bibcode:1983PhFl...26.3488L. doi:10.1063/1.864132. Archived from the original on September 23, 2017.
Shah, K.; Ramachandran, H. (2008). "Analytic, nonlinearly exact solutions for an rf confined plasma". Phys. Plasmas. 15 (6): 062303. Bibcode:2008PhPl...15f2303S. doi:10.1063/1.2926632.{{cite journal}}: CS1 maint: deprecated archival service (link)
Bucksbaum, P. H.; Freeman, R. R.; Bashkansky, M.; McIlrath, T. J. (1987). "Role of the ponderomotive potential in above-threshold ionization". Journal of the Optical Society of America B. 4 (5): 760. Bibcode:1987JOSAB...4..760B. CiteSeerX 10.1.1.205.4672. doi:10.1364/josab.4.000760. {{cite journal}}: Cite uses deprecated parameter |citeseerx= (help)
