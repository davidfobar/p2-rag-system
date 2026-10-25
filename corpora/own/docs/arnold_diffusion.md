# Arnold diffusion

Arnold diffusion

In applied mathematics, Arnold diffusion is the phenomenon of instability of nearly-integrable Hamiltonian systems. The phenomenon is named after Vladimir Arnold who was the first to publish a result in the field in 1964. More precisely, Arnold diffusion refers to results asserting the existence of solutions to nearly-integrable Hamiltonian systems that exhibit a significant change in the action variables.
Arnold diffusion describes the diffusion of trajectories due to the ergodic theorem in a portion of phase space unbound by any constraints (i.e. unbounded by Lagrangian tori arising from constants of motion) in Hamiltonian systems. It occurs in systems with more than N=2 degrees of freedom, since the N-dimensional invariant tori do not separate the 2N-1 dimensional phase space any more. Thus, an arbitrarily small perturbation may cause a number of trajectories to wander pseudo-randomly through the whole portion of phase space left by the destroyed tori.

Background and statement
For integrable systems, one has the conservation of the action variables. According to the KAM theorem if we perturb an integrable system slightly, then many, though certainly not all, of the solutions of the perturbed system stay close, for all time, to the unperturbed system. In particular, since the action variables were originally conserved, the theorem tells us that there is only a small change in action for many solutions of the perturbed system.
However, as first noted in Arnold's paper, there are nearly integrable systems for which there exist solutions that exhibit arbitrarily large growth in the action variables. More precisely, Arnold considered the example of nearly integrable Hamiltonian system with Hamiltonian

        H
        (
        I
        ,
        ϕ
        ,
        p
        ,
        q
        ,
        t
        )

            1
            2

          I

            2

        +

            1
            2

          p

            2

        +
        ϵ
        (
        cos
        ⁡

          q

        −
        1
        )
        +
        μ
        (
        cos
        ⁡

          q

        −
        1
        )
        (
        sin
        ⁡

          ϕ
          +
          cos
          ⁡
          t
          )

    {\displaystyle H(I,\phi ,p,q,t)={1 \over 2}I^{2}+{1 \over 2}p^{2}+\epsilon (\cos {q}-1)+\mu (\cos {q}-1)(\sin {\phi +\cos t)}}

The first three terms of this Hamiltonian describe a rotator-pendulum system.
Arnold showed that for this system, for any choice of

          I

            +

          I

            −

        0

    {\displaystyle I_{+}>I_{-}>0}

, and for

        0
        <
        μ
        ≪
        ϵ
        ≪
        1

    {\displaystyle 0<\mu \ll \epsilon \ll 1}

, there is a solution to the system for which

        I
        (
        0
        )
        <

          I

            −

           and

        I
        (
        T
        )

          I

            +

    {\displaystyle I(0)<I_{-}{\text{ and }}I(T)>I_{+}}

for some time

        T
        ≫
        0.

    {\displaystyle T\gg 0.}

His proof relies on the existence of 'transition chains' of 'whiskered' tori, that is, sequences of tori with transitive dynamics such that the unstable manifold (whisker) of one of these tori intersects transversally the stable manifold (whisker) of the next one. Arnold conjectured that "the mechanism of 'transition chains' which guarantees that nonstability in our example is also applicable to the general case (for example, to the problem of three bodies)."
The KAM theorem and Arnold diffusion has led to a compendium of rigorous mathematical results, with insights from physics.

General case
In Arnold's model the perturbation term is of a special type. The general case of Arnold's diffusion problem concerns Hamiltonian systems of one of the forms

(1)

          H

            ϵ

        (
        I
        ,
        ϕ
        ,
        p
        ,
        q
        )

          H

            0

        (
        I
        ,
        p
        ,
        q
        )
        +
        ϵ

          H

            1

        (
        I
        ,
        ϕ
        ,
        p
        ,
        q
        ,
        t
        )

    {\displaystyle H_{\epsilon }(I,\phi ,p,q)=H_{0}(I,p,q)+\epsilon H_{1}(I,\phi ,p,q,t)}

where

        (
        I
        ,
        ϕ
        ,
        p
        ,
        q
        ,
        t
        )
        ∈

            R

            m

        ×

            T

            m

        ×

            R

            n

        ×

            T

            n

        ×

            T

            1

    {\displaystyle (I,\phi ,p,q,t)\in \mathbb {R} ^{m}\times \mathbb {T} ^{m}\times \mathbb {R} ^{n}\times \mathbb {T} ^{n}\times \mathbb {T} ^{1}}

,

        m
        ,
        n
        ≥
        1

    {\displaystyle m,n\geq 1}

, and

          H

            0

        (
        I
        ,
        p
        ,
        q
        )

    {\displaystyle H_{0}(I,p,q)}

 describes a rotator-pendulum system, or

(2)

          H

            ϵ

        (
        I
        ,
        ϕ
        )

          H

            0

        (
        I
        )
        +
        ϵ

          H

            1

        (
        I
        ,
        ϕ
        ,
        t
        )

    {\displaystyle H_{\epsilon }(I,\phi )=H_{0}(I)+\epsilon H_{1}(I,\phi ,t)}

where

        (
        I
        ,
        ϕ
        ,
        t
        )
        ∈

            R

            N

        ×

            T

            N

        ×

            T

            1

    {\displaystyle (I,\phi ,t)\in \mathbb {R} ^{N}\times \mathbb {T} ^{N}\times \mathbb {T} ^{1}}

,

        N
        ≥
        2.

    {\displaystyle N\geq 2.}

For systems as in (1), the unperturbed Hamiltonian possesses smooth families of invariant tori that have hyperbolic stable and unstable manifolds; such systems are referred to as a priori unstable. For system as in (2), the phase space of the unperturbed Hamiltonian is foliated by Lagrangian invariant tori; such systems are referred to as a priori stable. In either case, the Arnold diffusion problem asserts that, for `generic' systems, there exists

        ρ

        0

    {\displaystyle \rho >0}

 such that for every

        ϵ

        0

    {\displaystyle \epsilon >0}

 sufficiently small there exist solution curves for which

        ‖
        I
        (
        T
        )
        −
        I
        (
        0
        )
        ‖
        ≥
        ρ

    {\displaystyle |I(T)-I(0)|\geq \rho }

for some time

        T
        ≫
        0.

    {\displaystyle T\gg 0.}

  Precise formulations of possible genericity conditions in the context of a priori unstable and a priori stable system can be found in, respectively. Informally, the Arnold diffusion problem says that small perturbations can accumulate to large effects.
Recent results in the a priori unstable case include, and in the a priori stable case.
In the context of the restricted three-body problem, Arnold diffusion can be interpreted in the sense that, for all sufficiently small, non-zero values of the eccentricity of the elliptic orbits of the massive bodies, there are solutions along which the energy of the negligible mass changes by a quantity that is independent of eccentricity.
