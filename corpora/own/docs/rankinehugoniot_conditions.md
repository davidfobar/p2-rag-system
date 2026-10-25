# Rankine–Hugoniot conditions

Rankine–Hugoniot conditions

The Rankine–Hugoniot conditions, also referred to as Rankine–Hugoniot jump conditions or Rankine–Hugoniot relations, describe the relationship between the states on both sides of a shock wave or a combustion wave (deflagration or detonation) in a one-dimensional flow in fluids or a one-dimensional deformation in solids. They are named in recognition of the work carried out by Scottish engineer and physicist William John Macquorn Rankine and French engineer Pierre Henri Hugoniot.
The basic idea of the jump conditions is to consider what happens to a fluid when it undergoes a rapid change. Consider, for example, driving a piston into a tube filled with non-reacting gas. A disturbance is propagated through the fluid somewhat faster than the speed of sound. Because the disturbance propagates supersonically, it is a shock wave, and the fluid downstream of the shock has no advance information of it. In a frame of reference moving with the wave, atoms or molecules in front of the wave slam into the wave supersonically. On a microscopic level, they undergo collisions on the scale of the mean free path length until they come to rest in the post-shock flow (but moving in the frame of reference of the wave or of the tube). The bulk transfer of kinetic energy heats the post-shock flow. Because the mean free path length is assumed to be negligible in comparison to all other length scales in a hydrodynamic treatment, the shock front is essentially a hydrodynamic discontinuity. The jump conditions then establish the transition between the pre- and post-shock flow, based solely upon the conservation of mass, momentum, and energy. The conditions are correct even though the shock actually has a positive thickness. This non-reacting example of a shock wave also generalizes to reacting flows, where a combustion front (either a detonation or a deflagration) can be modeled as a discontinuity in a first approximation.

Governing equations
In a coordinate system that is moving with the discontinuity, the Rankine–Hugoniot conditions can be expressed as:

where m is the mass flow rate per unit area, ρ1 and ρ2 are the mass density of the fluid upstream and downstream of the wave, u1 and u2 are the fluid velocity upstream and downstream of the wave, p1 and p2 are the pressures in the two regions, and h1 and h2 are the specific (with the sense of per unit mass) enthalpies in the two regions. If in addition, the flow is reactive, then the species conservation equations demands that

          ω

            i
            ,
            1

          ω

            i
            ,
            2

        0
        ,

        i

        1
        ,
        2
        ,
        3
        ,
        …
        ,
        N
        ,

          Conservation of species

    {\displaystyle \omega _{i,1}=\omega _{i,2}=0,\quad i=1,2,3,\dots ,N,\qquad {\text{Conservation of species}}}

to vanish both upstream and downstream of the discontinuity. Here,

        ω

    {\displaystyle \omega }

 is the mass production rate of the i-th species of total N species involved in the reaction.
Combining conservation of mass and momentum gives us

                p

                  2

              −

                p

                  1

              1

                /

                ρ

                  2

              −
              1

                /

                ρ

                  1

        −

          m

            2

    {\displaystyle {\frac {p_{2}-p_{1}}{1/\rho _{2}-1/\rho _{1}}}=-m^{2}}

which defines a straight line known as the Michelson–Rayleigh line, named after the Russian physicist Vladimir A. Mikhelson (usually anglicized as Michelson) and Lord Rayleigh, that has a negative slope (since

          m

            2

    {\displaystyle m^{2}}

 is always positive) in the

        p
        −

          ρ

            −
            1

    {\displaystyle p-\rho ^{-1}}

 plane. Using the Rankine–Hugoniot equations for the conservation of mass and momentum to eliminate u1 and u2, the equation for the conservation of energy can be expressed as the Hugoniot equation:

          h

            2

        −

          h

            1

            1
            2

          (

                1

                  ρ

                    2

            +

                1

                  ρ

                    1

          )

        (

          p

            2

        −

          p

            1

        )
        .

    {\displaystyle h_{2}-h_{1}={\frac {1}{2}}\,\left({\frac {1}{\rho _{2}}}+{\frac {1}{\rho {1}}}\right)\,(p{2}-p_{1}).}

The inverse of the density can also be expressed as the specific volume,

        v

        1

          /

        ρ

    {\displaystyle v=1/\rho }

. Along with these, one has to specify the relation between the upstream and downstream equation of state

        f
        (

          p

            1

        ,

          ρ

            1

        ,

          T

            1

        ,

          Y

            i
            ,
            1

        )

        f
        (

          p

            2

        ,

          ρ

            2

        ,

          T

            2

        ,

          Y

            i
            ,
            2

        )

    {\displaystyle f(p_{1},\rho {1},T{1},Y_{i,1})=f(p_{2},\rho {2},T{2},Y_{i,2})}

where

          Y

            i

    {\displaystyle Y_{i}}

 is the mass fraction of the species. Finally, the calorific equation of state

        h

        h
        (
        p
        ,
        ρ
        ,

          Y

            i

        )

    {\displaystyle h=h(p,\rho ,Y_{i})}

 is assumed to be known, i.e.,

        h
        (

          p

            1

        ,

          ρ

            1

        ,

          Y

            i
            ,
            1

        )

        h
        (

          p

            2

        ,

          ρ

            2

        ,

          Y

            i
            ,
            2

        )
        .

    {\displaystyle h(p_{1},\rho {1},Y{i,1})=h(p_{2},\rho {2},Y{i,2}).}

Simplified Rankine–Hugoniot relations
Source:

The following assumptions are made in order to simplify the Rankine–Hugoniot equations. The mixture is assumed to obey the ideal gas law, so that relation between the downstream and upstream equation of state can be written as

              p

                2

                ρ

                  2

                T

                  2

              p

                1

                ρ

                  1

                T

                  1

            R

              W
              ¯

    {\displaystyle {\frac {p_{2}}{\rho {2}T{2}}}={\frac {p_{1}}{\rho {1}T{1}}}={\frac {R}{\overline {W}}}}

where

        R

    {\displaystyle R}

 is the universal gas constant and the mean molecular weight

            W
            ¯

    {\displaystyle {\overline {W}}}

 is assumed to be constant (otherwise,

            W
            ¯

    {\displaystyle {\overline {W}}}

 would depend on the mass fraction of the all species). If one assumes that the specific heat at constant pressure

          c

            p

    {\displaystyle c_{p}}

 is also constant across the wave, the change in enthalpies (calorific equation of state) can be simply written as

          h

            2

        −

          h

            1

        −
        q
        +

          c

            p

        (

          T

            2

        −

          T

            1

        )

    {\displaystyle h_{2}-h_{1}=-q+c_{p}(T_{2}-T_{1})}

where the first term in the above expression represents the amount of heat released per unit mass of the upstream mixture by the wave and the second term represents the sensible heating. Eliminating temperature using the equation of state and substituting the above expression for the change in enthalpies into the Hugoniot equation, one obtains an Hugoniot equation expressed only in terms of pressure and densities,

          (

              γ

                γ
                −
                1

          )

          (

                  p

                    2

                  ρ

                    2

            −

                  p

                    1

                  ρ

                    1

          )

        −

            1
            2

          (

                1

                  ρ

                    2

            +

                1

                  ρ

                    1

          )

        (

          p

            2

        −

          p

            1

        )

        q
        ,

    {\displaystyle \left({\frac {\gamma }{\gamma -1}}\right)\left({\frac {p_{2}}{\rho {2}}}-{\frac {p{1}}{\rho _{1}}}\right)-{\frac {1}{2}}\left({\frac {1}{\rho _{2}}}+{\frac {1}{\rho {1}}}\right)(p{2}-p_{1})=q,}

where

        γ

    {\displaystyle \gamma }

 is the specific heat ratio, which for ordinary room temperature air (T = 298 K) = 1.40. An Hugoniot curve without heat release (

        q

        0

    {\displaystyle q=0}

) is often called a "shock Hugoniot", or simply a(n) "Hugoniot". Along with the Rayleigh line equation, the above equation completely determines the state of the system. These two equations can be written compactly by introducing the following non-dimensional scales,

              p
              ~

              p

                2

              p

                1

        ,

              v
              ~

              ρ

                1

              ρ

                2

        ,

        α

              q

                ρ

                  1

              p

                1

        ,

        μ

              m

                2

                p

                  1

                ρ

                  1

        .

    {\displaystyle {\tilde {p}}={\frac {p_{2}}{p_{1}}},\quad {\tilde {v}}={\frac {\rho _{1}}{\rho _{2}}},\quad \alpha ={\frac {q\rho {1}}{p{1}}},\quad \mu ={\frac {m^{2}}{p_{1}\rho _{1}}}.}

The Rayleigh line equation and the Hugoniot equation then simplifies to

                            p
                            ~

                      −
                      1

                            v
                            ~

                      −
                      1

                −
                μ

                      p
                      ~

                      [
                      2
                      α
                      +
                      (
                      γ
                      +
                      1
                      )

                        /

                      (
                      γ
                      −
                      1
                      )
                      ]
                      −

                            v
                            ~

                      [
                      (
                      γ
                      +
                      1
                      )

                        /

                      (
                      γ
                      −
                      1
                      )
                      ]

                            v
                            ~

                      −
                      1

                .

    {\displaystyle {\begin{aligned}{\frac {{\tilde {p}}-1}{{\tilde {v}}-1}}&=-\mu \{\tilde {p}}&={\frac {[2\alpha +(\gamma +1)/(\gamma -1)]-{\tilde {v}}}{[(\gamma +1)/(\gamma -1)]{\tilde {v}}-1}}.\end{aligned}}}

Given the upstream conditions, the intersection of above two equations in the

              v
              ~

    {\displaystyle {\tilde {v}}}

-

              p
              ~

    {\displaystyle {\tilde {p}}}

 plane determine the downstream conditions; in the

              v
              ~

    {\displaystyle {\tilde {v}}}

-

              p
              ~

    {\displaystyle {\tilde {p}}}

 plane, the upstream condition correspond to the point

        (

              v
              ~

        ,

              p
              ~

        )

        (
        1
        ,
        1
        )

    {\displaystyle ({\tilde {v}},{\tilde {p}})=(1,1)}

. If no heat release occurs, for example, shock waves without chemical reaction, then

        α

        0

    {\displaystyle \alpha =0}

. The Hugoniot curves asymptote to the lines

              v
              ~

        (
        γ
        −
        1
        )

          /

        (
        γ
        +
        1
        )

    {\displaystyle {\tilde {v}}=(\gamma -1)/(\gamma +1)}

 and

              p
              ~

        −
        (
        γ
        −
        1
        )

          /

        (
        γ
        +
        1
        )

    {\displaystyle {\tilde {p}}=-(\gamma -1)/(\gamma +1)}

, which are depicted as dashed lines in the figure. As mentioned in the figure, only the white region bounded by these two asymptotes are allowed so that

        μ

    {\displaystyle \mu }

 is positive. Shock waves and detonations correspond to the top-left white region wherein

              p
              ~

        1

    {\displaystyle {\tilde {p}}>1}

 and

              v
              ~

        <
        1

    {\displaystyle {\tilde {v}}<1}

, that is to say, the pressure increases and the specific volume decreases across the wave (the Chapman–Jouguet condition for detonation is where Rayleigh line is tangent to the Hugoniot curve). Deflagrations, on the other hand, correspond to the bottom-right white region wherein

              p
              ~

        <
        1

    {\displaystyle {\tilde {p}}<1}

 and

              v
              ~

        1

    {\displaystyle {\tilde {v}}>1}

, that is to say, the pressure decreases and the specific volume increases across the wave; the pressure decrease a flame is typically very small which is seldom considered when studying deflagrations.
For shock waves and detonations, the pressure increase across the wave can take any values between

        0
        ≤

              p
              ~

        <
        ∞

    {\displaystyle 0\leq {\tilde {p}}<\infty }

; the steeper the slope of the Rayleigh line, the stronger is the wave. On the contrary, here the specific volume ratio is restricted to the finite interval

        (
        γ
        −
        1
        )

          /

        (
        γ
        +
        1
        )
        ≤

              v
              ~

        ≤
        2
        α
        +
        (
        γ
        +
        1
        )

          /

        (
        γ
        −
        1
        )

    {\displaystyle (\gamma -1)/(\gamma +1)\leq {\tilde {v}}\leq 2\alpha +(\gamma +1)/(\gamma -1)}

 (the upper bound is derived for the case

              p
              ~

        →
        0

    {\displaystyle {\tilde {p}}\rightarrow 0}

 because pressure cannot take negative values). If

        γ

        1.4

    {\displaystyle \gamma =1.4}

 (diatomic gas without the vibrational mode excitation), the interval is

        1

          /

        6
        ≤

              v
              ~

        ≤
        2
        α
        +
        6

    {\displaystyle 1/6\leq {\tilde {v}}\leq 2\alpha +6}

, in other words, the shock wave can increase the density at most by a factor of 6. For monatomic gas,

        γ

        5

          /

        3

    {\displaystyle \gamma =5/3}

, the allowed interval is

        1

          /

        4
        ≤

              v
              ~

        ≤
        2
        α
        +
        4

    {\displaystyle 1/4\leq {\tilde {v}}\leq 2\alpha +4}

. For diatomic gases with vibrational mode excited, we have

        γ

        9

          /

        7

    {\displaystyle \gamma =9/7}

 leading to the interval

        1

          /

        8
        ≤

              v
              ~

        ≤
        2
        α
        +
        8

    {\displaystyle 1/8\leq {\tilde {v}}\leq 2\alpha +8}

. In reality, the specific heat ratio is not constant in the shock wave due to molecular dissociation and ionization, but even in these cases, density ratio in general do not exceed a factor of about 11–13.

Derivation from Euler equations
Consider gas in a one-dimensional container (e.g., a long thin tube). Assume that the fluid is inviscid (i.e., it shows no viscosity effects as for example friction with the tube walls). Furthermore, assume that there is no heat transfer by conduction or radiation and that gravitational acceleration can be neglected. Such a system can be described by the following system of conservation laws, known as the 1D Euler equations, that in conservation form is:

where

        ρ
        ,

    {\displaystyle \rho ,}

 fluid mass density,

        u
        ,

    {\displaystyle u,}

 fluid velocity,

        e
        ,

    {\displaystyle e,}

 specific internal energy of the fluid,

        p
        ,

    {\displaystyle p,}

 fluid pressure, and

          E

            t

        ρ
        e
        +
        ρ

              1
              2

          u

            2

        ,

    {\displaystyle E^{t}=\rho e+\rho {\tfrac {1}{2}}u^{2},}

 is the total energy density of the fluid, [J/m3], while e is its specific internal energy
Assume further that the gas is calorically ideal and that therefore a polytropic equation-of-state of the simple form

is valid, where

        γ

    {\displaystyle \gamma }

 is the constant ratio of specific heats

          c

            p

          /

          c

            v

    {\displaystyle c_{p}/c_{v}}

. This quantity also appears as the polytropic exponent of the polytropic process described by

For an extensive list of compressible flow equations, etc., refer to NACA Report 1135 (1953).
Note: For a calorically ideal gas

        γ

    {\displaystyle \gamma }

 is a constant and for a thermally ideal gas

        γ

    {\displaystyle \gamma }

 is a function of temperature. In the latter case, the dependence of pressure on mass density and internal energy might differ from that given by equation (4).

The jump condition
Before proceeding further it is necessary to introduce the concept of a jump condition – a condition that holds at a discontinuity or abrupt change.
Consider a 1D situation where there is a jump in the scalar conserved physical quantity

        w

    {\displaystyle w}

, which is governed by integral conservation law

for any

          x

            1

    {\displaystyle x_{1}}

,

          x

            2

    {\displaystyle x_{2}}

,

          x

            1

        <

          x

            2

    {\displaystyle x_{1}<x_{2}}

, and, therefore, by partial differential equation

for smooth solutions.
Let the solution exhibit a jump (or shock) at

        x

          x

            s

        (
        t
        )

    {\displaystyle x=x_{s}(t)}

, where

          x

            1

        <

          x

            s

        (
        t
        )

    {\displaystyle x_{1}<x_{s}(t)}

 and

          x

            s

        (
        t
        )
        <

          x

            2

    {\displaystyle x_{s}(t)<x_{2}}

, then

The subscripts 1 and 2 indicate conditions just upstream and just downstream of the jump respectively, i.e.

          w

            1

          lim

            ϵ
            →

              0

                +

        w

          (

              x

                s

            −
            ϵ

          )

    {\textstyle w_{1}=\lim {\epsilon \to 0^{+}}w\left(x{s}-\epsilon \right)}

 and

          w

            2

          lim

            ϵ
            →

              0

                +

        w

          (

              x

                s

            +
            ϵ

          )

    {\textstyle w_{2}=\lim {\epsilon \to 0^{+}}w\left(x{s}+\epsilon \right)}

.

        ∴

    {\displaystyle \therefore }

 is the therefore sign.
Note, to arrive at equation (8) we have used the fact that

        d

          x

            1

          /

        d
        t

        0

    {\displaystyle dx_{1}/dt=0}

 and

        d

          x

            2

          /

        d
        t

        0

    {\displaystyle dx_{2}/dt=0}

.
Now, let

          x

            1

        →

          x

            s

        (
        t
        )
        −
        ϵ

    {\displaystyle x_{1}\to x_{s}(t)-\epsilon }

 and

          x

            2

        →

          x

            s

        (
        t
        )
        +
        ϵ

    {\displaystyle x_{2}\to x_{s}(t)+\epsilon }

, when we have

          ∫

              x

                1

              x

                s

            (
            t
            )
            −
            ϵ

          w

            t

        d
        x
        →
        0

    {\textstyle \int {x{1}}^{x_{s}(t)-\epsilon }w_{t}\,dx\to 0}

 and

          ∫

              x

                s

            (
            t
            )
            +
            ϵ

              x

                2

          w

            t

        d
        x
        →
        0

    {\textstyle \int {x{s}(t)+\epsilon }^{x_{2}}w_{t}\,dx\to 0}

, and in the limit

where we have defined

          u

            s

        d

          x

            s

        (
        t
        )

          /

        d
        t

    {\displaystyle u_{s}=dx_{s}(t)/dt}

 (the system characteristic or shock speed), which by simple division is given by

Equation (9) represents the jump condition for conservation law (6). A shock situation arises in a system where its characteristics intersect, and under these conditions a requirement for a unique single-valued solution is that the solution should satisfy the admissibility condition or entropy condition. For physically real applications this means that the solution should satisfy the Lax entropy condition

where

          f
          ′

          (

            w

              1

          )

    {\displaystyle f'\left(w_{1}\right)}

 and

          f
          ′

          (

            w

              2

          )

    {\displaystyle f'\left(w_{2}\right)}

 represent characteristic speeds at upstream and downstream conditions respectively.

Shock condition
In the case of the hyperbolic conservation law (6), we have seen that the shock speed can be obtained by simple division. However, for the 1D Euler equations (1), (2) and (3), we have the vector state variable

              [

                    ρ

                    ρ
                    u

                    E

              ]

              T

    {\displaystyle {\begin{bmatrix}\rho &\rho u&E\end{bmatrix}}^{\mathsf {T}}}

 and the jump conditions become

Equations (12), (13) and (14) are known as the Rankine–Hugoniot conditions for the Euler equations and are derived by enforcing the conservation laws in integral form over a control volume that includes the shock. For this situation

          u

            s

    {\displaystyle u_{s}}

 cannot be obtained by simple division. However, it can be shown by transforming the problem to a moving co-ordinate system
(setting

          u

            s

          ′

        :=

          u

            s

        −

          u

            1

    {\displaystyle u_{s}':=u_{s}-u_{1}}

,

          u

            1

          ′

        :=
        0

    {\displaystyle u'_{1}:=0}

,

          u

            2

          ′

        :=

          u

            2

        −

          u

            1

    {\displaystyle u'{2}:=u{2}-u_{1}}

 to remove

          u

            1

    {\displaystyle u_{1}}

) and some algebraic manipulation (involving the elimination of

          u

            2

          ′

    {\displaystyle u'_{2}}

 from the transformed equation (13) using the transformed equation (12)), that the shock speed is given by

where

          c

            1

            γ

              p

                1

              /

              ρ

                1

    {\textstyle c_{1}={\sqrt {\gamma p_{1}/\rho _{1}}}}

 is the speed of sound in the fluid at upstream conditions.

Shock Hugoniot and Rayleigh line in solids

For shocks in solids, a closed form expression such as equation (15) cannot be derived from first principles. Instead, experimental observations indicate that a linear relation can be used instead (called the shock Hugoniot in the us-up plane) that has the form

where c0 is the bulk speed of sound in the material (in uniaxial compression), s is a parameter (the slope of the shock Hugoniot) obtained from fits to experimental data, and up = u2 is the particle velocity inside the compressed region behind the shock front.

The above relation, when combined with the Hugoniot equations for the conservation of mass and momentum, can be used to determine the shock Hugoniot in the p-v plane, where v is the specific volume (per unit mass):

Alternative equations of state, such as the Mie–Grüneisen equation of state may also be used instead of the above equation.
The shock Hugoniot describes the locus of all possible thermodynamic states a material can exist in behind a shock, projected onto a two dimensional state-state plane. It is therefore a set of equilibrium states and does not specifically represent the path through which a material undergoes transformation.
Weak shocks are isentropic and that the isentrope represents the path through which the material is loaded from the initial to final states by a compression wave with converging characteristics. In the case of weak shocks, the Hugoniot will therefore fall directly on the isentrope and can be used directly as the equivalent path. In the case of a strong shock we can no longer make that simplification directly. However, for engineering calculations, it is deemed that the isentrope is close enough to the Hugoniot that the same assumption can be made.
If the Hugoniot is approximately the loading path between states for an "equivalent" compression wave, then the jump conditions for the shock loading path can be determined by drawing a straight line between the initial and final states. This line is called the Rayleigh line and has the following equation:

Hugoniot elastic limit
Most solid materials undergo plastic deformations when subjected to strong shocks. The point on the shock Hugoniot at which a material transitions from a purely elastic state to an elastic-plastic state is called the Hugoniot elastic limit (HEL) and the pressure at which this transition takes place is denoted pHEL. Values of pHEL can range from 0.2 GPa to 20 GPa. Above the HEL, the material loses much of its shear strength and starts behaving like a fluid.

Magnetohydrodynamics

Rankine–Hugoniot conditions in magnetohydrodynamics are interesting to consider since they are very relevant to astrophysical applications. Across the discontinuity the normal component

          H

            n

    {\displaystyle H_{n}}

 of the magnetic field

          H

    {\displaystyle \mathbf {H} }

 and the tangential component

            E

            t

    {\displaystyle \mathbf {E} _{t}}

 of the electric field

          E

        −

          u

        ×

          H

          /

        c

    {\displaystyle \mathbf {E} =-\mathbf {u} \times \mathbf {H} /c}

 (infinite conductivity limit) must be continuous. We thus have

where

        j
        ≡
        ρ

          u

            n

    {\displaystyle j\equiv \rho u_{n}}

 and

        [

        [
        ⋅
        ]

        ]

    {\displaystyle [![\cdot ]!]}

 is the difference between the values of any physical quantity on the two sides of the discontinuity. The remaining conditions are given by

These conditions are general in the sense that they include contact discontinuities (

        j

        0
        ,

          H

            n

        ≠
        0

    {\displaystyle j=0,\,H_{n}\neq 0}

,

        [

        [

          u

        ]

        ]

        [

        [
        p
        ]

        ]

        [

        [

          H

        ]

        ]

        0

    {\displaystyle [![\mathbf {u} ]!]=[![p]!]=[![\mathbf {H} ]!]=0}

,

        [

        [
        ρ
        ]

        ]
        ≠
        0

    {\displaystyle [![\rho ]!]\neq 0}

) tangential discontinuities (

        j

          H

            n

        0

    {\displaystyle j=H_{n}=0}

,

        [

        [

            u

            t

        ρ
        ]

        ]
        ≠
        0

    {\displaystyle [![\mathbf {u} _{t}\rho ]!]\neq 0}

,

        [

        [

            H

            t

        ]

        ]
        ≠
        0

    {\displaystyle [![\mathbf {H} _{t}]!]\neq 0}

,

        [

        [
        ρ
        ]

        ]
        ≠
        0

    {\displaystyle [![\rho ]!]\neq 0}

), rotational or Alfvén discontinuities (

        j

          H

            n

            ρ

              /

            4
            π

        ≠
        0

    {\textstyle j=H_{n}{\sqrt {\rho /4\pi }}\neq 0}

,

        [

        [
        ρ
        ]

        ]

        [

        [

          u

            n

        ]

        ]

        [

        [
        p
        ]

        ]

        [

        [

            H

            t

        ]

        ]

        0

    {\displaystyle [![\rho ]!]=[![u_{n}]!]=[![p]!]=[![\mathbf {H} _{t}]!]=0}

) and shock waves (

        j
        ≠
        0

    {\displaystyle j\neq 0}

,

        [

        [
        ρ
        ]

        ]
        ≠
        0

    {\displaystyle [![\rho ]!]\neq 0}

).
