### reference solution 1
Without loss of generality, we may divide all elements of $\mathcal{S}$ by any common factor, after which they cannot all be even. As $a \nmid b+2 c$ for $a$ even and $b$ odd, the elements of $\mathcal{S}$ are all odd.

We now divide into three cases:\\
Case 1: $|\mathcal{S}|=1$.\\
The set $\mathcal{S}=\{t\}$ clearly works.\\
Case 2: $|\mathcal{S}|=2$.\\
Say $\mathcal{S}=\{r, s\}$ with $r<s$, so either $s \mid r+2 r$ or $s \mid r+2 s$, and in either case $s \mid 3 r$. We cannot have $s=3 r / 2$ as we assumed that $r$ is odd, so $s=3 r$ and $\mathcal{S}=\{r, 3 r\}$, which clearly works by examining cases for $a$ and $b$.\\
Case 3: $|\mathcal{S}| \geqslant 3$.\\
If all elements of $\mathcal{S}$ are odd then for any $b, c \in \mathcal{S}, b+2 c \not \equiv b(\bmod 4)$. If $a \mid b+2 c$ with $a \equiv b(\bmod 4)$, this means there exists $k$ with $b+2 c=k a$ and $k \equiv 3(\bmod 4)$, so $k \geqslant 3$. If $a$ is the greatest element of $\mathcal{S}$ and $b<a$, we have $b+2 c<3 a$, a contradiction. Thus when $a$ is the greatest element, no $b<a$ has $b \equiv a(\bmod 4)$ (and thus all elements other than the greatest are congruent modulo 4).

Let $d$ and $e$ be the largest and second largest element of $\mathcal{S}$ respectively. Let $f \neq d, e$ be any other element of $\mathcal{S}$. There is some $c \in \mathcal{S}$ with $e \mid f+2 c$, and $e \not \equiv f+2 c(\bmod 4)$, so $f+2 c \geqslant 3 e$, so $c>e$. Since $e$ is the second largest element of $\mathcal{S}, c=d$, so $e \mid f+2 d$, and this holds for all $f \in \mathcal{S}$ with $f<e$, but can only hold for at most one such $f$. So $|\mathcal{S}| \leqslant 3$.

Hence the elements of $\mathcal{S}$ are $d>e>f$, and by the discussion above without loss of generality we may suppose these elements are all odd, $e \equiv f(\bmod 4)$ and $d \not \equiv e(\bmod 4)$. We have above that $e \mid f+2 d$. Furthermore, there exists some $c \in \mathcal{S}$ with $d \mid f+2 c$, and $c \neq d$ as $d>f$ so $d \nmid f$, so $c \leqslant e$; as $f+2 e<3 e$, we have $e>d / 3$. Since $f+2 c$ is odd and $f+2 c<3 d$, we have $f+2 c=d$.\\
Subcase 3.1: $c=f$.\\
Here $d=3 f$ and $e \mid f+2 d=7 f$. As $e>f$ and $e \equiv f(\bmod 4)$, we have $e=7 f / 3$ and the elements are some multiples of $\{3,7,9\}$. But $a=7$ and $b=9$ have no corresponding value of $c$.

Subcase 3.2: $c=e$.\\
Here $d=f+2 e$ and $e \mid f+2 d=3 f+4 e$ so $e \mid 3 f$. But this is not possible with $e>f$ and $e \equiv f(\bmod 4)$.

---


---

### reference solution 2
As in Solution 1, we reduce to the case where all elements of $\mathcal{S}$ are odd. Since all one-element sets satisfy the given conditions, we show that if $|\mathcal{S}| \geqslant 2$, then $|\mathcal{S}|=2$ and $\mathcal{S}=\{t, 3 t\}$ for some positive integer $t$.

Let $d$ be the largest element. For any $e \in \mathcal{S}$ with $e \neq d$ there must be a $f \in \mathcal{S}$ such that $d \mid e+2 f$. This implies $2 f \equiv-e(\bmod d)$, hence $2 f \equiv d-e(\bmod d)$. Now $d-e$ is even (because all elements in $\mathcal{S}$ are odd) and $d$ is odd, so $\frac{d-e}{2}$ is an integer and we have $f \equiv \frac{d-e}{2} (\bmod d)$. Further, $0<\frac{d-e}{2}<d$, while we must also have $0<f \leqslant d$, so $f=\frac{d-e}{2}$. We conclude that for any $e \in \mathcal{S}$ with $e \neq d$ the integer $\frac{d-e}{2}$ is also in $\mathcal{S}$ and not equal to $d$.

Denote by $e_{1}<e_{2}<\cdots<e_{k}<d$ the elements of $\mathcal{S}$, where $k \geqslant 1$. Then $\frac{d-e_{1}}{2}>\frac{d-e_{2}}{2}> \cdots>\frac{d-e_{k}}{2}$ are also elements of $\mathcal{S}$, none of them equal to $d$. Hence we must have $e_{1}=\frac{d-e_{k}}{2}$ and\\
$e_{k}=\frac{d-e_{1}}{2}$, so $2 e_{1}+e_{k}=d=2 e_{k}+e_{1}$. We conclude $e_{1}=e_{k}$, so $k=1$, and also $d=2 e_{k}+e_{1}=3 e_{1}$. Hence $\mathcal{S}=\left\{e_{1}, 3 e_{1}\right\}$ for some positive integer $e_{1}$.

---


---

### reference solution 3
As in Solution 1, we reduce to the case where all elements of $\mathcal{S}$ are odd. Since all one-element sets satisfy the given conditions, we show that if $|\mathcal{S}| \geqslant 2$, then $|\mathcal{S}|=2$ and $\mathcal{S}=\{t, 3 t\}$ for some positive integer $t$.

Let $d$ be the largest element, and let $e \in \mathcal{S}$ be any other element. We will say that $x \in \mathcal{S} (\bmod d)$ if the unique element $y$ in $\{1, \ldots, d\}$ such that $x \equiv y(\bmod d)$ is an element of $\mathcal{S}$. Note that by the choice of $d$ being the largest element, if $x \neq d$, then $x \not \equiv 0(\bmod d)$. The given condition implies that if $b \in \mathcal{S}$, then $-\frac{b}{2} \in \mathcal{S}(\bmod d)$. Repeating this gives $-\frac{b}{2} \in \mathcal{S} \Rightarrow \frac{b}{4} \in \mathcal{S} (\bmod d)$, and by iterating, we have $b \in \mathcal{S} \Rightarrow \frac{b}{(-2)^{k}} \in \mathcal{S}(\bmod d)$ for all $k$. Since $d$ is odd, there is some $g$ such that $(-2)^{g} \equiv 1(\bmod d)$, so by setting $k=g-1$, we get that

$$
\text { for all } d \neq e \in \mathcal{S},-2 e \in \mathcal{S} \quad(\bmod d) \text {. }
$$

Now, if $e>\frac{d}{2}$, then $-2 e \in \mathcal{S}(\bmod d)$ and $d-2 e<0$, so $2 d-2 e \in \mathcal{S}$, contradicting the lack of even elements. Then $e<\frac{d}{2}$ for any $e \in \mathcal{S} \backslash\{d\}$, so we have $e \in \mathcal{S} \Rightarrow d-2 e \in \mathcal{S}$. Since $d-2 e \neq d$, we must have $d-2 e<\frac{d}{2}$, which rearranges to $e>\frac{d}{4}$.

Let $\lambda \in(0,1)$ be a positive real number and suppose we have proved that $e>\lambda d$ for any $e \in \mathcal{S} \backslash\{d\}$. Then $d-2 e>\lambda d$, which rearranges to $e<\frac{(1-\lambda) d}{2}$. Then $d-2 e<\frac{(1-\lambda) d}{2}$, which rearranges to $e>\frac{(1+\lambda) d}{4}$. Defining $\lambda_{0}=\frac{1}{4}$ and $\lambda_{i}=\frac{1+\lambda_{i-1}}{4}$ for $i \geqslant 1$, we have shown that for all $e \in \mathcal{S} \backslash\{d\}$ and all $\lambda_{i}, e>\lambda_{i} d$. Now note that the sequence $\lambda_{i}$ is increasing and bounded above by $\frac{1}{3}$, so it converges to some limit $\ell$, which satisfies $\ell=\frac{1+\ell}{4}$, so $\ell=\frac{1}{3}$. Hence $e \geqslant \frac{d}{3}$, but then $d-2 e \geqslant \frac{d}{3}$ implies $e \leqslant \frac{d}{3}$, so $e$ must be $\frac{d}{3}$, and we are done.

---


---

### reference comment
We can finish Solution 3 alternatively as follows: after showing that if $e \in \mathcal{S} \backslash\{d\}$ then $d-2 e \in \mathcal{S} \backslash\{d\}$, note that

$$
(d-2 e)-\frac{d}{3}=\frac{2 d}{3}-2 e=-2\left(e-\frac{d}{3}\right)
$$

So consider $e \in \mathcal{S} \backslash\{d\}$ maximising $\left|e-\frac{d}{3}\right|$. If $e \neq \frac{d}{3}$, them the above shows that $\left|(d-2 e)-\frac{d}{3}\right|>\left|e-\frac{d}{3}\right|$, which is a contradiction. Thus $\mathcal{S} \backslash\{d\}$ is empty or equal to $\left\{\frac{d}{3}\right\}$, which completes the proof.

---
