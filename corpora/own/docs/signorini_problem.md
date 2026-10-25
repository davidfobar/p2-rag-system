# Signorini problem

Signorini problem

The Signorini problem is an elastostatics problem in linear elasticity: it consists in finding the elastic equilibrium configuration of an anisotropic non-homogeneous elastic body, resting on a rigid frictionless surface and subject only to its mass forces. The name was coined by Gaetano Fichera to honour his teacher, Antonio Signorini: the original name coined by him is problem with ambiguous boundary conditions.

History

The problem was posed by Antonio Signorini during a course taught at the Istituto Nazionale di Alta Matematica in 1959, later published as the article (Signorini 1959), expanding a previous short exposition he gave in a note published in 1933. Signorini (1959, p. 128) himself called it problem with ambiguous boundary conditions, since there are two alternative sets of boundary conditions the solution must satisfy on any given contact point. The statement of the problem involves not only equalities but also inequalities, and it is not a priori known what of the two sets of boundary conditions is satisfied at each point. Signorini asked to determine if the problem is well-posed or not in a physical sense, i.e. if its solution exists and is unique or not: he explicitly invited young analysts to study the problem.
Gaetano Fichera and Mauro Picone attended the course, and Fichera started to investigate the problem: since he found no references to similar problems in the theory of boundary value problems, he decided to approach it by starting from first principles, specifically from the virtual work principle.
During Fichera's researches on the problem, Signorini began to suffer serious health problems: nevertheless, he desired to know the answer to his question before his death. Picone, being tied by a strong friendship with Signorini, began to chase Fichera to find a solution: Fichera himself, being tied as well to Signorini by similar feelings, perceived the last months of 1962 as worrying days. Finally, on the first days of January 1963, Fichera was able to give a complete proof of the existence of a unique solution for the problem with ambiguous boundary condition, which he called the "Signorini problem" to honour his teacher. A preliminary research announcement, later published as (Fichera 1963), was written up and submitted to Signorini exactly a week before his death. Signorini expressed great satisfaction to see a solution to his question.
A few days later, Signorini had with his family Doctor, Damiano Aprile, the conversation quoted above.
The solution of the Signorini problem coincides with the birth of the field of variational inequalities.

Formal statement of the problem
The content of this section and the following subsections follows closely the treatment of Gaetano Fichera in Fichera 1963, Fichera 1964b and also Fichera 1995: his derivation of the problem is different from Signorini's one in that he does not consider only incompressible bodies and a plane rest surface, as Signorini does. The problem consists in finding the displacement vector from the natural configuration

            u

          (

            x

          )

            (

                u

                  1

              (

                x

              )
              ,

                u

                  2

              (

                x

              )
              ,

                u

                  3

              (

                x

              )

            )

    {\displaystyle \scriptstyle {\boldsymbol {u}}({\boldsymbol {x}})=\left(u_{1}({\boldsymbol {x}}),u_{2}({\boldsymbol {x}}),u_{3}({\boldsymbol {x}})\right)}

 of an anisotropic non-homogeneous elastic body that lies in a subset

        A

    {\displaystyle A}

 of the three-dimensional euclidean space whose boundary is

          ∂
          A

    {\displaystyle \scriptstyle \partial A}

 and whose interior normal is the vector

        n

    {\displaystyle n}

, resting on a rigid frictionless surface whose contact surface (or more generally contact set) is

        Σ

    {\displaystyle \Sigma }

 and subject only to its body forces

            f

          (

            x

          )

            (

                f

                  1

              (

                x

              )
              ,

                f

                  2

              (

                x

              )
              ,

                f

                  3

              (

                x

              )

            )

    {\displaystyle \scriptstyle {\boldsymbol {f}}({\boldsymbol {x}})=\left(f_{1}({\boldsymbol {x}}),f_{2}({\boldsymbol {x}}),f_{3}({\boldsymbol {x}})\right)}

, and surface forces

            g

          (

            x

          )

            (

                g

                  1

              (

                x

              )
              ,

                g

                  2

              (

                x

              )
              ,

                g

                  3

              (

                x

              )

            )

    {\displaystyle \scriptstyle {\boldsymbol {g}}({\boldsymbol {x}})=\left(g_{1}({\boldsymbol {x}}),g_{2}({\boldsymbol {x}}),g_{3}({\boldsymbol {x}})\right)}

 applied on the free (i.e. not in contact with the rest surface) surface

          ∂
          A
          ∖
          Σ

    {\displaystyle \scriptstyle \partial A\setminus \Sigma }

: the set

        A

    {\displaystyle A}

 and the contact surface

        Σ

    {\displaystyle \Sigma }

 characterize the natural configuration of the body and are known a priori. Therefore, the body has to satisfy the general equilibrium equations

(1)

              ∂

                σ

                  i
                  k

              ∂

                x

                  k

        −

          f

            i

        0

          for

        i

        1
        ,
        2
        ,
        3

    {\displaystyle \qquad {\frac {\partial \sigma {ik}}{\partial x{k}}}-f_{i}=0\qquad {\text{for }}i=1,2,3}

written using the Einstein notation as all in the following development, the ordinary boundary conditions on

          ∂
          A
          ∖
          Σ

    {\displaystyle \scriptstyle \partial A\setminus \Sigma }

(2)

          σ

            i
            k

          n

            k

        −

          g

            i

        0

          for

        i

        1
        ,
        2
        ,
        3

    {\displaystyle \qquad \sigma {ik}n{k}-g_{i}=0\qquad {\text{for }}i=1,2,3}

and the following two sets of boundary conditions on

        Σ

    {\displaystyle \Sigma }

, where

            σ

            σ

          (

            u

          )

    {\displaystyle \scriptstyle {\boldsymbol {\sigma }}={\boldsymbol {\sigma }}({\boldsymbol {u}})}

 is the Cauchy stress tensor. Obviously, the body forces and surface forces cannot be given in arbitrary way but they must satisfy a condition in order for the body to reach an equilibrium configuration: this condition will be deduced and analyzed in the following development.

The ambiguous boundary conditions
If

            τ

          (

            τ

              1

          ,

            τ

              2

          ,

            τ

              3

          )

    {\displaystyle \scriptstyle {\boldsymbol {\tau }}=(\tau _{1},\tau _{2},\tau _{3})}

 is any tangent vector to the contact set

        Σ

    {\displaystyle \Sigma }

, then the ambiguous boundary condition in each point of this set are expressed by the following two systems of inequalities

(3)

            {

                    u

                      i

                    n

                      i

                  0

                    σ

                      i
                      k

                    n

                      i

                    n

                      k

                  ≥
                  0

                    σ

                      i
                      k

                    n

                      i

                    τ

                      k

                  0

    {\displaystyle \quad {\begin{cases}u_{i}n_{i}&=0\\sigma {ik}n{i}n_{k}&\geq 0\\sigma {ik}n{i}\tau _{k}&=0\end{cases}}}

     or (4)

            {

                    u

                      i

                    n

                      i

                  0

                    σ

                      i
                      k

                    n

                      i

                    n

                      k

                  0

                    σ

                      i
                      k

                    n

                      i

                    τ

                      k

                  0

    {\displaystyle {\begin{cases}u_{i}n_{i}&>0\\sigma {ik}n{i}n_{k}&=0\\sigma {ik}n{i}\tau _{k}&=0\end{cases}}}

Let's analyze their meaning:

Each set of conditions consists of three relations, equalities or inequalities, and all the second members are the zero function.
The quantities at first member of each first relation are proportional to the norm of the component of the displacement vector directed along the normal vector

        n

    {\displaystyle n}

.
The quantities at first member of each second relation are proportional to the norm of the component of the tension vector directed along the normal vector

        n

    {\displaystyle n}

,
The quantities at the first member of each third relation are proportional to the norm of the component of the tension vector along any vector

        τ

    {\displaystyle \tau }

 tangent in the given point to the contact set

        Σ

    {\displaystyle \Sigma }

.
The quantities at the first member of each of the three relations are positive if they have the same sense of the vector they are proportional to, while they are negative if not, therefore the constants of proportionality are respectively

          +
          1

    {\displaystyle \scriptstyle +1}

 and

          −
          1

    {\displaystyle \scriptstyle -1}

.
Knowing these facts, the set of conditions (3) applies to points of the boundary of the body which do not leave the contact set

        Σ

    {\displaystyle \Sigma }

 in the equilibrium configuration, since, according to the first relation, the displacement vector

        u

    {\displaystyle u}

 has no components directed as the normal vector

        n

    {\displaystyle n}

, while, according to the second relation, the tension vector may have a component directed as the normal vector

        n

    {\displaystyle n}

 and having the same sense. In an analogous way, the set of conditions (4) applies to points of the boundary of the body which leave that set in the equilibrium configuration, since displacement vector

        u

    {\displaystyle u}

 has a component directed as the normal vector

        n

    {\displaystyle n}

, while the tension vector has no components directed as the normal vector

        n

    {\displaystyle n}

. For both sets of conditions, the tension vector has no tangent component to the contact set, according to the hypothesis that the body rests on a rigid frictionless surface.
Each system expresses a unilateral constraint, in the sense that they express the physical impossibility of the elastic body to penetrate into the surface where it rests: the ambiguity is not only in the unknown values non-zero quantities must satisfy on the contact set but also in the fact that it is not a priori known if a point belonging to that set satisfies the system of boundary conditions (3) or (4). The set of points where (3) is satisfied is called the area of support of the elastic body on

        Σ

    {\displaystyle \Sigma }

, while its complement respect to

        Σ

    {\displaystyle \Sigma }

 is called the area of separation.
The above formulation is general since the Cauchy stress tensor i.e. the constitutive equation of the elastic body has not been made explicit: it is equally valid assuming the hypothesis of linear elasticity or the ones of nonlinear elasticity. However, as it would be clear from the following developments, the problem is inherently nonlinear, therefore assuming a linear stress tensor does not simplify the problem.

The form of the stress tensor in the formulation of Signorini and Fichera
The form assumed by Signorini and Fichera for the elastic potential energy is the following one (as in the previous developments, the Einstein notation is adopted)

        W
        (

          ε

        )

          a

            i
            k
            ,
            j
            h

        (

          x

        )

          ε

            i
            k

          ε

            j
            h

    {\displaystyle W({\boldsymbol {\varepsilon }})=a_{ik,jh}({\boldsymbol {x}})\varepsilon _{ik}\varepsilon _{jh}}

where

            a

          (

            x

          )

            (

                a

                  i
                  k
                  ,
                  j
                  h

              (

                x

              )

            )

    {\displaystyle \scriptstyle {\boldsymbol {a}}({\boldsymbol {x}})=\left(a_{ik,jh}({\boldsymbol {x}})\right)}

 is the elasticity tensor

            ε

            ε

          (

            u

          )

            (

                ε

                  i
                  k

              (

                u

              )

            )

            (

                  1
                  2

                (

                        ∂

                          u

                            i

                        ∂

                          x

                            k

                  +

                        ∂

                          u

                            k

                        ∂

                          x

                            i

                )

            )

    {\displaystyle \scriptstyle {\boldsymbol {\varepsilon }}={\boldsymbol {\varepsilon }}({\boldsymbol {u}})=\left(\varepsilon {ik}({\boldsymbol {u}})\right)=\left({\frac {1}{2}}\left({\frac {\partial u{i}}{\partial x_{k}}}+{\frac {\partial u_{k}}{\partial x_{i}}}\right)\right)}

 is the infinitesimal strain tensor
The Cauchy stress tensor has therefore the following form

(5)

          σ

            i
            k

        −

              ∂
              W

              ∂

                ε

                  i
                  k

          for

        i
        ,
        k

        1
        ,
        2
        ,
        3

    {\displaystyle \sigma _{ik}=-{\frac {\partial W}{\partial \varepsilon _{ik}}}\qquad {\text{for }}i,k=1,2,3}

and it is linear with respect to the components of the infinitesimal strain tensor; however, it is not homogeneous nor isotropic.

Solution of the problem
As for the section on the formal statement of the Signorini problem, the contents of this section and the included subsections follow closely the treatment of Gaetano Fichera in Fichera 1963, Fichera 1964b, Fichera 1972 and also Fichera 1995: obviously, the exposition focuses on the basics steps of the proof of the existence and uniqueness for the solution of problem (1), (2), (3), (4) and (5), rather than the technical details.

The potential energy
The first step of the analysis of Fichera as well as the first step of the analysis of Antonio Signorini in Signorini 1959 is the analysis of the potential energy, i.e. the following functional

(6)

        I
        (

          u

        )

          ∫

            A

        W
        (

          x

        ,

          ε

        )

          d

        x
        −

          ∫

            A

          u

            i

          f

            i

          d

        x
        −

          ∫

            ∂
            A
            ∖
            Σ

          u

            i

          g

            i

          d

        σ

    {\displaystyle I({\boldsymbol {u}})=\int _{A}W({\boldsymbol {x}},{\boldsymbol {\varepsilon }})\mathrm {d} x-\int {A}u{i}f_{i}\mathrm {d} x-\int {\partial A\setminus \Sigma }u{i}g_{i}\mathrm {d} \sigma }

where

        u

    {\displaystyle u}

 belongs to the set of admissible displacements

                U

              Σ

    {\displaystyle \scriptstyle {\mathcal {U}}_{\Sigma }}

 i.e. the set of displacement vectors satisfying the system of boundary conditions (3) or (4). The meaning of each of the three terms is the following

the first one is the total elastic potential energy of the elastic body
the second one is the total potential energy due to the body forces, for example the gravitational force
the third one is the potential energy due to surface forces, for example the forces exerted by the atmospheric pressure
Signorini (1959, pp. 129–133) was able to prove that the admissible displacement

        u

    {\displaystyle u}

 which minimize the integral

        I
        (
        u
        )

    {\displaystyle I(u)}

 is a solution of the problem with ambiguous boundary conditions (1), (2), (3), (4) and (5), provided it is a

          C

            1

    {\displaystyle C^{1}}

 function supported on the closure

                A
                ¯

    {\displaystyle \scriptstyle {\bar {A}}}

 of the set

        A

    {\displaystyle A}

: however Gaetano Fichera gave a class of counterexamples in (Fichera 1964b, pp. 619–620) showing that in general, admissible displacements are
not smooth functions of these class. Therefore, Fichera tries to minimize the functional (6) in a wider function space: in doing so, he first calculates the first variation (or functional derivative) of the given functional in the neighbourhood of the sought minimizing admissible displacement

            u

          ∈

                U

              Σ

    {\displaystyle \scriptstyle {\boldsymbol {u}}\in {\mathcal {U}}_{\Sigma }}

, and then requires it to be greater than or equal to zero

                    d

                      d

                    t

              I
              (

                u

              +
              t

                v

              )

            t

            0

        −

          ∫

            A

          σ

            i
            k

        (

          u

        )

          ε

            i
            k

        (

          v

        )

          d

        x
        −

          ∫

            A

          v

            i

          f

            i

          d

        x
        −

          ∫

            ∂
            A
            ∖
            Σ

          v

            i

          g

            i

          d

        σ
        ≥
        0

        ∀

          v

        ∈

              U

            Σ

    {\displaystyle \left.{\frac {\mathrm {d} }{\mathrm {d} t}}I({\boldsymbol {u}}+t{\boldsymbol {v}})\right\vert _{t=0}=-\int _{A}\sigma _{ik}({\boldsymbol {u}})\varepsilon _{ik}({\boldsymbol {v}})\mathrm {d} x-\int {A}v{i}f_{i}\mathrm {d} x-\int {\partial A\setminus \Sigma }!!!!!v{i}g_{i}\mathrm {d} \sigma \geq 0\qquad \forall {\boldsymbol {v}}\in {\mathcal {U}}_{\Sigma }}

Defining the following functionals

        B
        (

          u

        ,

          v

        )

        −

          ∫

            A

          σ

            i
            k

        (

          u

        )

          ε

            i
            k

        (

          v

        )

          d

        x

          u

        ,

          v

        ∈

              U

            Σ

    {\displaystyle B({\boldsymbol {u}},{\boldsymbol {v}})=-\int _{A}\sigma _{ik}({\boldsymbol {u}})\varepsilon {ik}({\boldsymbol {v}})\mathrm {d} x\qquad {\boldsymbol {u}},{\boldsymbol {v}}\in {\mathcal {U}}{\Sigma }}

and

        F
        (

          v

        )

          ∫

            A

          v

            i

          f

            i

          d

        x
        +

          ∫

            ∂
            A
            ∖
            Σ

          v

            i

          g

            i

          d

        σ

          v

        ∈

              U

            Σ

    {\displaystyle F({\boldsymbol {v}})=\int {A}v{i}f_{i}\mathrm {d} x+\int {\partial A\setminus \Sigma }!!!!!v{i}g_{i}\mathrm {d} \sigma \qquad {\boldsymbol {v}}\in {\mathcal {U}}_{\Sigma }}

the preceding inequality is can be written as

(7)

        B
        (

          u

        ,

          v

        )
        −
        F
        (

          v

        )
        ≥
        0

        ∀

          v

        ∈

              U

            Σ

    {\displaystyle B({\boldsymbol {u}},{\boldsymbol {v}})-F({\boldsymbol {v}})\geq 0\qquad \forall {\boldsymbol {v}}\in {\mathcal {U}}_{\Sigma }}

This inequality is the variational inequality for the Signorini problem.
