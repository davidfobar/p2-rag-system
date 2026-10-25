# Vibration of plates

Vibration of plates

The vibration of plates is a special case of the more general problem of mechanical vibrations. The equations governing the motion of plates are simpler than those for general three-dimensional objects because one of the dimensions of a plate is much smaller than the other two. This permits a two-dimensional plate theory to give an excellent approximation to the actual three-dimensional motion of a plate-like object.
There are several theories that have been developed to describe the motion of plates. The most commonly used are the Kirchhoff-Love theory and the Uflyand-Mindlin. The latter theory is discussed in detail by Elishakoff. Solutions to the governing equations predicted by these theories can give us insight into the behavior of plate-like objects both under free and forced conditions. This includes
the propagation of waves and the study of standing waves and vibration modes in plates. The topic of plate vibrations is treated in books by Leissa, Gontkevich, Rao, Soedel, Yu, Gorman and Rao.

Kirchhoff-Love plates

The governing equations for the dynamics of a Kirchhoff-Love plate are

                  N

                    α
                    β
                    ,
                    β

                  J

                    1

                        u
                        ¨

                    α

                  M

                    α
                    β
                    ,
                    α
                    β

                +
                q
                (
                x
                ,
                t
                )

                  J

                    1

                      w
                      ¨

                −

                  J

                    3

                        w
                        ¨

                    ,
                    α
                    α

    {\displaystyle {\begin{aligned}N_{\alpha \beta ,\beta }&=J_{1}~{\ddot {u}}{\alpha }\M{\alpha \beta ,\alpha \beta }+q(x,t)&=J_{1}~{\ddot {w}}-J_{3}~{\ddot {w}}_{,\alpha \alpha }\end{aligned}}}

where

          u

            α

    {\displaystyle u_{\alpha }}

 are the in-plane displacements of the mid-surface of the plate,

        w

    {\displaystyle w}

 is the transverse (out-of-plane) displacement of the mid-surface of the plate,

        q

    {\displaystyle q}

 is an applied transverse load pointing to

          x

            3

    {\displaystyle x_{3}}

 (upwards), and the resultant forces and moments are defined as

          N

            α
            β

        :=

          ∫

            −
            h

            h

          σ

            α
            β

        d

          x

            3

          and

          M

            α
            β

        :=

          ∫

            −
            h

            h

          x

            3

          σ

            α
            β

        d

          x

            3

        .

    {\displaystyle N_{\alpha \beta }:=\int _{-h}^{h}\sigma {\alpha \beta }~dx{3}\quad {\text{and}}\quad M_{\alpha \beta }:=\int {-h}^{h}x{3}~\sigma {\alpha \beta }~dx{3}\,.}

Note that the thickness of the plate is

        2
        h

    {\displaystyle 2h}

 and that the resultants are defined as weighted averages of the in-plane stresses

          σ

            α
            β

    {\displaystyle \sigma _{\alpha \beta }}

. The derivatives in the governing equations are defined as

                u
                ˙

            i

        :=

              ∂

                u

                  i

              ∂
              t

        ;

                u
                ¨

            i

        :=

                ∂

                  2

                u

                  i

              ∂

                t

                  2

        ;

          u

            i
            ,
            α

        :=

              ∂

                u

                  i

              ∂

                x

                  α

        ;

          u

            i
            ,
            α
            β

        :=

                ∂

                  2

                u

                  i

              ∂

                x

                  α

              ∂

                x

                  β

    {\displaystyle {\dot {u}}{i}:={\frac {\partial u{i}}{\partial t}}~;{\ddot {u}}{i}:={\frac {\partial ^{2}u{i}}{\partial t^{2}}}~;u_{i,\alpha }:={\frac {\partial u_{i}}{\partial x_{\alpha }}}~;~~u_{i,\alpha \beta }:={\frac {\partial ^{2}u_{i}}{\partial x_{\alpha }\partial x_{\beta }}}}

where the Latin indices go from 1 to 3 while the Greek indices go from 1 to 2. Summation over repeated indices is implied. The

          x

            3

    {\displaystyle x_{3}}

 coordinates is out-of-plane while the coordinates

          x

            1

    {\displaystyle x_{1}}

 and

          x

            2

    {\displaystyle x_{2}}

 are in plane.
For a uniformly thick plate of thickness

        2
        h

    {\displaystyle 2h}

 and homogeneous mass density

        ρ

    {\displaystyle \rho }

          J

            1

        :=

          ∫

            −
            h

            h

        ρ

        d

          x

            3

        2
        ρ
        h

          and

          J

            3

        :=

          ∫

            −
            h

            h

          x

            3

            2

        ρ

        d

          x

            3

            2
            3

        ρ

          h

            3

        .

    {\displaystyle J_{1}:=\int {-h}^{h}\rho ~dx{3}=2\rho h\quad {\text{and}}\quad J_{3}:=\int {-h}^{h}x{3}^{2}~\rho ~dx_{3}={\frac {2}{3}}\rho h^{3}\,.}

Isotropic Kirchhoff–Love plates

For an isotropic and homogeneous plate, the stress-strain relations are

            [

                    σ

                      11

                    σ

                      22

                    σ

                      12

            ]

                  E

                  1
                  −

                    ν

                      2

            [

                  1

                  ν

                  0

                  ν

                  1

                  0

                  0

                  0

                  1
                  −
                  ν

            ]

            [

                    ε

                      11

                    ε

                      22

                    ε

                      12

            ]

        .

    {\displaystyle {\begin{bmatrix}\sigma _{11}\\sigma _{22}\\sigma _{12}\end{bmatrix}}={\cfrac {E}{1-\nu ^{2}}}{\begin{bmatrix}1&\nu &0\\nu &1&0\0&0&1-\nu \end{bmatrix}}{\begin{bmatrix}\varepsilon _{11}\\varepsilon _{22}\\varepsilon _{12}\end{bmatrix}}\,.}

where

          ε

            α
            β

    {\displaystyle \varepsilon _{\alpha \beta }}

 are the in-plane strains and

        ν

    {\displaystyle \nu }

 is the Poisson's ratio of the material. The strain-displacement relations
for Kirchhoff-Love plates are

          ε

            α
            β

            1
            2

        (

          u

            α
            ,
            β

        +

          u

            β
            ,
            α

        )
        −

          x

            3

          w

            ,
            α
            β

        .

    {\displaystyle \varepsilon {\alpha \beta }={\frac {1}{2}}(u{\alpha ,\beta }+u_{\beta ,\alpha })-x_{3}\,w_{,\alpha \beta }\,.}

Therefore, the resultant moments corresponding to these stresses are

            [

                    M

                      11

                    M

                      22

                    M

                      12

            ]

        −

                  2

                    h

                      3

                  E

                  3
                  (
                  1
                  −

                    ν

                      2

                  )

            [

                  1

                  ν

                  0

                  ν

                  1

                  0

                  0

                  0

                  1
                  −
                  ν

            ]

            [

                    w

                      ,
                      11

                    w

                      ,
                      22

                    w

                      ,
                      12

            ]

    {\displaystyle {\begin{bmatrix}M_{11}\M_{22}\M_{12}\end{bmatrix}}=-{\cfrac {2h^{3}E}{3(1-\nu ^{2})}}~{\begin{bmatrix}1&\nu &0\\nu &1&0\0&0&1-\nu \end{bmatrix}}{\begin{bmatrix}w_{,11}\w_{,22}\w_{,12}\end{bmatrix}}}

If we ignore the in-plane displacements

          u

            α
            β

    {\displaystyle u_{\alpha \beta }}

, the governing equations reduce to

        D

          ∇

            2

          ∇

            2

        w

        q
        (
        x
        ,
        t
        )
        −
        2
        ρ
        h

              w
              ¨

    {\displaystyle D\nabla ^{2}\nabla ^{2}w=q(x,t)-2\rho h{\ddot {w}}\,}

where

        D

    {\displaystyle D}

 is the bending stiffness of the plate. For a uniform plate of thickness

        2
        h

    {\displaystyle 2h}

,

        D
        :=

                  2

                    h

                      3

                  E

                  3
                  (
                  1
                  −

                    ν

                      2

                  )

        .

    {\displaystyle D:={\cfrac {2h^{3}E}{3(1-\nu ^{2})}}\,.}

The above equation can also be written in an alternative notation:

        μ
        Δ
        Δ
        w
        −

              q
              ^

        +
        ρ

          w

            t
            t

        0

        .

    {\displaystyle \mu \Delta \Delta w-{\hat {q}}+\rho w_{tt}=0\,.}

In solid mechanics, a plate is often modeled as a two-dimensional elastic body whose potential energy depends on how it is bent from a planar configuration, rather than how it is stretched (which is the instead the case for a membrane such as a drumhead). In such situations, a vibrating plate can be modeled in a manner analogous to a vibrating drum. However, the resulting partial differential equation for the vertical displacement w of a plate from its equilibrium position is fourth order, involving the square of the Laplacian of w, rather than second order, and its qualitative behavior is fundamentally different from that of the circular membrane drum.

Free vibrations of isotropic plates
For free vibrations, the external force q is zero, and the governing equation of an isotropic plate reduces to

        D

          ∇

            2

          ∇

            2

        w

        −
        2
        ρ
        h

              w
              ¨

    {\displaystyle D\nabla ^{2}\nabla ^{2}w=-2\rho h{\ddot {w}}}

or

        μ
        Δ
        Δ
        w
        +
        ρ

          w

            t
            t

        0

        .

    {\displaystyle \mu \Delta \Delta w+\rho w_{tt}=0\,.}

This relation can be derived in an alternative manner by considering the curvature of the plate. The potential energy density of a plate depends how the plate is deformed, and so on the mean curvature and Gaussian curvature of the plate. For small deformations, the mean curvature is expressed in terms of w, the vertical displacement of the plate from kinetic equilibrium, as Δw, the Laplacian of w, and the Gaussian curvature is the Monge–Ampère operator wxxwyy−w2xy. The total potential energy of a plate Ω therefore has the form

        U

          ∫

            Ω

        [
        (
        Δ
        w

          )

            2

        +
        (
        1
        −
        μ
        )
        (

          w

            x
            x

          w

            y
            y

        −

          w

            x
            y

            2

        )
        ]

        d
        x

        d
        y

    {\displaystyle U=\int {\Omega }[(\Delta w)^{2}+(1-\mu )(w{xx}w_{yy}-w_{xy}^{2})]\,dx\,dy}

apart from an overall inessential normalization constant. Here μ is a constant depending on the properties of the material.
The kinetic energy is given by an integral of the form

        T

            ρ
            2

          ∫

            Ω

          w

            t

            2

        d
        x

        d
        y
        .

    {\displaystyle T={\frac {\rho }{2}}\int {\Omega }w{t}^{2}\,dx\,dy.}

Hamilton's principle asserts that w is a stationary point with respect to variations of the total energy T+U. The resulting partial differential equation is

        ρ

          w

            t
            t

        +
        μ
        Δ
        Δ
        w

        0.

    {\displaystyle \rho w_{tt}+\mu \Delta \Delta w=0.\,}

Circular plates
For freely vibrating circular plates,

        w

        w
        (
        r
        ,
        t
        )

    {\displaystyle w=w(r,t)}

, and the Laplacian in cylindrical coordinates has the form

          ∇

            2

        w
        ≡

            1
            r

            ∂

              ∂
              r

          (

            r

                  ∂
                  w

                  ∂
                  r

          )

        .

    {\displaystyle \nabla ^{2}w\equiv {\frac {1}{r}}{\frac {\partial }{\partial r}}\left(r{\frac {\partial w}{\partial r}}\right)\,.}

Therefore, the governing equation for free vibrations of a circular plate of thickness

        2
        h

    {\displaystyle 2h}

 is

            1
            r

            ∂

              ∂
              r

          [

            r

                ∂

                  ∂
                  r

              {

                    1
                    r

                    ∂

                      ∂
                      r

                  (

                    r

                          ∂
                          w

                          ∂
                          r

                  )

              }

          ]

        −

              2
              ρ
              h

            D

                ∂

                  2

              w

              ∂

                t

                  2

        .

    {\displaystyle {\frac {1}{r}}{\frac {\partial }{\partial r}}\left[r{\frac {\partial }{\partial r}}\left{{\frac {1}{r}}{\frac {\partial }{\partial r}}\left(r{\frac {\partial w}{\partial r}}\right)\right}\right]=-{\frac {2\rho h}{D}}{\frac {\partial ^{2}w}{\partial t^{2}}}\,.}

Expanded out,

                ∂

                  4

              w

              ∂

                r

                  4

        +

            2
            r

                ∂

                  3

              w

              ∂

                r

                  3

        −

            1

              r

                2

                ∂

                  2

              w

              ∂

                r

                  2

        +

            1

              r

                3

              ∂
              w

              ∂
              r

        −

              2
              ρ
              h

            D

                ∂

                  2

              w

              ∂

                t

                  2

        .

    {\displaystyle {\frac {\partial ^{4}w}{\partial r^{4}}}+{\frac {2}{r}}{\frac {\partial ^{3}w}{\partial r^{3}}}-{\frac {1}{r^{2}}}{\frac {\partial ^{2}w}{\partial r^{2}}}+{\frac {1}{r^{3}}}{\frac {\partial w}{\partial r}}=-{\frac {2\rho h}{D}}{\frac {\partial ^{2}w}{\partial t^{2}}}\,.}

To solve this equation we use the idea of separation of variables and assume a solution of the form

        w
        (
        r
        ,
        t
        )

        W
        (
        r
        )
        F
        (
        t
        )

        .

    {\displaystyle w(r,t)=W(r)F(t)\,.}

Plugging this assumed solution into the governing equation gives us

            1

              β
              W

          [

                    d

                      4

                  W

                  d

                    r

                      4

            +

                2
                r

                    d

                      3

                  W

                  d

                    r

                      3

            −

                1

                  r

                    2

                    d

                      2

                  W

                  d

                    r

                      2

            +

                1

                  r

                    3

                  d
                  W

                  d
                  r

          ]

        −

            1
            F

                    d

                      2

                  F

                  d

                    t

                      2

          ω

            2

    {\displaystyle {\frac {1}{\beta W}}\left[{\frac {d^{4}W}{dr^{4}}}+{\frac {2}{r}}{\frac {d^{3}W}{dr^{3}}}-{\frac {1}{r^{2}}}{\frac {d^{2}W}{dr^{2}}}+{\frac {1}{r^{3}}}{\frac {dW}{dr}}\right]=-{\frac {1}{F}}{\cfrac {d^{2}F}{dt^{2}}}=\omega ^{2}}

where

          ω

            2

    {\displaystyle \omega ^{2}}

 is a constant and

        β
        :=
        2
        ρ
        h

          /

        D

    {\displaystyle \beta :=2\rho h/D}

. The solution of the right hand equation is

        F
        (
        t
        )

          Re

        [
        A

          e

            i
            ω
            t

        +
        B

          e

            −
            i
            ω
            t

        ]

        .

    {\displaystyle F(t)={\text{Re}}[Ae^{i\omega t}+Be^{-i\omega t}]\,.}

The left hand side equation can be written as

                d

                  4

              W

              d

                r

                  4

        +

            2
            r

                d

                  3

              W

              d

                r

                  3

        −

            1

              r

                2

                d

                  2

              W

              d

                r

                  2

        +

            1

              r

                3

                  d
                  W

                  d
                  r

          λ

            4

        W

    {\displaystyle {\frac {d^{4}W}{dr^{4}}}+{\frac {2}{r}}{\frac {d^{3}W}{dr^{3}}}-{\frac {1}{r^{2}}}{\frac {d^{2}W}{dr^{2}}}+{\frac {1}{r^{3}}}{\cfrac {dW}{dr}}=\lambda ^{4}W}

where

          λ

            4

        :=
        β

          ω

            2

    {\displaystyle \lambda ^{4}:=\beta \omega ^{2}}

. The general solution of this eigenvalue problem that is
appropriate for plates has the form

        W
        (
        r
        )

          C

            1

          J

            0

        (
        λ
        r
        )
        +

          C

            2

          I

            0

        (
        λ
        r
        )

    {\displaystyle W(r)=C_{1}J_{0}(\lambda r)+C_{2}I_{0}(\lambda r)}

where

          J

            0

    {\displaystyle J_{0}}

 is the order 0 Bessel function of the first kind and

          I

            0

    {\displaystyle I_{0}}

 is the order 0 modified Bessel function of the first kind. The constants

          C

            1

    {\displaystyle C_{1}}

 and

          C

            2

    {\displaystyle C_{2}}

 are determined from the boundary conditions. For a plate of radius

        a

    {\displaystyle a}

 with a clamped circumference, the boundary conditions are

        W
        (
        r
        )

        0

          and

                  d
                  W

                  d
                  r

        0

          at

        r

        a

        .

    {\displaystyle W(r)=0\quad {\text{and}}\quad {\cfrac {dW}{dr}}=0\quad {\text{at}}\quad r=a\,.}

From these boundary conditions we find that

          J

            0

        (
        λ
        a
        )

          I

            1

        (
        λ
        a
        )
        +

          I

            0

        (
        λ
        a
        )

          J

            1

        (
        λ
        a
        )

        0

        .

    {\displaystyle J_{0}(\lambda a)I_{1}(\lambda a)+I_{0}(\lambda a)J_{1}(\lambda a)=0\,.}

We can solve this equation for

          λ

            n

    {\displaystyle \lambda _{n}}

 (and there are an infinite number of roots) and from that find the modal frequencies

          ω

            n

          λ

            n

            2

          /

            β

    {\displaystyle \omega _{n}=\lambda _{n}^{2}/{\sqrt {\beta }}}

. We can also express the displacement in the form

        w
        (
        r
        ,
        t
        )

          ∑

            n

            1

            ∞

          C

            n

          [

              J

                0

            (

              λ

                n

            r
            )
            −

                    J

                      0

                  (

                    λ

                      n

                  a
                  )

                    I

                      0

                  (

                    λ

                      n

                  a
                  )

              I

                0

            (

              λ

                n

            r
            )

          ]

        [

          A

            n

          e

            i

              ω

                n

            t

        +

          B

            n

          e

            −
            i

              ω

                n

            t

        ]

        .

    {\displaystyle w(r,t)=\sum {n=1}^{\infty }C{n}\left[J_{0}(\lambda {n}r)-{\frac {J{0}(\lambda {n}a)}{I{0}(\lambda {n}a)}}I{0}(\lambda {n}r)\right][A{n}e^{i\omega {n}t}+B{n}e^{-i\omega _{n}t}]\,.}

For a given frequency

          ω

            n

    {\displaystyle \omega _{n}}

 the first term inside the sum in the above equation gives the mode shape. We can find the value
of

          C

            n

    {\displaystyle C_{n}}

 using the appropriate boundary condition at

        r

        0

    {\displaystyle r=0}

 and the coefficients

          A

            n

    {\displaystyle A_{n}}

 and

          B

            n

    {\displaystyle B_{n}}

 from the initial conditions by taking advantage of the orthogonality of Fourier components.

Rectangular plates

Consider a rectangular plate which has dimensions

        a
        ×
        b

    {\displaystyle a\times b}

 in the

        (

          x

            1

        ,

          x

            2

        )

    {\displaystyle (x_{1},x_{2})}

-plane and thickness

        2
        h

    {\displaystyle 2h}

 in the

          x

            3

    {\displaystyle x_{3}}

-direction. We seek to find the free vibration modes of the plate.
Assume a displacement field of the form

        w
        (

          x

            1

        ,

          x

            2

        ,
        t
        )

        W
        (

          x

            1

        ,

          x

            2

        )
        F
        (
        t
        )

        .

    {\displaystyle w(x_{1},x_{2},t)=W(x_{1},x_{2})F(t)\,.}

Then,

          ∇

            2

          ∇

            2

        w

          w

            ,
            1111

        +
        2

          w

            ,
            1212

        +

          w

            ,
            2222

          [

                    ∂

                      4

                  W

                  ∂

                    x

                      1

                      4

            +
            2

                    ∂

                      4

                  W

                  ∂

                    x

                      1

                      2

                  ∂

                    x

                      2

                      2

            +

                    ∂

                      4

                  W

                  ∂

                    x

                      2

                      4

          ]

        F
        (
        t
        )

    {\displaystyle \nabla ^{2}\nabla ^{2}w=w_{,1111}+2w_{,1212}+w_{,2222}=\left[{\frac {\partial ^{4}W}{\partial x_{1}^{4}}}+2{\frac {\partial ^{4}W}{\partial x_{1}^{2}\partial x_{2}^{2}}}+{\frac {\partial ^{4}W}{\partial x_{2}^{4}}}\right]F(t)}

and

              w
              ¨

        W
        (

          x

            1

        ,

          x

            2

        )

                d

                  2

              F

              d

                t

                  2

        .

    {\displaystyle {\ddot {w}}=W(x_{1},x_{2}){\frac {d^{2}F}{dt^{2}}}\,.}

Plugging these into the governing equation gives

            D

              2
              ρ
              h
              W

          [

                    ∂

                      4

                  W

                  ∂

                    x

                      1

                      4

            +
            2

                    ∂

                      4

                  W

                  ∂

                    x

                      1

                      2

                  ∂

                    x

                      2

                      2

            +

                    ∂

                      4

                  W

                  ∂

                    x

                      2

                      4

          ]

        −

            1
            F

                d

                  2

              F

              d

                t

                  2

          ω

            2

    {\displaystyle {\frac {D}{2\rho hW}}\left[{\frac {\partial ^{4}W}{\partial x_{1}^{4}}}+2{\frac {\partial ^{4}W}{\partial x_{1}^{2}\partial x_{2}^{2}}}+{\frac {\partial ^{4}W}{\partial x_{2}^{4}}}\right]=-{\frac {1}{F}}{\frac {d^{2}F}{dt^{2}}}=\omega ^{2}}

where

          ω

            2

    {\displaystyle \omega ^{2}}

 is a constant because the left hand side is independent of

        t

    {\displaystyle t}

 while the right hand side is independent of

          x

            1

        ,

          x

            2

    {\displaystyle x_{1},x_{2}}

. From the right hand side, we then have

        F
        (
        t
        )

        A

          e

            i
            ω
            t

        +
        B

          e

            −
            i
            ω
            t

        .

    {\displaystyle F(t)=Ae^{i\omega t}+Be^{-i\omega t}\,.}

From the left hand side,

                ∂

                  4

              W

              ∂

                x

                  1

                  4

        +
        2

                ∂

                  4

              W

              ∂

                x

                  1

                  2

              ∂

                x

                  2

                  2

        +

                ∂

                  4

              W

              ∂

                x

                  2

                  4

              2
              ρ
              h

                ω

                  2

            D

        W
        =:

          λ

            4

        W

    {\displaystyle {\frac {\partial ^{4}W}{\partial x_{1}^{4}}}+2{\frac {\partial ^{4}W}{\partial x_{1}^{2}\partial x_{2}^{2}}}+{\frac {\partial ^{4}W}{\partial x_{2}^{4}}}={\frac {2\rho h\omega ^{2}}{D}}W=:\lambda ^{4}W}

where

          λ

            2

        ω

                2
                ρ
                h

              D

        .

    {\displaystyle \lambda ^{2}=\omega {\sqrt {\frac {2\rho h}{D}}}\,.}

Since the above equation is a biharmonic eigenvalue problem, we look for Fourier expansion
solutions of the form

          W

            m
            n

        (

          x

            1

        ,

          x

            2

        )

        sin
        ⁡

              m
              π

                x

                  1

            a

        sin
        ⁡

              n
              π

                x

                  2

            b

        .

    {\displaystyle W_{mn}(x_{1},x_{2})=\sin {\frac {m\pi x_{1}}{a}}\sin {\frac {n\pi x_{2}}{b}}\,.}

We can check and see that this solution satisfies the boundary conditions for a freely vibrating
rectangular plate with simply supported edges:

                w
                (

                  x

                    1

                ,

                  x

                    2

                ,
                t
                )

                0

                  at

                  x

                    1

                0
                ,
                a

                  and

                  x

                    2

                0
                ,
                b

                  M

                    11

                D

                  (

                            ∂

                              2

                          w

                          ∂

                            x

                              1

                              2

                    +
                    ν

                            ∂

                              2

                          w

                          ∂

                            x

                              2

                              2

                  )

                0

                  at

                  x

                    1

                0
                ,
                a

                  M

                    22

                D

                  (

                            ∂

                              2

                          w

                          ∂

                            x

                              2

                              2

                    +
                    ν

                            ∂

                              2

                          w

                          ∂

                            x

                              1

                              2

                  )

                0

                  at

                  x

                    2

                0
                ,
                b

                .

    {\displaystyle {\begin{aligned}w(x_{1},x_{2},t)=0&\quad {\text{at}}\quad x_{1}=0,a\quad {\text{and}}\quad x_{2}=0,b\M_{11}=D\left({\frac {\partial ^{2}w}{\partial x_{1}^{2}}}+\nu {\frac {\partial ^{2}w}{\partial x_{2}^{2}}}\right)=0&\quad {\text{at}}\quad x_{1}=0,a\M_{22}=D\left({\frac {\partial ^{2}w}{\partial x_{2}^{2}}}+\nu {\frac {\partial ^{2}w}{\partial x_{1}^{2}}}\right)=0&\quad {\text{at}}\quad x_{2}=0,b\,.\end{aligned}}}

Plugging the solution into the biharmonic equation gives us

          λ

            2

          π

            2

          (

                  m

                    2

                  a

                    2

            +

                  n

                    2

                  b

                    2

          )

        .

    {\displaystyle \lambda ^{2}=\pi ^{2}\left({\frac {m^{2}}{a^{2}}}+{\frac {n^{2}}{b^{2}}}\right)\,.}

Comparison with the previous expression for

          λ

            2

    {\displaystyle \lambda ^{2}}

 indicates that we can have an infinite
number of solutions with

          ω

            m
            n

          (

                  m

                    2

                  a

                    2

            +

                  n

                    2

                  b

                    2

          )

                D

                  π

                    4

                2
                ρ
                h

        .

    {\displaystyle \omega _{mn}=\left({\frac {m^{2}}{a^{2}}}+{\frac {n^{2}}{b^{2}}}\right){\sqrt {\frac {D\pi ^{4}}{2\rho h}}}\,.}

Therefore the general solution for the plate equation is

        w
        (

          x

            1

        ,

          x

            2

        ,
        t
        )

          ∑

            m

            1

            ∞

          ∑

            n

            1

            ∞

        sin
        ⁡

              m
              π

                x

                  1

            a

        sin
        ⁡

              n
              π

                x

                  2

            b

          (

              A

                m
                n

              e

                i

                  ω

                    m
                    n

                t

            +

              B

                m
                n

              e

                −
                i

                  ω

                    m
                    n

                t

          )

        .

    {\displaystyle w(x_{1},x_{2},t)=\sum _{m=1}^{\infty }\sum {n=1}^{\infty }\sin {\frac {m\pi x{1}}{a}}\sin {\frac {n\pi x_{2}}{b}}\left(A_{mn}e^{i\omega {mn}t}+B{mn}e^{-i\omega _{mn}t}\right)\,.}

To find the values of

          A

            m
            n

    {\displaystyle A_{mn}}

 and

          B

            m
            n

    {\displaystyle B_{mn}}

 we use initial conditions and the orthogonality of Fourier components. For example, if

        w
        (

          x

            1

        ,

          x

            2

        ,
        0
        )

        φ
        (

          x

            1

        ,

          x

            2

        )

          on

          x

            1

        ∈
        [
        0
        ,
        a
        ]

          and

              ∂
              w

              ∂
              t

        (

          x

            1

        ,

          x

            2

        ,
        0
        )

        ψ
        (

          x

            1

        ,

          x

            2

        )

          on

          x

            2

        ∈
        [
        0
        ,
        b
        ]

    {\displaystyle w(x_{1},x_{2},0)=\varphi (x_{1},x_{2})\quad {\text{on}}\quad x_{1}\in [0,a]\quad {\text{and}}\quad {\frac {\partial w}{\partial t}}(x_{1},x_{2},0)=\psi (x_{1},x_{2})\quad {\text{on}}\quad x_{2}\in [0,b]}

we get,

                  A

                    m
                    n

                    4

                      a
                      b

                  ∫

                    0

                    a

                  ∫

                    0

                    b

                φ
                (

                  x

                    1

                ,

                  x

                    2

                )
                sin
                ⁡

                      m
                      π

                        x

                          1

                    a

                sin
                ⁡

                      n
                      π

                        x

                          2

                    b

                d

                  x

                    1

                d

                  x

                    2

                  B

                    m
                    n

                    4

                      a
                      b

                        ω

                          m
                          n

                  ∫

                    0

                    a

                  ∫

                    0

                    b

                ψ
                (

                  x

                    1

                ,

                  x

                    2

                )
                sin
                ⁡

                      m
                      π

                        x

                          1

                    a

                sin
                ⁡

                      n
                      π

                        x

                          2

                    b

                d

                  x

                    1

                d

                  x

                    2

                .

    {\displaystyle {\begin{aligned}A_{mn}&={\frac {4}{ab}}\int _{0}^{a}\int {0}^{b}\varphi (x{1},x_{2})\sin {\frac {m\pi x_{1}}{a}}\sin {\frac {n\pi x_{2}}{b}}dx_{1}dx_{2}\B_{mn}&={\frac {4}{ab\omega _{mn}}}\int _{0}^{a}\int {0}^{b}\psi (x{1},x_{2})\sin {\frac {m\pi x_{1}}{a}}\sin {\frac {n\pi x_{2}}{b}}dx_{1}dx_{2}\,.\end{aligned}}}
