<TeXmacs|1.0.6>

<style|generic>

<\body>
  <doc-data|<doc-title|New TutteEx Paper--for Math >>

  Theme:Electrical Networks and the Matrix Tree Theorem are the main
  historical and current context of this paper.

  <\with|par-left|1in>
    <\with|par-left|1cm>
      <\with|par-right|1cm>
        Electrical networks have a long history of (giving, providing,
        donating, ???) motivations for graph and combinatorial theory. \ A
        graphs Laplacian matrix L appears in the equation
        <with|mode|math|><with|mode|math|L<inactive|<hybrid|phi>>=I> that can
        be solved for the electrical node potential
        <with|mode|math|<inactive|<hybrid|phi>>> in terms of the electrical
        currents <with|mode|math|I> flowing into the nodes. \ [Matrix Tree
        Theorem and things like Maxwell's rule]

        Suppose we fix the potential <with|mode|math|\<phi\>(\<gamma\>)=0> at
        node <with|mode|math|\<gamma\>>; impose unit current
        <with|mode|math|I(<inactive|<hybrid|alpha>>)=1> into node
        <with|mode|math|<inactive|<hybrid|alpha>>> and insulate the other
        nodes so <with|mode|math|I(<inactive|<hybrid|nu>>)=0 >for all
        <with|mode|math|<inactive|<hybrid|nu>><inactive|<hybrid|not\\in>><inactive|<hybrid|{>><inactive|<hybrid|gamma>>,<inactive|<hybrid|alpha>><inactive|<hybrid|}>>>.
        Let us assume <with|mode|math|L\<phi\>=I> can be solved with these
        conditions. \ The resulting difference of potential
        <with|mode|math|<inactive|<hybrid|phi>>(<inactive|<hybrid|alpha>>)-<inactive|<hybrid|phi>>(<inactive|<hybrid|gamma>>)>
        <with|mode|math|=> <with|mode|math|<inactive|<hybrid|phi>>(<inactive|<hybrid|alpha>>)>
        is called the equivalent resistance between
        <with|mode|math|<inactive|<hybrid|alpha>>> and
        <inactive|<hybrid|gamma>>. A routine application of Cramer's rule to
        a submatrix of <with|mode|math|L> together with the matrix tree
        theorem appied to the network <with|mode|math|N> and to
        <with|mode|math|N> with <with|mode|math|<inactive|<hybrid|alpha>>>
        and <with|mode|math|<inactive|<hybrid|gamma>>> identified will prove
        \ Maxwell's Rule (for two nodes):\ 

        Maxwells Rule: \ The equivalent resistance equals

        <\equation*>
          <frac|<big|sum><rsub|F is a spanning tree in
          N/(<inactive|<hybrid|alpha>>,<inactive|<hybrid|gamma>>)>g<rsub|F>|<big|sum><rsub|T
          is a spanning tree in N>g<rsub|T>>
        </equation*>

        Here, <with|mode|math|g<rsub|F>=<big|prod>g<rsub|e> \ >for edges
        <with|mode|math|e<inactive|<hybrid|in>>F>. \ Maxwell's rule in
        general expresses the potential difference between any two nodes
        <inactive|<hybrid|beta>>, <inactive|<hybrid|delta>> under these
        conditions. The numerator is a sum of terms representing spanning
        forests in <with|mode|math|N> with exactly two trees, where
        <with|mode|math|<inactive|<hybrid|alpha>> > and
        <inactive|<hybrid|gamma>> are in separate trees and also
        <with|mode|math|<inactive|<hybrid|beta>>> and
        <inactive|<hybrid|delta>> are in separate trees. So, there are two
        cases: (+) <with|mode|math|<inactive|<hybrid|{>><inactive|<hybrid|alpha>>,<inactive|<hybrid|beta>><inactive|<hybrid|}>>>
        are in one tree and <inactive|<hybrid|{\\gamma>>,<inactive|<hybrid|delta>><inactive|<hybrid|}>>
        in the other tree and (-) <inactive|<hybrid|{>><inactive|<hybrid|alpha,\\delta>><inactive|<hybrid|}>>
        are in one tree and <inactive|<hybrid|{>><inactive|<hybrid|beta>>,<inactive|<hybrid|gamma>><inactive|<hybrid|}>>
        are in the other tree. Terms of case (+) appear with positive sign
        and terms of case (-) apear with negative sign. The denominator is
        the spanning tree enumerator as before.

        Our contribution is to characterize the signs in Maxwell's rule
        within the theory of oriented matroids. \ Another outcome is an
        apparently new variation of the well-known Tutte equations for many
        matroid invariants in which the equations apply to certain (fully)
        decomposible elements in an exterior algebra, which we call extensors
        for short. We present new \ Tutte-like functions which map extensors
        to extensors; the multiplication in our Tutte-like equations is
        anticommutative because it is wedge product. \ \ 

        Our result require two problem reformulations which might be of
        intependent interest. First, instead of network nodes like
        <with|mode|math|<inactive|<hybrid|alpha>>, <inactive|<hybrid|beta>>,
        <inactive|<hybrid|gamma>>, and <inactive|<hybrid|delta>>> used as
        above to define environmental currents and observable potentials, we
        introduce distinguished network edges called ports, which easily
        generalize to distinguished matroid elements. Second, instead of the
        Laplacian matrix and variables like
        <with|mode|math|<inactive|<hybrid|phi>>> and <with|mode|math|I>, we
        specify Kirchhoff's two laws by separate equations, introduce edge
        conductance and resistance parameters symmetrically, and then study
        the wedge product of the rows of the equation coeffient matrix.\ 

        An outcome is a generalization of Maxwell's rule that interprets\ 

        Proofs have been given \ ......

        \;

        Theme: My discovery is interesting because it domonstrates a new
        relationship between two interesting topics.

        The spanning tree enumerator is of course the special case for
        graphic matroids of the basis enumerator, which is one member of the
        important family of Tutte matroid invariants.

        The [SUPER] consequence of our result is that it is not a coincidence
        that electrical network solutions are ratios of minors of Laplacians
        and that each minor satisfies the Tutte equations. We have found that
        when the solution set to a suitably formulated system of electrical
        network equations is expressed as an extensor, the function that maps
        the network's graphic matroid to this extensor satisfies the Tutte
        equations. Of course, this requires that those equations [Tutte?] be
        extended [rewritten? formulated?] from commutative rings to exterior
        algebra. \ This is because the [wedge] exterior product, or wedge, is
        anti-commutative. \ This paper presents the technicalities that seem
        to be necessary [to make this program work?] for this generaliztion
        to work. \ 
      </with>

      Theme: Understanding my discovery requires that each topic be looked at
      in a somewhat unfamiliar way to most readers of this journal.

      Theme: What is the definition of <with|mode|math|M<rsub|E>(N)> with the
      minimum of theory?

      Theme: What is the main point of the TutteEx paper, informed by the
      refs report?

      We can formuate a [Laplace/Dirichlet problem, CHECK] so the [solution,
      kernel, Green's function CHECK] satisfies the [anticommutive, exterior
      algebra?? these are new to this paper] Tutte equations.

      When we express the [??] of the [??] problem in exterior algebra, the
      [??] satisfies the Tutte equations. \ Our formulation requires that
      some elements are distinguished as ports: The ports determine the
      coordinate system for the [solution??] There is one instance of the
      Tutte eq. for each of the remaining elements: For each
      <with|mode|math|e> not a port, <with|mode|math|M(N)=r<rsub|e>M(N<inactive|<hybrid|setminus>>e)+g<rsub|e>M(N/e).
      >We believe that this [??] underscores the importance of distinguishing
      port elements [the ports] [to obtain results of this kind?]

      Our other line of work investingates the [consequences of ]
      distinguishing of port elements within matroid theory. \ There is less
      novelty. \ This idea has been studied before, but not in the electrical
      network context [by mathematicians, but by EEs] We present the fairly
      straightforward generaliztions of Tutte function theory. \ We can then
      see how our algebraic result fits into the discrete theory.
    </with>
  </with>
</body>

<\initial>
  <\collection>
    <associate|language|american>
    <associate|page-type|letter>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|auto-2|<tuple|2|?>>
  </collection>
</references>