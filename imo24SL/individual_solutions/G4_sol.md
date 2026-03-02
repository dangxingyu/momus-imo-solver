### reference solution 1
Let $M$ and $N$ be the midpoints of $A D$ and $B C$, respectively and let the perpendicular bisector of $A B$ intersect the line through $P$ parallel to $A B$ at $R$.\\
Lemma. Triangles $Q A B$ and $R N M$ are similar.\\
Proof. Let $O$ be the circumcentre of triangle $A B C$, and let $S$ be the midpoint of $C X$. Since $N, S$, and $R$ are the respective perpendicular feet from $O$ to $B C, C X$, and $P R$, we have that quadrilaterals $P R N O$ and $C N S O$ are cyclic. Furthermore, $P, S$, and $O$ are collinear as $P C=P X$. Since $A B C X$ is also cyclic, we have that

$$
\angle Q A B=\angle X C B=\angle P O N=180^{\circ}-\angle N R P=\angle M N R .
$$

Analogously, we have that $\angle A B Q=\angle R M N$, so triangles $Q A B$ and $R N M$ are similar.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-073}

Let $d(Z, \ell)$ denote the perpendicular distance from the point $Z$ to the line $\ell$. Using that $P R \| A B$ along with the similarities $Q A B \sim R N M$ and $P A B \sim P M N$, we have that

$$
\frac{d(Q, A B)}{A B}=\frac{d(R, M N)}{M N}=\frac{d(P, M N)}{M N}=\frac{d(P, A B)}{A B},
$$

which implies that $P Q \| A B$.

---


---

### reference solution 2
Let $B D$ and $A C$ intersect at $T$ and let the line through $P$ parallel to $A B$ intersect $B D$ at $V$. Next, let $Q^{\prime}$ be the foot of the perpendicular from $T$ to $P V$. Finally, let $Q^{\prime} A$ intersect circle $A B C$ again at $X^{\prime}$ and $Q^{\prime} B$ intersect circle $A B D$ again at $Y^{\prime}$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-074}

Claim. $P Q^{\prime}$ bisects $\angle B Q^{\prime} D$ externally.\\
Proof. Let $P T$ intersect $C D$ at $L$. Let $\infty_{C D}$ be the point at infinity on line $C D$. From the standard Ceva-Menelaus configuration we have ( $D, C ; L, \infty_{C D}$ ) is harmonic. Hence projecting through $P$ we have

$$
-1=\left(D, C ; L, \infty_{C D}\right)=(D, B ; T, V) .
$$

As ( $D, B ; T, V$ ) is harmonic, and also $\angle V Q^{\prime} T=90^{\circ}$ (by construction), the claim follows.\\
Now as

$$
\angle Q^{\prime} P D=\angle B A D=180^{\circ}-\angle D Y^{\prime} B=180^{\circ}-\angle D Y^{\prime} Q^{\prime}
$$

we have $Q^{\prime} P D Y^{\prime}$ cyclic. By the claim, we have that $P$ is the midpoint of $\operatorname{arc} \widetilde{D Q^{\prime} Y^{\prime}}$, so $P D=P Y^{\prime}$.

Since $Y$ is the unique point not equal to $D$ on circle $A B D$ satisfying $P D=P Y$, we have $Y^{\prime}=Y$.

Likewise $X^{\prime}=X$ so $Q^{\prime}=Q$ and we are done.

---


---

### reference solution 3
Let $A X$ intersect circle $P C X$ for the second time at $Q^{\prime}$. Then

$$
\angle A Q^{\prime} P=\angle X Q^{\prime} P=\angle X C P=\angle X C B=180^{\circ}-\angle B A X=\angle Q^{\prime} A B
$$

so $P Q^{\prime}$ is parallel to $A B$. Hence, it suffices to show that $Q^{\prime}$ is equal to $Q$. To do so, we aim to show the common chord of circles $P C X$ and $P D Y$ is parallel to $A B$, since then by symmetry $Q^{\prime}$ is also the second intersection of $B Y$ and circle $P D Y$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-075}

Let the centres of circles $P C X$ and $P D Y$ be $O_{X}$ and $O_{Y}$, respectively. Let the centres of circles $A B C$ and $A B D$ be $O_{C}$ and $O_{D}$, respectively.

Note $P, O_{X}$, and $O_{C}$ are collinear since they all lie on the perpendicular bisector of $C X$. Likewise $P, O_{Y}$, and $O_{D}$ are collinear on the perpendicular bisector of $D Y$. By considering the projections of $O_{X}$ and $O_{C}$ onto $B C$, and $O_{Y}$ and $O_{D}$ onto $A D$, we have

$$
\frac{P O_{X}}{P O_{C}}=\frac{\frac{P C}{2}}{\frac{P B+P C}{2}}=\frac{\frac{P D}{2}}{\frac{P A+P D}{2}}=\frac{P O_{Y}}{P O_{D}} .
$$

Hence $O_{X} O_{Y}$ is parallel to $O_{C} O_{D}$, which is perpendicular to $A B$ as desired.

---
