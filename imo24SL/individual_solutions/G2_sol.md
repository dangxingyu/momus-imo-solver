### reference solution 1
Let $A^{\prime}$ be the reflection of $A$ in $I$, then $A^{\prime}$ lies on the angle bisector $A P$. Lines $A^{\prime} X$ and $A^{\prime} Y$ are the reflections of $A C$ and $A B$ in $I$, respectively, and so they are the tangents to $\omega$ from $X$ and $Y$. As is well-known, $P B=P C=P I$, and since $\angle B A P=\angle P A C>30^{\circ}$, $P B=P C$ is greater than the circumradius. Hence $P I>\frac{1}{2} A P>A I$; we conclude that $A^{\prime}$ lies in the interior of segment $A P$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-067}

We have $\angle A P B=\angle A C B$ in the circumcircle and $\angle A C B=\angle A^{\prime} X C$ because $A^{\prime} X \| A C$. Hence, $\angle A P B=\angle A^{\prime} X C$, and so quadrilateral $B P A^{\prime} X$ is cyclic. Similarly, it follows that $C Y A^{\prime} P$ is cyclic.

Now we are ready to transform $\angle K I L+\angle Y P X$ to the sum of angles in triangle $A^{\prime} C B$. By a homothety of factor 2 at $A$ we have $\angle K I L=\angle C A^{\prime} B$. In circles $B P A^{\prime} X$ and $C Y A^{\prime} P$ we have $\angle A P X=\angle A^{\prime} B C$ and $\angle Y P A=\angle B C A^{\prime}$, therefore

$$
\angle K I L+\angle Y P X=\angle C A^{\prime} B+(\angle Y P A+\angle A P X)=\angle C A^{\prime} B+\angle B C A^{\prime}+\angle A^{\prime} B C=180^{\circ} .
$$

---


---

### reference comment
The constraint $A B<A C<B C$ was added by the Problem Selection Committee in order to reduce case-sensitivity. Without that, there would be two more possible configurations according to the possible orders of points $A, P$ and $A^{\prime}$, as shown in the pictures below. The solution for these cases is broadly the same, but some extra care is required in the degenerate case when $A^{\prime}$ coincides with $P$ and line $A P$ is a common tangent to circles $B P X$ and $C P Y$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-068}

---


---

### reference solution 2
Let $B C=a, A C=b, A B=c$ and $s=\frac{a+b+c}{2}$, and let the radii of the incircle, $B$-excircle and $C$-excircle be $r, r_{b}$ and $r_{c}$, respectively. Let the incircle be tangent to $A C$ and $A B$ at $B_{0}$ and $C_{0}$, respectively; let the $B$-excircle be tangent to $A C$ at $B_{1}$, and let the $C$-excircle be tangent to $A B$ at $C_{1}$. As is well-known, $A B_{1}=s-c$ and area $(\triangle A B C)=r s=r_{c}(s-c)$.

Let the line through $X$, parallel to $A C$ be tangent to the incircle at $E$, and the line through $Y$, parallel to $A B$ be tangent to the incircle at $D$. Finally, let $A P$ meet $B B_{1}$ at $F$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-069}

It is well-known that points $B, E$, and $B_{1}$ are collinear by the homothety between the incircle and the $B$-excircle, and $B E \| I K$ because $I K$ is a midline in triangle $B_{0} E B_{1}$. Similarly, it follows that $C, D$, and $C_{1}$ are collinear and $C D \| I L$. Hence, the problem reduces to proving $\angle Y P A=\angle C B E$ (and its symmetric counterpart $\angle A P X=\angle D C B$ with respect to the vertex $C$ ), so it suffices to prove that $F Y P B$ is cyclic. Since $A C P B$ is cyclic, that is equivalent to $F Y \| B_{1} C$ and $\frac{B F}{F B_{1}}=\frac{B Y}{Y C}$.

By the angle bisector theorem we have

$$
\frac{B F}{F B_{1}}=\frac{A B}{A B_{1}}=\frac{c}{s-c} .
$$

The homothety at $C$ that maps the incircle to the $C$-excircle sends $Y$ to $B$, so

$$
\frac{B C}{Y C}=\frac{r_{c}}{r}=\frac{s}{s-c} .
$$

So,

$$
\frac{B Y}{Y C}=\frac{B C}{Y C}-1=\frac{s}{s-c}-1=\frac{c}{s-c}=\frac{B F}{F B_{1}},
$$

which completes the solution.

---
