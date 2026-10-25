# Rotation number

Rotation number

In mathematics, the rotation number is an invariant of homeomorphisms of the circle.

History
It was first defined by Henri Poincaré in 1885, in relation to the precession of the perihelion of a planetary orbit. Poincaré later proved a theorem characterizing the existence of periodic orbits in terms of rationality of the rotation number.

Definition
Suppose that

        f
        :

          S

            1

        →

          S

            1

    {\displaystyle f:S^{1}\to S^{1}}

 is an orientation-preserving homeomorphism of the circle

          S

            1

          R

          /

          Z

        .

    {\displaystyle S^{1}=\mathbb {R} /\mathbb {Z} .}

 Then f may be lifted to a homeomorphism

        F
        :

          R

        →

          R

    {\displaystyle F:\mathbb {R} \to \mathbb {R} }

 of the real line, satisfying

        F
        (
        x
        +
        m
        )

        F
        (
        x
        )
        +
        m

    {\displaystyle F(x+m)=F(x)+m}

for every real number x and every integer m.
The rotation number of f is defined in terms of the iterates of F:

        ω
        (
        f
        )

          lim

            n
            →
            ∞

                F

                  n

              (
              x
              )
              −
              x

            n

        .

    {\displaystyle \omega (f)=\lim _{n\to \infty }{\frac {F^{n}(x)-x}{n}}.}

Henri Poincaré proved that the limit exists and is independent of the choice of the starting point x. The lift F is unique modulo integers, therefore the rotation number is a well-defined element of

          R

          /

          Z

        .

    {\displaystyle \mathbb {R} /\mathbb {Z} .}

 Intuitively, it measures the average rotation angle along the orbits of f.

Example
If

        f

    {\displaystyle f}

 is a rotation by

        2
        π
        a

    {\displaystyle 2\pi a}

 (where

        0
        <
        a
        <
        1

    {\displaystyle 0<a<1}

), then

        F
        (
        x
        )

        x
        +
        a
        ,

    {\displaystyle F(x)=x+a,}

and its rotation number is

        a

    {\displaystyle a}

 (cf. irrational rotation).

Properties
The rotation number is invariant under topological conjugacy, and even monotone topological semiconjugacy: if f and g are two homeomorphisms of the circle and

        h
        ∘
        f

        g
        ∘
        h

    {\displaystyle h\circ f=g\circ h}

for a monotone continuous map h of the circle into itself (not necessarily homeomorphic) then f and g have the same rotation numbers. It was used by Poincaré and Arnaud Denjoy for topological classification of homeomorphisms of the circle. There are two distinct possibilities.

The rotation number of f is a rational number p/q (in the lowest terms). Then f has a periodic orbit, every periodic orbit has period q, and the order of the points on each such orbit coincides with the order of the points for a rotation by p/q. Moreover, every forward orbit of f converges to a periodic orbit. The same is true for backward orbits, corresponding to iterations of f –1, but the limiting periodic orbits in forward and backward directions may be different.
The rotation number of f is an irrational number θ. Then f has no periodic orbits (this follows immediately by considering a periodic point x of f). There are two subcases.
There exists a dense orbit. In this case f is topologically conjugate to the irrational rotation by the angle θ and all orbits are dense. Denjoy proved that this possibility is always realized when f is twice continuously differentiable.
There exists a Cantor set C invariant under f. Then C is a unique minimal set and the orbits of all points both in forward and backward direction converge to C. In this case, f is semiconjugate to the irrational rotation by θ, and the semiconjugating map h of degree 1 is constant on components of the complement of C.
The rotation number is continuous when viewed as a map from the group of homeomorphisms (with C0 topology) of the circle into the circle.
