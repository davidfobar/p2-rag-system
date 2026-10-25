# Torricelli's equation

Torricelli's equation

In physics, Torricelli's equation, or Torricelli's formula, is an equation created by Evangelista Torricelli to find the final velocity of a moving object with constant acceleration along an axis (for example, the x axis) without having a known time interval.
The equation itself is

          v

            f

            2

          v

            i

            2

        +
        2
        a
        Δ
        x
        ,

    {\displaystyle v_{\text{f}}^{2}=v_{\text{i}}^{2}+2a\Delta x,}

where

          v

            f

    {\displaystyle v_{\text{f}}}

 is the object's final velocity along the x axis on which the acceleration is constant,

          v

            i

    {\displaystyle v_{\text{i}}}

 is the object's initial velocity along the x axis,

        a

    {\displaystyle a}

 is the object's acceleration along the x axis, which is given as a constant,

        Δ
        x

    {\displaystyle \Delta x}

 is the object's change in position along the x axis, also called displacement.
In this and all subsequent equations in this article, the subscript

        x

    {\displaystyle x}

 (as in

              v

                f

            x

    {\displaystyle {v_{\text{f}}}_{x}}

) is implied, but is not expressed explicitly for clarity in presenting the equations.
This equation is valid along any axis on which the acceleration is constant.

Derivation

Without differentials and integration
Begin with the following relations for the case of uniform acceleration:

Take (1), and multiply both sides with acceleration

        a

    {\textstyle a}

The following rearrangement of the right hand side makes it easier to recognize the coming substitution:

Use (2) to substitute the product

        a
        t

    {\textstyle at}

:

Work out the multiplications:

The crossterms

          v

            i

          v

            f

    {\textstyle v_{\text{i}}v_{\text{f}}}

 drop away against each other, leaving only squared terms:

(7) rearranges to the form of Torricelli's equation as presented at the start of the article:

Using differentials and integration
Begin with the definitions of velocity as the derivative of the position, and acceleration as the derivative of the velocity:

Set up integration from initial position

          x

            i

    {\textstyle x_{\text{i}}}

 to final position

          x

            f

    {\textstyle x_{\text{f}}}

In accordance with (9) we can substitute

        d
        x

    {\textstyle dx}

 with

        v

        d
        t

    {\textstyle v\,dt}

, with corresponding change of limits.

Here changing the order of

        a

    {\textstyle a}

 and

        v

    {\textstyle v}

 makes it easier to recognize the upcoming substitution.

In accordance with (10) we can substitute

        a

        d
        t

    {\textstyle a\,dt}

 with

        d
        v

    {\textstyle dv}

, with corresponding change of limits.

So we have:

Since the acceleration is constant, we can factor it out of the integration:

Evaluating the integration:

The factor

          x

            f

        −

          x

            i

    {\textstyle x_{\text{f}}-x_{\text{i}}}

 is the displacement

        Δ
        x

    {\textstyle \Delta x}

:

Application
Combining Torricelli's equation with

        F

        m
        a

    {\textstyle F=ma}

 gives the work-energy theorem.
Torricelli's equation and the generalization to non-uniform acceleration have the same form:
Repeat of (16):

Evaluating the right hand side:

To compare with Torricelli's equation: repeat of (7):

To derive the work-energy theorem: start with

        F

        m
        a

    {\textstyle F=ma}

 and on both sides state the integral with respect to the position coordinate. If both sides are integrable then the resulting expression is valid:

Use (22) to process the right hand side:

The reason that the right hand sides of (22) and (23) are the same:
First consider the case with two consecutive stages of different uniform acceleration, first from

          s

            0

    {\textstyle s_{0}}

 to

          s

            1

    {\textstyle s_{1}}

, and then from

          s

            1

    {\textstyle s_{1}}

 to

          s

            2

    {\textstyle s_{2}}

.
Expressions for each of the two stages:

          a

            1

        (

          s

            1

        −

          s

            0

        )

              1
              2

          v

            1

            2

        −

              1
              2

          v

            0

            2

    {\displaystyle a_{1}(s_{1}-s_{0})={\tfrac {1}{2}}v_{1}^{2}-{\tfrac {1}{2}}v_{0}^{2}}

          a

            2

        (

          s

            2

        −

          s

            1

        )

              1
              2

          v

            2

            2

        −

              1
              2

          v

            1

            2

    {\displaystyle a_{2}(s_{2}-s_{1})={\tfrac {1}{2}}v_{2}^{2}-{\tfrac {1}{2}}v_{1}^{2}}

Since these expressions are for consecutive intervals they can be added; the result is a valid expression.
Upon addition the intermediate term

              1
              2

          v

            1

            2

    {\textstyle {\tfrac {1}{2}}v_{1}^{2}}

 drops out; only the outer terms

              1
              2

          v

            2

            2

    {\textstyle {\tfrac {1}{2}}v_{2}^{2}}

 and

              1
              2

          v

            0

            2

    {\textstyle {\tfrac {1}{2}}v_{0}^{2}}

 remain:

The above result generalizes: the total distance can be subdivided into any number of subdivisions; after adding everything together only the outer terms remain; all of the intermediate terms drop out.
The generalization of (26) to an arbitrary number of subdivisions of the total interval from

          s

            0

    {\textstyle s_{0}}

 to

          s

            n

    {\textstyle s_{n}}

 can be expressed as a summation:
