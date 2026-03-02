### reference solution 1
Let $X$ be the intersection of $I_{B} J_{C}$ and $J_{B} I_{C}$. We will prove that, provided that $A B<A C<B C$, the following two conditions are equivalent:\\
(1) $A X$ bisects $\angle B A C$;\\
(2) $I_{B}, I_{C}, J_{B}$, and $J_{C}$ are concyclic.

Let circles $A I B$ and $A I C$ meet $B C$ again at $P$ and $Q$, respectively. Note that $A B=B Q$ and $A C=C P$ because the centres of circles $A I B$ and $A I C$ lie on $C I$ and $B I$, respectively. Thus, $B, P, Q$, and $C$ are collinear in this order as $B Q+P C=A B+A C>B C$ by the triangle inequality.\\
Claim 1. Points $P, J_{B}$, and $I_{C}$ are collinear, and points $Q, I_{B}$, and $J_{C}$ are collinear.\\
Proof. We have that

$$
\angle A J_{B} B=90^{\circ}+\frac{1}{2} \angle A E B=90^{\circ}+\frac{1}{2} \angle A C B=\angle A I B=\angle A P B,
$$

so $A B J_{B} P$ is cyclic. As $A$ is the centre of spiral similarity between $A B E$ and $A D C$, it is also the centre of spiral similarity between $A B J_{B}$ and $A D I_{C}$. Hence, $A$ is the Miquel point of self-intersecting quadrilateral $B D I_{C} J_{B}$, so $P$ lies on $J_{B} I_{C}$. Analogously, we have that $Q$ lies on $I_{B} J_{C}$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-090}

Throughout the rest of the solution, we will use directed angles.

Proof of (1) $\Longrightarrow$ (2). We assume that (1) holds.\\
Claim 1 and the similarities $A B D I_{B} \sim A E C J_{C}$ and $A B E J_{B} \sim A D C I_{C}$ tell us that

$$
\Varangle I_{B} X I_{C}=\Varangle J_{C} Q C+\Varangle B P J_{B}=\Varangle J_{C} A C+\Varangle B A J_{B}=\Varangle I_{B} A D+\Varangle D A I_{C}=\Varangle I_{B} A I_{C},
$$

so $A I_{B} X I_{C}$ is cyclic. Also, as $X \in A I$, we have that

$$
\Varangle I_{B} A X=\Varangle B A I-\Varangle B A I_{B}=\Varangle I_{B} A I_{C}-\Varangle I B_{A} D=\Varangle D A I_{C} .
$$

Using these, we have that

$$
\Varangle I_{B} I_{C} P=\Varangle I_{B} A X=\Varangle D A I_{C}=\Varangle B A J_{B}=\Varangle B P J_{B},
$$

so $I_{B} I_{C} \| B C$. Hence,

$$
\Varangle I_{B} I_{C} J_{B}=\Varangle B P J_{B}=\Varangle B I J_{B}=\Varangle I_{B} I J_{B},
$$

so $I I_{B} J_{B} I_{C}$ is cyclic. Analogously, we have that $I I_{C} J_{C} I_{B}$ is cyclic, so $I_{B} J_{B} J_{C} I_{C}$ is cyclic, thus proving (2).\\
Proof of (2) $\Longrightarrow$ (1). We assume that (2) holds.\\
Claim 2. Circles $I B C, I J_{B} I_{C}$, and $I I_{B} J_{C}$ are tangent at $I$.\\
Proof. Using the cyclic quadrilateral $B I J_{B} P$, we have that

$$
\Varangle I B C=\Varangle I B P=\Varangle I J_{B} P=\Varangle I J_{B} I_{C} .
$$

As $C, I_{C}$, and $I$ are collinear, the tangents to circles $I_{B} I_{C}$ and $I B C$ at $I$ coincide, so circles $I J_{B} I_{C}$ and $I B C$ are tangent at $I$. Analogously, circles $I I_{B} J_{C}$ and $I B C$ are tangent at $I$, so all three circles are tangent at $I$.\\
Claim 3. Point $I$ lies on circle $I_{B} J_{B} J_{C} I_{C}$.\\
Proof. Suppose that $I$ does not lie on circle $I_{B} J_{B} J_{C} I_{C}$. Then the circles $I I_{B} J_{C}, I J_{B} I_{C}$, and $I_{B} J_{B} J_{C} I_{C}$ are distinct. We apply the radical axis theorem to these three circles. By Claim 2, the radical axis of circles $I I_{B} J_{C}$ and $I J_{B} I_{C}$ is the tangent to circle $I B C$ at $I$. As $I_{B} J_{C}$ and $J_{B} I_{C}$ intersect at $X, I X$ must be tangent to circle $I B C$.

However, by Claim 1 we have that $X$ is the intersection of $P I_{C}$ and $Q I_{B}$. As $D$ lies on the interior of segment $B C, I_{B}$ lies on the interior of segment $B I$ and $I_{C}$ lies on the interior of segment $C I$. Hence, $I_{B}, P, Q$, and $I_{C}$ all lie on the perimeter of triangle $I B C$ in this order, so $X$ must be in the interior of triangle $I B C$. This means that $I X$ cannot be tangent to circle $B I C$, so $I$ must lie on circle $I_{B} J_{B} J_{C} I_{C}$.

By Claims 2 and 3, circles $I I_{B} I_{C}$ and $I B C$ are tangent, so $I_{B} I_{C} \| B C$. Since $I_{B} J_{B} J_{C} I_{C}$ is cyclic, we have that

$$
\Varangle P J_{B} J_{C}=\Varangle I_{C} J_{B} J_{C}=\Varangle I_{C} I_{B} J_{C}=\Varangle P Q I_{B}=\Varangle P Q J_{C} \text {, }
$$

so $P J_{B} J_{C} Q$ is cyclic. By the radical axis theorem on circles $A I P J_{B}, A I Q J_{C}$, and $P J_{B} J_{C} Q$, we have that $A I, I_{B} J_{C}$, and $J_{B} I_{C}$ concur at $X$, thus proving (1).

---


---

### reference solution 2
Let $X$ be the intersection of $I_{B} J_{C}$ and $J_{B} I_{C}$. As in Solution 1, we will prove that conditions (1) and (2) are equivalent. To do so, we introduce the new condition:\\
(3) $I_{B} I_{C} \| B C$\\
and show that (3) is equivalent to both (1) and (2), provided that $A B<A C<B C$.\\
Note that $A B D{ }^{+} A E C$ and $A B E{ }^{+} A D C$, where ${ }^{+}$denotes positive similarity. We will make use of the following fact.

Fact. For points $P, P_{1}, P_{2}, P_{3}$, and $P_{4}$, the positive similarities

$$
P P_{1} P_{2} \stackrel{+}{\sim} P P_{3} P_{4} \quad \text { and } \quad P P_{1} P_{3} \stackrel{ \pm}{\sim} P P_{2} P_{4}
$$

are equivalent.\\
Proof of (1) $\Longleftrightarrow$ (3). Let $A I_{B}$ and $A I_{C}$ meet $B C$ at $S$ and $T$, respectively. Let $A J_{B}$ meet $B E$ at $K, A J_{C}$ meet $C E$ at $L$, and $K T$ and $S L$ meet at $Y$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-092}

Claim 1. Line $A Y$ bisects $\angle B A C$.\\
Proof. Let $Y^{\prime}$ be the intersection of $K T$ and the bisector of $\angle B A C$. As

$$
\angle B A K=\frac{1}{2} \angle B A E=\frac{1}{2} \angle D A C=\angle T A C,
$$

$A Y^{\prime}$ also bisects $\angle K A T$. Hence, $Y^{\prime}$ is the foot of the bisector of $\angle K A T$ in triangle $A K T$. Using the Fact, we have that

$$
\begin{aligned}
A B E \sim^{+} A D C & \Longrightarrow A B E K \sim^{+} A D C T \\
& \Longrightarrow A B D \sim^{+} A K T \sim^{+} A E C \\
& \Longrightarrow A B D S \sim^{+} A K T Y^{\prime} \sim^{+} A E C L \\
& \Longrightarrow A B E K \sim^{+} A S L Y^{\prime} \sim^{+} A D C T .
\end{aligned}
$$

As $K$ lies on $B E$, we have that $Y^{\prime}$ lies on $S L$, so $Y=Y^{\prime}$ and $A Y$ bisects $\angle B A C$.\\
We show that $X$ lies on $A Y$ if and only if $I_{B} I_{C} \| B C$, which implies the equivalence of (1) and (3) by Claim 1. Let $A Y$ meet $I_{B} J_{C}$ and $J_{B} I_{C}$ at $X_{1}$ and $X_{2}$, respectively. As $A B D$ and $A E C$ are similar, we have that $\frac{A I_{B}}{A S}=\frac{A J_{C}}{A L}$, so $I_{B} J_{C} \| S L$. Analogously, we have that $J_{B} I_{C} \| K T$. Hence, $X_{1}$ and $X_{2}$ coincide with $X$ if and only if

$$
\frac{A I_{B}}{A S}=\frac{A X_{1}}{A Y}=\frac{A X_{2}}{A Y}=\frac{A I_{C}}{A T},
$$

which is equivalent to $I_{B} I_{C} \| B C$.

Proof of (2) $\Longleftrightarrow$ (3). Let $A J_{B}$ and $A J_{C}$ meet circle $A B C$ at $M$ and $N$, respectively, and let $I_{B}^{\prime}$ and $I_{C}^{\prime}$ be the $A$-excentres of $A B D$ and $A D C$, respectively.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-093(1)}

Claim 2. Lines $I_{B} I_{C}, I_{B}^{\prime} I_{C}^{\prime}$, and $B C$ are concurrent or pairwise parallel.\\
Proof. We work in the projective plane. Let $I_{B} I_{C}$ and $I_{B}^{\prime} I_{C}^{\prime}$ meet $B C$ at $Z$ and $Z^{\prime}$, respectively. Note that $Z$ is the intersection of the external common tangents of the incircles of $A B D$ and $A D C$ and $A D$ is a common internal tangent of the incircles of $A B D$ and $A D C$, so $\left(A D, A Z ; A I_{B}, A I_{C}\right)=-1$. Applying the same argument to the $A$-excircles of $A B D$ and $A D C$ gives $\left(A D, A Z^{\prime} ; A I_{B}^{\prime}, A I_{C}^{\prime}\right)=-1$, which means that $Z=Z^{\prime}$. Thus, $I_{B} I_{C}, I_{B}^{\prime} I_{C}^{\prime}$, and $B C$ concur, possibly at infinity.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-093}

Claim 3. Lines $J_{B} I_{C}$ and $C M$ are parallel, and lines $I_{B} J_{C}$ and $B N$ are parallel. Proof. Using the Fact, we have that

$$
A B E \stackrel{+}{\sim} A D C \Longrightarrow A B E J_{B} \stackrel{+}{\sim} A D C I_{C} \Longrightarrow A J_{B} I_{C} \stackrel{+}{\sim} A B D .
$$

Thus, $\angle\left(B D, J_{B} I_{C}\right)=\angle B A J_{B}=\angle B C M$, so $J_{B} I_{C} \| C M$. Similarly, we have that $I_{B} J_{C} \| B N$.\\
Claim 4. The centre of spiral similarity between $J_{B} J_{C}$ and $I_{B}^{\prime} I_{C}^{\prime}$ is $A$.\\
Proof. As $I_{B}$ and $I_{B}^{\prime}$ are respectively the incentre and $A$-excentre of triangle $A B D$, we have that $A B I_{B}^{\prime} \stackrel{+}{\sim} A I_{B} D$. Using the similarity $A B D \stackrel{+}{\sim} A E C$, this means that $A B I_{B}^{\prime} \stackrel{+}{\sim} A J_{C} C$, so $A B \cdot A C=A I_{B}^{\prime} \cdot A J_{C}$ and $\angle B A I_{B}^{\prime}=\angle J_{C} A C$. Similarly, we have that $A B \cdot A C=A J_{B} \cdot A I_{C}^{\prime}$ and $\angle B A J_{B}=\angle I_{C}^{\prime} A C$. Together, these imply that $A I_{B}^{\prime} \cdot A J_{C}=A J_{B} \cdot A I_{C}^{\prime}$ and $\angle J_{B} A J_{C}=\angle I_{B}^{\prime} A I_{C}^{\prime}$, so $A J_{B} J_{C} \stackrel{+}{\sim} A I_{B}^{\prime} I_{C}^{\prime}$.

We proceed using directed angles. By Claim 3, we have that $I_{B} J_{B} J_{C} I_{C}$ is cyclic if and only if

$$
\begin{aligned}
\npreceq I_{B} I_{C} J_{B}=\Varangle I_{B} J_{C} J_{B} & \Longleftrightarrow \npreceq I_{B} I_{C} J_{B}+\npreceq M C B=\Varangle I_{B} J_{C} J_{B}+\npreceq M N B \\
& \Longleftrightarrow \npreceq\left(I_{B} I_{C}, B C\right)=\Varangle\left(M N, J_{B} J_{C}\right) .
\end{aligned}
$$

By Claim 4, we have that

$$
\begin{aligned}
\npreceq\left(J_{B} J_{C}, I_{B}^{\prime} I_{C}^{\prime}\right) & =\Varangle J_{B} A I_{B}^{\prime} \\
& =\Varangle B A I_{B}+\npreceq M A B \\
& =\Varangle E A J_{C}+\npreceq M A B \\
& =\Varangle N A C+\not 口 M A B \\
& =\Varangle(M N, B C),
\end{aligned}
$$

which is equivalent to $\Varangle\left(B C, I_{B}^{\prime} I_{C}^{\prime}\right)=\Varangle\left(M N, J_{B} J_{C}\right)$. Thus, $I_{B} J_{B} J_{C} I_{C}$ is cyclic if and only if


\begin{equation*}
\Varangle\left(I_{B} I_{C}, B C\right)=\Varangle\left(B C, I_{B}^{\prime} I_{C}^{\prime}\right) . \tag{*}
\end{equation*}


Suppose that $I_{B} I_{C}$ is parallel to $B C$. By Claim 2, $I_{B}^{\prime} I_{C}^{\prime}$ is also parallel to $B C$, so we have that $\Varangle\left(I_{B} I_{C}, B C\right)=\Varangle\left(B C, I_{B}^{\prime} I_{C}^{\prime}\right)=0^{\circ}$. Thus, (*) is satisfied, so $I_{B} J_{B} J_{C} I_{C}$ is cyclic.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-094}

Suppose now that $I_{B} I_{C}$ is not parallel to $B C$ while $I_{B} J_{B} J_{C} I_{C}$ is cyclic. By Claim $2, I_{B} I_{C}$, $I_{B}^{\prime} I_{C}^{\prime}$, and $B C$ concur at a point $Z$. As $I_{B}$ and $I_{C}$ lie on segments $B I$ and $C I, Z$ must lie outside segment $B C$. Since $A$ is the intersection of the common external tangents of the incircle and $A$-excircle of $A B D$ and $Z D$ is a common internal tangent of the incircle and $A$-excircle of $A B D$, we have that ( $Z A, Z D ; Z I_{B}, Z I_{B}^{\prime}$ ) = -1. By (*), $Z D$ bisects $\angle I_{B} Z I_{B}^{\prime}$, so $\angle A Z D=90^{\circ}$ : that is, $Z$ is the foot from $A$ to $B C$. But this implies that $\angle A B C$ or $\angle B C A$ is obtuse, contradicting the fact that $A B<A C<B C$.

---


---

### reference comment
While we have written the solution using harmonic bundles for the sake of brevity, there are ways to prove Claim 2 and obtain the final contradiction without the use of projective geometry. Claim 2 can be proven using an application of Menelaus's theorem, and the final contradiction can be obtained using the fact that an excircle of a triangle is always larger than its incircle.

---


---

### reference solution 3
Let $\omega_{B}$ and $\omega_{C}$ denote circles $A I B$ and $A I C$, respectively. Introduce $P, Q$ and $X$ as in Solution 1 and recall from Claim 1 in Solution 1 that $P, J_{B}$ and $I_{C}$ are collinear with $J_{B}$ lying on $\omega_{B}$. From this, we can define $J_{B}$ and $I_{C}$ in terms of $X$ by $I_{C}=X P \cap C I$ and $J_{B} \neq P$ as the second intersection of line $X P$ with $\omega_{B}$. Similarly, we can define $I_{B}=X Q \cap B I$ and $J_{C} \neq Q$ as the second intersection of line $X Q$ with $\omega_{C}$. Note that this now detaches the definitions of points $I_{B}, I_{C}, J_{B}$, and $J_{C}$ from points $D$ and $E$.

Let $\ell$ be a line passing through $I$. We now allow $X$ to vary along $\ell$ while fixing $\triangle A B C$ and points $I, P$, and $Q$. We use the definitions from above to construct $I_{B}, I_{C}, J_{B}$, and $J_{C}$. We will classify all cases where these four points are concyclic. Throughout the rest of the solution we use directed angles and directed lengths.

For nondegeneracy reasons, we exclude cases where $X=I$ and $X$ lies on line $B C$, which means that $I_{B}, J_{B} \neq B$ and $I_{C}, J_{C} \neq C$. We also exclude the cases where $\ell$ is tangent to either $\omega_{B}$ or $\omega_{C}$. Similar results hold in these cases and they can be treated as limit cases.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-095}

Claim 1. Line $I_{B} J_{B}$ passes through a fixed point on $\omega_{B}$, and line $I_{C} J_{C}$ passes through a fixed point on $\omega_{C}$ as $X$ varies on $\ell$.\\
Proof. Let $U \neq J_{B}$ be the second intersection of $I_{B} J_{B}$ with $\omega_{B}$. We have by the law of sines that

$$
\frac{\sin \Varangle I J_{B} U}{\sin \Varangle U J_{B} B}=\frac{\sin \Varangle I J_{B} I_{B}}{\sin \Varangle I_{B} J_{B} B}=\frac{\sin \Varangle J_{B} I I_{B}}{\sin \Varangle J_{B} B I_{B}} \cdot \frac{I I_{B}}{I_{B} B}=\frac{\sin \Varangle J_{B} I B}{\sin \Varangle J_{B} B I} \cdot \frac{I I_{B}}{I_{B} B}=\frac{\sin \Varangle X P Q}{\sin \Varangle X P I} \cdot \frac{I I_{B}}{I_{B} B} .
$$

We also have

$$
\frac{I I_{B}}{I_{B} B}=\frac{\sin \Varangle I Q I_{B}}{\sin \Varangle I_{B} Q B} \cdot \frac{|I Q|}{|B Q|}=\frac{\sin \Varangle I Q X}{\sin \Varangle X Q P} \cdot \frac{|I Q|}{|B Q|} .
$$

Combining these and applying Ceva's Theorem in $\triangle P I Q$ with point $X$, we get

$$
\frac{\sin \Varangle I J_{B} U}{\sin \Varangle U J_{B} B}=\frac{\sin \Varangle X P Q}{\sin \Varangle X P I} \cdot \frac{\sin \Varangle I Q X}{\sin \Varangle X Q P} \cdot \frac{|I Q|}{|B Q|}=\frac{\sin \Varangle X I Q}{\sin \Varangle X I P} \cdot \frac{|I Q|}{|B Q|}=\frac{\sin \Varangle(\ell, I Q)}{\sin \Varangle(\ell, I P)} \cdot \frac{|I Q|}{|B Q|},
$$

which is independent of the choice of $X$ on $\ell$. As $\Varangle I J_{B} U+\Varangle U J_{B} B=\Varangle I J_{B} B=\Varangle I A B$ is fixed, this is enough to show point $U$ is fixed on $\omega_{B}$.

Similarly, if we define $V \neq J_{C}$ to be the second intersection of $I_{C} J_{C}$ with $\omega_{C}$, we get that $V$ is fixed on $\omega_{C}$.

Let $G \neq X$ and $H \neq X$ be the second intersections of $\ell$ with $\omega_{B}$ and $\omega_{C}$, respectively which exist as we are assuming $\ell$ is not tangent to either $\omega_{B}$ or $\omega_{C}$.\\
Claim 2. Points $U, G$ and $Q$ are collinear and points $V, H$ and $P$ are collinear.\\
Proof. Taking $X=G$, we have $J_{B}=G$ and $I_{B}=X Q \cap B I$. Both of these points lie on line $Q G$ which, by Claim 1, shows that $U, G, Q$ are collinear. Similarly, $V, H, P$ are collinear.\\
Claim 3. Points $I_{B}, I_{C}, J_{B}, J_{C}$ are concyclic if and only if points $P, Q, G, H$ are concyclic. In particular, this depends only on $\ell$, not on the choice of $X$ on $\ell$.\\
Proof. We have that

$$
\begin{aligned}
& \Varangle I_{C} J_{B} I_{B}=\Varangle P J_{B} U=\Varangle P G U=\Varangle P G Q \\
& \not \Varangle I_{C} J_{C} I_{B}=\Varangle V J_{C} Q=\Varangle V H Q=\Varangle P H Q .
\end{aligned}
$$

Thus $\Varangle I_{C} J_{B} I_{B}=\Varangle I_{C} J_{C} I_{B} \Longleftrightarrow \Varangle P G Q=\Varangle P H Q$ which proves the claim.\\
Claim 4. $P, Q, G, H$ are concyclic if and only if $\ell \in\{I A, I P, I Q, t\}$ where $t$ is the tangent to circle $B I C$ at $I$.\\
Proof. When $\ell=I A$, we have $G=H=A$ so the cyclic condition from Claim 3 holds. Similarly, when $\ell=I P$ or $\ell=I Q, G=P$ or $H=Q$, respectively, so again the cyclic condition holds.

Now, consider the case where $\ell \notin\{I A, I P, I Q\}$. In this case it is straightforward to see that the four points $P, Q, G$, and $H$ are distinct. We then have that $\Varangle Q P G=\Varangle B P G=\Varangle B I G$, so

$$
P Q G H \text { concyclic } \Longleftrightarrow \npreceq Q H G=\Varangle Q P G \Longleftrightarrow \Varangle Q H G=\Varangle B I G \Longleftrightarrow Q H \| B I .
$$

We also have that $\Varangle C Q H=\Varangle C I H$, so

$$
\ell \text { tangent to circle } B I C \Longleftrightarrow \Varangle C I H=\Varangle C B I \Longleftrightarrow \npreceq C Q H=\Varangle C B I \Longleftrightarrow Q H \| B I \text {. }
$$

Hence, in this case $P, Q, G, H$ are concyclic if and only if $\ell$ is tangent to circle $B I C$, as claimed.

We now revert to using points $D$ and $E$ to define points $I_{B}, I_{C}, J_{B}, J_{C}$, and $X$, returning to the original set-up.\\
Claim 5. Let $\Gamma$ be the circle passing through $P$ and $Q$ that is tangent to $I P$ and $I Q$, which exists as $I P=I Q=I A$. Then $X$ lies on $\Gamma$. Furthermore, $X$ lies on the same side of $B C$ as $A$ and does not lie on line $B C$.\\
Proof. We have that

$$
\begin{aligned}
\npreceq X P I & =\Varangle J_{B} P I=\Varangle J_{B} A I=\Varangle B A I-\npreceq B A J_{B}=\Varangle J_{B} A J_{C}-\npreceq J_{B} A E \\
& =\Varangle E A J_{C}=\Varangle J_{C} A C=\Varangle J_{C} Q C=\Varangle X Q P,
\end{aligned}
$$

so circle $X P Q$ is tangent to $I P$. Similarly, circle $X P Q$ is tangent to $I Q$, so $X$ lies on $\Gamma$.\\
As $D$ lies in the interior of segment $B C, I_{C}$ lies in the interior of segment $C I$. Since $X$ is the second intersection of $P I_{C}$ with $\Gamma$ and $I P$ is tangent to $\Gamma, X$ lies in the interior of $\widetilde{P Q}$ on $\Gamma$ on the same side of $B C$ as $A$. This implies the second part of the claim.

By Claim 5, we cannot have $\ell \in\{I P, I Q\}$ in the original problem. Furthermore, as shown in Claim 2 of Solution 1, we have that $X$ lies inside triangle $I B C$, which means that $\ell \neq t$. Thus, the only remaining possibility in Claim 4 is $\ell=A I$. We then have

$$
I_{B} I_{C} J_{B} J_{C} \text { concyclic } \stackrel{\text { Claim } 3}{\Longleftrightarrow} P Q G H \text { concyclic } \stackrel{\text { Claim } 4}{\Longleftrightarrow} X \text { lies on } A I,
$$

finishing the problem.\\

---


---

### reference comment
The condition $A B<A C<B C$ is used in an essential way in the solutions. In Solution 1, it is used in the proof of Claim 3 to ensure that $X$ lies in the interior of triangle $I B C$. In Solution 2, it is used in the final step to ensure that $\angle A B C$ and $\angle B C A$ cannot be obtuse. In Solution 3, it is used to exclude the case $\ell=t$. If the condition is removed, then the problem is no longer true: whenever $\angle A B C$ or $\angle B C A$ is obtuse, there exists a choice of $D$ on $B C$ such that $I_{B} J_{B} J_{C} I_{C}$ is cyclic but $A I, I_{B} J_{C}$, and $J_{B} I_{C}$ do not concur. This counterexample configuration can be constructed using Solution 3 by letting $X$ be the intersection of $t$ with $\Gamma$ that lies on the same side of $B C$ as $A$ and constructing $I_{B}, I_{C}, J_{B}$, and $J_{C}$ as described in the solution, from which we can reconstruct $D$.

Conversely, the problem holds whenever $\angle A B C$ and $\angle B C A$ are both not obtuse, as can be seen from

---


---

### reference solution 2
This is thus the weakest possible condition on triangle $A B C$ that is necessary for the problem to be true.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-097}

When $X$ lies on the tangent to circle $I B C$ at $I$, there is no contradiction in the proof of Claim 3 in Solution 1: circles $I I_{B} J_{C}$ and $I J_{B} I_{C}$ are distinct, and $X$ is the radical centre of circles $I I_{B} J_{C}, I J_{B} I_{C}$, and $I_{B} J_{B} I_{C} J_{C}$. There is also no contradiction in the final step of Solution 2, and indeed $I_{B} I_{C}$ and $B C$ intersect at the foot of the altitude from $A$ to $B C$.

There are no configuration issues with the direction (1) $\Longrightarrow$ (2). This implication holds without any constraint on triangle $A B C$, and the proofs in Solutions 1 and 2 apply without any modification.

\section*{Number Theory}

---
