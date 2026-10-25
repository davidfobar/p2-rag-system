# Irrational rotation

Irrational rotation

An irrational rotation in the mathematical theory of dynamical systems, is defined as a map

        f

    {\displaystyle f}

, as follows:
Let

        x
        ∈
        [
        0
        ,
        1
        )

    {\displaystyle x\in [0,1)}

 be arbitrary, and let

        θ

    {\displaystyle \theta }

 be any irrational number. For

        i
        ∈

    {\displaystyle i\in }

 {0, 1, 2 ...} define

          f

            θ

            i

        :
        [
        0
        ,
        1
        )
        →
        [
        0
        ,
        1
        )

    {\displaystyle f_{\theta }^{i}:[0,1)\rightarrow [0,1)}

 by

          f

            θ

            i

        (
        x
        )

        x
        +
        i
        ⋅
        θ

    {\displaystyle f_{\theta }^{i}(x)=x+i\cdot \theta }

  (mod 1)
Under the identification of a circle with R/Z, or with the interval [0, 1) with the boundary points glued together, this map becomes a rotation of a circle by a proportion θ of a full revolution (i.e., an angle of 2πθ radians). Since θ is irrational, the rotation has infinite order in the circle group, and the map fθ has no periodic orbits.
Alternatively, we can use multiplicative notation for an irrational rotation by introducing the map

          f

            θ

        :

          S

            1

        →

          S

            1

        ,

          f

            θ

        (
        x
        )

        x

          e

            2
            π
            i
            θ

    {\displaystyle f_{\theta }:S^{1}\to S^{1},\quad \quad \quad f_{\theta }(x)=xe^{2\pi i\theta }}

The relationship between the additive and multiplicative notations is the group isomorphism

        φ
        :
        (
        [
        0
        ,
        1
        )
        ,
        +
        )
        →
        (

          S

            1

        ,
        ⋅
        )

        φ
        (
        x
        )

        x

          e

            2
            π
            i
            θ

    {\displaystyle \varphi :([0,1),+)\to (S^{1},\cdot )\quad \varphi (x)=xe^{2\pi i\theta }}

.
It can be shown that φ is an isometry.
There is a strong distinction in circle rotations that depends on whether θ is rational or irrational. Rational rotations are less interesting examples of dynamical systems because if

        θ

            a
            b

    {\displaystyle \theta ={\frac {a}{b}}}

 and

        gcd
        (
        a
        ,
        b
        )

        1

    {\displaystyle \gcd(a,b)=1}

, then

          f

            θ

            b

        (
        x
        )

        x

    {\displaystyle f_{\theta }^{b}(x)=x}

 when

        x
        ∈
        [
        0
        ,
        1
        )

    {\displaystyle x\in [0,1)}

. It can also be shown that

          f

            θ

            i

        (
        x
        )
        ≠
        x

    {\displaystyle f_{\theta }^{i}(x)\neq x}

 when

        1
        ≤
        i
        <
        b

    {\displaystyle 1\leq i<b}

.

Significance
Irrational rotations form a fundamental example in the theory of dynamical systems. According to the Denjoy theorem, every orientation-preserving C2-diffeomorphism of the circle with an irrational rotation number θ is topologically conjugate to fθ. An irrational rotation is a measure-preserving ergodic transformation, but it is not mixing. The Poincaré map for the dynamical system associated with the Kronecker foliation on a torus with angle θ> is the irrational rotation by θ. C*-algebras associated with irrational rotations, known as irrational rotation algebras, have been extensively studied.

Properties
If θ is irrational, then the orbit of any element of [0, 1] under the rotation fθ is dense in [0, 1). Therefore, irrational rotations are topologically transitive.
Irrational (and rational) rotations are not topologically mixing.
Irrational rotations are uniquely ergodic, with the Lebesgue measure serving as the unique invariant probability measure.
Suppose [a, b] ⊂ [0, 1). Since fθ is ergodic,

            lim

            N
            →
            ∞

            1
            N

          ∑

            n

            0

            N
            −
            1

          χ

            [
            a
            ,
            b
            )

        (

          f

            θ

            n

        (
        t
        )
        )

        b
        −
        a

    {\displaystyle {\text{lim}}_{N\to \infty }{\frac {1}{N}}\sum _{n=0}^{N-1}\chi {[a,b)}(f{\theta }^{n}(t))=b-a}

.

Generalizations
Circle rotations are examples of group translations.
For a general orientation preserving homomorphism f of S1 to itself we call a homeomorphism

        F
        :

          R

        →

          R

    {\displaystyle F:\mathbb {R} \to \mathbb {R} }

 a lift of f if

        π
        ∘
        F

        f
        ∘
        π

    {\displaystyle \pi \circ F=f\circ \pi }

 where

        π
        (
        t
        )

        t

          mod

            1

    {\displaystyle \pi (t)=t{\bmod {1}}}

.
The circle rotation can be thought of as a subdivision of a circle into two parts, which are then exchanged with each other. A subdivision into more than two parts, which are then permuted with one-another, is called an interval exchange transformation.
Rigid rotations of compact groups effectively behave like circle rotations; the invariant measure is the Haar measure.

Applications
Skew Products over Rotations of the Circle: In 1969 William A. Veech constructed examples of minimal and not uniquely ergodic dynamical systems as follows: "Take two copies of the unit circle and mark off segment J of length 2πα in the counterclockwise direction on each one with endpoint at 0. Now take θ irrational and consider the following dynamical system. Start with a point p, say in the first circle. Rotate counterclockwise by 2πθ until the first time the orbit lands in J; then switch to the corresponding point in the second circle, rotate by 2πθ until the first time the point lands in J; switch back to the first circle and so forth. Veech showed that if θ is irrational, then there exists irrational α for which this system is minimal and the Lebesgue measure is not uniquely ergodic."
