# Betti's theorem

Betti's theorem

Betti's theorem, also known as Maxwell–Betti reciprocal work theorem, discovered by Enrico Betti in 1872, states that for a linear elastic structure subject to two sets of forces {Pi} i=1,...,n and {Qj}, j=1,2,...,n, the work done by the set P through the displacements produced by the set Q is equal to the work done by the set Q through the displacements produced by the set P. This theorem has applications in structural engineering where it is used to define influence lines and derive the boundary element method.
Betti's theorem is used in the design of compliant mechanisms by topology optimization approach.

Proof
Consider a solid body subjected to a pair of external force systems, referred to as

          F

            i

            P

    {\displaystyle F_{i}^{P}}

 and

          F

            i

            Q

    {\displaystyle F_{i}^{Q}}

. Consider that each force system causes a displacement field, with the displacements measured at the external force's point of application referred to as

          d

            i

            P

    {\displaystyle d_{i}^{P}}

 and

          d

            i

            Q

    {\displaystyle d_{i}^{Q}}

.
When the

          F

            i

            P

    {\displaystyle F_{i}^{P}}

 force system is applied to the structure, the balance between the work performed by the external force system and the strain energy is:

            1
            2

          ∑

            i

            1

            n

          F

            i

            P

          d

            i

            P

            1
            2

          ∫

            Ω

          σ

            i
            j

            P

          ϵ

            i
            j

            P

        d
        Ω

    {\displaystyle {\frac {1}{2}}\sum {i=1}^{n}F{i}^{P}d_{i}^{P}={\frac {1}{2}}\int _{\Omega }\sigma _{ij}^{P}\epsilon _{ij}^{P}\,d\Omega }

The work-energy balance associated with the

          F

            i

            Q

    {\displaystyle F_{i}^{Q}}

 force system is as follows:

            1
            2

          ∑

            i

            1

            n

          F

            i

            Q

          d

            i

            Q

            1
            2

          ∫

            Ω

          σ

            i
            j

            Q

          ϵ

            i
            j

            Q

        d
        Ω

    {\displaystyle {\frac {1}{2}}\sum {i=1}^{n}F{i}^{Q}d_{i}^{Q}={\frac {1}{2}}\int _{\Omega }\sigma _{ij}^{Q}\epsilon _{ij}^{Q}\,d\Omega }

Now, consider that with the

          F

            i

            P

    {\displaystyle F_{i}^{P}}

 force system applied, the

          F

            i

            Q

    {\displaystyle F_{i}^{Q}}

 force system is applied subsequently. As the

          F

            i

            P

    {\displaystyle F_{i}^{P}}

 is already applied and therefore won't cause any extra displacement, the work-energy balance assumes the following expression:

            1
            2

          ∑

            i

            1

            n

          F

            i

            P

          d

            i

            P

        +

            1
            2

          ∑

            i

            1

            n

          F

            i

            Q

          d

            i

            Q

        +

          ∑

            i

            1

            n

          F

            i

            P

          d

            i

            Q

            1
            2

          ∫

            Ω

          σ

            i
            j

            P

          ϵ

            i
            j

            P

        d
        Ω
        +

            1
            2

          ∫

            Ω

          σ

            i
            j

            Q

          ϵ

            i
            j

            Q

        d
        Ω
        +

          ∫

            Ω

          σ

            i
            j

            P

          ϵ

            i
            j

            Q

        d
        Ω

    {\displaystyle {\frac {1}{2}}\sum {i=1}^{n}F{i}^{P}d_{i}^{P}+{\frac {1}{2}}\sum {i=1}^{n}F{i}^{Q}d_{i}^{Q}+\sum {i=1}^{n}F{i}^{P}d_{i}^{Q}={\frac {1}{2}}\int _{\Omega }\sigma _{ij}^{P}\epsilon _{ij}^{P}\,d\Omega +{\frac {1}{2}}\int _{\Omega }\sigma _{ij}^{Q}\epsilon _{ij}^{Q}\,d\Omega +\int _{\Omega }\sigma _{ij}^{P}\epsilon _{ij}^{Q}\,d\Omega }

Conversely, if we consider the

          F

            i

            Q

    {\displaystyle F_{i}^{Q}}

 force system already applied and the

          F

            i

            P

    {\displaystyle F_{i}^{P}}

 external force system applied subsequently, the work-energy balance will assume the following expression:

            1
            2

          ∑

            i

            1

            n

          F

            i

            Q

          d

            i

            Q

        +

            1
            2

          ∑

            i

            1

            n

          F

            i

            P

          d

            i

            P

        +

          ∑

            i

            1

            n

          F

            i

            Q

          d

            i

            P

            1
            2

          ∫

            Ω

          σ

            i
            j

            Q

          ϵ

            i
            j

            Q

        d
        Ω
        +

            1
            2

          ∫

            Ω

          σ

            i
            j

            P

          ϵ

            i
            j

            P

        d
        Ω
        +

          ∫

            Ω

          σ

            i
            j

            Q

          ϵ

            i
            j

            P

        d
        Ω

    {\displaystyle {\frac {1}{2}}\sum {i=1}^{n}F{i}^{Q}d_{i}^{Q}+{\frac {1}{2}}\sum {i=1}^{n}F{i}^{P}d_{i}^{P}+\sum {i=1}^{n}F{i}^{Q}d_{i}^{P}={\frac {1}{2}}\int _{\Omega }\sigma _{ij}^{Q}\epsilon _{ij}^{Q}\,d\Omega +{\frac {1}{2}}\int _{\Omega }\sigma _{ij}^{P}\epsilon _{ij}^{P}\,d\Omega +\int _{\Omega }\sigma _{ij}^{Q}\epsilon _{ij}^{P}\,d\Omega }

If the work-energy balance for the cases where the external force systems are applied in isolation are respectively subtracted from the cases where the force systems are applied simultaneously, we arrive at the following equations:

          ∑

            i

            1

            n

          F

            i

            P

          d

            i

            Q

          ∫

            Ω

          σ

            i
            j

            P

          ϵ

            i
            j

            Q

        d
        Ω

    {\displaystyle \sum {i=1}^{n}F{i}^{P}d_{i}^{Q}=\int _{\Omega }\sigma _{ij}^{P}\epsilon _{ij}^{Q}\,d\Omega }

          ∑

            i

            1

            n

          F

            i

            Q

          d

            i

            P

          ∫

            Ω

          σ

            i
            j

            Q

          ϵ

            i
            j

            P

        d
        Ω

    {\displaystyle \sum {i=1}^{n}F{i}^{Q}d_{i}^{P}=\int _{\Omega }\sigma _{ij}^{Q}\epsilon _{ij}^{P}\,d\Omega }

If the solid body where the force systems are applied is formed by a linear elastic material and if the force systems are such that only infinitesimal strains are observed in the body, then the body's constitutive equation, which may follow Hooke's law, can be expressed in the following manner:

          σ

            i
            j

          D

            i
            j
            k
            l

          ϵ

            k
            l

    {\displaystyle \sigma {ij}=D{ijkl}\epsilon _{kl}}

Replacing this result in the previous set of equations leads us to the following result:

          ∑

            i

            1

            n

          F

            i

            P

          d

            i

            Q

          ∫

            Ω

          D

            i
            j
            k
            l

          ϵ

            i
            j

            P

          ϵ

            k
            l

            Q

        d
        Ω

    {\displaystyle \sum {i=1}^{n}F{i}^{P}d_{i}^{Q}=\int {\Omega }D{ijkl}\epsilon _{ij}^{P}\epsilon _{kl}^{Q}\,d\Omega }

          ∑

            i

            1

            n

          F

            i

            Q

          d

            i

            P

          ∫

            Ω

          D

            i
            j
            k
            l

          ϵ

            i
            j

            Q

          ϵ

            k
            l

            P

        d
        Ω

    {\displaystyle \sum {i=1}^{n}F{i}^{Q}d_{i}^{P}=\int {\Omega }D{ijkl}\epsilon _{ij}^{Q}\epsilon _{kl}^{P}\,d\Omega }

If we subtract both equations then we obtain the following result:

          ∑

            i

            1

            n

          F

            i

            P

          d

            i

            Q

          ∑

            i

            1

            n

          F

            i

            Q

          d

            i

            P

    {\displaystyle \sum {i=1}^{n}F{i}^{P}d_{i}^{Q}=\sum {i=1}^{n}F{i}^{Q}d_{i}^{P}}

Proof using stiffness matrix properties
Elastic energy is

        E

            1
            2

          d

            T

        K
        d

    {\displaystyle E={\frac {1}{2}}d^{T}Kd}

, where

        d

    {\displaystyle d}

 is the displacement vector and

        K

    {\displaystyle K}

 is the stiffness matrix of the system.

        K

    {\displaystyle K}

 is symmetric and positive definite. Forces at these

        n

    {\displaystyle n}

 points are given by Hooke's law

          F

            P

        K

          d

            P

        ,

          F

            Q

        K

          d

            Q

    {\displaystyle F^{P}=Kd^{P},F^{Q}=Kd^{Q}}

Therefore

        (

          F

            P

          )

            T

          d

            Q

        (

          d

            P

          )

            T

          K

            T

          d

            Q

        (

          d

            P

          )

            T

        K

          d

            Q

        (

          d

            P

          )

            T

          F

            Q

    {\displaystyle (F^{P})^{T}d^{Q}=(d^{P})^{T}K^{T}d^{Q}=(d^{P})^{T}Kd^{Q}=(d^{P})^{T}F^{Q}}

Example
For a simple example let n=2. Consider a horizontal beam on which two points have been defined: point 1 and point 2. First we apply a vertical force P at point 1 and measure the vertical displacement of point 2, denoted

          Δ

            P
            2

    {\displaystyle \Delta _{P2}}

. Next we remove force P and apply a vertical force Q at point 2, which produces the vertical displacement at point 1 of

          Δ

            Q
            1

    {\displaystyle \Delta _{Q1}}

. Betti's reciprocity theorem states that:

        P

          Δ

            Q
            1

        Q

          Δ

            P
            2

        .

    {\displaystyle P\,\Delta _{Q1}=Q\,\Delta _{P2}.}
