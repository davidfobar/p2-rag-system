# Rotational Brownian motion (astronomy)

Rotational Brownian motion (astronomy)

In astronomy, rotational Brownian motion is the random walk in orientation of a binary star's orbital plane, induced by gravitational perturbations from passing stars.

Theory
Consider a binary that consists of two massive objects (stars, black holes etc.) and that is embedded in a stellar system containing a large number of stars. Let

          M

            1

    {\displaystyle M_{1}}

 and

          M

            2

    {\displaystyle M_{2}}

 be the masses of the two components of the binary whose total mass is

          M

            12

          M

            1

        +

          M

            2

    {\displaystyle M_{12}=M_{1}+M_{2}}

. A field star that approaches the binary with impact parameter

        p

    {\displaystyle p}

 and velocity

        V

    {\displaystyle V}

 passes a distance

          r

            p

    {\displaystyle r_{p}}

 from the binary, where

          p

            2

          r

            p

            2

          (

            1
            +
            2
            G

              M

                12

              /

              V

                2

              r

                p

          )

        ≈
        2
        G

          M

            12

          r

            p

          /

          V

            2

        ;

    {\displaystyle p^{2}=r_{p}^{2}\left(1+2GM_{12}/V^{2}r_{p}\right)\approx 2GM_{12}r_{p}/V^{2};}

the latter expression is valid in the limit that gravitational focusing dominates the encounter rate. The rate of encounters with stars that interact strongly with the binary, i.e. that satisfy

          r

            p

        <
        a

    {\displaystyle r_{p}<a}

, is approximately

        n
        π

          p

            2

        σ

        2
        π
        G

          M

            12

        n
        a

          /

        σ

    {\displaystyle n\pi p^{2}\sigma =2\pi GM_{12}na/\sigma }

 where

        n

    {\displaystyle n}

 and

        σ

    {\displaystyle \sigma }

 are the number density and velocity dispersion of the field stars and

        a

    {\displaystyle a}

 is the semi-major axis of the binary.
As it passes near the binary, the field star experiences a change in velocity of order

        Δ
        V
        ≈

          V

              b
              i
              n

            G

              M

                12

              /

            a

    {\displaystyle \Delta V\approx V_{\rm {bin}}={\sqrt {GM_{12}/a}}}

,
where

          V

              b
              i
              n

    {\displaystyle V_{\rm {bin}}}

 is the relative velocity of the two stars in the binary.
The change in the field star's specific angular momentum with respect to the binary,

        l

    {\displaystyle l}

, is then Δl ≈ a Vbin. Conservation of angular momentum implies that the binary's angular momentum changes by Δlbin ≈ -(m/μ12)Δl where m is the mass of a field star and μ12 is the binary reduced mass. Changes in the magnitude of lbin correspond to changes in the binary's orbital eccentricity via the relation e = 1 - lb2/GM12μ12a. Changes in the direction of lbin correspond to changes in the orientation of the binary, leading to rotational diffusion. The rotational diffusion coefficient is

        ⟨
        Δ

          ξ

            2

        ⟩

        ⟨
        Δ

          l

              b
              i
              n

            2

        ⟩

          /

          l

              b
              i
              n

            2

        ≈

            (

                m

                  M

                    12

            )

            2

        ⟨
        Δ

          l

            2

        ⟩

          /

        G

          M

            12

        a
        ≈

            m

              M

                12

              G
              ρ
              a

            σ

    {\displaystyle \langle \Delta \xi ^{2}\rangle =\langle \Delta l_{\rm {bin}}^{2}\rangle /l_{\rm {bin}}^{2}\approx \left({m \over M_{12}}\right)^{2}\langle \Delta l^{2}\rangle /GM_{12}a\approx {m \over M_{12}}{G\rho a \over \sigma }}

where ρ = mn is the mass density of field stars.
Let F(θ,t) be the probability that the rotation axis of the binary is oriented at angle θ at time t. The evolution equation for F is

              ∂
              F

              ∂
              t

            1

              sin
              ⁡
              θ

            ∂

              ∂
              θ

          (

            sin
            ⁡
            θ

                  ⟨
                  Δ

                    ξ

                      2

                  ⟩

                4

                  ∂
                  F

                  ∂
                  θ

          )

        .

    {\displaystyle {\partial F \over \partial t}={1 \over \sin \theta }{\partial \over \partial \theta }\left(\sin \theta {\langle \Delta \xi ^{2}\rangle \over 4}{\partial F \over \partial \theta }\right).}

If <Δξ2>, a, ρ and σ are constant in time, this becomes

              ∂
              F

              ∂
              τ

            1
            2

            ∂

              ∂
              μ

          [

            (
            1
            −

              μ

                2

            )

                  ∂
                  F

                  ∂
                  μ

          ]

    {\displaystyle {\partial F \over \partial \tau }={1 \over 2}{\partial \over \partial \mu }\left[(1-\mu ^{2}){\partial F \over \partial \mu }\right]}

where μ = cos θ and τ is the time in units of the relaxation time trel, where

          t

              r
              e
              l

        ≈

              M

                12

            m

            σ

              G
              ρ
              a

        .

    {\displaystyle t_{\rm {rel}}\approx {M_{12} \over m}{\sigma \over G\rho a}.}

The solution to this equation states that the expectation value of μ decays with time as

            μ
            ¯

              μ
              ¯

            0

          e

            −
            τ

        .

    {\displaystyle {\overline {\mu }}={\overline {\mu }}_{0}e^{-\tau }.}

Hence, trel is the time constant for the binary's orientation to be randomized by torques from field stars.

Applications
Rotational Brownian motion was first discussed in the context of binary supermassive black holes at the centers of galaxies. Perturbations from passing stars can alter the orbital plane of such a binary, which in turn alters the direction of the spin axis of the single black hole that forms when the two coalesce.
Rotational Brownian motion is often observed in N-body simulations of galaxies containing binary black holes. The massive binary sinks to the center of the galaxy via dynamical friction where it interacts with passing stars. The same gravitational perturbations that induce a random walk in the orientation of the binary, also cause the binary to shrink, via the gravitational slingshot. It can be shown that the rms change in the binary's orientation, from the time the binary forms until the two black holes collide, is roughly

        δ
        θ
        ≈

            20
            m

              /

              M

                12

        .

    {\displaystyle \delta \theta \approx {\sqrt {20m/M_{12}}}.}

In a real galaxy, the two black holes would eventually coalesce due to emission of gravitational waves. The spin axis of the coalesced hole will be aligned with the angular momentum axis of the orbit of the pre-existing binary. Hence, a mechanism like rotational Brownian motion that affects the orbits of binary black holes can also affect the distribution of black hole spins. This may explain in part why the spin axes of supermassive black holes appear to be randomly aligned with respect to their host galaxies.
