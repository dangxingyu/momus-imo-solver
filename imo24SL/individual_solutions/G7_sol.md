### reference solution 1
}
\begin{center}
\includegraphics[max width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-082}
\end{center}

Let $O$ be the circumcentre of $\triangle A B C$. First we note from standard properties of the Miquel point $S$ we have:

\begin{itemize}
  \item $\triangle S M_{C} M_{B} \sim \triangle S B C \sim \triangle S P Q ; \quad(*)$
  \item $I$ and $S$ are inverses with respect to circle $A B C$;
  \item $\angle O S X=90^{\circ}$.
\end{itemize}

Claim 1. $\angle M_{A} P B=\angle C D A$.\\
Proof. From the above we have $\triangle O M_{A} I \sim \triangle O S M_{A}$ and

$$
\angle M_{A} P B=\angle M_{A} P X=\angle M_{A} S X=90^{\circ}+\angle M_{A} S O=90^{\circ}+\angle O M_{A} I=\angle M_{A} B A=\angle C D A \text {. }
$$

Claim 2. $\quad \frac{M_{C} B}{B P}=\frac{M_{B} C}{C Q}=\frac{A I}{I D}$.\\
Proof. Observe that $\angle P M_{C} M_{A}=\angle B M_{C} M_{A}=\angle D A C$ and $\angle M_{C} M_{A} B=\angle I C D$. Combining these with Claim 1 shows $M_{C} P M_{A} B \sim A D C I$. Therefore, $\frac{M_{C} B}{B P}=\frac{A I}{I D}$. Similarly, $\frac{M_{B} C}{C Q}=\frac{A I}{I D}$.

Claim 3. $\quad \frac{D P}{D Q}=\frac{I B}{I C}$.\\
Proof. Firstly, observe that $\angle I C B=\angle A M_{B} M_{C}$ and $\angle C B I=\angle M_{B} M_{C} A$ which gives that $\triangle I B C \sim \triangle A M_{C} M_{B}$. This, combined with Claim 2, is enough to show $\triangle D P Q \sim \triangle I B C$ by linearity, proving the claim.\\
Claim 4. $\frac{I P}{I Q}=\frac{I B}{I C}$.\\
Proof. Combining $\triangle I B M_{C} \sim \triangle I C M_{B}$ with Claim 2 shows $I B M_{C} P \sim I C M_{B} Q$ giving the result.

Finally, we have that

$$
\frac{S P}{S Q}=\frac{S B}{S C}=\frac{B M_{C}}{C M_{B}}=\frac{I B}{I C}
$$

from (*) and $\triangle I B M_{C} \sim \triangle I C M_{B}$. Putting this together with Claims 3 and 4, we have that

$$
\frac{I B}{I C}=\frac{D P}{D Q}=\frac{I P}{I Q}=\frac{S P}{S Q}
$$

which shows that circle $S I D$ is an Apollonius circle with respect to $P$ and $Q$, giving the desired conclusion.

---


---

### reference comment
The condition $A B<A C$ ensures $S \neq X$. We also need to avoid the case $\angle B A C=60^{\circ}$ as then $B M_{C} \| C M_{B}$.

---


---

### reference solution 2
We use Claim 1 from

---


---

### reference solution 1
We will show that $P$ and $Q$ are inverses in circle $S I D$ which implies the result. Perform an inversion in circle $B I C$ and denote the inverse of a point $\bullet$ by $\bullet^{\prime}$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-084}

Claim 1. $\quad S^{\prime}=J$ where $J$ is the reflection of $I$ across $B C$.\\
Proof. We have that $S$ and $I$ are inverses in circle $A B C$. Inverting this assertion in circle $B I C$ shows that $S^{\prime}$ and $I$ are inverses with respect to line $B C$, which is just a reflection in line $B C$.

Let $Y=M_{B} M_{C} \cap B C$. From $\angle I M_{C} M_{B}=\angle M_{B} M_{C} A$ and $\angle A M_{B} M_{C}=\angle M_{C} M_{B} I$, we see that $A$ and $I$ are reflections in line $M_{B} M_{C}$ so $Y A=Y I$. We have that circle $S I D$ maps to circle $A I J$ which, from the previous comment, has centre $Y$. Inverting the conclusion that $P$ and $Q$ are inverses with respect to circle $S I D$ in circle $B I C$, it suffices to show $P^{\prime}$ and $Q^{\prime}$ are inverses with respect to circle $A I J$ or equivalently, that $Y P^{\prime} \cdot Y Q^{\prime}=Y A^{2}$.\\
Claim 2. Circle $X S M_{A}$ maps to line $Y J$ under the inversion in circle $B I C$.\\
Proof. Since circle $B I C$ has centre $M_{A}$, the inverse of this circle is a line. By Claim 1, this line passes through $J$ hence it suffices to prove that circle $X S M_{A}$ passes through $Y^{\prime}$. From inverting line $B C$ in circle $B I C$, we have that $B C M_{A} Y^{\prime}$ is cyclic so

$$
Y S \cdot Y X=Y B \cdot Y C=Y Y^{\prime} \cdot Y M_{A} .
$$

where we have used that $Y, S$ and $X$ are collinear by a standard property of the Miquel point. Hence $Y^{\prime}$ lies on circle $X S M_{A}$ as required.

Let $A_{1}$ be the reflection of $A$ in the perpendicular bisector of $B C$. Using Claim 1 from Solution 1,

$$
\angle P^{\prime} B M_{A}=\angle M_{A} P B=\angle C D A=180^{\circ}-\angle A C M_{A}=180^{\circ}-\angle M_{A} B A_{1} .
$$

Hence, $P^{\prime}, B$, and $A_{1}$ are collinear. Similarly $Q^{\prime}, C$, and $A_{1}$ are collinear. Let $P_{1}$ and $Q_{1}$ be the reflections of $P^{\prime}$ and $Q^{\prime}$ across $B C$. As $P^{\prime}$ and $Q^{\prime}$ lie on line $Y J$, it follows that $P_{1}$ and $Q_{1}$ lie on line $Y I$. Also from the previous collinearities, we get $B P_{1} \| A C$ and $C Q_{1} \| A B$.

We have now reduced the problem to the following:\\
Claim 3 (Inverted Problem). Let $A B C$ be a triangle with incentre $I$. Let $Y$ be the point on $B C$ such that $Y A=Y I$. Let $P_{1}$ and $Q_{1}$ be points on $Y I$ such that $B P_{1} \| A C$ and $C Q_{1} \| A B$. Then $Y A^{2}=Y P_{1} \cdot Y Q_{1}$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-085}

Proof. Let $Y I$ intersect $A B$ and $A C$ at $E$ and $F$, respectively. From the parallel lines, we get that $\triangle B E P_{1}$ and $\triangle C Q_{1} F$ are homothetic with centre $Y$. Thus we have

$$
\frac{Y E}{Y P_{1}}=\frac{Y Q_{1}}{Y F} \Longrightarrow Y P_{1} \cdot Y Q_{1}=Y E \cdot Y F
$$

Moreover, $A I$ bisects $\angle E A F$ and $Y A=Y I$ so the circle centred at $Y$ with radius $Y A$ is the Apollonius circle of $\triangle A E F$ with respect to the feet of the internal and external angle bisectors at $A$. This gives $Y E \cdot Y F=Y A^{2}$. Combining these results proves the claim.

---


---

### reference solution 3
As in Solution 1, let $O$ be the circumcentre of $\triangle A B C$. Let $X I$ intersect circle $X S M_{A}$ again at $Z \neq X$ and let $Y=B C \cap M_{B} M_{C}$. Let $X^{*}$ be the inverse of $X$ in circle $A B C$. We will use the properties of Miquel point $S$ noted at the top of Solution 1 and in addition, that $S$ lies on line $X Y$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-086}

Claim 1. YSAD is cyclic.\\
Proof. From $O M_{A} \perp B C$ and $Y S \perp O S$ we have $\angle D Y S=180^{\circ}-\angle S O M_{A}$. From inverting collinear points $A, I$ and $M_{A}$ in circle $A B C$ we get $A S M_{A} O$ is cyclic which gives

$$
\angle S O M_{A}=\angle S A M_{A}=\angle S A D \Longrightarrow \angle S A D+\angle D Y S=180^{\circ}
$$

proving the claim.\\
Claim 2. $\quad X^{*}$ lies on circle BIC which has centre $M_{A}$.\\
Proof. This follows immediately from inverting circle $S B C X$ in circle $A B C$.\\
Claim 3. $Z$ lies on circle SID.\\
Proof. We have that

$$
\angle I Z S=\angle X M_{A} S=\angle O M_{A} S-\angle O M_{A} X=\angle M_{A} I O-\angle M_{A} X^{*} O=\angle D I O-\angle M_{A} X^{*} O
$$

where in the penultimate step we inverted in circle $A B C$ to get the angle equalities.

From Brocard's Theorem applied to cyclic quadrilateral $B M_{C} M_{B} C$, we get $Y, I$, and $X^{*}$ collinear and $\angle Y X^{*} O=90^{\circ}$. This gives that

$$
\angle M_{A} X^{*} O=90^{\circ}-\angle I X^{*} M_{A}=90^{\circ}-\angle M_{A} I X^{*}=90^{\circ}-\angle A I Y
$$

where the second equality is by Claim 2. We have that $A$ and $I$ are reflections in line $M_{B} M_{C}$. Hence,

$$
90^{\circ}-\angle A I Y=90^{\circ}-\angle Y A D=90^{\circ}-\angle Y S D=\angle D S O
$$

where the second step is by Claim 1, and in the last step we are using $O S \perp Y S$. Putting these together,

$$
\angle I Z S=\angle D I O-\angle D S O=\angle I D S
$$

proving the claim.\\
Let the tangents from $S$ and $Z$ to circle $X S M_{A}$ intersect at $K$. Observe from the standard Ceva-Menelaus configuration,

$$
-1=(X Y, X I ; X B, X C) \stackrel{X}{=}(S, Z ; P, Q) .
$$

This shows that $K$ lies on line $P Q$. We then have

$$
\angle Z K S=180^{\circ}-2 \angle S X Z=2\left(90^{\circ}-\angle S X I\right)=2\left(180^{\circ}-\angle S I Z\right),
$$

where we are using $\angle I S X=90^{\circ}$. As $K$ lies on the perpendicular bisector of $S Z$, this is enough to show that $K$ is the centre of circle $S I D Z$ completing the proof.

---


---

### reference solution 4
Solution 1 solves the problem by establishing $\frac{S P}{S Q}=\frac{I P}{I Q}=\frac{D P}{D Q}$, which implies that circle $S I D$ is an Apollonius circle with respect to $P$ and $Q$. We demonstrate an alternate approach that only requires us to show two of the ratios $\frac{S P}{S Q}, \frac{I P}{I Q}$, and $\frac{D P}{D Q}$ to be equal. This can arise from missing some of the observations in Solution 1, for example not proving Claim 3.\\
Claim. Given we have shown two of the ratios listed above to be equal, it suffices to show that circle $S I D$ is orthogonal to circle $S X M_{A}$, which the same circle as $S P Q$.\\
Proof. Supposing we have shown the orthogonality, if $\frac{S P}{S Q}=\frac{I P}{I Q}$ or $\frac{S P}{S Q}=\frac{D P}{D Q}$, then we immediately have that circle $S I D$ is an Apollonius circle with respect to $P$ and $Q$. If $\frac{I P}{I Q}=\frac{D P}{D Q}$ and $S$ does not lie on the Apollonius circle $\mathcal{C}$ defined by this common ratio, then $I$ and $D$ lie on two distinct circles orthogonal to circle $S P Q$, namely circle $S I D$ and $\mathcal{C}$. This implies that $I$ and $D$ are inverses with respect to circle $S P Q$, which is a contradiction as both $I$ and $D$ lie inside circle $S P Q$.

Throughout this solution, we will use the properties of $S$ from the beginning of

---


---

### reference solution 1
Define $O$ and $Y$ as in previous solutions, and let $E$ be the second intersection of circles $S O M_{A}$ and $S M_{B} M_{C}$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-088}

\section*{Lemma. We have that $O E \perp A Y$.}
Proof. Let $M_{A}^{\prime}, B^{\prime}$, and $C^{\prime}$ be the respective reflections of $M_{A}, B$, and $C$ over line $M_{B} M_{C}$. As noted in Solution 3, $A$ and $I$ are reflections across $M_{B} M_{C}$. Because $M_{A}$ is the centre of circle $B I C$, it follows that $M_{A}^{\prime}$ is the centre of circle $A B^{\prime} C^{\prime}$. On the other hand, $Y$ lies on $M_{B} M_{C}$, so we have that $Y B \cdot Y C=Y B^{\prime} \cdot Y C^{\prime}$. Thus, $Y$ lies on the radical axis of circles $A B C$ and $A B^{\prime} C^{\prime}$, so $O M_{A}^{\prime} \perp A Y$. Finally, note that the inverses of circles $S O M_{A}$ and $S M_{B} M_{C}$ in circle $A B C$ are line $I M_{A}$ and circle $I M_{B} M_{C}$ respectively, so $E$ and $M_{A}^{\prime}$ are inverses in circle $A B C$. Thus, $E$ lies on $O M_{A}^{\prime}$ and the lemma follows.

Let $\mathcal{T}$ denote the composition of an inversion at $S$ with radius $\sqrt{S I \cdot S O}$ with a reflection across line $S I$. By standard properties of the Miquel point, $\mathcal{T}$ swaps $X$ and $Y$ and any points $Z_{1}$ and $Z_{2}$ on circle $A B C$ with $I \in Z_{1} Z_{2}$. Hence, $\mathcal{T}$ swaps the pairs $\left(A, M_{A}\right),\left(B, M_{B}\right),\left(C, M_{C}\right)$, $(O, I)$, and $(X, Y)$. As $D=A I \cap B C$ and $E$ is the intersection of circles $S O M_{A}$ and $S M_{B} M_{C}$, we have that $\mathcal{T}(D)=E$. Thus, $\mathcal{T}$ maps circles SID and SXM ${ }_{A}$ to lines $O E$ and $A Y$, so by the Lemma, circles SID and SXM ${ }_{A}$ are orthogonal, as required.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-089}

---
