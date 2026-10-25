# Constant of motion

Constant of motion

In mechanics, a constant of motion is a physical quantity conserved throughout the motion, imposing in effect a constraint on the motion. However, it is a mathematical constraint, the natural consequence of the equations of motion, rather than a physical constraint (which would require extra constraint forces). Common examples include energy, linear momentum, angular momentum and the Laplace–Runge–Lenz vector (for inverse-square force laws).

Applications
Constants of motion are useful because they allow properties of the motion to be derived without solving the equations of motion. In fortunate cases, even the trajectory of the motion can be derived as the intersection of isosurfaces corresponding to the constants of motion. For example, Poinsot's construction shows that the torque-free rotation of a rigid body is the intersection of a sphere (conservation of total angular momentum) and an ellipsoid (conservation of energy), a trajectory that might be otherwise hard to derive and visualize. Therefore, the identification of constants of motion is an important objective in mechanics.

Methods for identifying constants of motion
There are several methods for identifying constants of motion.

The simplest but least systematic approach is the intuitive ("psychic") derivation, in which a quantity is hypothesized to be constant (perhaps because of experimental data) and later shown mathematically to be conserved throughout the motion.
The Hamilton–Jacobi equations provide a commonly used and straightforward method for identifying constants of motion, particularly when the Hamiltonian adopts recognizable functional forms in orthogonal coordinates.
Another approach is to recognize that a conserved quantity corresponds to a symmetry of the Lagrangian. Noether's theorem provides a systematic way of deriving such quantities from the symmetry. For example, conservation of energy results from the invariance of the Lagrangian under shifts in the origin of time, conservation of linear momentum results from the invariance of the Lagrangian under shifts in the origin of space (translational symmetry) and conservation of angular momentum results from the invariance of the Lagrangian under rotations. The converse is also true; every symmetry of the Lagrangian corresponds to a constant of motion, often called a conserved charge or current.
A quantity

        A

    {\displaystyle A}

 is a constant of the motion if its total time derivative is zero

        0

              d
              A

              d
              t

              ∂
              A

              ∂
              t

        +
        {
        A
        ,
        H
        }
        ,

    {\displaystyle 0={\frac {dA}{dt}}={\frac {\partial A}{\partial t}}+{A,H},}

 which occurs when

        A

    {\displaystyle A}

's Poisson bracket with the Hamiltonian equals minus its partial derivative with respect to time

              ∂
              A

              ∂
              t

        −
        {
        A
        ,
        H
        }
        .

    {\displaystyle {\frac {\partial A}{\partial t}}=-{A,H}.}

Another useful result is Poisson's theorem, which states that if two quantities

        A

    {\displaystyle A}

 and

        B

    {\displaystyle B}

 are constants of motion, so is their Poisson bracket

        {
        A
        ,
        B
        }

    {\displaystyle {A,B}}

.
A system with n degrees of freedom, and n constants of motion, such that the Poisson bracket of any pair of constants of motion vanishes, is known as a completely integrable system. Such a collection of constants of motion are said to be in involution with each other. For a closed system (Lagrangian not explicitly dependent on time), the energy of the system is a constant of motion (a conserved quantity).

In quantum mechanics
An observable quantity Q will be a constant of motion if it commutes with the Hamiltonian, H, and it does not itself depend explicitly on time. This is because

            d

              d
              t

        ⟨
        ψ

        Q

        ψ
        ⟩

        −

            1

              i
              ℏ

          ⟨
          ψ

          [

            H
            ,
            Q

          ]

          ψ
          ⟩

        +

          ⟨
          ψ

              d
              Q

              d
              t

          ψ
          ⟩

    {\displaystyle {\frac {d}{dt}}\langle \psi |Q|\psi \rangle =-{\frac {1}{i\hbar }}\left\langle \psi \right|\left[H,Q\right]\left|\psi \right\rangle +\left\langle \psi \right|{\frac {dQ}{dt}}\left|\psi \right\rangle \,}

where

        [
        H
        ,
        Q
        ]

        H
        Q
        −
        Q
        H

    {\displaystyle [H,Q]=HQ-QH\,}

is the commutator relation.

Derivation
Say there is some observable quantity Q which depends on position, momentum and time,

        Q

        Q
        (
        x
        ,
        p
        ,
        t
        )

    {\displaystyle Q=Q(x,p,t)}

And also, that there is a wave function which obeys Schrödinger's equation

        i
        ℏ

              ∂
              ψ

              ∂
              t

        H
        ψ
        .

    {\displaystyle i\hbar {\frac {\partial \psi }{\partial t}}=H\psi .}

Taking the time derivative of the expectation value of Q requires use of the product rule, and results in

                    d

                      d
                      t

                  ⟨
                  Q
                  ⟩

                    d

                      d
                      t

                  ⟨
                  ψ

                Q

                  ψ
                  ⟩

                  (

                        d

                          d
                          t

                      ⟨
                      ψ

                  )

                Q

                  ψ
                  ⟩

                +

                  ⟨
                  ψ

                      d
                      Q

                      d
                      t

                  ψ
                  ⟩

                +

                  ⟨
                  ψ

                Q

                  (

                        d

                          d
                          t

                      ψ
                      ⟩

                  )

                −

                    1

                      i
                      ℏ

                  ⟨

                    H
                    ψ

                Q

                  ψ
                  ⟩

                +

                  ⟨
                  ψ

                      d
                      Q

                      d
                      t

                  ψ
                  ⟩

                +

                    1

                      i
                      ℏ

                  ⟨
                  ψ

                Q

                    H
                    ψ

                  ⟩

                −

                    1

                      i
                      ℏ

                  ⟨
                  ψ

                H
                Q

                  ψ
                  ⟩

                +

                  ⟨
                  ψ

                      d
                      Q

                      d
                      t

                  ψ
                  ⟩

                +

                    1

                      i
                      ℏ

                  ⟨
                  ψ

                Q
                H

                  ψ
                  ⟩

                −

                    1

                      i
                      ℏ

                  ⟨
                  ψ

                  [

                    H
                    ,
                    Q

                  ]

                  ψ
                  ⟩

                +

                  ⟨
                  ψ

                      d
                      Q

                      d
                      t

                  ψ
                  ⟩

    {\displaystyle {\begin{aligned}{\frac {d}{dt}}\left\langle Q\right\rangle &={\frac {d}{dt}}\left\langle \psi \right|Q\left|\psi \right\rangle \[1ex]&=\left({\frac {d}{dt}}\left\langle \psi \right|\right)Q\left|\psi \right\rangle +\left\langle \psi \right|{\frac {dQ}{dt}}\left|\psi \right\rangle +\left\langle \psi \right|Q\left({\frac {d}{dt}}\left|\psi \right\rangle \right)\[1ex]&=-{\frac {1}{i\hbar }}\left\langle H\psi \right|Q\left|\psi \right\rangle +\left\langle \psi \right|{\frac {dQ}{dt}}\left|\psi \right\rangle +{\frac {1}{i\hbar }}\left\langle \psi \right|Q\left|H\psi \right\rangle \[1ex]&=-{\frac {1}{i\hbar }}\left\langle \psi \right|HQ\left|\psi \right\rangle +\left\langle \psi \right|{\frac {dQ}{dt}}\left|\psi \right\rangle +{\frac {1}{i\hbar }}\left\langle \psi \right|QH\left|\psi \right\rangle \[1ex]&=-{\frac {1}{i\hbar }}\left\langle \psi \right|\left[H,Q\right]\left|\psi \right\rangle +\left\langle \psi \right|{\frac {dQ}{dt}}\left|\psi \right\rangle \end{aligned}}}

So finally,

Comment
For an arbitrary state of a Quantum Mechanical system, if H and Q commute, i.e. if

          [

            H
            ,
            Q

          ]

        0

    {\displaystyle \left[H,Q\right]=0}

and Q is not explicitly dependent on time, then

            d

              d
              t

        ⟨
        Q
        ⟩

        0

    {\displaystyle {\frac {d}{dt}}\langle Q\rangle =0}

But if

        ψ

    {\displaystyle \psi }

 is an eigenfunction of the Hamiltonian, then even if

          [

            H
            ,
            Q

          ]

        ≠
        0

    {\displaystyle \left[H,Q\right]\neq 0}

it is still the case that

            d

              d
              t

        ⟨
        Q
        ⟩

        0

    {\displaystyle {\frac {d}{dt}}\langle Q\rangle =0}

provided Q is independent of time.

Derivation

            d

              d
              t

        ⟨
        Q
        ⟩

        −

            1

              i
              ℏ

        ⟨
        ψ

          [

            H
            ,
            Q

          ]

        ψ
        ⟩

        −

            1

              i
              ℏ

        ⟨
        ψ

          (

            H
            Q
            −
            Q
            H

          )

        ψ
        ⟩

    {\displaystyle {\frac {d}{dt}}\langle Q\rangle =-{\frac {1}{i\hbar }}\langle \psi |\left[H,Q\right]|\psi \rangle =-{\frac {1}{i\hbar }}\langle \psi |\left(HQ-QH\right)|\psi \rangle }

Since

        H

        ψ
        ⟩

        E

        ψ
        ⟩

    {\displaystyle H|\psi \rangle =E|\psi \rangle \,}

then

                    d

                      d
                      t

                ⟨
                Q
                ⟩

                −

                    1

                      i
                      ℏ

                  (

                    E
                    ⟨
                    ψ

                    Q

                    ψ
                    ⟩
                    −
                    E
                    ⟨
                    ψ

                    Q

                    ψ
                    ⟩

                  )

                0

    {\displaystyle {\begin{aligned}{\frac {d}{dt}}\langle Q\rangle &=-{\frac {1}{i\hbar }}\left(E\langle \psi |Q|\psi \rangle -E\langle \psi |Q|\psi \rangle \right)\[1ex]&=0\end{aligned}}}

This is the reason why eigenstates of the Hamiltonian are also called stationary states.

Relevance for quantum chaos
In general, an integrable system has constants of motion other than the energy. By contrast, energy is the only constant of motion in a non-integrable system; such systems are termed chaotic. In general, a classical mechanical system can be quantized only if it is integrable; as of 2026, there is no known consistent method for quantizing chaotic dynamical systems.

Integral of motion
A constant of motion may be defined in a given force field as any function of phase-space coordinates (position and velocity, or position and momentum) and time that is constant throughout a trajectory. A subset of the constants of motion are the integrals of motion, or first integrals, defined as any functions of only the phase-space coordinates that are constant along an orbit. Every integral of motion is a constant of motion, but the converse is not true because a constant of motion may depend on time. Examples of integrals of motion are the angular momentum vector,

          L

          x

        ×

          v

    {\displaystyle \mathbf {L} =\mathbf {x} \times \mathbf {v} }

, or a Hamiltonian without time dependence, such as

        H
        (

          x

        ,

          v

        )

            1
            2

          v

            2

        +
        Φ
        (

          x

        )

    {\textstyle H(\mathbf {x} ,\mathbf {v} )={\frac {1}{2}}v^{2}+\Phi (\mathbf {x} )}

. An example of a function that is a constant of motion but not an integral of motion would be the function

        C
        (
        x
        ,
        v
        ,
        t
        )

        x
        −
        v
        t

    {\displaystyle C(x,v,t)=x-vt}

 for an object moving at a constant speed in one dimension.

Dirac observables
In order to extract physical information from gauge theories, one either constructs gauge invariant observables or fixes a gauge. In a canonical language, this usually means either constructing functions which Poisson-commute on the constraint surface with the gauge generating first class constraints or to fix the flow of the latter by singling out points within each gauge orbit. Such gauge invariant observables are thus the `constants of motion' of the gauge generators and referred to as Dirac observables.
