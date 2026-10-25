# Derivative (multivariable calculus)

Derivative (multivariable calculus)

In mathematics, the derivative of a function at a point is the linear part of the best affine approximation to the function near the point. In one-variable calculus, this is the tangent line approximation. In multivariable calculus, the same property is generalized to define the derivative of a vector-valued function or function of a vector argument. Sometimes called the total derivative, in contrast with partial derivatives, the derivative approximates the function with respect to all of its arguments, not just a single one. In many situations, this is the same as considering all partial derivatives simultaneously.
In functional analysis, particularly in infinite dimensions, the derivative in this sense is called the Fréchet derivative.

Derivative as a linear map
Let

        U
        ⊆

            R

            n

    {\displaystyle U\subseteq \mathbb {R} ^{n}}

 be an open subset. Then a function

        f
        :
        U
        →

            R

            m

    {\displaystyle f\colon U\to \mathbb {R} ^{m}}

 is said to be differentiable at a point

        a
        ∈
        U

    {\displaystyle a\in U}

 if there exists a linear transformation

        D

          f

            a

        :

            R

            n

        →

            R

            m

    {\displaystyle Df_{a}\colon \mathbb {R} ^{n}\to \mathbb {R} ^{m}}

 such that

          lim

            x
            →
            a

              f
              (
              x
              )
              −
              f
              (
              a
              )
              −
              D

                f

                  a

              (
              x
              −
              a
              )

              ‖
              x
              −
              a
              ‖

        0

    {\displaystyle \lim {x\to a}{\frac {f(x)-f(a)-Df{a}(x-a)}{|x-a|}}=0}

where

        ‖
        …
        ‖

    {\displaystyle |\ldots |}

 denotes the norm of

        …

    {\displaystyle \ldots }

. The linear map

        D

          f

            a

    {\displaystyle Df_{a}}

 is called the derivative or differential of

        f

    {\displaystyle f}

 at

        a

    {\displaystyle a}

. Here

        D

          f

            a

        (
        x
        −
        a
        )

    {\displaystyle Df_{a}(x-a)}

 refers to applying the linear transformation

        D

          f

            a

    {\displaystyle Df_{a}}

 to the vector

        (
        x
        −
        a
        )

    {\displaystyle (x-a)}

; in coordinates, this is a matrix-vector product. Other notations for the derivative include

          D

            a

        f

    {\displaystyle D_{a}f}

 and

        D
        f
        (
        a
        )

    {\displaystyle Df(a)}

. A function is differentiable if its derivative exists at every point in its domain.
Conceptually, the definition of the derivative expresses the idea that

        D

          f

            a

    {\displaystyle Df_{a}}

 is the best linear approximation to

        f
        (
        a
        +
        h
        )
        −
        f
        (
        a
        )

    {\displaystyle f(a+h)-f(a)}

 for small

        h

    {\displaystyle h}

. This can be made precise by quantifying the error in the linear approximation

        D

          f

            a

    {\displaystyle Df_{a}}

. To do so, write

        f
        (
        a
        +
        h
        )

        f
        (
        a
        )
        +
        D

          f

            a

        (
        h
        )
        +
        ε
        (
        h
        )
        ,

    {\displaystyle f(a+h)=f(a)+Df_{a}(h)+\varepsilon (h),}

where

        ε
        (
        h
        )

    {\displaystyle \varepsilon (h)}

 equals the error in the approximation. To say that the derivative of

        f

    {\displaystyle f}

 at

        a

    {\displaystyle a}

 is

        D

          f

            a

    {\displaystyle Df_{a}}

 is equivalent to the statement

        ε
        (
        h
        )

        o
        (
        h
        )
        ,

    {\displaystyle \varepsilon (h)=o(h),}

where

        o

    {\displaystyle o}

 is little-o notation and means that

        ε
        (
        h
        )

          /

        ‖
        h
        ‖

    {\displaystyle \varepsilon (h)/|h|}

 tends to zero as

        h
        →
        0

    {\displaystyle h\to 0}

. The derivative

        D

          f

            a

    {\displaystyle Df_{a}}

 is the unique linear transformation for which the error term is this small, and this is the sense in which it is the best linear approximation to

        f
        (
        a
        +
        h
        )
        −
        f
        (
        a
        )

    {\displaystyle f(a+h)-f(a)}

.

Differentiability

The function

        f

    {\displaystyle f}

 is differentiable if and only if each of its components

          f

            i

        :
        U
        →

          R

    {\displaystyle f_{i}\colon U\to \mathbb {R} }

 is differentiable, so when studying derivatives, it is often possible to work one coordinate at a time in the codomain. However, the same is not true of the coordinates in the domain. It is true that if

        f

    {\displaystyle f}

 is differentiable at

        a

    {\displaystyle a}

, then each partial derivative

        ∂
        f

          /

        ∂

          x

            i

    {\displaystyle \partial f/\partial x_{i}}

 exists at

        a

    {\displaystyle a}

.
The converse does not hold: it can happen that all of the partial derivatives of

        f

    {\displaystyle f}

 at

        a

    {\displaystyle a}

 exist, but

        f

    {\displaystyle f}

 is not differentiable at

        a

    {\displaystyle a}

. An example is the following function, which is continuous and has both partial derivatives zero at the origin, but is not differentiable there:

        f
        (
        x
        ,
        y
        )

            {

                        x
                        y

                          x

                            2

                        +

                          y

                            2

                  (
                  x
                  ,
                  y
                  )
                  ≠
                  (
                  0
                  ,
                  0
                  )

                  0

                  (
                  x
                  ,
                  y
                  )

                  (
                  0
                  ,
                  0
                  )

        .

    {\displaystyle f(x,y)={\begin{cases}{\frac {xy}{\sqrt {x^{2}+y^{2}}}}&(x,y)\neq (0,0)\0&(x,y)=(0,0)\end{cases}}.}

(In polar coordinates, this function is

        f

        r
        cos
        ⁡
        θ
        sin
        ⁡
        θ

    {\displaystyle f=r\cos \theta \sin \theta }

.)
Even the existence and linearity of all directional derivatives at a point is not sufficient for differentiability; the essential additional requirement is that the linear approximation hold uniformly as the increment tends to zero from all directions. An example is

        f
        (
        x
        ,
        y
        )

            {

                          x

                            2

                        y

                          x

                            4

                        +

                          y

                            2

                        x

                          2

                      +

                        y

                          2

                  (
                  x
                  ,
                  y
                  )
                  ≠
                  (
                  0
                  ,
                  0
                  )

                  0

                  (
                  x
                  ,
                  y
                  )

                  (
                  0
                  ,
                  0
                  )

    {\displaystyle f(x,y)={\begin{cases}{\frac {x^{2}y}{x^{4}+y^{2}}}{\sqrt {x^{2}+y^{2}}}&(x,y)\neq (0,0)\0&(x,y)=(0,0)\end{cases}}}

whose directional derivatives are all 0 at (0,0), but which fails to be differentiable there.
However, if all the partial derivatives of

        f

    {\displaystyle f}

 at

        a

    {\displaystyle a}

 exist in a neighborhood of

        a

    {\displaystyle a}

 and are continuous at

        a

    {\displaystyle a}

, then

        f

    {\displaystyle f}

 is differentiable at

        a

    {\displaystyle a}

. If

        f

    {\displaystyle f}

 is differentiable at a point, then the derivative of

        f

    {\displaystyle f}

 is the linear transformation corresponding to the Jacobian matrix of partial derivatives at the point.

Differentials
In some advanced calculus texts, the derivative is also called the differential. However, this term has several different, but closely connected meanings, in mathematics and the sciences.
When a differentiable function

        f
        :

            R

            n

        →

          R

    {\displaystyle f\colon \mathbb {R} ^{n}\to \mathbb {R} }

 is scalar valued, the derivative of

        f

    {\displaystyle f}

 at

        a

    {\displaystyle a}

 may be written as the Jacobian matrix, which in this instance is a row matrix (a matrix consisting of elements in a single row, i.e., a row vector):

        D

          f

            a

            [

                        ∂
                        f

                        ∂

                          x

                            1

                  (
                  a
                  )

                  ⋯

                        ∂
                        f

                        ∂

                          x

                            n

                  (
                  a
                  )

            ]

        .

    {\displaystyle Df_{a}={\begin{bmatrix}{\frac {\partial f}{\partial x_{1}}}(a)&\cdots &{\frac {\partial f}{\partial x_{n}}}(a)\end{bmatrix}}.}

The linear approximation property of the derivative implies that if

        Δ
        x

              [

                    Δ

                      x

                        1

                    ⋯

                    Δ

                      x

                        n

              ]

              T

    {\displaystyle \Delta x={\begin{bmatrix}\Delta x_{1}&\cdots &\Delta x_{n}\end{bmatrix}}^{\mathsf {T}}}

is a small vector (where the

            T

    {\displaystyle {\mathsf {T}}}

 denotes transpose, so that this vector is a column vector), then

        f
        (
        a
        +
        Δ
        x
        )
        −
        f
        (
        a
        )
        ≈
        D

          f

            a

        Δ
        x

          ∑

            i

            1

            n

              ∂
              f

              ∂

                x

                  i

        (
        a
        )

        Δ

          x

            i

        .

    {\displaystyle f(a+\Delta x)-f(a)\approx Df_{a}\,\Delta x=\sum {i=1}^{n}{\frac {\partial f}{\partial x{i}}}(a)\,\Delta x_{i}.}

Heuristically, this suggests that if

        d

          x

            1

        ,
        …
        ,
        d

          x

            n

    {\displaystyle dx_{1},\ldots ,dx_{n}}

 are infinitesimal increments in the coordinate directions, then

        d

          f

            a

          ∑

            i

            1

            n

              ∂
              f

              ∂

                x

                  i

        (
        a
        )

        d

          x

            i

    {\displaystyle df_{a}=\sum {i=1}^{n}{\frac {\partial f}{\partial x{i}}}(a)\,dx_{i}}

and this is the differential of

        f

    {\textstyle f}

 at

        a

    {\textstyle a}

. In fact, the notion of the infinitesimal, which is merely symbolic here, can be equipped with extensive mathematical structure. Techniques, such as the theory of differential forms, effectively give analytical and algebraic descriptions of objects like infinitesimal increments,

        d

          x

            i

    {\displaystyle dx_{i}}

. For instance,

        d

          x

            i

    {\displaystyle dx_{i}}

 may be inscribed as a linear functional on the vector space

            R

            n

    {\displaystyle \mathbb {R} ^{n}}

. Evaluating

        d

          x

            i

    {\displaystyle dx_{i}}

 at a vector

        h

    {\displaystyle h}

 in

            R

            n

    {\displaystyle \mathbb {R} ^{n}}

 measures how much

        h

    {\displaystyle h}

 points in the

        i

    {\displaystyle i}

-th coordinate direction. The differential

        d

          f

            a

    {\displaystyle df_{a}}

 is a linear combination of linear functionals and hence is itself a linear functional. The evaluation

        d

          f

            a

        (
        h
        )

    {\displaystyle df_{a}(h)}

 is the directional derivative of

        f

    {\displaystyle f}

 along

        h

    {\displaystyle h}

. This point of view makes the derivative an instance of the exterior derivative.
Being a linear form, the differential is naturally a covector. In a Euclidean space, a covector is naturally dual to a vector (its transpose). This vector is called the gradient of

        f

    {\displaystyle f}

, and points in the direction in which

        f

    {\displaystyle f}

 increases most rapidly.
Suppose now that

        f

    {\displaystyle f}

 is a vector-valued function, that is,

        f
        :

            R

            n

        →

            R

            m

    {\displaystyle f\colon \mathbb {R} ^{n}\to \mathbb {R} ^{m}}

. In this case, the components

          f

            i

    {\displaystyle f_{i}}

 of

        f

    {\displaystyle f}

 are real-valued functions, so they have associated differential forms

        d

          f

            i

    {\displaystyle df_{i}}

. The differential

        d
        f

    {\displaystyle df}

 amalgamates these forms into a single object and is therefore an instance of a vector-valued differential form.
If

        f
        :
        M
        →
        N

    {\displaystyle f\colon M\to N}

 is a mapping between differentiable manifolds, differentiability can be formulated by differentiability in any coordinate chart. Invariantly, the differential of

        f

    {\displaystyle f}

 at a point

        p
        ∈
        M

    {\displaystyle p\in M}

 is a linear map

        d

          f

            p

        :

          T

            p

        M
        →

          T

            f
            (
            p
            )

        N

    {\displaystyle df_{p}\colon T_{p}M\to T_{f(p)}N}

 from the tangent space of

        M

    {\displaystyle M}

 at

        p

    {\displaystyle p}

 to that of

        N

    {\displaystyle N}

 at

        f
        (
        p
        )

    {\displaystyle f(p)}

. This is also known as the pushforward. This is closely related to the derivative as a linear approximation, since evaluating

        d

          f

            p

    {\displaystyle df_{p}}

 on a tangent vector gives the directional derivative of

        f

    {\displaystyle f}

 in that direction. Nevertheless, the differential is not quite the same thing as the derivative of a function between vector spaces:

        f

    {\displaystyle f}

 is a mapping of manifolds and not of the vector spaces

          T

            p

        M

    {\displaystyle T_{p}M}

 and

          T

            f
            (
            p
            )

        N

    {\displaystyle T_{f(p)}N}

 where the linear approximation lives.
In applications such as thermodynamics, the language of differentials often has an additional conceptual role. Expressions such as

        d
        U

        T

        d
        S
        −
        P

        d
        V

    {\displaystyle dU=T\,dS-P\,dV}

 describe differentials of state functions and lead to questions about exactness, natural variables, and relations among partial derivatives. This use is related to the derivative of a multivariable function, but it is not just another name for the linear map

        D

          f

            a

    {\displaystyle Df_{a}}

 associated with an ordinary function.

Total derivative
The term total derivative is also used in more than one way. In some mathematical texts it denotes the full derivative

        D

          f

            a

    {\displaystyle Df_{a}}

, as opposed to any one partial derivative. In that sense, the total derivative is the linear map that accounts for variation in all coordinate directions simultaneously.
In many applied contexts, however, "total derivative" refers instead to the derivative of a composite dependence. For example, if

        z

        f
        (
        x
        ,
        y
        )
        ,

        x

        x
        (
        t
        )
        ,

        y

        y
        (
        t
        )
        ,

    {\displaystyle z=f(x,y),\qquad x=x(t),\quad y=y(t),}

then the total derivative of

        z

    {\displaystyle z}

 with respect to

        t

    {\displaystyle t}

 is

              d
              z

              d
              t

              ∂
              f

              ∂
              x

              d
              x

              d
              t

        +

              ∂
              f

              ∂
              y

              d
              y

              d
              t

        .

    {\displaystyle {\frac {dz}{dt}}={\frac {\partial f}{\partial x}}{\frac {dx}{dt}}+{\frac {\partial f}{\partial y}}{\frac {dy}{dt}}.}

This is the ordinary derivative of the composite function

        f
        (
        x
        (
        t
        )
        ,
        y
        (
        t
        )
        )

    {\displaystyle f(x(t),y(t))}

, computed by the chain rule. Equivalently, it is obtained by applying the derivative of

        f

    {\displaystyle f}

 to the velocity vector of the path

        t
        ↦
        (
        x
        (
        t
        )
        ,
        y
        (
        t
        )
        )

    {\displaystyle t\mapsto (x(t),y(t))}

:

            d

              d
              t

        f
        (
        x
        (
        t
        )
        ,
        y
        (
        t
        )
        )

        D

          f

            (
            x
            (
            t
            )
            ,
            y
            (
            t
            )
            )

        (

          x
          ′

        (
        t
        )
        ,

          y
          ′

        (
        t
        )
        )
        .

    {\displaystyle {\frac {d}{dt}}f(x(t),y(t))=Df_{(x(t),y(t))}(x'(t),y'(t)).}

This chain-rule sense of "total derivative" is common in physics, engineering, economics, and other applied fields. In mechanics, for instance, the total time derivative of a function

        F
        (
        q
        ,
        p
        ,
        t
        )

    {\displaystyle F(q,p,t)}

 along a trajectory includes both explicit dependence on

        t

    {\displaystyle t}

 and implicit dependence through the time-dependent variables

        q
        (
        t
        )

    {\displaystyle q(t)}

 and

        p
        (
        t
        )

    {\displaystyle p(t)}

. In fluid mechanics, related terminology appears in the material derivative, which differentiates a quantity along the motion of a fluid parcel.
Another example is in classical mechanics, where the total derivative of a function that depends on phase space parameters and time is its partial derivative in time plus its Poisson bracket with the Hamiltonian

        H

    {\displaystyle H}

:

              d
              f

              d
              t

              ∂
              f

              ∂
              t

        +
        {
        f
        ,
        H
        }

    {\displaystyle {\frac {df}{dt}}={\frac {\partial f}{\partial t}}+{f,H}}

Like the material derivative, total derivative in mechanics has the property that it is the derivative of the composite when pulled back to any Hamiltonian trajectory, but is still treated as a function of all phase space coordinates and time.
In comparative statics, total derivatives often describe how endogenous variables change with respect to exogenous variables in an implicitly defined system of equations. The endogeneous variables are generally not explicit functions of the exogeneous variables, other than through the implicit function theorem, and the total derivative is handled implicitly.
Thus, although "total derivative" can mean the derivative

        D

          f

            a

    {\displaystyle Df_{a}}

 in the sense above, the term also commonly refers to a derivative along a specified dependence or process. This ambiguity is one reason to distinguish between the derivative as a linear map and the various differential or total-derivative notations used in applications.

Chain rule

A form of the chain rule generalizes from one-variable calculus. It says that, for two functions

        f

    {\displaystyle f}

 and

        g

    {\displaystyle g}

, the derivative of the composite function

        f
        ∘
        g

    {\displaystyle f\circ g}

 at

        a

    {\displaystyle a}

 satisfies

        D
        (
        f
        ∘
        g

          )

            a

        D

          f

            g
            (
            a
            )

        ∘
        D

          g

            a

    {\displaystyle D(f\circ g){a}=Df{g(a)}\circ Dg_{a}}

where the composite on the right-hand side is the composition of linear maps. If the derivatives of

        f

    {\displaystyle f}

 and

        g

    {\displaystyle g}

 are identified with their Jacobian matrices, then the composite on the right-hand side is simply matrix multiplication.

Example: Differentiation with direct dependencies
Suppose that f is a function of two variables, x and y. If these two variables are independent, so that the domain of f is

            R

            2

    {\displaystyle \mathbb {R} ^{2}}

, then the behavior of f may be understood in terms of its partial derivatives in the x and y directions. However, in some situations, x and y may be dependent. For example, it might happen that f is constrained to a curve

        y

        y
        (
        x
        )

    {\displaystyle y=y(x)}

. In this case, we are actually interested in the behavior of the composite function

        f
        (
        x
        ,
        y
        (
        x
        )
        )

    {\displaystyle f(x,y(x))}

. The partial derivative of f with respect to x does not give the true rate of change of f with respect to changing x because changing x necessarily changes y, while the partial derivative assumes y is fixed. However, the chain rule takes such dependencies into account. Write

        γ
        (
        x
        )

        (
        x
        ,
        y
        (
        x
        )
        )

    {\displaystyle \gamma (x)=(x,y(x))}

. Then, the chain rule says

        D
        (
        f
        ∘
        γ

          )

              x

                0

        D

          f

            (

              x

                0

            ,
            y
            (

              x

                0

            )
            )

        ∘
        D

          γ

              x

                0

        .

    {\displaystyle D(f\circ \gamma ){x{0}}=Df_{(x_{0},y(x_{0}))}\circ D\gamma {x{0}}.}

By expressing the derivative using Jacobian matrices such as

                D

                  f

                    (

                      x

                        0

                    ,
                    y
                    (

                      x

                        0

                    )
                    )

                      [

                                  ∂
                                  f

                                  ∂
                                  x

                                  ∂
                                  f

                                  ∂
                                  y

                      ]

                    (

                      x

                        0

                    ,
                    y
                    (

                      x

                        0

                    )
                    )

                D

                  γ

                      x

                        0

                      [

                                  ∂
                                  x

                                  ∂
                                  x

                                  ∂
                                  y

                                  ∂
                                  x

                      ]

                      x

                        0

                .

    {\displaystyle {\begin{array}{lcl}Df_{(x_{0},y(x_{0}))}&=&{\begin{bmatrix}{\frac {\partial f}{\partial x}}&{\frac {\partial f}{\partial y}}\end{bmatrix}}{(x{0},y(x_{0}))}\D\gamma {x{0}}&=&{\begin{bmatrix}{\frac {\partial x}{\partial x}}\{\frac {\partial y}{\partial x}}\end{bmatrix}}{x{0}}.\end{array}}}

This becomes:

              d
              f
              (
              x
              ,
              y
              (
              x
              )
              )

              d
              x

        (

          x

            0

        )

              ∂
              f

              ∂
              x

        (

          x

            0

        ,
        y
        (

          x

            0

        )
        )

              d
              x

              d
              x

        (

          x

            0

        )
        +

              ∂
              f

              ∂
              y

        (

          x

            0

        ,
        y
        (

          x

            0

        )
        )

              d
              y

              d
              x

        (

          x

            0

        )
        .

    {\displaystyle {\frac {df(x,y(x))}{dx}}(x_{0})={\frac {\partial f}{\partial x}}(x_{0},y(x_{0}))\,{\frac {dx}{dx}}(x_{0})+{\frac {\partial f}{\partial y}}(x_{0},y(x_{0}))\,{\frac {dy}{dx}}(x_{0}).}

Suppressing the evaluation at

          x

            0

    {\displaystyle x_{0}}

 for legibility, we may also write this as

              d
              f
              (
              x
              ,
              y
              (
              x
              )
              )

              d
              x

              ∂
              f

              ∂
              x

              d
              x

              d
              x

        +

              ∂
              f

              ∂
              y

              d
              y

              d
              x

        .

    {\displaystyle {\frac {df(x,y(x))}{dx}}={\frac {\partial f}{\partial x}}{\frac {dx}{dx}}+{\frac {\partial f}{\partial y}}{\frac {dy}{dx}}.}

This gives a straightforward formula for the derivative of

        f
        (
        x
        ,
        y
        (
        x
        )
        )

    {\displaystyle f(x,y(x))}

 in terms of the partial derivatives of

        f

    {\displaystyle f}

 and the derivative of

        y
        (
        x
        )

    {\displaystyle y(x)}

.
For example, suppose

        f
        (
        x
        ,
        y
        )

        x
        y
        .

    {\displaystyle f(x,y)=xy.}

The rate of change of f with respect to x is usually the partial derivative of f with respect to x; in this case,

              ∂
              f

              ∂
              x

        y
        .

    {\displaystyle {\frac {\partial f}{\partial x}}=y.}

However, if y depends on x, the partial derivative does not give the true rate of change of f as x changes because the partial derivative assumes that y is fixed. Suppose we are constrained to the line

        y

        x
        .

    {\displaystyle y=x.}

Then

        f
        (
        x
        ,
        y
        )

        f
        (
        x
        ,
        x
        )

          x

            2

        ,

    {\displaystyle f(x,y)=f(x,x)=x^{2},}

and the total derivative of f with respect to x is

              d
              f

              d
              x

        2
        x
        ,

    {\displaystyle {\frac {df}{dx}}=2x,}

which we see is not equal to the partial derivative

        ∂
        f

          /

        ∂
        x

    {\displaystyle \partial f/\partial x}

. Instead of immediately substituting for y in terms of x, however, we can also use the chain rule as above:

              d
              f

              d
              x

              ∂
              f

              ∂
              x

        +

              ∂
              f

              ∂
              y

              d
              y

              d
              x

        y
        +
        x
        ⋅
        1

        x
        +
        y

        2
        x
        .

    {\displaystyle {\frac {df}{dx}}={\frac {\partial f}{\partial x}}+{\frac {\partial f}{\partial y}}{\frac {dy}{dx}}=y+x\cdot 1=x+y=2x.}

Example: Differentiation with indirect dependencies
While one can often perform substitutions to eliminate indirect dependencies, the chain rule provides for a more efficient and general technique. Suppose

        L
        (
        t
        ,

          x

            1

        ,
        …
        ,

          x

            n

        )

    {\displaystyle L(t,x_{1},\dots ,x_{n})}

 is a function of time

        t

    {\displaystyle t}

 and

        n

    {\displaystyle n}

 variables

          x

            i

    {\displaystyle x_{i}}

 which themselves depend on time. Then, the time derivative of

        L

    {\displaystyle L}

 is

              d
              L

              d
              t

            d

              d
              t

        L

            (

        t
        ,

          x

            1

        (
        t
        )
        ,
        …
        ,

          x

            n

        (
        t
        )

            )

        .

    {\displaystyle {\frac {dL}{dt}}={\frac {d}{dt}}L{\bigl (}t,x_{1}(t),\ldots ,x_{n}(t){\bigr )}.}

The chain rule expresses this derivative in terms of the partial derivatives of

        L

    {\displaystyle L}

 and the time derivatives of the functions

          x

            i

    {\displaystyle x_{i}}

:

              d
              L

              d
              t

              ∂
              L

              ∂
              t

        +

          ∑

            i

            1

            n

              ∂
              L

              ∂

                x

                  i

              d

                x

                  i

              d
              t

            (

            ∂

              ∂
              t

        +

          ∑

            i

            1

            n

              d

                x

                  i

              d
              t

            ∂

              ∂

                x

                  i

            )

        (
        L
        )
        .

    {\displaystyle {\frac {dL}{dt}}={\frac {\partial L}{\partial t}}+\sum {i=1}^{n}{\frac {\partial L}{\partial x{i}}}{\frac {dx_{i}}{dt}}={\biggl (}{\frac {\partial }{\partial t}}+\sum {i=1}^{n}{\frac {dx{i}}{dt}}{\frac {\partial }{\partial x_{i}}}{\biggr )}(L).}

This expression is often used in physics for a gauge transformation of the Lagrangian, as two Lagrangians that differ only by the total time derivative of a function of time and the

        n

    {\displaystyle n}

 generalized coordinates lead to the same equations of motion. An interesting example concerns the resolution of causality concerning the Wheeler–Feynman time-symmetric theory. The operator in brackets (in the final expression above) is also called the total derivative operator (with respect to

        t

    {\displaystyle t}

).
For example, the total derivative of

        f
        (
        x
        (
        t
        )
        ,
        y
        (
        t
        )
        )

    {\displaystyle f(x(t),y(t))}

 is

              d
              f

              d
              t

              ∂
              f

              ∂
              x

              d
              x

              d
              t

        +

              ∂
              f

              ∂
              y

              d
              y

              d
              t

        .

    {\displaystyle {\frac {df}{dt}}={\partial f \over \partial x}{dx \over dt}+{\partial f \over \partial y}{dy \over dt}.}

Here there is no

        ∂
        f

          /

        ∂
        t

    {\displaystyle \partial f/\partial t}

 term since

        f

    {\displaystyle f}

 itself does not depend on the independent variable

        t

    {\displaystyle t}

 directly.

Total differential equation

A total differential equation is a differential equation expressed in terms of total derivatives. Since the exterior derivative is coordinate-free, in a sense that can be given a technical meaning, such equations are intrinsic and geometric.

Application to equation systems
In economics, it is common for the total derivative to arise in the context of a system of equations. For example, a simple supply-demand system might specify the quantity q of a product demanded as a function D of its price p and consumers' income I, the latter being an exogenous variable, and might specify the quantity supplied by producers as a function S of its price and two exogenous resource cost variables r and w. The resulting system of equations

                q

                D
                (
                p
                ,
                I
                )

                q

                S
                (
                p
                ,
                r
                ,
                w
                )

    {\displaystyle {\begin{aligned}q&=D(p,I)\q&=S(p,r,w)\end{aligned}}}

determines the market equilibrium values of the variables p and q. The total derivative

        d
        p

          /

        d
        r

    {\displaystyle dp/dr}

 of p with respect to r, for example, gives the sign and magnitude of the reaction of the market price to the exogenous variable r. In the indicated system, there are a total of six possible total derivatives, also known in this context as comparative static derivatives: dp/dr, dp/dw, dp/dI, dq/dr, dq/dw, and dq/dI. The total derivatives are found by totally differentiating the system of equations, dividing through by, say dr, treating dq/dr and dp/dr as the unknowns, setting dI = dw = 0, and solving the two totally differentiated equations simultaneously, typically by using Cramer's rule.
