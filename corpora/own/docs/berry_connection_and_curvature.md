# Berry connection and curvature

Berry connection and curvature

In physics, Berry connection and Berry curvature are related concepts which can be viewed, respectively, as a local gauge potential and gauge field associated with the Berry phase or geometric phase. The concept was first introduced by S. Pancharatnam as geometric phase and later elaborately explained and popularized by Michael Berry in a paper published in 1984 emphasizing how geometric phases provide a powerful unifying concept in several branches of classical and quantum physics.

Berry phase
The Berry phase is a geometric phase acquired by a quantum system undergoing adiabatic evolution. It arises from the dependence of the instantaneous eigenstates of the Hamiltonian on a set of externally controlled parameters, collectively denoted by

          R

    {\displaystyle \mathbf {R} }

. As these parameters vary, the eigenstates evolve through the corresponding parameter space and can acquire a phase that depends on the path taken through that space.
Consider a quantum system whose Hamiltonian depends on time through a set of parameters

          R

        (
        t
        )

    {\displaystyle \mathbf {R} (t)}

. The quantum state

        Ψ
        (

          R

        (
        t
        )
        )
        ⟩

    {\displaystyle |\Psi (\mathbf {R} (t))\rangle }

 evolves according to the time-dependent Schrödinger equation

        i
        ℏ

            d

              d
              t

        Ψ
        (

          R

        (
        t
        )
        )
        ⟩

              H
              ^

        (

          R

        (
        t
        )
        )

        Ψ
        (

          R

        (
        t
        )
        )
        ⟩
        .

    {\displaystyle i\hbar {\frac {d}{dt}}|\Psi (\mathbf {R} (t))\rangle ={\hat {H}}(\mathbf {R} (t))|\Psi (\mathbf {R} (t))\rangle .}

At each instant, the instantaneous eigenstates of the Hamiltonian are defined by the eigenvalue equation

              H
              ^

        (

          R

        (
        t
        )
        )

        n
        (

          R

        (
        t
        )
        )
        ⟩

          ε

            n

        (

          R

        (
        t
        )
        )

        n
        (

          R

        (
        t
        )
        )
        ⟩
        ,

    {\displaystyle {\hat {H}}(\mathbf {R} (t))|n(\mathbf {R} (t))\rangle =\varepsilon _{n}(\mathbf {R} (t))|n(\mathbf {R} (t))\rangle ,}

where

          ε

            n

        (

          R

        (
        t
        )
        )

    {\displaystyle \varepsilon _{n}(\mathbf {R} (t))}

 are the instantaneous eigenenergies and

        n
        (

          R

        (
        t
        )
        )
        ⟩

    {\displaystyle |n(\mathbf {R} (t))\rangle }

 are the corresponding instantaneous eigenstates.
Suppose that the system is initially prepared in a non-degenerate eigenstate

        n
        (

          R

        (
        0
        )
        )
        ⟩

    {\displaystyle |n(\mathbf {R} (0))\rangle }

. If the parameters

          R

        (
        t
        )

    {\displaystyle \mathbf {R} (t)}

 vary sufficiently slowly, the adiabatic theorem states that the system remains in the corresponding instantaneous eigenspace throughout the evolution, provided that the eigenvalue remains non-degenerate along the path. Thus, the quantum state can be written as

          Ψ

            n

        (
        t
        )
        ⟩

          c

            n

        (
        t
        )

        n
        (

          R

        (
        t
        )
        )
        ⟩
        ,

    {\displaystyle |\Psi {n}(t)\rangle =c{n}(t)|n(\mathbf {R} (t))\rangle ,}

where

          c

            n

        (
        t
        )

    {\displaystyle c_{n}(t)}

 is a complex coefficient. Since both

          Ψ

            n

        (
        t
        )
        ⟩

    {\displaystyle |\Psi _{n}(t)\rangle }

 and

        n
        (

          R

        (
        t
        )
        )
        ⟩

    {\displaystyle |n(\mathbf {R} (t))\rangle }

 are normalized, it follows that

          c

            n

        (
        t
        )

            2

        1

    {\displaystyle |c_{n}(t)|^{2}=1}

. Consequently,

          c

            n

        (
        t
        )

    {\displaystyle c_{n}(t)}

 can be written as a phase factor,

          c

            n

        (
        t
        )

          e

            i

              θ

                n

            (
            t
            )

        ,

    {\displaystyle c_{n}(t)=e^{i\theta _{n}(t)},}

and hence

          Ψ

            n

        (
        t
        )
        ⟩

          e

            i

              θ

                n

            (
            t
            )

        n
        (

          R

        (
        t
        )
        )
        ⟩
        .

    {\displaystyle |\Psi _{n}(t)\rangle =e^{i\theta _{n}(t)}|n(\mathbf {R} (t))\rangle .}

Substituting this expression into the time-dependent Schrödinger equation the resulting time-evolution of the quantum state is given with

          Ψ

            n

        (
        t
        )
        ⟩

          e

            i

              γ

                n

            (
            t
            )

          e

            −

                i
                ℏ

              ∫

                0

                t

              ε

                n

            (

              R

            (

              t
              ′

            )
            )

            d

              t
              ′

        n
        (

          R

        (
        t
        )
        )
        ⟩
        .

    {\displaystyle |\Psi _{n}(t)\rangle =e^{i\gamma _{n}(t)}e^{-{\frac {i}{\hbar }}\int _{0}^{t}\varepsilon _{n}(\mathbf {R} (t'))\,dt'}|n(\mathbf {R} (t))\rangle .}

The first exponential factor is the geometric phase, with

          γ

            n

        (
        t
        )

    {\displaystyle \gamma _{n}(t)}

 denoting the Berry phase. The second exponential factor is the dynamical phase, which depends on the instantaneous energy and on the time taken during the evolution. The dynamical phase equals the phase of the time evolution of a time-independent Hamiltonian.
The Berry phase originates from the evolution of the instantaneous eigenstate itself as the parameters

          R

    {\displaystyle \mathbf {R} }

 change. Since the eigenstate depends on time only implicitly through

          R

        (
        t
        )

    {\displaystyle \mathbf {R} (t)}

, its total time derivative is

            d

              d
              t

        n
        (

          R

        (
        t
        )
        )
        ⟩

              d

                R

              d
              t

        ⋅

          ∇

              R

        n
        (

          R

        (
        t
        )
        )
        ⟩
        ,

    {\displaystyle {\frac {d}{dt}}|n(\mathbf {R} (t))\rangle ={\frac {d\mathbf {R} }{dt}}\cdot \nabla _{\mathbf {R} }|n(\mathbf {R} (t))\rangle ,}

where

          ∇

              R

    {\displaystyle \nabla _{\mathbf {R} }}

 denotes the gradient with respect to the parameters

          R

    {\displaystyle \mathbf {R} }

. Thus, even though the evolution is adiabatic and the system remains in the same instantaneous eigenstate, the eigenstate itself changes as the system moves through parameter space.
Requiring

          Ψ

            n

        (
        t
        )
        ⟩

    {\displaystyle |\Psi _{n}(t)\rangle }

 to satisfy the time-dependent Schrödinger equation gives the Berry phase as

          γ

            n

        (
        t
        )

        i

          ∫

            0

            t

          ⟨

            n
            (

              R

            (

              t
              ′

            )
            )

                d

                  d

                    t
                    ′

            n
            (

              R

            (

              t
              ′

            )
            )

          ⟩

        d

          t
          ′

        .

    {\displaystyle \gamma _{n}(t)=i\int _{0}^{t}\left\langle n(\mathbf {R} (t'))\vert {\frac {d}{dt'}}\vert n(\mathbf {R} (t'))\right\rangle dt'.}

Using

        d

          R

              d

                R

              d

                t
                ′

        d

          t
          ′

        ,

    {\displaystyle d\mathbf {R} ={\frac {d\mathbf {R} }{dt'}}dt',}

this can be written as a line integral through parameter space,

          γ

            n

        (
        t
        )

        i

          ∫

              R

            (
            0
            )

              R

            (
            t
            )

          ⟨

            n
            (

              R

            )

              ∇

                  R

            n
            (

              R

            )

          ⟩

        ⋅
        d

          R

        .

    {\displaystyle \gamma _{n}(t)=i\int _{\mathbf {R} (0)}^{\mathbf {R} (t)}\left\langle n(\mathbf {R} )|\nabla _{\mathbf {R} }|n(\mathbf {R} )\right\rangle \cdot d\mathbf {R} .}

This expression shows that the Berry phase depends on the path followed by the system in parameter space rather than on the rate at which that path is traversed. The quantity

            A

            n

        (

          R

        )

        i

          ⟨

            n
            (

              R

            )

              ∇

                  R

            n
            (

              R

            )

          ⟩

    {\displaystyle \mathbf {A} _{n}(\mathbf {R} )=i\left\langle n(\mathbf {R} )|\nabla _{\mathbf {R} }|n(\mathbf {R} )\right\rangle }

is known as the Berry connection, so that

          γ

            n

        (
        t
        )

          ∫

              R

            (
            0
            )

              R

            (
            t
            )

            A

            n

        (

          R

        )
        ⋅
        d

          R

        .

    {\displaystyle \gamma _{n}(t)=\int _{\mathbf {R} (0)}^{\mathbf {R} (t)}\mathbf {A} _{n}(\mathbf {R} )\cdot d\mathbf {R} .}

For a cyclic evolution in which the parameters return to their initial values after a period

        T

    {\displaystyle T}

,

          R

        (
        T
        )

          R

        (
        0
        )
        ,

    {\displaystyle \mathbf {R} (T)=\mathbf {R} (0),}

the system traverses a closed path

            C

    {\displaystyle {\mathcal {C}}}

 in parameter space. The Berry phase acquired during this cycle is then

          γ

            n

        (

            C

        )

        i

          ∮

              C

          ⟨

            n
            (

              R

            )

              ∇

                  R

            n
            (

              R

            )

          ⟩

        ⋅
        d

          R

        .

    {\displaystyle \gamma _{n}({\mathcal {C}})=i\oint _{\mathcal {C}}\left\langle n(\mathbf {R} )|\nabla _{\mathbf {R} }|n(\mathbf {R} )\right\rangle \cdot d\mathbf {R} .}

Unlike the dynamical phase, the Berry phase is determined solely by the geometry of the path in parameter space. It therefore represents a geometric property of the quantum state. The Berry phase plays an important role in a variety of physical systems, including cyclotron motion, where it contributes to the semiclassical quantization condition.

Gauge transformation
A gauge transformation can be performed

              n
              ~

        (

          R

        )
        ⟩

          e

            −
            i
            β
            (

              R

            )

        n
        (

          R

        )
        ⟩

    {\displaystyle |{\tilde {n}}(\mathbf {R} )\rangle =e^{-i\beta (\mathbf {R} )}|n(\mathbf {R} )\rangle }

to a new set of states that differ from the original ones only by an

          R

    {\displaystyle \mathbf {R} }

-dependent phase factor. This modifies the open-path Berry phase to be

                γ
                ~

            n

        (
        t
        )

          γ

            n

        (
        t
        )
        +
        β
        (
        t
        )
        −
        β
        (
        0
        )

    {\displaystyle {\tilde {\gamma }}_{n}(t)=\gamma _{n}(t)+\beta (t)-\beta (0)}

. For a closed path, continuity requires that

        β
        (
        T
        )
        −
        β
        (
        0
        )

        2
        π
        m

    {\displaystyle \beta (T)-\beta (0)=2\pi m}

 (

        m

    {\displaystyle m}

 an integer), and it follows that

          γ

            n

    {\displaystyle \gamma _{n}}

 is invariant, modulo

        2
        π

    {\displaystyle 2\pi }

, under an arbitrary gauge transformation.

Berry connection
The closed-path Berry phase defined above can be expressed as

          γ

            n

          ∫

              C

        d

          R

        ⋅

              A

            n

        (

          R

        )

    {\displaystyle \gamma _{n}=\int {\mathcal {C}}d\mathbf {R} \cdot {\mathcal {A}}{n}(\mathbf {R} )}

where

              A

            n

        (

          R

        )

        i
        ⟨
        n
        (

          R

        )

          ∇

              R

        n
        (

          R

        )
        ⟩

    {\displaystyle {\mathcal {A}}_{n}(\mathbf {R} )=i\langle n(\mathbf {R} )|\nabla _{\mathbf {R} }|n(\mathbf {R} )\rangle }

is a vector-valued function known as the Berry connection (or Berry potential). The Berry connection is gauge-dependent, transforming as

                  A

                ~

            n

        (

          R

        )

              A

            n

        (

          R

        )
        +

          ∇

              R

        β
        (

          R

        )

    {\displaystyle {\tilde {\mathcal {A}}}{n}(\mathbf {R} )={\mathcal {A}}{n}(\mathbf {R} )+\nabla _{\mathbf {R} \,}\beta (\mathbf {R} )}

. Hence the local Berry connection

              A

            n

        (

          R

        )

    {\displaystyle {\mathcal {A}}_{n}(\mathbf {R} )}

 can never be physically observable. However, its integral along a closed path, the Berry phase

          γ

            n

    {\displaystyle \gamma _{n}}

, is gauge-invariant up to an integer multiple of

        2
        π

    {\displaystyle 2\pi }

. Thus,

          e

            i

              γ

                n

    {\displaystyle e^{i\gamma _{n}}}

 is absolutely gauge-invariant, and may be related to physical observables.

Berry curvature
The Berry curvature is an anti-symmetric second-rank tensor derived from the Berry connection via

          Ω

            n
            ,
            μ
            ν

        (

          R

        )

            ∂

              ∂

                R

                  μ

              A

            n
            ,
            ν

        (

          R

        )
        −

            ∂

              ∂

                R

                  ν

              A

            n
            ,
            μ

        (

          R

        )
        .

    {\displaystyle \Omega {n,\mu \nu }(\mathbf {R} )={\partial \over \partial R^{\mu }}{\mathcal {A}}{n,\nu }(\mathbf {R} )-{\partial \over \partial R^{\nu }}{\mathcal {A}}_{n,\mu }(\mathbf {R} ).}

In a three-dimensional parameter space the Berry curvature can be written in the pseudovector form

            Ω

            n

        (

          R

        )

          ∇

              R

        ×

              A

            n

        (

          R

        )
        .

    {\displaystyle \mathbf {\Omega } _{n}(\mathbf {R} )=\nabla {\mathbf {R} }\times {\mathcal {A}}{n}(\mathbf {R} ).}

The tensor and pseudovector forms of the Berry curvature are related to each other through the Levi-Civita antisymmetric tensor as

          Ω

            n
            ,
            μ
            ν

          ϵ

            μ
            ν
            ξ

            Ω

            n
            ,
            ξ

    {\displaystyle \Omega _{n,\mu \nu }=\epsilon _{\mu \nu \xi }\,\mathbf {\Omega } _{n,\xi }}

. In contrast to the Berry connection, which is physical only after integrating around a closed path, the Berry curvature is a gauge-invariant local manifestation of the geometric properties of the wavefunctions in the parameter space, and has proven to be an essential physical ingredient for understanding a variety of electronic properties.
For a closed path

            C

    {\displaystyle {\mathcal {C}}}

 that forms the boundary of a surface

            S

    {\displaystyle {\mathcal {S}}}

, the closed-path Berry phase can be rewritten using Stokes' theorem as

          γ

            n

          ∫

              S

        d

          S

        ⋅

            Ω

            n

        (

          R

        )
        .

    {\displaystyle \gamma _{n}=\int _{\mathcal {S}}d\mathbf {S} \cdot \mathbf {\Omega } _{n}(\mathbf {R} ).}

If the surface is a closed manifold, the boundary term vanishes, but the indeterminacy of the boundary term modulo

        2
        π

    {\displaystyle 2\pi }

 manifests itself in the Chern theorem, which states that the integral of the Berry curvature over a closed manifold is quantized in units of

        2
        π

    {\displaystyle 2\pi }

. This number is the so-called Chern number, and is essential for understanding various quantization effects.
Finally, by using

          ⟨

            n

            ∂
            H

              /

            ∂

              R

              n
              ′

          ⟩

          ⟨

            ∂
            n

              /

            ∂

              R

              n
              ′

          ⟩

        (

          ε

            n

        −

          ε

              n
              ′

        )

    {\displaystyle \left\langle n|\partial H/\partial \mathbf {R} |n'\right\rangle =\left\langle \partial n/\partial \mathbf {R} |n'\right\rangle (\varepsilon _{n}-\varepsilon _{n'})}

 for

        n
        ≠

          n
          ′

    {\displaystyle n\neq n'}

, the Berry curvature can also be written as a summation over all the other eigenstates in the form

          Ω

            n
            ,
            μ
            ν

        (

          R

        )

        i

          ∑

              n
              ′

            ≠
            n

            1

              (

                ε

                  n

              −

                ε

                    n
                    ′

                )

                  2

            (

                ⟨
                n

                    ∂
                    H

                    ∂

                      R

                        μ

                  n
                  ′

                ⟩

                ⟨

                  n
                  ′

                    ∂
                    H

                    ∂

                      R

                        ν

                n
                ⟩

              −

                ⟨
                n

                    ∂
                    H

                    ∂

                      R

                        ν

                  n
                  ′

                ⟩

                ⟨

                  n
                  ′

                    ∂
                    H

                    ∂

                      R

                        μ

                n
                ⟩

            )

        .

    {\displaystyle \Omega _{n,\mu \nu }(\mathbf {R} )=i\sum _{n'\neq n}{\frac {1}{(\varepsilon _{n}-\varepsilon {n'})^{2}}}{\left(\left\langle n\right|{\frac {\partial H}{\partial R{\mu }}}\left|n'\right\rangle \left\langle n'\right|{\frac {\partial H}{\partial R_{\nu }}}\left|n\right\rangle -\left\langle n\right|{\frac {\partial H}{\partial R_{\nu }}}\left|n'\right\rangle \left\langle n'\right|{\frac {\partial H}{\partial R_{\mu }}}\left|n\right\rangle \right)}.}

Note that the curvature of the nth energy level is contributed by all the other energy levels. That is, the Berry curvature can
be viewed as the result of the residual interaction of
those projected-out eigenstates. This gives the local conservation law for the Berry
curvature,

          ∑

            n

          Ω

            n
            ,
            μ
            ν

        (

          R

        )

        0
        ,

    {\displaystyle \sum _{n}\Omega _{n,\mu \nu }(\mathbf {R} )=0,}

  if we sum over all possible energy levels for each value of

          R

        .

    {\displaystyle \mathbf {R} .}

This equation also offers the advantage that no differentiation on the eigenstates is involved, and thus it can be
computed under any gauge choice.

Example: Spinor in a magnetic field
The Hamiltonian of a spin-1/2 particle in a magnetic field can be written as

        H

        μ

          σ

        ⋅

          B

        ,

    {\displaystyle H=\mu \mathbf {\sigma } \cdot \mathbf {B} ,}

where

          σ

    {\displaystyle \mathbf {\sigma } }

 denote the Pauli matrices,

        μ

    {\displaystyle \mu }

 is the magnetic moment, and B is the magnetic field. In three dimensions, the eigenstates have energies

        ±
        μ
        B

    {\displaystyle \pm \mu B}

 and their eigenvectors are

          u

            −

        ⟩

            (

                  sin
                  ⁡

                      θ
                      2

                    e

                      −
                      i
                      ϕ

                  −
                  cos
                  ⁡

                      θ
                      2

            )

        ,

          u

            +

        ⟩

            (

                  cos
                  ⁡

                      θ
                      2

                    e

                      −
                      i
                      ϕ

                  sin
                  ⁡

                      θ
                      2

            )

        .

    {\displaystyle |u_{-}\rangle ={\begin{pmatrix}\sin {\theta \over 2}e^{-i\phi }\-\cos {\theta \over 2}\end{pmatrix}},|u_{+}\rangle ={\begin{pmatrix}\cos {\theta \over 2}e^{-i\phi }\\sin {\theta \over 2}\end{pmatrix}}.}

Now consider the

          u

            −

        ⟩

    {\displaystyle |u_{-}\rangle }

 state. Its Berry connection can be computed as

              A

            θ

        ⟨

          u

            −

        i

            1
            r

          ∂

            θ

          u

            −

        ⟩

        0
        ,

    {\textstyle {\mathcal {A}}{\theta }=\langle u{-}|i{\frac {1}{r}}\partial {\theta }|u{-}\rangle =0,}

              A

            ϕ

        ⟨

          u

            −

        i

              1

                r
                sin
                ⁡

                  θ

          ∂

            ϕ

          u

            −

        ⟩

                sin

                  2

              ⁡

                  θ
                  2

              r
              sin
              ⁡

                θ

    {\displaystyle {\mathcal {A}}{\phi }=\langle u{-}|i{\tfrac {1}{r\sin {\theta }}}\partial {\phi }|u{-}\rangle ={\frac {\sin ^{2}{\theta \over 2}}{r\sin {\theta }}}}

, and the Berry curvature is

          Ω

            r

            1

              r
              sin
              ⁡

                θ

        [

          ∂

            θ

        (

              A

            ϕ

        sin
        ⁡

          θ

        )
        −

          ∂

            ϕ

              A

            θ

        ]

              r
              ^

            1

              2

                r

                  2

              r
              ^

        .

    {\displaystyle \ \Omega _{r}={\frac {1}{r\sin {\theta }}}[\partial {\theta }({\mathcal {A}}{\phi }\sin {\theta })-\partial {\phi }{\mathcal {A}}{\theta }]{\hat {r}}={\frac {1}{2r^{2}}}{\hat {r}}.}

If we choose a new gauge by multiplying

          u

            −

        ⟩

    {\displaystyle |u_{-}\rangle }

 by

          e

            i
            ϕ

    {\displaystyle e^{i\phi }}

 (or any other phase

          e

            i
            α
            ϕ

    {\displaystyle e^{i\alpha \phi }}

,

        α
        ∈

          R

    {\displaystyle \alpha \in \mathbb {R} }

), the Berry connections are

              A

            θ

        0

    {\displaystyle {\mathcal {A}}_{\theta }=0}

 and

              A

            ϕ

        −

                cos

                  2

              ⁡

                  θ
                  2

              r
              sin
              ⁡

                θ

    {\displaystyle {\mathcal {A}}_{\phi }=-{\frac {\cos ^{2}{\theta \over 2}}{r\sin {\theta }}}}

, while the Berry curvature remains the same. This is consistent with the conclusion that the Berry connection is gauge-dependent while the Berry curvature is not.
The Berry curvature per solid angle is given by

              Ω
              ¯

            θ
            ϕ

          Ω

            θ
            ϕ

          /

        sin
        ⁡
        θ

        1

          /

        2

    {\displaystyle {\overline {\Omega }}_{\theta \phi }=\Omega _{\theta \phi }/\sin \theta =1/2}

. In this case, the Berry phase corresponding to any given path on the unit sphere

              S

            2

    {\displaystyle {\mathcal {S}}^{2}}

 in magnetic-field space is just half the solid angle subtended by the path.
The integral of the Berry curvature over the whole sphere is therefore exactly

        2
        π

    {\displaystyle 2\pi }

, so that the Chern number is unity, consistent with the Chern theorem.

Applications in crystals
The Berry phase plays an important role in modern investigations of electronic properties in crystalline solids and in the theory of the quantum Hall effect.
The periodicity of the crystalline potential allows the application of the Bloch theorem, which states that the Hamiltonian eigenstates take the form

          ψ

            n

              k

        (

          r

        )

          e

            i

              k

            ⋅

              r

          u

            n

              k

        (

          r

        )
        ,

    {\displaystyle \psi {n\mathbf {k} }(\mathbf {r} )=e^{i\mathbf {k} \cdot \mathbf {r} }u{n\mathbf {k} }(\mathbf {r} ),}

where

        n

    {\displaystyle n}

 is a band index,

          k

    {\displaystyle \mathbf {k} }

 is a wavevector in the reciprocal-space (Brillouin zone), and

          u

            n

              k

        (

          r

        )

    {\displaystyle u_{n\mathbf {k} }(\mathbf {r} )}

 is a periodic function of

          r

    {\displaystyle \mathbf {r} }

. Due to translational symmetry, the momentum operator

                p
                ^

            i

    {\displaystyle {\hat {p}}_{i}}

 could be replaced with

            m
            ℏ

        ∂
        H

          /

        ∂

          k

            i

    {\displaystyle {\frac {m}{\hbar }}\partial H/\partial k_{i}}

 by the Peierls substitution and the wavevector

          k

    {\displaystyle \mathbf {k} }

 plays the role of the parameter

          R

    {\displaystyle \mathbf {R} }

. Thus, one can define Berry phases, connections, and curvatures in the reciprocal space. For example, in an
N-band system, the Berry connection of the nth band in reciprocal space is

              A

            n

        (

          k

        )

        i
        ⟨

          u

            n

              k

          ∇

              k

          u

            n

              k

        ⟩
        .

    {\displaystyle {\mathcal {A}}{n}(\mathbf {k} )=i\langle u{n\mathbf {k} }|\nabla {\mathbf {k} }|u{n\mathbf {k} }\rangle .}

In the system, the Berry curvature of the nth band

          Ω

            n
            ,
            μ
            ν

        (

          k

        )

    {\displaystyle \Omega _{n,\mu \nu }(\mathbf {k} )}

 is given by all the other N − 1 bands for each value of

          k

        .

    {\displaystyle \mathbf {k} .}

  In a 2D crystal, the Berry curvature only has
the component out of the plane and behaves as a pseudoscalar. It is because there only exists in-plane translational symmetry when translational symmetry is broken along z direction for a 2D crystal.
Because the Bloch theorem also implies that the reciprocal space itself is closed, with the Brillouin zone having the topology of a 3-torus in three dimensions, the requirements of integrating over a closed loop or manifold can easily be satisfied. In this way, such properties as the electric polarization, orbital magnetization, anomalous Hall conductivity, and orbital magnetoelectric coupling can be expressed in terms of Berry phases, connections, and curvatures.
