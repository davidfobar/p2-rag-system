# Virial stress

Virial stress

In mechanics, virial stress is a measure of stress on an atomic scale for homogeneous systems. The name is derived from Latin vis 'force': "Virial is then derived from Latin as well, stemming from the word virias (plural of vis) meaning forces." The expression of the (local) virial stress can be derived as the functional derivative of the free energy of a molecular system with respect to the deformation tensor.

Volume averaged Definition
The instantaneous volume averaged virial stress is given by

          τ

            i
            j

            1
            Ω

          ∑

            k
            ∈
            Ω

          [

            −

              m

                (
                k
                )

              (

                  u

                    i

                    (
                    k
                    )

                −

                        u
                        ¯

                    i

              )

              (

                  u

                    j

                    (
                    k
                    )

                −

                        u
                        ¯

                    j

              )

            +

                1
                2

              ∑

                ℓ
                ∈
                Ω

              (

                  x

                    i

                    (
                    ℓ
                    )

                −

                  x

                    i

                    (
                    k
                    )

              )

              f

                j

                (
                k
                ℓ
                )

          ]

    {\displaystyle \tau _{ij}={\frac {1}{\Omega }}\sum {k\in \Omega }\left[-m^{(k)}\left(u{i}^{(k)}-{\bar {u}}{i}\right)\left(u{j}^{(k)}-{\bar {u}}_{j}\right)+{\frac {1}{2}}\sum {\ell \in \Omega }\left(x{i}^{(\ell )}-x_{i}^{(k)}\right)f_{j}^{(k\ell )}\right]}

where

        k

    {\displaystyle k}

 and

        ℓ

    {\displaystyle \ell }

 are atoms in the domain,

        Ω

    {\displaystyle \Omega }

 is the volume of the domain,

          m

            (
            k
            )

    {\displaystyle m^{(k)}}

 is the mass of atom k,

          u

            i

            (
            k
            )

    {\displaystyle u_{i}^{(k)}}

 is the i-th component of the velocity of atom k,

                u
                ¯

            j

    {\displaystyle {\bar {u}}_{j}}

 is the j-th component of the average velocity of atoms in the volume,

          x

            i

            (
            k
            )

    {\displaystyle x_{i}^{(k)}}

 is the i-th component of the position of atom k, and

          f

            i

            (
            k
            ℓ
            )

    {\displaystyle f_{i}^{(k\ell )}}

 is the i-th component of the force applied on atom k by atom ℓ.
At zero kelvin, all velocities are zero so we have

          τ

            i
            j

            1

              2
              Ω

          ∑

            k
            ,
            ℓ
            ∈
            Ω

          (

              x

                i

                (
                ℓ
                )

            −

              x

                i

                (
                k
                )

          )

          f

            j

            (
            k
            ℓ
            )

    {\displaystyle \tau _{ij}={\frac {1}{2\Omega }}\sum {k,\ell \in \Omega }\left(x{i}^{(\ell )}-x_{i}^{(k)}\right)f_{j}^{(k\ell )}}

This can be thought of as follows. The τ11 component of stress is the force in the x1-direction divided by the area of a plane perpendicular to that direction. Consider two adjacent volumes separated by such a plane. The 11-component of stress on that interface is the sum of all pairwise forces between atoms on the two sides.
The volume averaged virial stress is then the ensemble average of the instantaneous volume averaged virial stress.
In a three dimensional, isotropic system, at equilibrium the "instantaneous" atomic pressure is usually defined as the average over the diagonals of the negative stress tensor:

              P

            a
            t

        −

            1
            3

        T
        r
        (
        τ
        )
        .

    {\displaystyle {\mathcal {P}}_{at}=-{\frac {1}{3}}Tr(\tau ).}

The pressure then is the ensemble average of the instantaneous pressure

          P

            a
            t

        ⟨

              P

            a
            t

        ⟩
        .

    {\displaystyle P_{at}=\langle {\mathcal {P}}_{at}\rangle .}

This pressure is the average pressure in the volume Ω.

Equivalent Definition
It's worth noting that some articles and textbook use a slightly different but equivalent version of the equation

          τ

            i
            j

            1
            Ω

          ∑

            k
            ∈
            Ω

          [

            −

              m

                (
                k
                )

              (

                  u

                    i

                    (
                    k
                    )

                −

                        u
                        ¯

                    i

              )

              (

                  u

                    j

                    (
                    k
                    )

                −

                        u
                        ¯

                    j

              )

            −

                1
                2

              ∑

                ℓ
                ∈
                Ω

              x

                i

                (
                k
                ℓ
                )

              f

                j

                (
                k
                ℓ
                )

          ]

    {\displaystyle \tau _{ij}={\frac {1}{\Omega }}\sum {k\in \Omega }\left[-m^{(k)}\left(u{i}^{(k)}-{\bar {u}}{i}\right)\left(u{j}^{(k)}-{\bar {u}}_{j}\right)-{\frac {1}{2}}\sum {\ell \in \Omega }x{i}^{(k\ell )}f_{j}^{(k\ell )}\right]}

where

          x

            i

            (
            k
            ℓ
            )

    {\displaystyle x_{i}^{(k\ell )}}

 is the i-th component of the vector oriented from the ℓ-th atoms to the k-th calculated via the difference

          x

            i

            k
            ℓ

          x

            i

            (
            k
            )

        −

          x

            i

            (
            ℓ
            )

    {\displaystyle x_{i}^{k\ell }=x_{i}^{(k)}-x_{i}^{(\ell )}}

Both equation being strictly equivalent, the definition of the vector can still lead to confusion.

Derivation
The virial pressure can be derived, using the virial theorem and splitting forces between particles and the container or, alternatively, via direct application of the defining equation

        P

        −

                ∂
                F
                (
                N
                ,
                V
                ,
                T
                )

                ∂
                V

    {\displaystyle P=-{\tfrac {\partial F(N,V,T)}{\partial V}}}

 and using scaled coordinates in the calculation.

Inhomogeneous Systems
If the system is not homogeneous in a given volume the above (volume averaged) pressure is not a good measure for the pressure. In inhomogeneous systems the pressure depends on the position and orientation of the surface on which the pressure acts. Therefore, in inhomogeneous systems a definition of a local pressure is needed. As a general example for a system with inhomogeneous pressure you can think of the pressure in the atmosphere of the earth which varies with height.

Instantaneous local virial stress
The (local) instantaneous virial stress is given by:

          τ

            a
            b

        (

              r
              →

        )

        −

          ∑

            i

            1

            N

        δ

          (

                  r
                  →

            −

                    r
                    →

                (
                i
                )

          )

          [

              m

                (
                i
                )

              u

                a

                (
                i
                )

              u

                b

                (
                i
                )

            +

                1
                2

              ∑

                j

                1
                ,
                j
                ≠
                i

                N

                (

                          r
                          →

                      (
                      i
                      )

                  −

                          r
                          →

                      (
                      j
                      )

                )

                a

                    f
                    →

                b

                (
                i
                j
                )

          ]

        ,

    {\displaystyle \tau _{ab}({\vec {r}})=-\sum {i=1}^{N}\delta \left({\vec {r}}-{\vec {r}}^{(i)}\right)\left[m^{(i)}u{a}^{(i)}u_{b}^{(i)}+{\frac {1}{2}}\sum {j=1,j\neq i}^{N}\left({\vec {r}}^{(i)}-{\vec {r}}^{(j)}\right){a}{\vec {f}}_{b}^{(ij)}\right],}

Measuring the virial pressure in molecular simulations
The virial pressure can be measured via the formulas above or using volume rescaling trial moves.

Virial pressure in active matter
The virial pressure in active matter is an extension of the classical virial pressure of equilibrium statistical mechanics to systems composed of self-propelled particles. In active systems, pressure contains an additional contribution originating from persistent self-propulsion, commonly referred to as the swim pressure or active pressure. For active Brownian particles (ABPs), the total pressure can be separated into contributions from thermal fluctuations, interparticle interactions, and the active motion of particles. The swim pressure arises from the continuous propulsion of active particles and represents the mechanical stress generated by their self-driven motion. Unlike equilibrium fluids, the pressure of generic active systems can depend on the nature of particle–wall interactions and confinement geometry; therefore, a universal equation of state does not generally exist for active matter. However, for specific systems such as spherical ABPs without aligning interactions, a well-defined bulk pressure and equation of state can be obtained.
The global pressure of an active system represents the spatially averaged mechanical stress and is commonly obtained using virial approaches or momentum transport arguments. In contrast, local pressure describes the spatial variation of stress inside the system and provides information about inhomogeneous regions such as interfaces, boundaries, and density gradients. Studies of local stress in active Brownian systems have shown that, for spherical ABPs, the local bulk stress can correspond to the mechanical pressure measured at confining walls, supporting the existence of an equation of state. However, the active contribution to the global pressure, particularly the swim pressure, does not always directly correspond to the local stress tensor. This difference becomes important in confined, inhomogeneous, or anisotropic active systems where particle orientation and boundary-induced polarization influence stress transmission.
In active systems with translational and rotational inertia, the virial stress contains contributions from translational motion, rotational motion, interparticle forces, and active propulsion forces. The translational inertial contribution arises from particle momentum, while rotational inertia introduces an additional stress contribution associated with angular motion. The interaction contribution originates from forces between particles, and the active contribution is generated by self-propulsion. These terms together describe the mechanical stress carried by inertial active particles and generalize the stress description of active Brownian systems.
In the overdamped limit, where translational and rotational inertia are neglected, the inertial contributions disappear and the stress reduces to the commonly used active Brownian particle pressure formulations. Studies of active Brownian particles with translational and rotational inertia have shown that the swim stress obtained from the global virial expression does not necessarily represent the local stress tensor, demonstrating that global pressure and local stress can have different physical interpretations in inertial active matter systems.
