# Frenkel–Kontorova model

Frenkel–Kontorova model

The Frenkel–Kontorova (FK) model is a fundamental model of low-dimensional nonlinear physics.
The generalized FK model describes a chain of classical particles with nearest neighbor interactions and subjected to a periodic on-site substrate potential. In its original and simplest form the interactions are taken to be harmonic and the potential to be sinusoidal with a periodicity commensurate with the equilibrium distance of the particles. Different choices for the interaction and substrate potentials and inclusion of a driving force may describe a wide range of different physical situations.
Originally introduced by Yakov Frenkel and Tatiana Kontorova in 1938 to describe the structure and dynamics of a crystal lattice near a dislocation core, the FK model has become one of the standard models in condensed matter physics due to its applicability to describe many physical phenomena. Physical phenomena that can be modeled by FK model include dislocations, the dynamics of adsorbate layers on surfaces, crowdions, domain walls in magnetically ordered structures, long Josephson junctions, hydrogen-bonded chains, and DNA type chains. A modification of the FK model, the Tomlinson model, plays an important role in the field of tribology.
The equations for stationary configurations of the FK model reduce to those of the standard map or Chirikov–Taylor map of stochastic theory.
In the continuum-limit approximation the FK model reduces to the exactly integrable sine-Gordon (SG) equation, which allows for soliton solutions. For this reason the FK model is also known as the "discrete sine-Gordon" or "periodic Klein–Gordon equation".

History
A simple model of a harmonic chain in a periodic substrate potential was proposed by Ulrich Dehlinger in 1928. Dehlinger derived an approximate analytical expression for the stable solutions of this model, which he termed Verhakungen, which correspond to what is today called kink pairs. An essentially similar model was developed by Ludwig Prandtl in 1912/13 but did not see publication until 1928.
The model was independently proposed by Yakov Frenkel and Tatiana Kontorova in their 1938 article On the theory of plastic deformation and twinning to describe the dynamics of a crystal lattice near a dislocation and to describe crystal twinning. In the standard linear harmonic chain any displacement of the atoms will result in waves, and the only stable configuration will be the trivial one.
For the nonlinear chain of Frenkel and Kontorova, there exist stable configurations beside the trivial one. For small atomic displacements the situation resembles the linear chain; however, for large enough displacements, it is possible to create a moving single dislocation, for which an analytical solution was derived by Frenkel and Kontorova. The shape of these dislocations is defined only by the parameters of the system such as the mass and the elastic constant of the springs.
Dislocations, also called solitons, are distributed non-local defects and mathematically are a type of topological defect. The defining characteristic of solitons/dislocations is that they behave much like stable particles, they can move while maintaining their overall shape. Two solitons of equal and opposite orientation may cancel upon collision, but a single soliton can not annihilate spontaneously.

Generalized model
The generalized FK model treats a one-dimensional chain of atoms with nearest-neighbor interaction in periodic on-site potential, the Hamiltonian for this system is

where the first term is the kinetic energy of the

        n

    {\displaystyle n}

 atoms of mass

          m

            a

    {\displaystyle m_{a}}

, and the potential energy

        U

    {\displaystyle U}

 is a sum of the potential energy due to the nearest-neighbor interaction and that of the substrate potential:

        U

          U

            sub

        +

          U

            int

    {\displaystyle U=U_{\text{sub}}+U_{\text{int}}}

.
The substrate potential is periodic, i.e.

          U

            sub

        (
        x
        +

          a

            s

        )

          U

            sub

        (
        x
        )

    {\displaystyle U_{\text{sub}}(x+a_{s})=U_{\text{sub}}(x)}

 for some

          a

            s

    {\displaystyle a_{s}}

.
For non-harmonic interactions and/or non-sinusoidal potential, the FK model will give rise to a commensurate–incommensurate phase transition.
The FK model can be applied to any system that can be treated as two coupled sub-systems where one subsystem can be approximated as a linear chain and the second subsystem as a motionless substrate potential.
An example would be the adsorption of a layer onto a crystal surface, here the adsorption layer can be approximated as the chain, and the crystal surface as an on-site potential.

Classical model
In this section we examine in detail the simplest form of the FK model. A detailed version of this derivation can be found in the literature. The model describes a one-dimensional chain of atoms with a harmonic nearest neighbor interaction and subject to a sinusoidal potential. Transverse motion of the atoms is ignored, i.e. the atoms can only move along the chain.
The Hamiltonian for this situation is given by 1, where we specify the interaction potential to be

          U

            int

            g
            2

          ∑

            n

        (

          x

            n
            +
            1

        −

          x

            n

        −

          a

            0

          )

            2

        ,

    {\displaystyle U_{\text{int}}={\frac {g}{2}}\sum {n}(x{n+1}-x_{n}-a_{0})^{2},}

where

        g

    {\displaystyle g}

 is the elastic constant, and

          a

            0

    {\displaystyle a_{0}}

 is the inter-atomic equilibrium distance. The substrate potential is

          U

            sub

              ϵ

                s

            2

          ∑

            n

          [

            1
            −
            cos
            ⁡

                  2
                  π

                    x

                      n

                  a

                    s

          ]

        ,

    {\displaystyle U_{\text{sub}}={\frac {\epsilon _{s}}{2}}\sum {n}\left[1-\cos {\frac {2\pi x{n}}{a_{s}}}\right],}

with

          ϵ

            s

    {\displaystyle \epsilon _{s}}

 being the amplitude, and

          a

            s

    {\displaystyle a_{s}}

 the period.
The following dimensionless variables are introduced in order to rewrite the Hamiltonian:

          x

            n

        →

          (

                2
                π

                a

                  s

          )

          x

            n

        ,

        t
        →

          (

                2
                π

                a

                  s

          )

                ϵ

                  s

                2

                  m

                    a

        t
        ,

          a

            0

        →

              2
              π

              a

                s

        ,

        g
        →
        g

                a

                  s

                /

              2

                π

                  2

                ϵ

                  s

                /

              2

        .

    {\displaystyle x_{n}\to \left({\frac {2\pi }{a_{s}}}\right)x_{n},\quad t\to \left({\frac {2\pi }{a_{s}}}\right){\sqrt {\frac {\epsilon {s}}{2m{a}}}}t,\quad a_{0}\to {\frac {2\pi }{a_{s}}},\quad g\to g{\frac {a_{s}/2\pi ^{2}}{\epsilon _{s}/2}}.}

In dimensionless form the Hamiltonian is

        H

              H

                ϵ

                  s

                /

              2

          ∑

            n

          [

                1
                2

                    d

                      x

                        n

                    d
                    t

                2

            +

              (

                1
                −
                cos
                ⁡

                  x

                    n

                +

                    1
                    2

                g
                (

                  x

                    n
                    +
                    1

                −

                  x

                    n

                −

                  a

                    0

                  )

                    2

              )

          ]

        ,

    {\displaystyle H={\frac {\mathcal {H}}{\epsilon _{s}/2}}=\sum {n}\left[{\frac {1}{2}}{\frac {dx{n}}{dt}}^{2}+\left(1-\cos x_{n}+{\frac {1}{2}}g(x_{n+1}-x_{n}-a_{0})^{2}\right)\right],}

which describes a harmonic chain of atoms of unit mass in a sinusoidal potential of period

          a

            s

        2
        π

    {\displaystyle a_{s}=2\pi }

 with amplitude

          ϵ

            s

        2

    {\displaystyle \epsilon _{s}=2}

. The equation of motion for this Hamiltonian is

                d

                  2

                x

                  n

              d

                t

                  2

        +
        sin
        ⁡

          x

            n

        −
        g
        (

          x

            n
            +
            1

        +

          x

            n
            −
            1

        −
        2

          x

            n

        )

        0.

    {\displaystyle {\frac {d^{2}x_{n}}{dt^{2}}}+\sin x_{n}-g(x_{n+1}+x_{n-1}-2x_{n})=0.}

We consider only the case where

          a

            0

    {\displaystyle a_{0}}

 and

          a

            s

    {\displaystyle a_{s}}

 are commensurate, for simplicity we take

          a

            0

          a

            s

    {\displaystyle a_{0}=a_{s}}

. Thus in the ground state of the chain each minimum of the substrate potential is occupied by one atom.
We introduce the variable

          u

            n

    {\displaystyle u_{n}}

 for atomic displacements which is defined by

          x

            n

        n

          a

            s

        +

          u

            n

        .

    {\displaystyle x_{n}=na_{s}+u_{n}.}

For small displacements

          u

            n

        ≪

          a

            s

    {\displaystyle u_{n}\ll a_{s}}

 the equation of motion may be linearized and takes the following form:

                d

                  2

                u

                  n

              d

                t

                  2

        +

          u

            n

        −
        g
        (

          u

            n
            +
            1

        +

          u

            n
            −
            1

        −
        2

          u

            n

        )

        0.

    {\displaystyle {\frac {d^{2}u_{n}}{dt^{2}}}+u_{n}-g(u_{n+1}+u_{n-1}-2u_{n})=0.}

This equation of motion describes phonons with

          u

            n

        ∝
        exp
        ⁡
        [
        i
        (

          ω

            ph

        (
        κ
        )
        t
        −
        κ
        n
        )
        ]

    {\displaystyle u_{n}\propto \exp[i(\omega _{\text{ph}}(\kappa )t-\kappa n)]}

 with the phonon dispersion relation

          ω

            ph

            2

        (
        κ
        )

          ω

            min

            2

        +
        2
        g
        (
        1
        −
        cos
        ⁡
        κ
        )

    {\displaystyle \omega _{\text{ph}}^{2}(\kappa )=\omega _{\text{min}}^{2}+2g(1-\cos \kappa )}

 with the dimensionless wavenumber

        κ

        ≤
        π

    {\displaystyle |\kappa |\leq \pi }

. This shows that the frequency spectrum of the chain has a band gap

          ω

            min

        ≡

          ω

            ph

        (
        0
        )

        1

    {\displaystyle \omega _{\text{min}}\equiv \omega _{\text{ph}}(0)=1}

 with cut-off frequency

          ω

            max

        ≡

          ω

            ph

        (
        π
        )

              ω

                min

                2

            +
            4
            g

    {\displaystyle \omega _{\text{max}}\equiv \omega _{\text{ph}}(\pi )={\sqrt {\omega _{\text{min}}^{2}+4g}}}

.
The linearised equation of motion are not valid when the atomic displacements are not small, and one must use the nonlinear equation of motion.
The nonlinear equations can support new types of localized excitations, which are best illuminated by considering the continuum limit of the FK model. Applying the standard procedure of Rosenau to derive continuum-limit equations from a discrete lattice results in the perturbed sine-Gordon equation

          u

            t
            t

        +
        sin
        ⁡
        u
        −
        (

          a

            s

            2

        g
        )

          u

            x
            x

        ϵ
        f
        (
        u
        )
        ,

    {\displaystyle u_{tt}+\sin u-(a_{s}^{2}g)u_{xx}=\epsilon f(u),}

where the function

        ϵ
        f
        (
        u
        )

            1
            12

          a

            s

            2

        (

          u

            x
            x
            t
            t

        +

          u

            x

            2

        sin
        ⁡
        u
        −

          u

            x
            x

        cos
        ⁡
        u
        )

    {\displaystyle \epsilon f(u)={\frac {1}{12}}a_{s}^{2}(u_{xxtt}+u_{x}^{2}\sin u-u_{xx}\cos u)}

describes in first order the effects due to the discreteness of the chain.
Neglecting the discreteness effects and introducing

        x
        →

            x

                a

                  s

                  g

    {\displaystyle x\to {\frac {x}{a_{s}{\sqrt {g}}}}}

 reduces the equation of motion to the sine-Gordon (SG) equation in its standard form

          u

            t
            t

        −

          u

            x
            x

        +
        sin
        ⁡
        u

        0.

    {\displaystyle u_{tt}-u_{xx}+\sin u=0.}

The SG equation gives rise to three elementary excitations/solutions: kinks, breathers and phonons.
Kinks, or topological solitons, can be understood as the solution connecting two nearest identical minima of the periodic substrate potential, thus they are a result of the degeneracy of the ground state. These solutions are

          u

            k

        (
        x
        ,
        t
        )

        4

          tan

            −
            1

        ⁡
        (
        exp
        ⁡
        [
        −
        σ
        γ
        (
        v
        )
        (
        x
        −
        v
        t
        )
        ]
        )
        ,

    {\displaystyle u_{\text{k}}(x,t)=4\tan ^{-1}(\exp[-\sigma \gamma (v)(x-vt)]),}

where

        σ

        ±
        1

    {\displaystyle \sigma =\pm 1}

 is the topological charge. For

        σ

        1

    {\displaystyle \sigma =1}

 the solution is called a kink, and for

        σ

        −
        1

    {\displaystyle \sigma =-1}

 it is an antikink. The kink width

        γ

    {\displaystyle \gamma }

 is determined by the kink velocity

        v

    {\displaystyle v}

, where

        v

    {\displaystyle v}

 is measured in units of the sound velocity

        c

    {\displaystyle c}

 and is

        γ
        (
        v
        )

        1

          /

            1
            −

              v

                2

    {\displaystyle \gamma (v)=1/{\sqrt {1-v^{2}}}}

. For kink motion with

          v

            2

        ≪

          c

            2

    {\displaystyle v^{2}\ll c^{2}}

, the width approximates 1.
The energy of the kink in dimensionless units is

          E

            k

        m

          c

            2

        γ
        (
        v
        )
        ≈
        m

          c

            2

        +

            1
            2

        m

          v

            2

        ,

    {\displaystyle E_{\text{k}}=mc^{2}\gamma (v)\approx mc^{2}+{\frac {1}{2}}mv^{2},}

from which the rest mass of the kink follows as

        m

            2

                π

                  2

                  g

    {\displaystyle m={\frac {2}{\pi ^{2}{\sqrt {g}}}}}

, and the kinks rest energy as

          ϵ

            k

        m

          c

            2

        8

            g

    {\displaystyle \epsilon _{\text{k}}=mc^{2}=8{\sqrt {g}}}

.
Two neighboring static kinks with distance

        R

    {\displaystyle R}

 have energy of repulsion

          v

            int

        ≈

          ϵ

            k

          sinh

            −
            2

        ⁡

            R

              2

                a

                  s

                  g

        ,

    {\displaystyle v_{\text{int}}\approx \epsilon {\text{k}}\sinh ^{-2}{\frac {R}{2a{s}{\sqrt {g}}}},}

whereas kink and antikink attract with interaction

          v

            int

        (
        R
        )
        ≈
        −

          ϵ

            k

          cosh

            −
            2

        ⁡

            R

              2

                a

                  s

                  g

        .

    {\displaystyle v_{\text{int}}(R)\approx -\epsilon {\text{k}}\cosh ^{-2}{\frac {R}{2a{s}{\sqrt {g}}}}.}

A breather is

          u

            br

        (
        x
        ,
        t
        )

        4

          tan

            −
            1

        ⁡

          [

                  1
                  −

                    Ω

                      2

                Ω

                  sin
                  ⁡
                  (
                  Ω
                  t
                  )

                  cosh
                  ⁡
                  (
                  x

                      1
                      −

                        Ω

                          2

                  )

          ]

        ,

    {\displaystyle u_{\text{br}}(x,t)=4\tan ^{-1}\left[{\frac {\sqrt {1-\Omega ^{2}}}{\Omega }}{\frac {\sin(\Omega t)}{\cosh(x{\sqrt {1-\Omega ^{2}}})}}\right],}

which describes nonlinear oscillation with frequency

        Ω

    {\displaystyle \Omega }

, with

        0
        <
        Ω
        <

          ω

            min

    {\displaystyle 0<\Omega <\omega _{\text{min}}}

.
The breather rest energy

          ϵ

            br

        2

          ϵ

            k

            1
            −

              Ω

                2

        .

    {\displaystyle \epsilon _{\text{br}}=2\epsilon _{\text{k}}{\sqrt {1-\Omega ^{2}}}.}

For low frequencies

        Ω
        ≪
        1

    {\displaystyle \Omega \ll 1}

 the breather can be seen as a coupled kink–antikink pair. Kinks and breathers can move along the chain without any dissipative energy loss. Furthermore, any collision between all the excitations of the SG equation result in only a phase shift. Thus kinks and breathers may be considered nonlinear quasi-particles of the SG model. For nearly integrable modifications of the SG equation such as the continuum approximation of the FK model kinks can be considered deformable quasi-particles, provided that discreetness effects are small.

Peierls–Nabarro potential

In the preceding section the excitations of the FK model were derived by considering the model in a continuum-limit approximation. Since the properties of kinks are only modified slightly by the discreteness of the primary model, the SG equation can adequately describe most features and dynamics of the system.
The discrete lattice does, however, influence the kink motion in a unique way with the existence of the Peierls–Nabarro (PN) potential

          V

            PN

        (
        X
        )

    {\displaystyle V_{\text{PN}}(X)}

, where

        X

    {\displaystyle X}

 is the position of the kink's center. The existence of the PN potential is due to the lack of translational invariance in a discrete chain. In the continuum limit the system is invariant for any translation of the kink along the chain. For a discrete chain, only those translations that are an integer multiple of the lattice spacing

          a

            s

    {\displaystyle a_{s}}

 leave the system invariant. The PN barrier,

          E

            PN

    {\displaystyle E_{\text{PN}}}

, is the smallest energy barrier for a kink to overcome so that it can move through the lattice. The value of the PN barrier is the difference between the kink's potential energy for a stable and unstable stationary configuration. The stationary configurations are shown schematically in the figure.
