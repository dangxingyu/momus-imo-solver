### reference solution 1
Let $T$ be the midpoint of $\operatorname{arc} \widehat{B A C}$ and let lines $B A$ and $C D$ intersect $E F$ at $K$ and $L$, respectively. Note that $T$ lies on the perpendicular bisector of segment $B C$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-064}

Since $A B C D$ is cyclic, $\frac{B D}{\sin \angle B A D}=\frac{A C}{\sin \angle A D C}$. From parallel lines we have $\angle D A F=\angle A D C$ and $\angle B A D=\angle E D A$. Hence,

$$
A F \cdot \sin \angle D A F=B D \cdot \sin \angle A D C=A C \cdot \sin \angle B A D=D E \cdot \sin \angle E D A .
$$

So $F$ and $E$ are equidistant from the line $A D$, meaning that $E F$ is parallel to $A D$.\\
We have that $K A D E$ and $F A D L$ are parallelograms, hence we get $K A=D E=A C$ and $D L=A F=B D$. Also, $K E=A D=F L$ so it suffices to prove the perpendicular bisector of $K L$ passes through $T$.

Triangle $A K C$ is isosceles so $\angle B T C=\angle B A C=2 \angle B K C$. Likewise, $\angle B T C=2 \angle B L C$. Since $T, K$, and $L$ all lie on the same side of $B C$ and $T$ lies on the perpendicular bisector of $B C, T$ is the centre of circle $B K L C$. The result follows.

---


---

### reference solution 2
Let $A F$ and $D E$ meet $\omega$ at $X$ and $Y$, respectively, and let $T$ be as in

---


---

### reference solution 1
\\
As $B D<A D, D Y \| A B$ and $\angle B A Y=\angle D B A<90^{\circ}$, we have $D Y<A B$ and $Y$ lies on the opposite side of line $A D$ to $C$. Also from $B D<A D$, we have $B, C$, and $D$ all lie on the same side of the perpendicular bisector of $A B$ which shows $A C>A B$. Combining these, we get $D Y<A B<A C=D E$ and, as $Y$ and $E$ both lie on the same side of line $A D, Y$ lies in the interior of segment $D E$. Similarly, $X$ lies in the interior of segment $D F$.

Since $A B$ is parallel to $D Y$, we have $Y A=B D=F A$. Likewise $X D=A C=E D$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-065}

Claim 1. $T$ is the midpoint of $\operatorname{arc} \wideparen{X Y}$.\\
Proof. From $A X \| C D$ and $A B \| D Y$ we have

$$
\angle C A X=\angle A X D=\angle A Y D=\angle Y D B .
$$

Since $T$ is the midpoint of $\operatorname{arc} \widehat{B A C}$, we have $\angle B A T=\angle T D C$, so

$$
\angle T A X=\angle C A X+\angle B A C-\angle B A T=\angle Y D B+\angle B D C-\angle T D C=\angle Y D T .
$$

Recall from above we have $A B<A C$ and analogously, $D C<D B$, which shows that $X, Y$ and $T$ all lie on the same side of line $A D$. In particular, $T$ and $A$ lie on opposite sides of $X Y$ so $T$ lies on the internal angle bisector of $\angle X A Y$. Since $A F=A Y$, we have $\triangle A T F \cong \triangle A T Y$, giving $T F=T Y$.

Likewise, $T E=T X$, so $T E=T F$, meaning that $T$ lies on the perpendicular bisector of segment $E F$ as required.

---


---

### reference comment
The statement remains true without the length and angle conditions on cyclic quadrilateral $A B C D$ however additional care is required to consider different cases based on the ordering of points on lines $D E$ and $A F$. It is also possible for $T$ to be on the external angle bisector of $\angle X A Y$.

---


---

### reference solution 3
From $A F=D B, A C=D E$ and

$$
\angle(A C, A F)=\angle(A C, C D)=\angle(A B, B D)=\angle(D E, D B),
$$

triangles $A C F$ and $D E B$ are congruent, so $C F=B E$.\\
Let $P=B E \cap C F$. Since

$$
\angle(C P, B P)=\angle(C F, B E)=\angle(A F, D B)=\angle(D C, D B),
$$

we have that $P$ lies on circle $A B C D$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-066}

Finally, let $T$ be the Miquel point of the quadrilateral $B C F E$ so $T$ lies on circles $E F P$ and $A B C D$. Note that $T$ is the centre of spiral similarity taking segments $B E$ to $C F$ and since $B E=C F$, this is in fact just a rotation, so $T B=T C$ and $T E=T F$; that is, the perpendicular bisectors of $B C$ and $E F$ meet at $T$, on circle $A B C D$.

---
