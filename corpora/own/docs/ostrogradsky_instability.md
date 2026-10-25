# Ostrogradsky instability

Ostrogradsky instability

In applied mathematics, the Ostrogradsky instability is a feature of some solutions of theories having equations of motion with more than two time derivatives (higher-derivative theories). It is suggested by a theorem of Mikhail Ostrogradsky in classical mechanics according to which a non-degenerate Lagrangian dependent on time derivatives higher than the first corresponds to a Hamiltonian unbounded from below. As usual, the Hamiltonian is associated with the Lagrangian via a Legendre transform. The Ostrogradsky instability has been proposed as an explanation as to why no differential equations of higher order than two appear to describe physical phenomena.
However, Ostrogradsky's theorem does not imply that all solutions of higher-derivative theories are unstable as many counterexamples are known.

Outline of proof
Source:
The main points of the proof can be made clearer by considering a one-dimensional system with a Lagrangian

        L
        (
        q
        ,

              q
              ˙

        ,

              q
              ¨

        )

    {\displaystyle L(q,{\dot {q}},{\ddot {q}})}

. The Euler–Lagrange equation is

              ∂
              L

              ∂
              q

        −

            d

              d
              t

              ∂
              L

              ∂

                    q
                    ˙

        +

              d

                2

              d

                t

                  2

              ∂
              L

              ∂

                    q
                    ¨

        0.

    {\displaystyle {\frac {\partial L}{\partial q}}-{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q}}}}+{\frac {d^{2}}{dt^{2}}}{\frac {\partial L}{\partial {\ddot {q}}}}=0.}

Non-degeneracy of

        L

    {\displaystyle L}

 means that the canonical coordinates can be expressed in terms of the derivatives of

          q

    {\displaystyle {q}}

 and vice versa. Thus,

        ∂
        L

          /

        ∂

              q
              ¨

    {\displaystyle \partial L/\partial {\ddot {q}}}

 is a function of

              q
              ¨

    {\displaystyle {\ddot {q}}}

 (if it were not, the Jacobian

        det
        [

          ∂

            2

        L

          /

        (
        ∂

                  q
                  ¨

              i

        ∂

                q
                ¨

            j

        )
        ]

    {\displaystyle \det[\partial ^{2}L/(\partial {{\ddot {q}}{i}}\,\partial {\ddot {q}}{j})]}

 would vanish, which would mean that

        L

    {\displaystyle L}

 is degenerate), meaning that we can write

          q

            (
            4
            )

        F
        (
        q
        ,

              q
              ˙

        ,

              q
              ¨

        ,

          q

            (
            3
            )

        )

    {\displaystyle q^{(4)}=F(q,{\dot {q}},{\ddot {q}},q^{(3)})}

 or, inverting,

        q

        G
        (
        t
        ,

          q

            0

        ,

                q
                ˙

            0

        ,

                q
                ¨

            0

        ,

          q

            0

            (
            3
            )

        )

    {\displaystyle q=G(t,q_{0},{\dot {q}}{0},{\ddot {q}}{0},q_{0}^{(3)})}

. Since the evolution of

        q

    {\displaystyle q}

 depends upon four initial parameters, this means that there are four canonical coordinates. We can write those as

          Q

            1

        :=
        q

    {\displaystyle Q_{1}:=q}

          Q

            2

        :=

              q
              ˙

    {\displaystyle Q_{2}:={\dot {q}}}

and by using the definition of the conjugate momentum,

          P

            1

        :=

              ∂
              L

              ∂

                    q
                    ˙

        −

            d

              d
              t

              ∂
              L

              ∂

                    q
                    ¨

    {\displaystyle P_{1}:={\frac {\partial L}{\partial {\dot {q}}}}-{\frac {d}{dt}}{\frac {\partial L}{\partial {\ddot {q}}}}}

          P

            2

        :=

              ∂
              L

              ∂

                    q
                    ¨

    {\displaystyle P_{2}:={\frac {\partial L}{\partial {\ddot {q}}}}}

The above results can be obtained as follows. First, we rewrite the Lagrangian into "ordinary" form by introducing a Lagrangian multiplier as a new dynamic variable

        λ

    {\displaystyle \lambda }

        L
        (
        q
        ,

              q
              ˙

        ,

              q
              ¨

        )
        →

              L
              ~

        L
        (

          Q

            1

        ,

                Q

                  1

              ˙

        ,

                Q

                  2

              ˙

        )
        −
        λ
        (

          Q

            2

        −

                Q

                  1

              ˙

        )

    {\displaystyle L(q,{\dot {q}},{\ddot {q}})\to {\tilde {L}}=L(Q_{1},{\dot {Q_{1}}},{\dot {Q_{2}}})-\lambda (Q_{2}-{\dot {Q_{1}}})}

,
from which, the Euler-Lagrangian equations for

          Q

            1

        ,

          Q

            2

        ,
        λ

    {\displaystyle Q_{1},Q_{2},\lambda }

 read

          Q

            1

        :

            d

              d
              t

              ∂
              L

              ∂

                      Q

                        1

                    ˙

        +

              λ
              ˙

        −

              ∂
              L

              ∂

                Q

                  1

        0

    {\displaystyle Q_{1}:{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {Q_{1}}}}}+{\dot {\lambda }}-{\frac {\partial L}{\partial Q_{1}}}=0}

,

          Q

            2

        :

            d

              d
              t

              ∂
              L

              ∂

                      Q

                        2

                    ˙

        +

          λ

        0

    {\displaystyle Q_{2}:{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {Q_{2}}}}}+{\lambda }=0}

,

        λ
        :

          Q

            2

        −

                Q

                  1

              ˙

        0

    {\displaystyle \lambda :Q_{2}-{\dot {Q_{1}}}=0}

,
Now, the canonical momentum

          P

            1

        ,

          P

            2

    {\displaystyle P_{1},P_{2}}

 with respect to

              L
              ~

    {\displaystyle {\tilde {L}}}

 are readily shown to be

          P

            1

              ∂

                    L
                    ~

              ∂

                      Q

                        1

                    ˙

              ∂
              L

              ∂

                      Q

                        1

                    ˙

        +
        λ

              ∂
              L

              ∂

                      Q

                        1

                    ˙

        −

            d

              d
              t

              ∂
              L

              ∂

                      Q

                        2

                    ˙

    {\displaystyle P_{1}={\frac {\partial {\tilde {L}}}{\partial {\dot {Q_{1}}}}}={\frac {\partial L}{\partial {\dot {Q_{1}}}}}+\lambda ={\frac {\partial L}{\partial {\dot {Q_{1}}}}}-{\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {Q_{2}}}}}}

          P

            2

              ∂

                    L
                    ~

              ∂

                      Q

                        2

                    ˙

              ∂

                L

              ∂

                      Q

                        2

                    ˙

    {\displaystyle P_{2}={\frac {\partial {\tilde {L}}}{\partial {\dot {Q_{2}}}}}={\frac {\partial {L}}{\partial {\dot {Q_{2}}}}}}

while

          P

            λ

        0

    {\displaystyle P_{\lambda }=0}

These are precisely the definitions given above by Ostrogradski.
One may proceed further to evaluate the Hamiltonian

              H
              ~

          P

            1

                Q

                  1

              ˙

        +

          P

            2

                Q

                  2

              ˙

        +

          p

            λ

              λ
              ˙

        −

              L
              ~

          P

            1

          Q

            2

        +

          P

            2

                Q

                  2

              ˙

        −

          L

    {\displaystyle {\tilde {H}}=P_{1}{\dot {Q_{1}}}+P_{2}{\dot {Q_{2}}}+p_{\lambda }{\dot {\lambda }}-{\tilde {L}}=P_{1}Q_{2}+P_{2}{\dot {Q_{2}}}-{L}}

,
where one makes use of the above Euler-Lagrangian equations for the second equality.
We note that due to non-degeneracy, we can write

              q
              ¨

                Q

                  2

              ˙

    {\displaystyle {\ddot {q}}={\dot {Q_{2}}}}

 as

        a
        (

          Q

            1

        ,

          Q

            2

        ,

          P

            2

        )

    {\displaystyle a(Q_{1},Q_{2},P_{2})}

.
Here, only three arguments are needed since the Lagrangian itself only has three free parameters.
Therefore, the last expression only depends on

          P

            1

        ,

          P

            2

        ,

          Q

            1

        ,

          Q

            2

    {\displaystyle P_{1},P_{2},Q_{1},Q_{2}}

, it effectively serves as the Hamiltonian of the original theory, namely,

        H

          P

            1

          Q

            2

        +

          P

            2

        a
        (

          Q

            1

        ,

          Q

            2

        ,

          P

            2

        )
        −
        L
        (

          Q

            1

        ,

          Q

            2

        ,

          P

            2

        )

    {\displaystyle H=P_{1}Q_{2}+P_{2}a(Q_{1},Q_{2},P_{2})-L(Q_{1},Q_{2},P_{2})}

.
We now notice that the Hamiltonian is linear in

          P

            1

    {\displaystyle P_{1}}

 and hence unbounded from below. This is a source of the Ostrogradsky instability, and it stems from the fact that the Lagrangian depends on fewer coordinates than there are canonical coordinates (which correspond to the initial parameters needed to specify the problem). The extension to higher dimensional systems is analogous, and the extension to higher derivatives simply means that the phase space is of even higher dimension than the configuration space.
