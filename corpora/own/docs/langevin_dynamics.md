# Langevin dynamics

Langevin dynamics

In physics, Langevin dynamics is an approach to the mathematical modeling of the dynamics of molecular systems using the Langevin equation. It was originally developed by French physicist Paul Langevin. The approach is characterized by the use of simplified models while accounting for omitted degrees of freedom by the use of stochastic differential equations. Langevin dynamics simulations are a kind of Monte Carlo simulation.

Overview
Real world molecular systems occur in air or solvents, rather than in isolation, in a vacuum. Jostling of solvent or air molecules causes friction, and the occasional high velocity collision will perturb the system. Langevin dynamics attempts to extend molecular dynamics to allow for these effects. Also, Langevin dynamics allows temperature to be controlled as with a thermostat, thus approximating the canonical ensemble.
Langevin dynamics mimics the viscous aspect of a solvent. It does not fully model an implicit solvent; specifically, the model does not account for the electrostatic screening and also not for the hydrophobic effect. For denser solvents, hydrodynamic interactions are not captured via Langevin dynamics.
For a system of

        N

    {\displaystyle N}

 particles with masses

        M

    {\displaystyle M}

, with coordinates

        X

        X
        (
        t
        )

    {\displaystyle X=X(t)}

 that constitute a time-dependent random variable, the resulting Langevin equation is

        M

                X

              ¨

        −

          ∇

        U
        (

          X

        )
        −
        γ

        M

                X

              ˙

        +

            2

            M

            γ

              k

                  B

            T

          R

        (
        t
        )

        ,

    {\displaystyle M\,{\ddot {\mathbf {X} }}=-\mathbf {\nabla } U(\mathbf {X} )-\gamma \,M\,{\dot {\mathbf {X} }}+{\sqrt {2\,M\,\gamma \,k_{\rm {B}}T}}\,\mathbf {R} (t)\,,}

where

        U
        (

          X

        )

    {\displaystyle U(\mathbf {X} )}

 is the particle interaction potential;

        ∇

    {\displaystyle \nabla }

 is the gradient operator such that

        −

          ∇

        U
        (

          X

        )

    {\displaystyle -\mathbf {\nabla } U(\mathbf {X} )}

 is the force calculated from the particle interaction potentials; the dot is a time derivative such that

                X

              ˙

    {\displaystyle {\dot {\mathbf {X} }}}

 is the velocity and

                X

              ¨

    {\displaystyle {\ddot {\mathbf {X} }}}

 is the acceleration;

        γ

    {\displaystyle \gamma }

 is the damping constant (units of reciprocal time), also known as the collision frequency;

        T

    {\displaystyle T}

 is the temperature,

          k

              B

    {\displaystyle k_{\rm {B}}}

 is the Boltzmann constant; and

          R

        (
        t
        )

    {\displaystyle \mathbf {R} (t)}

 is a delta-correlated stationary Gaussian process with zero-mean, called Gaussian white noise, satisfying

          ⟨

              R

            (
            t
            )

          ⟩

        0

    {\displaystyle \left\langle \mathbf {R} (t)\right\rangle =0}

          ⟨

              R

            (
            t
            )
            ⋅

              R

            (

              t
              ′

            )

          ⟩

        δ
        (
        t
        −

          t
          ′

        )

    {\displaystyle \left\langle \mathbf {R} (t)\cdot \mathbf {R} (t')\right\rangle =\delta (t-t')}

Here,

        δ

    {\displaystyle \delta }

 is the Dirac delta.

Stochastic Differential Formulation
Considering the covariance of standard Brownian motion or Wiener process

          W

            t

    {\displaystyle W_{t}}

, we can find that

          E

        (

          W

            t

          W

            τ

        )

        min
        (
        t
        ,
        τ
        )

    {\displaystyle \mathbb {E} (W_{t}W_{\tau })=\min(t,\tau )}

Define the covariance matrix of the derivative as

          E

        (

                W

                  t

              ˙

                W

                  τ

              ˙

        )

            ∂

              ∂
              t

            ∂

              ∂
              τ

          E

        (

          W

            t

          W

            τ

        )

            ∂

              ∂
              t

            ∂

              ∂
              τ

        min
        (
        t
        ,
        τ
        )

        δ
        (
        t
        −
        τ
        )

    {\displaystyle \mathbb {E} ({\dot {W_{t}}}{\dot {W_{\tau }}})={\frac {\partial }{\partial t}}{\frac {\partial }{\partial \tau }}\mathbb {E} (W_{t}W_{\tau })={\frac {\partial }{\partial t}}{\frac {\partial }{\partial \tau }}\min(t,\tau )=\delta (t-\tau )}

So under the sense of covariance we can say that

            d

          W

            t

          R

        (
        t
        )

            d

        t

    {\displaystyle {\rm {d}}W_{t}=\mathbf {R} (t){\rm {d}}t}

Without loss of generality, let the mass

        M

        1

    {\displaystyle M=1}

,

        σ

            M
            γ

              k

                  B

            T

    {\displaystyle \sigma ={\sqrt {M\gamma k_{\rm {B}}T}}}

, then the original SDE will become

            d

                X

              ˙

        −
        ∇
        U
        (

          X

        )

            d

        t
        −
        γ

            d

            X

        +

            2

        σ

            d

          W

        (
        t
        )

    {\displaystyle {\rm {d}}{\dot {\mathbf {X} }}=-\nabla U(\mathbf {X} ){\rm {d}}t-\gamma {\rm {d}}{\mathbf {X} }+{\sqrt {2}}\sigma {\rm {d}}\mathbf {W} (t)}

Overdamped Langevin dynamics
If the main objective is to control temperature, care should be exercised to use a small damping constant

        γ

    {\displaystyle \gamma }

. As

        γ

    {\displaystyle \gamma }

 grows, it spans from the inertial all the way to the diffusive (Brownian) regime. The Langevin dynamics limit of non-inertia is commonly described as Brownian dynamics. Brownian dynamics can be considered as overdamped Langevin dynamics, i.e. Langevin dynamics where no average acceleration takes place. Under this limit we have

            d

              X
              ˙

        0

    {\displaystyle {\rm {d}}{\dot {X}}=0}

, the original SDE then becomes

            d

            X

        −

            1
            γ

        ∇
        U
        (

          X

        )

            d

        t
        +

                  2

              σ

            γ

            d

          W

        (
        t
        )
        .

    {\displaystyle {\rm {d}}{\mathbf {X} }=-{\frac {1}{\gamma }}\nabla U(\mathbf {X} ){\rm {d}}t+{\frac {{\sqrt {2}}\sigma }{\gamma }}{\rm {d}}\mathbf {W} (t).}

The translational Langevin equation can be solved using various numerical methods with differences in the sophistication of analytical solutions, the allowed time-steps, time-reversibility (symplectic methods), in the limit of zero friction, etc.
The Langevin equation can be generalized to rotational dynamics of molecules, Brownian particles, etc. A standard (according to NIST) way to do it is to leverage a quaternion-based description of the stochastic rotational motion.

Applications

Langevin thermostat
Langevin thermostat is a type of Thermostat algorithm in molecular dynamics, which is used to simulate a canonical ensemble (NVT) under a desired temperature. It integrates the following Langevin equation of motion:

        M

                X

              ¨

        −
        ∇
        U
        (

          X

        )
        −
        γ

                X

              ˙

        +

            2
            γ

              k

                B

            T

            R

        (
        t
        )

    {\displaystyle M{\ddot {\mathbf {X} }}=-\nabla U(\mathbf {X} )-\gamma {\dot {\mathbf {X} }}+{\sqrt {2\gamma k_{B}T}}{\textbf {R}}(t)}

        −
        ∇
        U
        (

          X

        )

    {\displaystyle -\nabla U(\mathbf {X} )}

 is the deterministic force term;

        γ

    {\displaystyle \gamma }

 is the friction coefficient and

        γ

              X
              ˙

    {\displaystyle \gamma {\dot {X}}}

 is the friction or damping term; the last term is the random force term (

          k

            B

    {\displaystyle k_{B}}

: Boltzmann constant,

        T

    {\displaystyle T}

: temperature). This equation allows the system to couple with an imaginary "heat bath": the kinetic energy of the system dissipates from the friction/damping term, and gain from random force/fluctuation; the strength of coupling is controlled by

        γ

    {\displaystyle \gamma }

. This equation can be simulated with SDE solvers such as Euler–Maruyama method, where the random force term is replaced by a Gaussian random number in every integration step (variance

          σ

            2

        2
        γ

          k

            B

        T

          /

        Δ
        t

    {\displaystyle \sigma ^{2}=2\gamma k_{B}T/\Delta t}

,

        Δ
        t

    {\displaystyle \Delta t}

: time step), or Langevin Leapfrog integration, etc. This method is also known as Langevin Integrator.

Langevin Monte Carlo
The overdamped Langevin equation gives

            d

            x

            t

        −

            D

                k

                  B

              T

          ∇

              x

        U
        (

            x

            t

        )

            d

        t
        +

            2
            D

            d

          W

            t

    {\displaystyle {\rm {d}}\mathbf {x} {t}=-{\frac {D}{k{B}T}}\nabla _{\mathbf {x} }U(\mathbf {x} {t}){\rm {d}}t+{\sqrt {2D}}{\rm {d}}W{t}}

Here,

        D

          k

            B

        T

          /

        γ

    {\displaystyle D=k_{B}T/\gamma }

 is the diffusion coefficient from Einstein relation. As proven with Fokker-Planck equation, under appropriate conditions, the stationary distribution of

            x

            t

    {\displaystyle \mathbf {x} _{t}}

 is Boltzmann distribution

        p
        (

          x

        )
        ∝

          e

            −
            U
            (

              x

            )

              /

              k

                B

            T

    {\displaystyle p(\mathbf {x} )\propto e^{-U(\mathbf {x} )/k_{B}T}}

.
Since that

        ∇
        log
        ⁡
        p
        (

          x

        )

        −
        ∇
        U
        (

          x

        )

          /

          k

            B

        T

    {\displaystyle \nabla \log p(\mathbf {x} )=-\nabla U(\mathbf {x} )/k_{B}T}

, this equation is equivalent to the following form:

            d

            x

            t

        ϵ

          ∇

              x

        log
        ⁡
        p
        (

            x

            t

        )

            d

        t
        +

            2
            ϵ

            d

          W

            t

    {\displaystyle {\rm {d}}\mathbf {x} _{t}=\epsilon \nabla _{\mathbf {x} }\log p(\mathbf {x} {t}){\rm {d}}t+{\sqrt {2\epsilon }}{\rm {d}}W{t}}

And the distribution of

            x

            t

        (
        t
        →
        ∞
        )

    {\displaystyle \mathbf {x} _{t}(t\to \infty )}

 follows

        p
        (

          x

        )

    {\displaystyle p(\mathbf {x} )}

. In other words, Langevin dynamics drives particles towards a stationary distribution

        p
        (

          x

        )

    {\displaystyle p(\mathbf {x} )}

 along a gradient flow, due to the

        ∇
        log
        ⁡
        p
        (

          x

        )

    {\displaystyle \nabla \log p(\mathbf {x} )}

 term, while still allowing for some random fluctuations. This provides a Markov Chain Monte Carlo method that can be used to sample data

          x

    {\displaystyle \mathbf {x} }

 from a target distribution

        p
        (

          x

        )

    {\displaystyle p(\mathbf {x} )}

, known as Langevin Monte Carlo.
In many applications, we have a desired distribution

        p
        (

          x

        )

    {\displaystyle p(\mathbf {x} )}

 from which we would like to sample

          x

    {\displaystyle \mathbf {x} }

, but direct sampling might be challenging or inefficient. Langevin Monte Carlo offers another way to sample

          x

        ∼
        p
        (

          x

        )

    {\displaystyle \mathbf {x} \sim p(\mathbf {x} )}

 by sampling a Markov chain in accordance with the Langevin dynamics whose stationary state is

        p
        (

          x

        )

    {\displaystyle p(\mathbf {x} )}

. The Metropolis-adjusted Langevin algorithm (MALA) is an example : Given a current state

            x

            t

    {\displaystyle \mathbf {x} _{t}}

, the MALA method proposes a new state

                x
                ~

            t
            +
            1

    {\displaystyle {\tilde {x}}_{t+1}}

 using the Langevin dynamics above. The proposal is then accepted or rejected based on the Metropolis-Hastings algorithm. The incorporation of the Langevin dynamics in the choice of

                x
                ~

            t
            +
            1

    {\displaystyle {\tilde {x}}_{t+1}}

 provides greater computational efficiency, since the dynamics drive the particles into regions of higher

        p
        (

          x

        )

    {\displaystyle p(\mathbf {x} )}

 probability and are thus more likely to be accepted. Read more in Metropolis-adjusted Langevin algorithm.

Score-based generative model
Langevin dynamics is one of the bases of score-based generative models. From (overdamped) Langevin dynamics,

            d

            x

            t

        ϵ

          ∇

              x

        log
        ⁡
        p
        (

            x

            t

        )

            d

        t
        +

            2
            ϵ

            d

          W

            t

    {\displaystyle {\rm {d}}\mathbf {x} _{t}=\epsilon \nabla _{\mathbf {x} }\log p(\mathbf {x} {t}){\rm {d}}t+{\sqrt {2\epsilon }}{\rm {d}}W{t}}

A generative model aims to generate samples that follow (unknown data distribution)

        p
        (

          x

        )

    {\displaystyle p(\mathbf {x} )}

. To achieve that, a score-based model learns an approximate score function

            s

            θ

        (

          x

        )
        ≈

          ∇

              x

        log
        ⁡
        p
        (

          x

        )

    {\displaystyle \mathbf {s} _{\theta }(\mathbf {x} )\approx \nabla _{\mathbf {x} }\log p(\mathbf {x} )}

 (a process called score matching). With access to a score function, samples are generated by the following iteration,

            x

            i
            +
            1

        ←

            x

            i

        +
        ϵ

          ∇

              x

        log
        ⁡
        p
        (

            x

            i

        )
        +

            2
            ϵ

            z

            i

        ,

        i

        0
        ,
        1
        ,
        ⋯
        ,
        K

    {\displaystyle \mathbf {x} _{i+1}\gets \mathbf {x} _{i}+\epsilon \nabla _{\mathbf {x} }\log p(\mathbf {x} _{i})+{\sqrt {2\epsilon }}\mathbf {z} _{i},\quad i=0,1,\cdots ,K}

with

            z

            i

        ∼
        N
        (
        0
        ,
        1
        )

    {\displaystyle \mathbf {z} _{i}\sim N(0,1)}

. As

        ϵ
        →
        0

    {\displaystyle \epsilon \to 0}

 and

        K
        →
        ∞

    {\displaystyle K\to \infty }

, the generated

            x

            K

    {\displaystyle \mathbf {x} _{K}}

 converge to the target distribution

        p
        (

          x

        )

    {\displaystyle p(\mathbf {x} )}

. Score-based models use

            s

            θ

        (

          x

        )
        ≈

          ∇

              x

        log
        ⁡
        p
        (

          x

        )

    {\displaystyle \mathbf {s} _{\theta }(\mathbf {x} )\approx \nabla _{\mathbf {x} }\log p(\mathbf {x} )}

 as an approximation.

Relation to Other Theories

Klein-Kramers equation
As a stochastic differential equation(SDE), Langevin dynamics equation, has its corresponding partial differential equation(PDE), Klein-Kramers equation, a special Fokker–Planck equation that governs the probability distribution of the particles in the phase space. The original Langevin dynamics equation can be reformulated as the following first order SDEs:

            d

          X

          P

            d

        t

    {\displaystyle {\rm {d}}\mathbf {X} =\mathbf {P} {\rm {d}}t}

            d

          P

        −
        γ

          P

            d

        t
        −
        ∇
        U
        (

          X

        )

            d

        t
        +

            2

        σ

            d

          W

        (
        t
        )

    {\displaystyle {\rm {d}}\mathbf {P} =-\gamma \mathbf {P} {\rm {d}}t-\nabla U(\mathbf {X} ){\rm {d}}t+{\sqrt {2}}\sigma {\rm {d}}\mathbf {W} (t)}

Now consider the following cases and their law of

        (

          X

        ,

          P

        )

    {\displaystyle (\mathbf {X} ,\mathbf {P} )}

:
1.

              d

            X

          P

            d

        t
        ,

              d

            P

        −
        γ

          P

            d

        t
        −
        ∇
        U
        (

          X

        )

            d

        t
        +

            2

        σ

            d

          W

        (
        t
        )

    {\displaystyle \mathbf {{\rm {d}}{X}} =\mathbf {P} {\rm {d}}t,\mathbf {{\rm {d}}{P}} =-\gamma \mathbf {P} {\rm {d}}t-\nabla U(\mathbf {X} ){\rm {d}}t+{\sqrt {2}}\sigma {\rm {d}}\mathbf {W} (t)}

 with

        (

            X

            0

        ,

            P

            0

        )
        ∼

          ρ

            0

    {\displaystyle (\mathbf {X} _{0},\mathbf {P} _{0})\sim \rho _{0}}

2.

              ∂
              ρ

              ∂
              t

        −

          P

          ∇

              X

        ρ
        +

          ∇

              P

        (
        γ

          P

        ρ
        +

          ∇

              X

        U
        (

          X

        )
        ρ
        )
        +

          ∇

              P

            2

        (

          σ

            T

            2

        ρ
        )

    {\displaystyle {\frac {\partial \rho }{\partial t}}=-\mathbf {P} \nabla _{\mathbf {X} }\rho +\nabla _{\mathbf {P} }(\gamma \mathbf {P} \rho +\nabla _{\mathbf {X} }U(\mathbf {X} )\rho )+\nabla _{\mathbf {P} }^{2}(\sigma _{T}^{2}\rho )}

 with

        ρ
        (
        t

        0
        ,

          X

        ,

          P

        )

          ρ

            0

    {\displaystyle \rho (t=0,\mathbf {X} ,\mathbf {P} )=\rho _{0}}

Consider a general function of momentum and position

          Ψ

            t

        Ψ
        (

          X

        ,

          P

        )

    {\displaystyle \Psi _{t}=\Psi (\mathbf {X} ,\mathbf {P} )}

The expectation value of the function will be

          E

        [

          Ψ

            t

        ]

        ∫
        ρ
        (
        t
        ,

          X

        ,

          P

        )
        Ψ
        (

          X

        ,

          P

        )

            d

          P

            d

          X

    {\displaystyle \mathbb {E} [\Psi _{t}]=\int \rho (t,\mathbf {X} ,\mathbf {P} )\Psi (\mathbf {X} ,\mathbf {P} ){\rm {d}}\mathbf {P} {\rm {d}}\mathbf {X} }

Taking derivative with respect to time

        t

    {\displaystyle t}

, and applying Itô's formula, we have

          E

        [

              d

                  d

              t

        Ψ
        (

          X

        ,

          P

        )
        ]

          E

        [

          ∇

              X

        Ψ

                  d

                X

                  d

              t

        +

          ∇

              P

        Ψ

                  d

                P

                  d

              t

        +

          σ

            T

            2

          ∇

              P

            2

        Ψ

            1

                  d

              t

        (

            d

          W

        (
        t
        )

          )

            2

        ]

    {\displaystyle \mathbb {E} [{\frac {\rm {d}}{{\rm {d}}t}}\Psi (\mathbf {X} ,\mathbf {P} )]=\mathbb {E} [\nabla _{\mathbf {X} }\Psi {\frac {{\rm {d}}\mathbf {X} }{{\rm {d}}t}}+\nabla _{\mathbf {P} }\Psi {\frac {{\rm {d}}\mathbf {P} }{{\rm {d}}t}}+\sigma _{T}^{2}\nabla _{\mathbf {P} }^{2}\Psi {\frac {1}{{\rm {d}}t}}({\rm {d}}\mathbf {W} (t))^{2}]}

which can be simplified to

        ∫
        (

            ∂

              ∂
              t

        ρ
        )
        Ψ
        (

          X

        ,

          P

        )

            d

          X

            d

          P

          E

        [
        (

          ∇

              X

        Ψ
        )

          P

        +

          ∇

              P

        Ψ
        (
        −
        γ

          P

        −

          ∇

              X

        U
        (

          X

        )
        )
        +

          σ

            T

            2

          ∇

              P

            2

        Ψ
        ]

    {\displaystyle \int ({\frac {\partial }{\partial t}}\rho )\Psi (\mathbf {X} ,\mathbf {P} ){\rm {d}}\mathbf {X} {\rm {d}}\mathbf {P} =\mathbb {E} [(\nabla _{\mathbf {X} }\Psi )\mathbf {P} +\nabla _{\mathbf {P} }\Psi (-\gamma \mathbf {P} -\nabla _{\mathbf {X} }U(\mathbf {X} ))+\sigma _{T}^{2}\nabla _{\mathbf {P} }^{2}\Psi ]}

Integration by parts on right hand side, due to vanishing density for infinite momentum or velocity we have

        (

            ∂

              ∂
              t

        ρ
        )
        Ψ
        (

          X

        ,

          P

        )

            d

          X

            d

          P

        ∫
        (
        −

          P

          ∇

              X

        ρ
        +

          ∇

              P

        (
        γ

          P

        ρ
        +

          ∇

              X

        U
        (

          X

        )
        ρ
        )
        +

          ∇

              P

            2

        (

          σ

            T

            2

        ρ
        )
        )
        Ψ
        (

          X

        ,

          P

        )

            d

          X

            d

          P

    {\displaystyle ({\frac {\partial }{\partial t}}\rho )\Psi (\mathbf {X} ,\mathbf {P} ){\rm {d}}\mathbf {X} {\rm {d}}\mathbf {P} =\int (-\mathbf {P} \nabla _{\mathbf {X} }\rho +\nabla _{\mathbf {P} }(\gamma \mathbf {P} \rho +\nabla _{\mathbf {X} }U(\mathbf {X} )\rho )+\nabla _{\mathbf {P} }^{2}(\sigma _{T}^{2}\rho ))\Psi (\mathbf {X} ,\mathbf {P} ){\rm {d}}\mathbf {X} {\rm {d}}\mathbf {P} }

This equation holds for arbitrary

        Ψ

    {\displaystyle \Psi }

, so we require the density to satisfy

              ∂
              ρ

              ∂
              t

        −

          P

          ∇

              X

        ρ
        +

          ∇

              P

        (
        γ

          P

        ρ
        +

          ∇

              X

        U
        (

          X

        )
        ρ
        )
        +

          ∇

              P

            2

        (

          σ

            T

            2

        ρ
        )

    {\displaystyle {\frac {\partial \rho }{\partial t}}=-\mathbf {P} \nabla _{\mathbf {X} }\rho +\nabla _{\mathbf {P} }(\gamma \mathbf {P} \rho +\nabla _{\mathbf {X} }U(\mathbf {X} )\rho )+\nabla _{\mathbf {P} }^{2}(\sigma _{T}^{2}\rho )}

This equation is called the Klein-Kramers equation, a special version of Fokker Planck equation. It's a partial differential equation that describes the evolution of probability density of the system in the phase space.

Fokker Planck equation
For the overdamped limit, we have

            d

          P

        0

    {\displaystyle {\rm {d}}\mathbf {P} =0}

, so the evolution of system can be reduced to the position subspace. Following similar logic we can prove that the SDE for position,

            d

          X

        −

            1
            γ

        ∇
        U
        (

          X

        )

            d

        t
        +

            2

            σ
            γ

          R

        (
        t
        )

            d

        t

    {\displaystyle {\rm {d}}\mathbf {X} =-{\frac {1}{\gamma }}\nabla U(\mathbf {X} ){\rm {d}}t+{\sqrt {2}}{\frac {\sigma }{\gamma }}\mathbf {R} (t){\rm {d}}t}

corresponds to the Fokker Planck equation for probability density

              ∂
              ρ
              (
              t
              ,

                X

              )

              ∂
              t

          ∇

              X

        (

            1
            γ

          ∇

              X

        U
        (

          X

        )
        ρ
        (
        t
        ,

          X

        )
        )
        +

          Δ

              X

        (

              σ

                2

              γ

                2

        ρ
        (
        t
        ,

          X

        )
        )

    {\displaystyle {\frac {\partial \rho (t,\mathbf {X} )}{\partial t}}=\nabla _{\mathbf {X} }({\frac {1}{\gamma }}\nabla _{\mathbf {X} }U(\mathbf {X} )\rho (t,\mathbf {X} ))+\Delta _{\mathbf {X} }({\frac {\sigma ^{2}}{\gamma ^{2}}}\rho (t,\mathbf {X} ))}

Fluctuation-dissipation theorem
Consider Langevin dynamics of a free particle (i.e.

        U
        (

          X

        )

        0

    {\displaystyle U(\mathbf {X} )=0}

), then the equation for momentum will become

            d

          P

        −

            1
            γ

          P

            d

        t
        +

                  2

              σ

            γ

            d

            W

            t

    {\displaystyle {\rm {d}}\mathbf {P} =-{\frac {1}{\gamma }}\mathbf {P} {\rm {d}}t+{\frac {{\sqrt {2}}\sigma }{\gamma }}{\rm {d}}\mathbf {W} _{t}}

the analytical solution to this SDE is

          P

            P

            0

          e

            −
            t

              /

            γ

        +

                  2

              σ

            γ

          ∫

            0

            t

              e

            −
            (
            t
            −

              t
              ′

            )

              /

            γ

            d

            W

            t

          ′

    {\displaystyle \mathbf {P} =\mathbf {P} _{0}e^{-t/\gamma }+{\frac {{\sqrt {2}}\sigma }{\gamma }}\int _{0}^{t}{\rm {e}}^{-(t-t')/\gamma }{\rm {d}}\mathbf {W} _{t}'}

thus the average value of second moment of momentum will becomes (here we apply the Itô isometry)

          E

        (

            P

            2

        )

            P

            0

            2

              e

            −
            2
            t

              /

            γ

        +

              σ

                2

            γ

        (
        1
        −

              e

            −
            2
            t

              /

            γ

        )

            →

              t
              →
              ∞

              σ

                2

            γ

    {\displaystyle \mathbb {E} (\mathbf {P} ^{2})=\mathbf {P} _{0}^{2}{\rm {e}}^{-2t/\gamma }+{\frac {\sigma ^{2}}{\gamma }}(1-{\rm {e}}^{-2t/\gamma }){\overset {t\to \infty }{\to }}{\frac {\sigma ^{2}}{\gamma }}}

That is, the limiting behavior when time approaches positive infinity, the momentum fluctuation of this system is related to the energy dissipation (friction term parameter

        γ

    {\displaystyle \gamma }

) of this system. Combining this result with Equipartition theorem, which relates the average value of kinetic energy of particles with temperature

        ⟨

          v

            2

        ⟩

          k

              B

        T

    {\displaystyle \langle v^{2}\rangle =k_{\rm {B}}T}

we can determines the value of the variance

        σ

    {\displaystyle \sigma }

 in applications like Langevin thermostat.

          σ

            2

          /

        γ

          k

            B

        T
        →
        σ

              k

                  B

            T
            γ

    {\displaystyle \sigma ^{2}/\gamma =k_{B}T\to \sigma ={\sqrt {k_{\rm {B}}T\gamma }}}

This is consistent with the original definition assuming

        M

        1

    {\displaystyle M=1}

.

Path integral
Path integral formulation comes from quantum mechanics. But for a Langevin SDE we can also induce a corresponding path integral. Considering the following overdamped Langevin equation under, where without loss of generality we take

        γ

        σ

        1

    {\displaystyle \gamma =\sigma =1}

,

            d

          X

        −
        ∇
        U
        (

          X

        )

            d

        t
        +

            2

            d

          W

            t

    {\displaystyle {\rm {d}}{X}=-\nabla U({X}){\rm {d}}t+{\sqrt {2}}{\rm {d}}W_{t}}

Discretize and define

          t

            n

        n
        Δ
        t

    {\displaystyle t_{n}=n\Delta t}

, we get

            X

            n
            +
            1

        −

            X

            n

        +
        ∇
        U
        (

          X

        )
        Δ
        t

            2

        (

          W

              t

                n

        −

          W

              t

                n
                −
                1

        )
        ∼

            N

        (
        0
        ,
        2

            Δ
            t

        )

    {\displaystyle {X}{n+1}-{X}{n}+\nabla U({X})\Delta t={\sqrt {2}}(W_{t_{n}}-W_{t_{n-1}})\sim {\mathcal {N}}(0,2{\sqrt {\Delta t}})}

Therefore the propagation probability will be

        P
        (

            X

            n
            +
            1

            X

            n

        )

        ∫

            d

        ξ

            1

              2

                  π
                  Δ
                  t

              e

            −

                  ξ

                    2

                  4
                  Δ
                  t

        δ
        (

            X

            n
            +
            1

        −

            X

            n

        +
        ∇
        U
        (

          X

        )
        Δ
        t
        −
        ξ
        )

    {\displaystyle P({X}{n+1}|{X}{n})=\int {\rm {d}}\xi {\frac {1}{2{\sqrt {\pi \Delta t}}}}{\rm {e}}^{-{\frac {\xi ^{2}}{4\Delta t}}}\delta ({X}{n+1}-{X}{n}+\nabla U({X})\Delta t-\xi )}

Applying Fourier Transform of delta function, and we will get

        P

        ∫

                  d

              k

              2
              π

              e

                i

            k
            (

                X

                n
                +
                1

            −

                X

                n

            +
            ∇
            U
            (

              X

            )
            Δ
            t
            )

        ∫

            d

        ξ

            1

              2

                  π
                  Δ
                  t

              e

            −

                  ξ

                    2

                  4
                  Δ
                  t

              e

            −

                i

            k
            ξ

    {\displaystyle P=\int {\frac {{\rm {d}}k}{2\pi }}{\rm {e}}^{{\rm {i}}k({X}{n+1}-{X}{n}+\nabla U({X})\Delta t)}\int {\rm {d}}\xi {\frac {1}{2{\sqrt {\pi \Delta t}}}}{\rm {e}}^{-{\frac {\xi ^{2}}{4\Delta t}}}{\rm {e}}^{-{\rm {i}}k\xi }}

The second part is a Gaussian Integral, which yields

        P

        ∫

                  d

              k

              2
              π

              e

                i

            k
            (

                X

                n
                +
                1

            −

                X

                n

            +
            ∇
            U
            (

              X

            )
            Δ
            t
            )

              e

            −

              k

                2

            Δ
            t

    {\displaystyle P=\int {\frac {{\rm {d}}k}{2\pi }}{\rm {e}}^{{\rm {i}}k({X}{n+1}-{X}{n}+\nabla U({X})\Delta t)}{\rm {e}}^{-k^{2}\Delta t}}

Now consider the probability from initial

          X

            0

    {\displaystyle X_{0}}

to final

          X

            n

    {\displaystyle X_{n}}

.

        P
        (

            X

            n

            X

            0

        )

        ∫

            1

              2
              π

          ∏

            i

            N
            −
            1

            d

          k

            i

              e

            (

                i

              k

                i

            (

                  X
                  ˙

            +
            ∇
            U
            (
            X
            )
            )
            −

              k

                i

                2

            )
            Δ
            t

    {\displaystyle P(\mathbf {X} _{n}|\mathbf {X} _{0})=\int {\frac {1}{2\pi }}\prod {i}^{N-1}{\rm {d}}k{i}{\rm {e}}^{({\rm {i}}k_{i}({\dot {X}}+\nabla U(X))-k_{i}^{2})\Delta t}}

take the limit of

        Δ
        t
        →
        0

    {\displaystyle \Delta t\to 0}

,we will get

        P
        (

            X

            n

            X

            0

        )

        ∫

            D

        [
        k
        ]

              e

              ∫

                0

                  t

                    n

            (

                i

            k
            (

                  X
                  ˙

            +
            ∇
            U
            (
            X
            )
            )
            −

              k

                2

            )

                d

            t

    {\displaystyle P(\mathbf {X} _{n}|\mathbf {X} _{0})=\int {\mathcal {D}}[k]{\rm {e}}^{\int {0}^{t{n}}({\rm {i}}k({\dot {X}}+\nabla U(X))-k^{2}){\rm {d}}t}}
