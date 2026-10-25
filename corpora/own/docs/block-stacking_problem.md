# Block-stacking problem

Block-stacking problem

In statics, the block-stacking problem (sometimes known as The Leaning Tower of Lire (Johnson 1955), also the book-stacking problem, harmonic staircase, or a number of other similar terms) is a puzzle concerning the stacking of blocks at the edge of a table.

Statement
The block-stacking problem is the following puzzle:

Place

        N

    {\displaystyle N}

 identical rigid rectangular blocks in a stable stack on a table edge in such a way as to maximize the overhang.

Paterson et al. (2007) provide a long list of references on this problem going back to mechanics texts from the middle of the 19th century.

Variants

Single-wide
The single-wide problem involves having only one block at any given level. In the ideal case of perfectly rectangular blocks and uniform gravitational acceleration (value of g decreases with increase in height), the solution to the single-wide problem is that the maximum overhang is given by

          ∑

            i

            1

            N

            1

              2
              i

    {\textstyle \sum _{i=1}^{N}{\frac {1}{2i}}}

 times the width of a block. This sum is one half of the corresponding partial sum of the harmonic series. Because the harmonic series diverges, the maximal overhang tends to infinity as

        N

    {\displaystyle N}

 increases, meaning that it is possible to achieve any arbitrarily large overhang, with sufficient blocks.

The number of blocks required to reach at least

        N

    {\displaystyle N}

 block-lengths past the edge of the table is 4, 31, 227, 1674, 12367, 91380, ... (sequence A014537 in the OEIS).

Multi-wide

Multi-wide stacks using counterbalancing can give larger overhangs than a single width stack. Even for three blocks, stacking two counterbalanced blocks on top of another block can give an overhang of 1, while the overhang in the simple ideal case is at most 11/12. As Paterson et al. (2007) showed, asymptotically, the maximum overhang that can be achieved by multi-wide stacks is proportional to the cube root of the number of blocks, in contrast to the single-wide case in which the overhang is proportional to the logarithm of the number of blocks. However, it has been shown that in reality this is impossible and the number of blocks that we can move to the right, due to block stress, is not more than a specified number. For example, for a special brick with h = 0.20 m, Young's modulus E = 3000 MPa and density ρ = 1.8×103 kg/m3 and limiting compressive stress 3 MPa, the approximate value of N will be 853 and the maximum tower height becomes 170 m.

Proof of solution of single-wide variant
The above formula for the maximum overhang of

        n

    {\displaystyle n}

 blocks, each with length

        l

    {\displaystyle l}

 and mass

        m

    {\displaystyle m}

, stacked one at a level, can be proven by induction by considering the torques on the blocks about the edge of the table they overhang. The blocks can be modelled as point-masses located at the center of each block, assuming uniform mass-density. In the base case (

        n

        1

    {\displaystyle n=1}

), the center of mass of the block lies above the table's edge, meaning an overhang of

        l

          /

        2

    {\displaystyle l/2}

. For

        k

    {\displaystyle k}

 blocks, the center of mass of the

        k

    {\displaystyle k}

-block system must lie above the table's edge, and the center of mass of the

        k
        −
        1

    {\displaystyle k-1}

 top blocks must lie above the edge of the first for static equilibrium. If the

        k

    {\displaystyle k}

th block overhangs the

        (
        k
        −
        1
        )

    {\displaystyle (k-1)}

th by

        l

          /

        2

    {\displaystyle l/2}

 and the overhang of the first is

        x

    {\displaystyle x}

,

        (
        k
        −
        1
        )
        m
        g
        x

        (
        l

          /

        2
        −
        x
        )
        m
        g

        ⟹

        x

        l

          /

        2
        k
        ,

    {\displaystyle (k-1)mgx=(l/2-x)mg\implies x=l/2k,}

where

        g

    {\displaystyle g}

 denotes the gravitational field. If the

        k
        −
        1

    {\displaystyle k-1}

 top blocks overhang their center of mass by

        y

    {\displaystyle y}

, then, by assuming the inductive hypothesis, the maximum overhang off the table is

        y
        +

            l

              2
              k

          ∑

            i

            1

            k

          l

            /

          2
          i

        ⟹

        y

          ∑

            i

            1

            k
            −
            1

          l

            /

          2
          i

        .

    {\displaystyle y+{\frac {l}{2k}}=\sum _{i=1}^{k}{l/2i}\implies y=\sum _{i=1}^{k-1}{l/2i}.}

For

        k
        +
        1

    {\displaystyle k+1}

 blocks,

        y

    {\displaystyle y}

 denotes how much the

        k
        +
        1
        −
        1

    {\displaystyle k+1-1}

 top blocks overhang their center of mass

        (
        y

          ∑

            i

            1

            k

        l

          /

        2
        i
        )

    {\displaystyle (y=\sum _{i=1}^{k}l/2i)}

, and

        x

            l

              2
              (
              k
              +
              1
              )

    {\displaystyle x={\frac {l}{2(k+1)}}}

. Then, the maximum overhang would be:

            l

              2
              (
              k
              +
              1
              )

        +

          ∑

            i

            1

            k

        l

          /

        2
        i

          ∑

            i

            1

            k
            +
            1

        l

          /

        2
        i
        .

    {\displaystyle {\frac {l}{2(k+1)}}+\sum _{i=1}^{k}l/2i=\sum _{i=1}^{k+1}l/2i.}

Robustness
Hall (2005) discusses this problem, shows that it is robust to nonidealizations such as rounded block corners and finite precision of block placing, and introduces several variants including nonzero friction forces between adjacent blocks.
