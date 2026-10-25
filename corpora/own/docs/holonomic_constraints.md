# Holonomic constraints

Holonomic constraints

In classical mechanics, holonomic constraints are relations between the position variables (and possibly time) that can be expressed in the following form:

        f
        (

          u

            1

        ,

          u

            2

        ,

          u

            3

        ,
        …
        ,

          u

            n

        ,
        t
        )

        0

    {\displaystyle f(u_{1},u_{2},u_{3},\ldots ,u_{n},t)=0}

where

        {

          u

            1

        ,

          u

            2

        ,

          u

            3

        ,
        …
        ,

          u

            n

        }

    {\displaystyle {u_{1},u_{2},u_{3},\ldots ,u_{n}}}

 are n generalized coordinates that describe the system (in unconstrained configuration space) and

        f

    {\displaystyle f}

 is a continuous function. For example, the motion of a particle constrained to lie on the surface of a sphere is subject to a holonomic constraint, but if the particle is able to fall off the sphere under the influence of gravity, the constraint becomes non-holonomic. For the first case, the holonomic constraint may be given by the equation

          r

            2

        −

          a

            2

        0

    {\displaystyle r^{2}-a^{2}=0}

where

        r

    {\displaystyle r}

 is the distance from the centre of a sphere of radius

        a

    {\displaystyle a}

, whereas the second non-holonomic case may be given by

          r

            2

        −

          a

            2

        ≥
        0

    {\displaystyle r^{2}-a^{2}\geq 0}

Velocity-dependent constraints (also called semi-holonomic constraints) such as

        f
        (

          u

            1

        ,

          u

            2

        ,
        …
        ,

          u

            n

        ,

                u
                ˙

            1

        ,

                u
                ˙

            2

        ,
        …
        ,

                u
                ˙

            n

        ,
        t
        )

        0

    {\displaystyle f(u_{1},u_{2},\ldots ,u_{n},{\dot {u}}{1},{\dot {u}}{2},\ldots ,{\dot {u}}_{n},t)=0}

are not usually holonomic.

Holonomic system
In classical mechanics a system may be defined as holonomic if all constraints of the system are holonomic. For a constraint to be holonomic it must be expressible as a function:

        f
        (

          u

            1

        ,

          u

            2

        ,

          u

            3

        ,

        …
        ,

          u

            n

        ,

        t
        )

        0
        ,

    {\displaystyle f(u_{1},\ u_{2},\ u_{3},\ \ldots ,\ u_{n},\ t)=0,\,}

i.e. a holonomic constraint depends only on the coordinates

          u

            j

    {\displaystyle u_{j}}

 and maybe time

        t

    {\displaystyle t}

. It does not depend on the velocities or any higher-order derivative with respect to t. A constraint that cannot be expressed in the form shown above is a nonholonomic constraint.

Introduction
As described above, a holonomic system is (simply speaking) a system in which one can deduce the state of a system by knowing only the change of positions of the components of the system over time, but not needing to know the velocity or in what order the components moved relative to each other. In contrast, a nonholonomic system is often a system where the velocities of the components over time must be known to be able to determine the change of state of the system, or a system where a moving part is not able to be bound to a constraint surface, real or imaginary. Examples of holonomic systems are gantry cranes, pendulums, and robotic arms. Examples of nonholonomic systems are Segways, unicycles, and automobiles.

Terminology
The configuration space

          u

    {\displaystyle \mathbf {u} }

 lists the displacement of the components of the system, one for each degree of freedom. A system that can be described using a configuration space is called scleronomic.

          u

              [

                      u

                        1

                      u

                        2

                    …

                      u

                        n

              ]

              T

    {\displaystyle \mathbf {u} ={\begin{bmatrix}u_{1}&u_{2}&\ldots &u_{n}\end{bmatrix}}^{\mathrm {T} }}

The event space is identical to the configuration space except for the addition of a variable

        t

    {\displaystyle t}

 to represent the change in the system over time (if needed to describe the system). A system that must be described using an event space, instead of only a configuration space, is called rheonomic. Many systems can be described either scleronomically or rheonomically. For example, the total allowable motion of a pendulum can be described with a scleronomic constraint, but the motion over time of a pendulum must be described with a rheonomic constraint.

          u

              [

                      u

                        1

                      u

                        2

                    …

                      u

                        n

                    t

              ]

              T

    {\displaystyle \mathbf {u} ={\begin{bmatrix}u_{1}&u_{2}&\ldots &u_{n}&t\end{bmatrix}}^{\mathrm {T} }}

The state space

          q

    {\displaystyle \mathbf {q} }

 is the configuration space, plus terms describing the velocity of each term in the configuration space.

          q

            [

                    u

                        u
                        ˙

            ]

              [

                      u

                        1

                    …

                      u

                        n

                            u
                            ˙

                        1

                    …

                            u
                            ˙

                        n

              ]

              T

    {\displaystyle \mathbf {q} ={\begin{bmatrix}\mathbf {u} \\mathbf {\dot {u}} \end{bmatrix}}={\begin{bmatrix}u_{1}&\ldots &u_{n}&{\dot {u}}{1}&\ldots &{\dot {u}}{n}\end{bmatrix}}^{\mathrm {T} }}

The state-time space adds time

        t

    {\displaystyle t}

.

          q

            [

                    u

                        u
                        ˙

            ]

              [

                      u

                        1

                    …

                      u

                        n

                    t

                            u
                            ˙

                        1

                    …

                            u
                            ˙

                        n

              ]

              T

    {\displaystyle \mathbf {q} ={\begin{bmatrix}\mathbf {u} \\mathbf {\dot {u}} \end{bmatrix}}={\begin{bmatrix}u_{1}&\ldots &u_{n}&t&{\dot {u}}{1}&\ldots &{\dot {u}}{n}\end{bmatrix}}^{\mathrm {T} }}

Examples

Gantry crane

As shown on the right, a gantry crane is an overhead crane that is able to move its hook in 3 axes as indicated by the arrows. Intuitively, we can deduce that the crane should be a holonomic system as, for a given movement of its components, it doesn't matter what order or velocity the components move: as long as the total displacement of each component from a given starting condition is the same, all parts and the system as a whole will end up in the same state. Mathematically we can prove this as such:
We can define the configuration space of the system as:

          u

            [

                  x

                  y

                  z

            ]

    {\displaystyle \mathbf {u} ={\begin{bmatrix}x\y\z\end{bmatrix}}}

We can say that the deflection of each component of the crane from its "zero" position are

        B

    {\displaystyle B}

,

        G

    {\displaystyle G}

, and

        O

    {\displaystyle O}

, for the blue, green, and orange components, respectively. The orientation and placement of the coordinate system does not matter in whether a system is holonomic, but in this example the components happen to move parallel to its axes. If the origin of the coordinate system is at the back-bottom-left of the crane, then we can write the position constraint equation as:

        (
        x
        −
        B
        )
        +
        (
        y
        −
        G
        )
        +
        (
        z
        −
        (
        h
        −
        O
        )
        )

        0

    {\displaystyle (x-B)+(y-G)+(z-(h-O))=0}

Where

        h

    {\displaystyle h}

 is the height of the crane. Optionally, we may simplify to the standard form where all constants are placed after the variables:

        x
        +
        y
        +
        z
        −
        (
        B
        +
        G
        +
        h
        −
        O
        )

        0

    {\displaystyle x+y+z-(B+G+h-O)=0}

Because we have derived a constraint equation in holonomic form (specifically, our constraint equation has the form

        f
        (
        x
        ,
        y
        ,
        z
        )

        0

    {\displaystyle f(x,y,z)=0}

 where

        {
        x
        ,
        y
        ,
        z
        }
        ∈

          u

    {\displaystyle {x,y,z}\in \mathbf {u} }

), we can see that this system must be holonomic.

Pendulum

As shown on the right, a simple pendulum is a system composed of a weight and a string. The string is attached at the top end to a pivot and at the bottom end to a weight. Being inextensible, the string's length is a constant. This system is holonomic because it obeys the holonomic constraint

            x

              2

          +

            y

              2

        −

          L

            2

        0
        ,

    {\displaystyle {x^{2}+y^{2}}-L^{2}=0,}

where

        (
        x
        ,

        y
        )

    {\displaystyle (x,\ y)}

 is the position of the weight and

        L

    {\displaystyle L}

 is length of the string.

Rigid body
The particles of a rigid body obey the holonomic constraint

        (

            r

            i

        −

            r

            j

          )

            2

        −

          L

            i
            j

            2

        0
        ,

    {\displaystyle (\mathbf {r} _{i}-\mathbf {r} {j})^{2}-L{ij}^{2}=0,\,}

where

            r

            i

    {\displaystyle \mathbf {r} _{i}}

,

            r

            j

    {\displaystyle \mathbf {r} _{j}}

 are respectively the positions of particles

          P

            i

    {\displaystyle P_{i}}

 and

          P

            j

    {\displaystyle P_{j}}

, and

          L

            i
            j

    {\displaystyle L_{ij}}

 is the distance between them. If a given system is holonomic, rigidly attaching additional parts to components of the system in question cannot make it non-holonomic, assuming that the degrees of freedom are not reduced (in other words, assuming the configuration space is unchanged).

Pfaffian form

Consider the following differential form of a constraint:

          ∑

            j

          A

            i
            j

        d

          u

            j

        +

          A

            i

        d
        t

        0

    {\displaystyle \sum {j}\ A{ij}\,du_{j}+A_{i}\,dt=0}

where

          A

            i
            j

        ,

          A

            i

    {\displaystyle A_{ij},A_{i}}

 are the coefficients of the differentials

        d

          u

            j

        ,
        d
        t

    {\displaystyle du_{j},dt}

 for the ith constraint equation. This form is called the Pfaffian form or the differential form.
If the differential form is integrable, i.e., if there is a function

          f

            i

        (

          u

            1

        ,

          u

            2

        ,

          u

            3

        ,

        …
        ,

          u

            n

        ,

        t
        )

        0

    {\displaystyle f_{i}(u_{1},\ u_{2},\ u_{3},\ \ldots ,\ u_{n},\ t)=0}

 satisfying the equality

        d

          f

            i

          ∑

            j

          A

            i
            j

        d

          u

            j

        +

          A

            i

        d
        t

        0

    {\displaystyle df_{i}=\sum {j}\ A{ij}\,du_{j}+A_{i}\,dt=0}

then this constraint is a holonomic constraint; otherwise, it is nonholonomic. Therefore, all holonomic and some nonholonomic constraints can be expressed using the differential form. Examples of nonholonomic constraints that cannot be expressed this way are those that are dependent on generalized velocities. With a constraint equation in Pfaffian form, whether the constraint is holonomic or nonholonomic depends on whether the Pfaffian form is integrable. See Universal test for holonomic constraints below for a description of a test to verify the integrability (or lack of) of a Pfaffian form constraint.

Universal test for holonomic constraints

When the constraint equation of a system is written in Pfaffian constraint form, there exists a mathematical test to determine whether the system is holonomic.
For a constraint equation, or

        i

    {\displaystyle i}

 sets of constraint equations (note that variable(s) representing time can be included, as from above

          A

            i

        ∈

          A

            i
            j

    {\displaystyle A_{i}\in A_{ij}}

 and

        d
        t
        ∈
        d

          u

            j

    {\displaystyle \,dt\in du_{j}}

 in the following form):

          ∑

            j

            n

          A

            i
            j

        d

          u

            j

        0
        ;

    {\displaystyle \sum {j}^{n}\ A{ij}\,du_{j}=0;\,}

we can use the test equation:

          A

            γ

          (

                  ∂

                    A

                      β

                  ∂

                    u

                      α

            −

                  ∂

                    A

                      α

                  ∂

                    u

                      β

          )

        +

          A

            β

          (

                  ∂

                    A

                      α

                  ∂

                    u

                      γ

            −

                  ∂

                    A

                      γ

                  ∂

                    u

                      α

          )

        +

          A

            α

          (

                  ∂

                    A

                      γ

                  ∂

                    u

                      β

            −

                  ∂

                    A

                      β

                  ∂

                    u

                      γ

          )

        0

    {\displaystyle A_{\gamma }\left({\frac {\partial A_{\beta }}{\partial u_{\alpha }}}-{\frac {\partial A_{\alpha }}{\partial u_{\beta }}}\right)+A_{\beta }\left({\frac {\partial A_{\alpha }}{\partial u_{\gamma }}}-{\frac {\partial A_{\gamma }}{\partial u_{\alpha }}}\right)+A_{\alpha }\left({\frac {\partial A_{\gamma }}{\partial u_{\beta }}}-{\frac {\partial A_{\beta }}{\partial u_{\gamma }}}\right)=0}

where

        α
        ,
        β
        ,
        γ

        1
        ,
        2
        ,
        3
        …
        n

    {\displaystyle \alpha ,\beta ,\gamma =1,2,3\ldots n}

 in

              (

              n
              3

              )

              n
              (
              n
              −
              1
              )
              (
              n
              −
              2
              )

            6

    {\textstyle {\binom {n}{3}}={\frac {n(n-1)(n-2)}{6}}}

 combinations of test equations per constraint equation, for all

        i

    {\displaystyle i}

 sets of constraint equations.
In other words, a system of three variables would have to be tested once with one test equation with the terms

        α
        ,
        β
        ,
        γ

    {\displaystyle \alpha ,\beta ,\gamma }

 being terms

        1
        ,
        2
        ,
        3

    {\displaystyle 1,2,3}

 in the constraint equation (in any order), but to test a system of four variables the test would have to be performed up to four times with four different test equations, with the terms

        α
        ,
        β
        ,
        γ

    {\displaystyle \alpha ,\beta ,\gamma }

 being terms

        1
        ,
        2
        ,
        3

    {\displaystyle 1,2,3}

,

        1
        ,
        2
        ,
        4

    {\displaystyle 1,2,4}

,

        1
        ,
        3
        ,
        4

    {\displaystyle 1,3,4}

, and

        2
        ,
        3
        ,
        4

    {\displaystyle 2,3,4}

 in the constraint equation (each in any order) in four different tests. For a system of five variables, ten tests would have to be performed on a holonomic system to verify that fact, and for a system of five variables with three sets of constraint equations, thirty tests (assuming a simplification like a change-of-variable could not be performed to reduce that number). For this reason, it is advisable when using this method on systems of more than three variables to use common sense as to whether the system in question is holonomic, and only pursue testing if the system likely is not. Additionally, it is likewise best to use mathematical intuition to try to predict which test would fail first and begin with that one, skipping tests at first that seem likely to succeed.
If every test equation is true for the entire set of combinations for all constraint equations, the system is holonomic. If it is untrue for even one test combination, the system is nonholonomic.

Example
Consider this dynamical system described by a constraint equation in Pfaffian form.

        cos
        ⁡
        (
        θ
        )
        d
        x
        +
        sin
        ⁡
        (
        θ
        )
        d
        y
        +

          [

            y
            cos
            ⁡
            (
            θ
            )
            −
            x
            sin
            ⁡
            (
            θ
            )

          ]

        d
        θ

        0

    {\displaystyle \cos(\theta )dx+\sin(\theta )dy+\left[y\cos(\theta )-x\sin(\theta )\right]d\theta =0}

The configuration space, by inspection, is

          u

              [

                    x

                    y

                    θ

              ]

              T

    {\displaystyle \mathbf {u} ={\begin{bmatrix}x&y&\theta \end{bmatrix}}^{\mathrm {T} }}

. Because there are only three terms in the configuration space, there will be only one test equation needed.
We can organize the terms of the constraint equation as such, in preparation for substitution:

          A

            α

        cos
        ⁡
        θ

    {\displaystyle A_{\alpha }=\cos \theta }

          A

            β

        sin
        ⁡
        θ

    {\displaystyle A_{\beta }=\sin \theta }

          A

            γ

        y
        cos
        ⁡
        θ
        −
        x
        sin
        ⁡
        θ

    {\displaystyle A_{\gamma }=y\cos \theta -x\sin \theta }

          u

            α

        d
        x

    {\displaystyle u_{\alpha }=dx}

          u

            β

        d
        y

    {\displaystyle u_{\beta }=dy}

          u

            γ

        d
        θ

    {\displaystyle u_{\gamma }=d\theta }

Substituting the terms, our test equation becomes:

          (

            y
            cos
            ⁡
            θ
            −
            x
            sin
            ⁡
            θ

          )

          [

                ∂

                  ∂
                  x

            sin
            ⁡
            θ
            −

                ∂

                  ∂
                  y

            cos
            ⁡
            θ

          ]

        +
        sin
        ⁡
        θ

          [

                ∂

                  ∂
                  θ

            cos
            ⁡
            θ
            −

                ∂

                  ∂
                  x

            (
            y
            cos
            ⁡
            θ
            −
            x
            sin
            ⁡
            θ
            )

          ]

        +
        cos
        ⁡
        θ

          [

                ∂

                  ∂
                  y

            (
            y
            cos
            ⁡
            θ
            −
            x
            sin
            ⁡
            θ
            )
            −

                ∂

                  ∂
                  θ

            sin
            ⁡
            θ

          ]

        0

    {\displaystyle \left(y\cos \theta -x\sin \theta \right)\left[{\frac {\partial }{\partial x}}\sin \theta -{\frac {\partial }{\partial y}}\cos \theta \right]+\sin \theta \left[{\frac {\partial }{\partial \theta }}\cos \theta -{\frac {\partial }{\partial x}}(y\cos \theta -x\sin \theta )\right]+\cos \theta \left[{\frac {\partial }{\partial y}}(y\cos \theta -x\sin \theta )-{\frac {\partial }{\partial \theta }}\sin \theta \right]=0}

After calculating all partial derivatives, we get:

        (
        y
        cos
        ⁡
        θ
        −
        x
        sin
        ⁡
        θ
        )

          [

            0
            −
            0

          ]

        +
        sin
        ⁡
        θ

          [

            −
            sin
            ⁡
            θ
            −
            (
            −
            sin
            ⁡
            θ
            )

          ]

        +
        cos
        ⁡
        θ

          [

            cos
            ⁡
            θ
            −
            cos
            ⁡
            θ

          ]

        0

    {\displaystyle (y\cos \theta -x\sin \theta )\left[0-0\right]+\sin \theta \left[-\sin \theta -(-\sin \theta )\right]+\cos \theta \left[\cos \theta -\cos \theta \right]=0}

Simplifying, we find that:

        0

        0

    {\displaystyle 0=0}

We see that our test equation is true, and thus, the system must be holonomic.
We have finished our test, but now knowing that the system is holonomic, we may wish to find the holonomic constraint equation. We can attempt to find it by integrating each term of the Pfaffian form and attempting to unify them into one equation, as such:

        ∫
        cos
        ⁡
        θ

        d
        x

        x
        cos
        ⁡
        θ
        +
        f
        (
        y
        ,
        θ
        )

    {\displaystyle \int \cos \theta \,dx=x\cos \theta +f(y,\theta )}

        ∫
        sin
        ⁡
        θ

        d
        y

        y
        sin
        ⁡
        θ
        +
        f
        (
        x
        ,
        θ
        )

    {\displaystyle \int \sin \theta \,dy=y\sin \theta +f(x,\theta )}

        ∫

          (

            y
            cos
            ⁡
            θ
            −
            x
            sin
            ⁡
            θ

          )

        d
        θ

        y
        sin
        ⁡
        θ
        +
        x
        cos
        ⁡
        θ
        +
        f
        (
        x
        ,
        y
        )

    {\displaystyle \int \left(y\cos \theta -x\sin \theta \right)d\theta =y\sin \theta +x\cos \theta +f(x,y)}

It's easy to see that we can combine the results of our integrations to find the holonomic constraint equation:

        y
        sin
        ⁡
        θ
        +
        x
        cos
        ⁡
        θ
        +
        C

        0

    {\displaystyle y\sin \theta +x\cos \theta +C=0}

where C is the constant of integration.

Constraints of constant coefficients
For a given Pfaffian constraint where every coefficient of every differential is a constant, in other words, a constraint in the form:

          ∑

            j

          A

            i
            j

        d

          u

            j

        +

          A

            i

        d
        t

        0
        ;

        {

          A

            i
            j

        ,

          A

            i

        ;

        j

        1
        ,
        2
        ,
        …
        ;

        i

        1
        ,
        2
        ,
        …
        }
        ∈

          R

    {\displaystyle \sum {j}\ A{ij}\,du_{j}+A_{i}\,dt=0;\;{A_{ij},A_{i};\,j=1,2,\ldots ;\,i=1,2,\ldots }\in \mathbb {R} }

the constraint must be holonomic.
We may prove this as follows: consider a system of constraints in Pfaffian form where every coefficient of every differential is a constant, as described directly above. To test whether this system of constraints is holonomic, we use the universal test. We can see that in the test equation, there are three terms that must sum to zero. Therefore, if each of those three terms in every possible test equation are each zero, then all test equations are true and this the system is holonomic. Each term of each test equation is in the form:

          A

            3

          (

                  ∂

                    A

                      2

                  ∂

                    u

                      1

            −

                  ∂

                    A

                      1

                  ∂

                    u

                      2

          )

    {\displaystyle A_{3}\left({\frac {\partial A_{2}}{\partial u_{1}}}-{\frac {\partial A_{1}}{\partial u_{2}}}\right)}

where:

          A

            1

    {\displaystyle A_{1}}

,

          A

            2

    {\displaystyle A_{2}}

, and

          A

            3

    {\displaystyle A_{3}}

 are some combination (with

              (

              n
              3

              )

        n
        (
        n
        −
        1
        )
        (
        n
        −
        2
        )

          /

        6

    {\textstyle {\binom {n}{3}}=n(n-1)(n-2)/6}

 total combinations) of

          A

            i
            j

        ;

        j

        1
        ,
        2
        ,
        …

    {\displaystyle A_{ij};\,j=1,2,\ldots }

 and

          A

            i

    {\displaystyle A_{i}}

 for a given constraint

        i

    {\displaystyle i}

.

          u

            1

    {\displaystyle u_{1}}

,

          u

            2

    {\displaystyle u_{2}}

, and

          u

            3

    {\displaystyle u_{3}}

 are the corresponding combination of

          u

            j

        ;

        j

        1
        ,
        2
        ,
        …

    {\displaystyle u_{j};\,j=1,2,\ldots }

 and

        d
        t

    {\displaystyle dt}

.
Additionally, there are

        i

    {\displaystyle i}

 sets of test equations.
We can see that, by definition, all

          A

            n

    {\displaystyle A_{n}}

 are constants. It is well known in calculus that any derivative (full or partial) of any constant is

        0

    {\displaystyle 0}

. Hence, we can reduce each partial derivative to:

          A

            3

            (

        0
        −
        0

            )

    {\displaystyle A_{3}{\big (}0-0{\big )}}

and hence each term is zero, the left side each test equation is zero, each test equation is true, and the system is holonomic.

Configuration spaces of two or one variable
Any system that can be described by a Pfaffian constraint and has a configuration space or state space of only two variables or one variable is holonomic.
We may prove this as such: consider a dynamical system with a configuration space or state space described as:

          u

              [

                      u

                        1

                      u

                        2

              ]

              T

    {\displaystyle \mathbf {u} ={\begin{bmatrix}u_{1}&u_{2}\end{bmatrix}}^{\mathrm {T} }}

if the system is described by a state space, we simply say that

          u

            2

    {\displaystyle u_{2}}

 equals our time variable

        t

    {\displaystyle t}

. This system will be described in Pfaffian form:

          A

            i
            1

        d

          u

            1

        +

          A

            i
            2

        d

          u

            2

        0

    {\displaystyle A_{i1}\,du_{1}+A_{i2}\,du_{2}=0}

with

        i

    {\displaystyle i}

 sets of constraints. The system will be tested by using the universal test. However, the universal test requires three variables in the configuration or state space. To accommodate this, we simply add a dummy variable

        λ

    {\displaystyle \lambda }

 to the configuration or state space to form:

          u

              [

                      u

                        1

                      u

                        2

                    λ

              ]

              T

    {\displaystyle \mathbf {u} ={\begin{bmatrix}u_{1}&u_{2}&\lambda \end{bmatrix}}^{\mathrm {T} }}

Because the dummy variable

        λ

    {\displaystyle \lambda }

 is by definition not a measure of anything in the system, its coefficient in the Pfaffian form must be

        0

    {\displaystyle 0}

. Thus we revise our Pfaffian form:

          A

            i
            1

        d

          u

            1

        +

          A

            i
            2

        d

          u

            2

        +
        0

        d
        λ

        0

    {\displaystyle A_{i1}\,du_{1}+A_{i2}\,du_{2}+0\,d\lambda =0}

Now we may use the test as such, for a given constraint

        i

    {\displaystyle i}

 if there are a set of constraints:

        0

          (

                  ∂

                    A

                      i
                      2

                  ∂

                    u

                      1

            −

                  ∂

                    A

                      i
                      1

                  ∂

                    u

                      2

          )

        +

          A

            i
            2

          (

                  ∂

                    A

                      i
                      1

                  ∂
                  λ

            −

                ∂

                  ∂

                    u

                      1

            0

          )

        +

          A

            i
            1

          (

                ∂

                  ∂

                    u

                      2

            0
            −

                  ∂

                    A

                      i
                      2

                  ∂
                  λ

          )

        0

    {\displaystyle 0\left({\frac {\partial A_{i2}}{\partial u_{1}}}-{\frac {\partial A_{i1}}{\partial u_{2}}}\right)+A_{i2}\left({\frac {\partial A_{i1}}{\partial \lambda }}-{\frac {\partial }{\partial u_{1}}}0\right)+A_{i1}\left({\frac {\partial }{\partial u_{2}}}0-{\frac {\partial A_{i2}}{\partial \lambda }}\right)=0}

Upon realizing that :

            ∂

              ∂
              λ

        f
        (

          u

            1

        ,

          u

            2

        )

        0

    {\displaystyle {\frac {\partial }{\partial \lambda }}f(u_{1},u_{2})=0}

 because the dummy variable

        λ

    {\displaystyle \lambda }

 cannot appear in the coefficients used to describe the system, we see that the test equation must be true for all sets of constraint equations and thus the system must be holonomic. A similar proof can be conducted with one actual variable in the configuration or state space and two dummy variables to confirm that one-degree-of-freedom systems describable in Pfaffian form are also always holonomic.
In conclusion, we realize that even though it is possible to model nonholonomic systems in Pfaffian form, any system modellable in Pfaffian form with two or fewer degrees of freedom (the number of degrees of freedom is equal to the number of terms in the configuration space) must be holonomic.
Important note: realize that the test equation failed because the dummy variable, and hence the dummy differential included in the test, will differentiate anything that is a function of the actual configuration or state space variables to

        0

    {\displaystyle 0}

. Having a system with a configuration or state space of:

          u

              [

                      u

                        1

                      u

                        2

                      u

                        3

              ]

              T

    {\displaystyle \mathbf {u} ={\begin{bmatrix}u_{1}&u_{2}&u_{3}\end{bmatrix}}^{\mathrm {T} }}

and a set of constraints where one or more constraints are in the Pfaffian form:

          A

            i
            1

        d

          u

            1

        +

          A

            i
            2

        d

          u

            2

        +
        0
        d

          u

            3

        0

    {\displaystyle A_{i1}du_{1}+A_{i2}du_{2}+0du_{3}=0}

does not guarantee the system is holonomic, as even though one differential has a coefficient of

        0

    {\displaystyle 0}

, there are still three degrees of freedom described in the configuration or state space.

Transformation to independent generalized coordinates
The holonomic constraint equations can help us easily remove some of the dependent variables in our system. For example, if we want to remove

          x

            d

    {\displaystyle x_{d}}

, which is a parameter in the constraint equation

          f

            i

    {\displaystyle f_{i}}

, we can rearrange the equation into the following form, assuming it can be done,

          x

            d

          g

            i

        (

          x

            1

        ,

          x

            2

        ,

          x

            3

        ,

        …
        ,

          x

            d
            −
            1

        ,

          x

            d
            +
            1

        ,

        …
        ,

          x

            N

        ,

        t
        )
        ,

    {\displaystyle x_{d}=g_{i}(x_{1},\ x_{2},\ x_{3},\ \dots ,\ x_{d-1},\ x_{d+1},\ \dots ,\ x_{N},\ t),\,}

and replace the

          x

            d

    {\displaystyle x_{d}}

 in every equation of the system using the above function. This can always be done for general physical systems, provided that the derivative of

          f

            i

    {\displaystyle f_{i}}

 is continuous, then by the implicit function theorem, the solution

          g

            i

    {\displaystyle g_{i}}

, is guaranteed in some open set. Thus, it is possible to remove all occurrences of the dependent variable

          x

            d

    {\displaystyle x_{d}}

.
Suppose that a physical system has

        N

    {\displaystyle N}

 degrees of freedom. Now,

        h

    {\displaystyle h}

 holonomic constraints are imposed on the system. Then, the number of degrees of freedom is reduced to

        m

        N
        −
        h

    {\displaystyle m=N-h}

. We can use

        m

    {\displaystyle m}

 independent generalized coordinates (

          q

            j

    {\displaystyle q_{j}}

) to completely describe the motion of the system. The transformation equation can be expressed as follows:

          x

            i

          x

            i

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

            m

        ,

        t
        )

        ,

        i

        1
        ,

        2
        ,

        …
        N
        .

    {\displaystyle x_{i}=x_{i}(q_{1},\ q_{2},\ \ldots ,\ q_{m},\ t)\ ,\qquad i=1,\ 2,\ \ldots N.\,}

Classification of physical systems
In order to study classical physics rigorously and methodically, we need to classify systems. Based on previous discussion, we can classify physical systems into holonomic systems and non-holonomic systems. One of the conditions for the applicability of many theorems and equations is that the system must be a holonomic system. For example, if a physical system is a holonomic system and a monogenic system, then Hamilton's principle is the necessary and sufficient condition for the correctness of Lagrange's equation.
