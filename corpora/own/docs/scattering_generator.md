# Scattering generator

Scattering generator

In scattering theory, the scattering generator or S-generator is an effective Hamiltonian that directly generates the interaction-picture time evolution from far past to far future.
In quantum mechanics and quantum field theory, the scattering generator is the log of the S-matrix:

              Ω
              ^

        i
        ℏ
        log
        ⁡

              S
              ^

    {\displaystyle {\hat {\Omega }}=i\hbar \log {\hat {S}}}

. While the concept traces back to '80s,
an active revival has taken place in the modern literature on scattering theory and its applications. In classical mechanics, the classical scattering generator describes the Hamiltonian generator of the
S-symplectomorphism, which is the classical analog of the S-matrix. The quantum and classical scattering generators
are related by the classical limit by a precise correspondence.

History and Motivation

Exponential representation of S-matrix
The idea of taking the log of S-matrix
traces back to early days of quantum field theory
and has been known as the exponential representation
of S-matrix, which refers to the formula

                      S
                      ^

                exp
                ⁡

                    (

                    1

                      i
                      ℏ

                      Ω
                      ^

                    )

                .

    {\displaystyle {\begin{aligned}{\hat {S}}\,=\,\exp {\bigg (}{\frac {1}{i\hbar }}\,{\hat {\Omega }}{\bigg )}\,.\end{aligned}}}

Exponential representation as unit-time flow
Modern literature interprets

              Ω
              ^

    {\displaystyle {\hat {\Omega }}}

 as the unit-time generator of scattering, while prototypical observations trace back to the '80s. The above formula is viewed
as an effective time evolution through dimensionless unit time:

                      S
                      ^

                exp
                ⁡

                    (

                      (

                        “

                          Δ

                      t

                      1

                        ”

                      )

                      i
                      ℏ

                      Ω
                      ^

                    )

                .

    {\displaystyle {\begin{aligned}{\hat {S}}\,=\,\exp {\bigg (}{\frac {({\text{“}}{\mathit {\Delta }}t=1{\text{”}})}{i\hbar }}\,{\hat {\Omega }}{\bigg )}\,.\end{aligned}}}

This means that the result of scattering

              S
              ^

    {\displaystyle {\hat {S}}}

 is directly reproduced within "one second" (

            Δ

        t

        1

    {\displaystyle {\mathit {\Delta }}t=1}

) by taking

              Ω
              ^

    {\displaystyle {\hat {\Omega }}}

 as the Hamiltonian.
In this sense,

              Ω
              ^

    {\displaystyle {\hat {\Omega }}}

 is viewed as an "effective Hamiltonian" that encapsulates and summarizes
the entire history of scattering from

        t

        −
        ∞

    {\displaystyle t=-\infty }

 to

        t

        +
        ∞

    {\displaystyle t=+\infty }

.

Manifest unitarity
The motivation behind the exponential representation is manifest unitarity in scattering, i.e., trivializing the conservation of probability. Provided hermiticity

                Ω
                ^

            †

              Ω
              ^

    {\displaystyle {\hat {\Omega }}^{\dagger }={\hat {\Omega }}}

,the S-matrix is automatically unitary as

                        S
                        ^

                    †

                      S
                      ^

                exp
                ⁡

                    (

                  −

                      1

                        i
                        ℏ

                        Ω
                        ^

                    )

                exp
                ⁡

                    (

                    1

                      i
                      ℏ

                      Ω
                      ^

                    )

                      1
                      ^

                .

    {\displaystyle {\begin{aligned}{\hat {S}}^{\dagger }{\hat {S}}\,=\,\exp {\bigg (}{-{\frac {1}{i\hbar }}\,{\hat {\Omega }}}{\bigg )}\exp {\bigg (}{\frac {1}{i\hbar }}\,{\hat {\Omega }}{\bigg )}\,=\,{\hat {1}}\,.\end{aligned}}}

This also applies for the classical scattering generator as well, the conservation of classical probability in the sense of Liouville theorem.

Definition by Magnus Expansion
The S-matrix is concretely defined and computed by the Dyson series,
which expands a time-ordered exponential.The scattering generator is concretely defined and computed by
the Magnus series.

In quantum mechanics
For the quantum scattering generator

              Ω
              ^

    {\displaystyle {\hat {\Omega }}}

, the Magnus series formula reads

                      Ω
                      ^

                ∫
                d

                  t

                    1

                        V
                        ^

                    I

                (

                  t

                    1

                )
                +

                    1

                      2
                      (
                      i
                      ℏ

                        )

                          1

                  ∫

                      t

                        1

                      t

                        2

                  d

                    2

                t

                [

                        V
                        ^

                    I

                (

                  t

                    1

                )
                ,

                        V
                        ^

                    I

                (

                  t

                    2

                )
                ]

                +

                    1

                      6
                      (
                      i
                      ℏ

                        )

                          2

                  ∫

                      t

                        1

                      t

                        2

                      t

                        3

                  d

                    3

                t

                    (

                  [

                          V
                          ^

                      I

                  (

                    t

                      1

                  )
                  ,
                  [

                          V
                          ^

                      I

                  (

                    t

                      2

                  )
                  ,

                          V
                          ^

                      I

                  (

                    t

                      3

                  )
                  ]
                  ]
                  +
                  [

                          V
                          ^

                      I

                  (

                    t

                      3

                  )
                  ,
                  [

                          V
                          ^

                      I

                  (

                    t

                      2

                  )
                  ,

                          V
                          ^

                      I

                  (

                    t

                      1

                  )
                  ]
                  ]

                    )

                +
                ⋯

                .

    {\displaystyle {\begin{aligned}{\hat {\Omega }}\,=\,{}&{}\int dt_{1}\,\,{\hat {V}}{\text{I}}(t{1})+{\frac {1}{2(i\hbar )^{1}}}\int {t{1}>t_{2}}d^{2}t\,\,[{\hat {V}}{\text{I}}(t{1}),{\hat {V}}{\text{I}}(t{2})]\{}&{}+{\frac {1}{6(i\hbar )^{2}}}\int {t{1}>t_{2}>t_{3}}d^{3}t\,\,{\Big (}\,{[{\hat {V}}{\text{I}}(t{1}),[{\hat {V}}{\text{I}}(t{2}),{\hat {V}}{\text{I}}(t{3})]]+[{\hat {V}}{\text{I}}(t{3}),[{\hat {V}}{\text{I}}(t{2}),{\hat {V}}{\text{I}}(t{1})]]}\,{\Big )}+\cdots \,.\end{aligned}}}

This describes a sum of integrals whose integrands are nested commutators between the interaction-picture potential

                V
                ^

              I

        (
        t
        )

    {\displaystyle {\hat {V}}_{\mathrm {I} }(t)}

 at different times. Provided the free and interaction Hamiltonians are Hermitian, the scattering generator

              Ω
              ^

    {\displaystyle {\hat {\Omega }}}

 is also a Hermitian operator.

In classical mechanics
For the classical scattering generator

        Ω

    {\displaystyle \Omega }

, the Magnus series formula reads

                Ω

                ∫
                d

                  t

                    1

                  V

                    I

                (

                  t

                    1

                )
                +

                    1
                    2

                  ∫

                      t

                        1

                      t

                        2

                  d

                    2

                t

                {

                  V

                    I

                (

                  t

                    1

                )
                ,

                  V

                    I

                (

                  t

                    2

                )
                }

                +

                    1
                    6

                  ∫

                      t

                        1

                      t

                        2

                      t

                        3

                  d

                    3

                t

                    (

                  {

                    V

                      I

                  (

                    t

                      1

                  )
                  ,
                  {

                    V

                      I

                  (

                    t

                      2

                  )
                  ,

                    V

                      I

                  (

                    t

                      3

                  )
                  }
                  }
                  +
                  {

                    V

                      I

                  (

                    t

                      3

                  )
                  ,
                  {

                    V

                      I

                  (

                    t

                      2

                  )
                  ,

                    V

                      I

                  (

                    t

                      1

                  )
                  }
                  }

                    )

                +
                ⋯

                ,

    {\displaystyle {\begin{aligned}\Omega \,=\,{}&{}\int dt_{1}\,\,V_{\text{I}}(t_{1})+{\frac {1}{2}}\int {t{1}>t_{2}}d^{2}t\,\,{V_{\text{I}}(t_{1}),V_{\text{I}}(t_{2})}\{}&{}+{\frac {1}{6}}\int {t{1}>t_{2}>t_{3}}d^{3}t\,\,{\Big (}\,{{V_{\text{I}}(t_{1}),{V_{\text{I}}(t_{2}),V_{\text{I}}(t_{3})}}+{V_{\text{I}}(t_{3}),{V_{\text{I}}(t_{2}),V_{\text{I}}(t_{1})}}}\,{\Big )}+\cdots \,,\end{aligned}}}

which can be deduced by taking the classical limit to the above quantum formula
n spirit of the correspondence principle and canonical quantization.
This assumes a Hamiltonian system defined on a phase space equipped with a Poisson bracket.

        Ω

    {\displaystyle \Omega }

 is a function on the phase space.

          V

            I

        (
        t
        )

    {\displaystyle V_{\text{I}}(t)}

 is a time-dependent function on the phase space,
encoding the classical interaction Hamiltonian in the interaction picture.
More precisely, the frameworks of phase space formulation and deformation quantization
have been employed to establish the relationship between

              Ω
              ^

    {\displaystyle {\hat {\Omega }}}

 and

        Ω

    {\displaystyle \Omega }

in a rigorous fashion. The classical scattering generator is well-defined on Poisson manifolds.
The S-symplectomorphism

        S

    {\displaystyle S}

,
i.e., the canonical transformation from the initial phase space to the final phase space
in classical scattering, arises by exponentiating the Hamiltonian vector field of

        Ω

    {\displaystyle \Omega }

.

Use

In quantum mechanics
In the interaction picture, the quantum Liouville equation
reads

                    d

                      d
                      t

                        ρ
                        ^

                      I

                (
                t
                )

                    1

                      i
                      ℏ

                [

                        V
                        ^

                      I

                (
                t
                )
                ,

                        ρ
                        ^

                      I

                (
                t
                )
                ]

                ,

    {\displaystyle {\begin{aligned}{\frac {d}{dt}}\,{\hat {\rho }}{\mathrm {I} }(t)\,=\,{\frac {1}{i\hbar }}\,[{\hat {V}}{\mathrm {I} }(t),{\hat {\rho }}_{\mathrm {I} }(t)]\,,\end{aligned}}}

where

                ρ
                ^

              I

        (
        t
        )

    {\displaystyle {\hat {\rho }}_{\mathrm {I} }(t)}

is the density matrix in the interaction picture. Solving this equation gives rise to the S-matrix

              S
              ^

    {\displaystyle {\hat {S}}}

 as

                        ρ
                        ^

                      I

                (
                +
                ∞
                )

                      S
                      ^

                        ρ
                        ^

                      I

                (
                −
                ∞
                )

                      S
                      ^

                    −
                    1

                    A
                    d

                        S
                        ^

                        ρ
                        ^

                      I

                (
                −
                ∞
                )

                ,

    {\displaystyle {\begin{aligned}{\hat {\rho }}{\mathrm {I} }(+\infty )\,=\,{\hat {S}}\,{\hat {\rho }}{\mathrm {I} }(-\infty )\,{\hat {S}}{}^{-1}\,=\,\mathrm {Ad} {\hat {S}}\,{\hat {\rho }}{\mathrm {I} }(-\infty )\,,\end{aligned}}}

in terms of the adjoint action

            A
            d

                S
                ^

    {\displaystyle \mathrm {Ad} _{\hat {S}}}

.
The formula

              S
              ^

          e

                  Ω
                  ^

              /

            i
            ℏ

    {\displaystyle {\hat {S}}=e^{{\hat {\Omega }}/i\hbar }}

 then implies

                        ρ
                        ^

                      I

                (
                +
                ∞
                )

                exp
                ⁡

                    (

                      a
                      d

                            Ω
                            ^

                        /

                      i
                      ℏ

                    )

                        ρ
                        ^

                      I

                (
                −
                ∞
                )

                ,

                exp
                ⁡

                    (

                      1

                        i
                        ℏ

                  [

                        Ω
                        ^

                  ,

                  ]

                    )

                        ρ
                        ^

                      I

                (
                −
                ∞
                )

                ,

                        ρ
                        ^

                      I

                (
                −
                ∞
                )
                +

                    1

                      i
                      ℏ

                [

                      Ω
                      ^

                ,

                        ρ
                        ^

                      I

                (
                −
                ∞
                )
                ]
                +

                    1

                      2
                      !
                      (
                      i
                      ℏ

                        )

                          2

                [

                      Ω
                      ^

                ,
                [

                      Ω
                      ^

                ,

                        ρ
                        ^

                      I

                (
                −
                ∞
                )
                ]
                ]
                +
                ⋯

                ,

    {\displaystyle {\begin{aligned}{\hat {\rho }}_{\mathrm {I} }(+\infty )\,&=\,\exp {\Big (}\,{\mathrm {ad} {{\hat {\Omega }}/i\hbar }}\,{\Big )}\,{\hat {\rho }}{\mathrm {I} }(-\infty )\,,\\,&=\,\exp {\bigg (}\,{{\frac {1}{i\hbar }}\,[{\hat {\Omega }},\,\,\,]}\,{\bigg )}\,{\hat {\rho }}{\mathrm {I} }(-\infty )\,,\\,&=\,{\hat {\rho }}{\mathrm {I} }(-\infty )+{\frac {1}{i\hbar }}\,[{\hat {\Omega }},{\hat {\rho }}{\mathrm {I} }(-\infty )]+{\frac {1}{2!(i\hbar )^{2}}}\,[{\hat {\Omega }},[{\hat {\Omega }},{\hat {\rho }}{\mathrm {I} }(-\infty )]]+\cdots \,,\end{aligned}}}

which describes a sum of nested commutators.
This describes that the entire time evolution of the quantum (ensemble) state
from

                ρ
                ^

              I

        (
        −
        ∞
        )

    {\displaystyle {\hat {\rho }}_{\mathrm {I} }(-\infty )}

to

                ρ
                ^

              I

        (
        +
        ∞
        )

    {\displaystyle {\hat {\rho }}_{\mathrm {I} }(+\infty )}

is reproduced by a unit-time, exponentiated adjoint action
of the scattering generator

              Ω
              ^

    {\displaystyle {\hat {\Omega }}}

.

In classical mechanics
In classical Hamiltonian mechanics, an analogous formula holds for the
classical probability distribution

        ρ
        (
        t
        )

    {\displaystyle \rho (t)}

,
representing a statistical ensemble
and evolving under the classical Liouville equation:

                  ρ

                      I

                (
                +
                ∞
                )

                exp
                ⁡

                    (

                  {
                  Ω
                  ,

                  }

                    )

                    ρ

                      I

                (
                −
                ∞
                )

                ,

                    ρ

                      I

                (
                −
                ∞
                )
                +
                {

                  Ω

                ,

                    ρ

                      I

                (
                −
                ∞
                )
                }
                +

                    1

                      2
                      !

                {

                  Ω

                ,
                {

                  Ω

                ,

                    ρ

                      I

                (
                −
                ∞
                )
                }
                }
                +
                ⋯

                .

    {\displaystyle {\begin{aligned}\rho {\mathrm {I} }(+\infty )\,&=\,\exp {\Big (}\,{{\Omega ,\,\,\,}}\,{\Big )}\,{\rho }{\mathrm {I} }(-\infty )\,,\\,&=\,{\rho }{\mathrm {I} }(-\infty )+{{\Omega },{\rho }{\mathrm {I} }(-\infty )}+{\frac {1}{2!}}\,{{\Omega },{{\Omega },{\rho }_{\mathrm {I} }(-\infty )}}+\cdots \,.\end{aligned}}}

This is the nested Poisson bracket formula in the S-symplectomorphism framework.

Impulse formula
In quantum mechanics, the expectation value of an observable

                O

              ^

    {\displaystyle {\hat {\mathcal {O}}}}

 with respect to the density matrix

                ρ
                ^

            I

        (
        t
        )

    {\displaystyle {\hat {\rho }}_{\text{I}}(t)}

 in the interaction picture is

                    ⟨

                        O

                      ^

                      ⟩

                    t

                  T
                  r

                    (

                        ρ
                        ^

                    I

                (
                t
                )

                        O

                      ^

                    )

                .

    {\displaystyle {\begin{aligned}{\big \langle }{\hat {\mathcal {O}}}{\big \rangle }{t}\,=\,\mathrm {Tr} {\big (}\,{\hat {\rho }}{\text{I}}(t)\,{\hat {\mathcal {O}}}\,{\big )}\,.\end{aligned}}}

The impulse of observables in quantum scattering is

                    ⟨

                        O

                      ^

                      ⟩

                    +
                    ∞

                −

                    ⟨

                        O

                      ^

                      ⟩

                    −
                    ∞

                  e

                    [

                    ,

                          Ω
                          ^

                      /

                    i
                    ℏ
                    ]

                        O

                      ^

                −

                        O

                      ^

                    1

                      i
                      ℏ

                [

                        O

                      ^

                ,

                      Ω
                      ^

                ]
                +

                    1

                      2
                      !
                      (
                      i
                      ℏ

                        )

                          2

                [
                [

                        O

                      ^

                ,

                      Ω
                      ^

                ]
                ,

                      Ω
                      ^

                ]
                +
                ⋯

                .

    {\displaystyle {\begin{aligned}{\big \langle }{\hat {\mathcal {O}}}{\big \rangle }{+\infty }-{\big \langle }{\hat {\mathcal {O}}}{\big \rangle }{-\infty }\,&=\,e^{[\,\,\,\,,{\hat {\Omega }}/i\hbar ]}{\hat {\mathcal {O}}}-{\hat {\mathcal {O}}}\,=\,{\frac {1}{i\hbar }}\,[{\hat {\mathcal {O}}},{\hat {\Omega }}]+{\frac {1}{2!(i\hbar )^{2}}}\,[[{\hat {\mathcal {O}}},{\hat {\Omega }}],{\hat {\Omega }}]+\cdots \,.\end{aligned}}}

In classical mechanics, the expectation value of an observable

            O

    {\displaystyle {\mathcal {O}}}

 with respect to the probability distribution

          ρ

            I

        (
        t
        )

    {\displaystyle \rho _{\text{I}}(t)}

in the interaction picture is

                    ⟨

                    O

                      ⟩

                    t

                ∫

                  ρ

                    I

                (
                t
                )

                    O

                μ

                ,

    {\displaystyle {\begin{aligned}{\big \langle }{\mathcal {O}}{\big \rangle }_{t}\,=\,\int \rho _{\text{I}}(t)\,{\mathcal {O}}\,\,\mu \,,\end{aligned}}}

where

        μ

    {\displaystyle \mu }

 is the Liouville measure.
The impulse of observables in classical scattering is then

                    ⟨

                    O

                      ⟩

                    +
                    ∞

                −

                    ⟨

                    O

                      ⟩

                    −
                    ∞

                  e

                    {

                    ,
                    Ω
                    }

                    O

                −

                    O

                {

                    O

                ,

                  Ω

                }
                +

                    1

                      2
                      !

                {
                {

                    O

                ,

                  Ω

                }
                ,

                  Ω

                }
                +
                ⋯

                .

    {\displaystyle {\begin{aligned}{\big \langle }{\mathcal {O}}{\big \rangle }{+\infty }-{\big \langle }{\mathcal {O}}{\big \rangle }{-\infty }\,&=\,e^{{\,\,\,,\Omega }}{\mathcal {O}}-{\mathcal {O}}\,=\,{{\mathcal {O}},{\Omega }}+{\frac {1}{2!}}\,{{{\mathcal {O}},{\Omega }},{\Omega }}+\cdots \,.\end{aligned}}}

In both cases, the scattering generator acts on the observables as a Hamiltonian (thus in terms of right adjoint action). Note that the classical impulse formula
also follows by implementing the pullback by the inverse of the S-symplectomorphism,
which maps functions on the final phase space to functions on the initial phase space.

Conventions and Terminology
Another prominent convention for the scattering generator uses the definition

              N
              ^

        −
        i
        ℏ
        log
        ⁡

              S
              ^

    {\displaystyle {\hat {N}}=-i\hbar \log {\hat {S}}}

and the name "N-matrix." Technically speaking,
the scattering generator should be distinguished from
the Magnusian,
which is a broader term that can refer to the logarithm of time-evolution maps (not necessarily in scattering). A clarification has been made between the classical scattering generator, the eikonal phase, and the on-shell action.
