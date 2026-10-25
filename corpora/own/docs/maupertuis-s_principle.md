# Maupertuis's principle

Maupertuis's principle

In classical mechanics, Maupertuis's principle (named after Pierre Louis Maupertuis, 1698 – 1759) states that the path followed by a physical system is the one of least length (with a suitable interpretation of path and length). It is a special case of the more generally stated principle of least action. Using the calculus of variations, it results in an integral equation formulation of the equations of motion for the system.

Mathematical formulation
Maupertuis's principle states that the true path of a system described by

        N

    {\displaystyle N}

 generalized coordinates

          q

          (

              q

                1

            ,

              q

                2

            ,
            …
            ,

              q

                N

          )

    {\displaystyle \mathbf {q} =\left(q_{1},q_{2},\ldots ,q_{N}\right)}

 between two specified states

            q

            1

    {\displaystyle \mathbf {q} _{1}}

 and

            q

            2

    {\displaystyle \mathbf {q} _{2}}

 is a minimum or a saddle point of the abbreviated action functional,

              S

            0

        [

          q

        (
        t
        )
        ]

                  d
                  e
                  f

        ∫

          p

        ⋅
        d

          q

        ,

    {\displaystyle {\mathcal {S}}_{0}[\mathbf {q} (t)]\ {\stackrel {\mathrm {def} }{=}}\ \int \mathbf {p} \cdot d\mathbf {q} ,}

where

          p

          (

              p

                1

            ,

              p

                2

            ,
            …
            ,

              p

                N

          )

    {\displaystyle \mathbf {p} =\left(p_{1},p_{2},\ldots ,p_{N}\right)}

 are the conjugate momenta of the generalized coordinates, defined by the equation

          p

            k

                  d
                  e
                  f

              ∂
              L

              ∂

                      q
                      ˙

                  k

        ,

    {\displaystyle p_{k}\ {\stackrel {\mathrm {def} }{=}}\ {\frac {\partial L}{\partial {\dot {q}}_{k}}},}

where

        L
        (

          q

        ,

                q

              ˙

        ,
        t
        )

    {\displaystyle L(\mathbf {q} ,{\dot {\mathbf {q} }},t)}

 is the Lagrangian function for the system. In other words, any first-order perturbation of the path results in (at most) second-order changes in

              S

            0

    {\displaystyle {\mathcal {S}}_{0}}

. Note that the abbreviated action

              S

            0

    {\displaystyle {\mathcal {S}}_{0}}

 is a functional (i.e. a function from a vector space into its underlying scalar field), which in this case takes as its input a function (i.e. the paths between the two specified states).

Jacobi's formulation
For many systems, the kinetic energy

        T

    {\displaystyle T}

 is quadratic in the generalized velocities

                q

              ˙

    {\displaystyle {\dot {\mathbf {q} }}}

        T

            1
            2

                q

              ˙

          M

                  q

                ˙

            ⊺

    {\displaystyle T={\frac {1}{2}}{\dot {\mathbf {q} }}\ \mathbf {M} \ {\dot {\mathbf {q} }}^{\intercal }}

although the mass tensor

          M

    {\displaystyle \mathbf {M} }

 may be a complicated function of the generalized coordinates

          q

    {\displaystyle \mathbf {q} }

. For such systems, a simple relation relates the kinetic energy, the generalized momenta and the generalized velocities

        2
        T

          p

        ⋅

                q

              ˙

    {\displaystyle 2T=\mathbf {p} \cdot {\dot {\mathbf {q} }}}

provided that the potential energy

        V
        (

          q

        )

    {\displaystyle V(\mathbf {q} )}

 does not involve the generalized velocities. By defining a normalized distance or metric

        d
        s

    {\displaystyle ds}

 in the space of generalized coordinates

        d

          s

            2

        d

          q

          M

        d

            q

              ⊺

    {\displaystyle ds^{2}=d\mathbf {q} \ \mathbf {M} \ d\mathbf {q^{\intercal }} }

one may immediately recognize the mass tensor as a metric tensor. The kinetic energy may be written in a massless form

        T

            1
            2

            (

                  d
                  s

                  d
                  t

            )

            2

    {\displaystyle T={\frac {1}{2}}\left({\frac {ds}{dt}}\right)^{2}}

or,

        2
        T
        d
        t

            2
            T

        d
        s
        .

    {\displaystyle 2Tdt={\sqrt {2T}}\ ds.}

Therefore, the abbreviated action can be written

              S

            0

                  d
                  e
                  f

        ∫

          p

        ⋅
        d

          q

        ∫
        d
        s

            2

              E

                tot

            −
            V
            (

              q

            )

    {\displaystyle {\mathcal {S}}{0}\ {\stackrel {\mathrm {def} }{=}}\ \int \mathbf {p} \cdot d\mathbf {q} =\int ds\,{\sqrt {2}}{\sqrt {E{\text{tot}}-V(\mathbf {q} )}}}

since the kinetic energy

        T

          E

            tot

        −
        V
        (

          q

        )

    {\displaystyle T=E_{\text{tot}}-V(\mathbf {q} )}

 equals the (constant) total energy

          E

            tot

    {\displaystyle E_{\text{tot}}}

 minus the potential energy

        V
        (

          q

        )

    {\displaystyle V(\mathbf {q} )}

. In particular, if the potential energy is a constant, then Jacobi's principle reduces to minimizing the path length

        s

        ∫
        d
        s

    {\textstyle s=\int ds}

 in the space of the generalized coordinates, which is equivalent to Hertz's principle of least curvature.

Comparison with Hamilton's principle
Hamilton's principle and Maupertuis's principle are occasionally confused with each other and both have been called the principle of least action. They differ from each other in three important ways:

their definition of the action...
the solution that they determine...
...and the constraints on the variation.

History

Maupertuis was the first to publish a principle of least action, as a way of adapting Fermat's principle for waves to a corpuscular (particle) theory of light. Pierre de Fermat had explained Snell's law for the refraction of light by assuming light follows the path of shortest time, not distance. This troubled Maupertuis, since he felt that time and distance should be on an equal footing: "why should light prefer the path of shortest time over that of distance?" Maupertuis defined his action as

        ∫
        v

        d
        s

    {\textstyle \int v\,ds}

, which was to be minimized over all paths connecting two specified points. Here

        v

    {\displaystyle v}

 is the velocity of light the corpuscular theory. Fermat had minimized

        ∫

        d
        s

          /

        v

    {\textstyle \int \,ds/v}

 where

        v

    {\displaystyle v}

 is wave velocity; the two velocities are reciprocal so the two forms are equivalent.

Koenig's claim
In 1751, Maupertuis's priority for the principle of least action was challenged in print (Nova Acta Eruditorum of Leipzig) by an old acquaintance, Johann Samuel Koenig, who quoted a 1707 letter purportedly from Gottfried Wilhelm Leibniz to Jakob Hermann that described results similar to those derived by Leonhard Euler in 1744.
Maupertuis demanded that Koenig produce the original letter to authenticate it, as Leibniz had died in 1716 and Hermann in 1733. Koenig claimed to have a copy of the original letter, which had been lost after its owner Samuel Henzi had been executed in 1749 for sedition against the aristocratic government of Bern. Subsequently, the Berlin Academy under Euler's direction declared the letter fraudulent and supported Maupertuis. Curiously Voltaire got involved in the quarrel by composing Diatribe du docteur Akakia ("Diatribe of Doctor Akakia") to satirize Maupertuis' scientific theories (not limited to the principle of least action). While this work damaged Maupertuis's reputation, his claim to priority for least action remains secure.
