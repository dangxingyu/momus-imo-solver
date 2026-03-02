### reference solution 1
First, observe that no polynomial is 1-good (because $Q(X)(P(X)+Q(X))$ always has roots modulo 1) and the polynomial $P(X)=1$ is not 2-good (because $Q(X)(Q(X)+1)$ is always divisible by 2 ).

Now, if $P$ is $d$-good with some $Q$, then $Q \cdot(P+Q)$ has no roots mod $d$. Therefore, it certainly has no roots mod $n$ for $d \mid n$, so $P$ must be $n$-good. Consequently, it suffices to show that all polynomials are $n$-good whenever $n$ is an odd prime, or $n=4$.

We start by handling the case $n=4$. We will construct a $Q$ such that $Q(X)$ is never divisible by 4 and $Q(X)+P(X)$ is always odd; this will clearly show that $P$ is 4-good. Note that any function modulo 2 must be either constant or linear - in other words, there are $a, b \in\{0,1\}$ such that $P(X)=a X+b \bmod 2$ for all $X$. If $a=0$ then set $Q(X)=4 X^{2}+b+1$, and if $a=1$ then set $Q(X)=X^{2}+b+1$; in all cases, $Q$ will satisfy the required properties.

It remains to prove that any polynomial is $p$-good, where $p$ is an odd prime. We will prove that for any function $f$ defined $\bmod p$, there is a quadratic $Q$ with no roots $\bmod p$ such that $Q(x) \neq f(x) \bmod p$ for all $x$; the statement about $P$ then follows with $f$ replaced by $-P$. For the remainder of the proof, we will consider all equalities modulo $p$.

Suppose that a function $f$ not satisfying the above exists; in other words, $f$ has the property that for any quadratic $Q$ with no roots $\bmod p$, there is some $x$ such that $Q(x)=f(x)$. Without loss of generality, we may assume that $f$ has no roots $\bmod p$. To see why, suppose that $f(u)=0$ for some $u$, and let $g$ be the function such that $g(x)=f(x)$ for $x \neq u$ and $g(u)=1$. For any $Q$ with no roots, we know that there is some $x \neq u$ such that $P(x)=f(x)$, and so $P(x)=g(x)$ for that choice of $x$. In particular, $g$ is also not $p$-good.

Now, suppose first that there is some nonzero $t$ such that $t$ is not in the image of $f$. Then we may take $Q(X)=p X^{2}+t$; this quadratic is never equal to $f$ and is never zero. Thus, $f$ must be surjective onto the nonzero residues mod $p$. There are $p$ choices for $X$ and $p-1$ nonzero residues $\bmod p$, so there must be some $x_{1} \neq x_{2} \bmod p$ such that $f\left(x_{1}\right)=f\left(x_{2}\right)$, and $f$ is a bijection from the set of residues $\bmod p$ not equal to $x_{2}$ to the set of nonzero residues $\bmod p$.

Now, note that we may choose any $b$ and $c$ with $b$ nonzero and replace $f(X)$ with $g(X)= f(b X+c)$; if there were some $Q$ with no roots such that $Q(x) \neq g(x)$ for all $x$, then $Q(X / b-c / b)$ would work for $f$. Choose $b$ and $c$ such that $b x_{1}+c=1$ and $b x_{2}+c=-1$; such $b$ and $c$ must exist (we may take $b=2 /\left(x_{1}-x_{2}\right)$ and $c=\left(x_{1}+x_{2}\right) /\left(x_{2}-x_{1}\right)$ ). Renaming $g$ to $f$, we see that we may assume $f(1)=f(-1)$.

Let $r^{\prime}$ be a quadratic nonresidue $\bmod p$. Choose $y \neq 0$ such that $f(y)=\left(1-r^{\prime}\right) f(0)$, which must exist as the right hand side is nonzero and $1-r^{\prime}$ is not equal to 1 . Choose $r=y^{2} / r^{\prime}$, which is a quadratic nonresidue.

Consider $\phi(X)=f(X) /\left(X^{2}-r\right)$. By definition, $\phi(1)=\phi(-1)$ and $\phi(0)=\phi(y)$, so there are no more than $p-2$ values in the image of $\phi$. Choose some nonzero $a$ not in the image of $\phi$, so $f(X) /\left(X^{2}-r\right)$ is never equal to $a$. The quadratic $Q(X)=a\left(X^{2}-r\right)$ is never zero and also never equal to $f(X)$, which completes the proof.

---


---

### reference comment
In fact, there is no need to pass from polynomials $P$ to functions $f$, as any function mod $p$ is a polynomial. Concretely, instead of passing from $f$ to $g$, we would have instead replaced $P(X)$ with $P(X)+1-(X-u)^{p-1}$, which is a polynomial that is unchanged except at $X=u$.

---


---

### reference solution 2
Given $f$ a function mod $p$ such that $f$ is surjective onto the nonzero elements of $\mathbb{Z} / p \mathbb{Z}$ and $f(1)=f(-1)$, we provide an alternative approach to construct a nonzero quadratic $Q(X)$ such that $Q(X) \neq f(X)$. Let $r$ be the smallest quadratic nonresidue mod $p$ (so $r-1$ is a square) and let $a$ vary over the nonzero elements mod $p$; we will show that it is possible to choose $Q_{a}(X)=a\left(X^{2}-r\right)$ for some choice of $a$. Note that any quadratic of this form will be nowhere zero.

Suppose that no such $Q_{a}$ works. Then, for each $a$, there exists $x$ such that $a\left(x^{2}-r\right)=f(x)$. We may assume that $x \neq-1$, as if the equality holds for $x=-1$ then it also holds for $x=1$. However, $a\left(x^{2}-r\right)=f(x)$ implies $a=f(x) /\left(x^{2}-r\right)$, so $f(x) /\left(x^{2}-r\right)$ must be a surjection from $\{x \neq-1\}$ to the set of nonzero $a$, and so this is a bijection. In particular, for each $a$, there exists a unique $x_{a}$ such that $f\left(x_{a}\right)=a\left(x_{a}^{2}-r\right)$.

We now have

$$
\begin{aligned}
\prod_{t \neq 0} t & =\prod_{a \neq 0} f\left(x_{a}\right) \\
& =\prod_{a \neq 0} a \prod_{a \neq 0}\left(x_{a}^{2}-r\right) \\
& =\prod_{a \neq 0} a \prod_{x \neq-1}\left(x^{2}-r\right)
\end{aligned}
$$

where the first equality follows because $f$ is surjective onto the nonzero residues mod $p$, and the second equality follows from the definition of $x_{a}$. The two products cancel, which means that $\prod_{x \neq-1}\left(x^{2}-r\right)=1$.

However, we also get

$$
\prod_{x \neq-1}\left(x^{2}-r\right)=(-r)(1-r)\left(\prod_{x=2}^{(p-1) / 2}\left(x^{2}-r\right)\right)^{2}
$$

However, this is a contradiction as $-r(1-r)=r(r-1)$, which is not a quadratic residue (by our choice of $r$ ).

---


---

### reference comment
By Wilson's theorem, we know that the product of the nonzero elements mod $p$ is -1 ; however, this fact was not necessary for the solution so we chose to present the solution without needing to state it.

---


---

### reference comment
One can in fact show that

$$
\prod_{x \neq-1}\left(x^{2}-r\right)=\frac{-4 r}{1-r}
$$

To do this, note that the polynomial $X^{\frac{p-1}{2}}-1$ has the $\frac{p-1}{2}$ quadratic residues as roots, so we have

$$
\prod_{s \text { quad. res. }}(X-s)=X^{\frac{p-1}{2}}-1
$$

and so

$$
\prod_{x \neq 0}\left(X-x^{2}\right)=\left(X^{\frac{p-1}{2}}-1\right)^{2}
$$

Since $r$ is a quadratic nonresidue, by Euler's criterion $r^{\frac{p-1}{2}}=-1$, and the result follows.\\
Therefore, one can replace the condition that $r$ is the smallest quadratic nonresidue with the condition that $r$ is a quadratic nonresidue not equal to $-\frac{1}{3}$ (which is possible for all $p \geqslant 3$ ).

---


---

### reference solution 3
As in Solution 1, we will reduce to the case of $p$ being an odd prime and $f$ being a function $\bmod p$ with no roots which is surjective onto the set of nonzero residues $\bmod p$, although we make no assumption about the values of $x_{1}$ and $x_{2}$ with $f\left(x_{1}\right)=f\left(x_{2}\right)$.

We will again consider quadratics of the form $Q_{a, b, c}(X)=a R(b X+c)$, where $R(X)=X^{2}-r$ for an arbitrary fixed quadratic nonresidue $r, a$ and $b$ are nonzero $\bmod p$, and $c$ is any residue $\bmod p$.

For each fixed $b$ and $c$, there must be $n$ pairs ( $a, x$ ) such that $a R(b x+c)=f(x)$, because there must be exactly one value of $a$ for each $x$. If any $a$ appears in no such pair then we are done, so assume otherwise. In other words, there must be exactly one $a$ such that there are two such $x$, and for all other $a$ there is only one such $x$.

Thus, for each ( $b, c$ ), there is exactly one unordered pair $\left\{x_{1}, x_{2}\right\}$ such that for some $a$ we have $f\left(x_{i}\right)=a R\left(b x_{i}+c\right)$; in other words, there is exactly one unordered pair $\left\{x_{1}, x_{2}\right\}$ such that $f\left(x_{1}\right) / R\left(b x_{1}+c\right)=f\left(x_{2}\right) / R\left(b x_{2}+c\right)$.

Now, we show that for each unordered pair $\left\{x_{1}, x_{2}\right\}$ there must be at least one pair ( $b, c$ ) such that $f\left(x_{1}\right) / R\left(b x_{1}+c\right)=f\left(x_{2}\right) / R\left(b x_{2}+c\right)$. Indeed, let $t=f\left(x_{1}\right) / f\left(x_{2}\right)$. There must be some $x_{1}^{\prime}, x_{2}^{\prime}$ such that $R\left(x_{1}^{\prime}\right) / R\left(x_{2}^{\prime}\right)=t$; this is because $R(X)$ and $t R(X)$ both take $\frac{p+1}{2}$ nonzero values $\bmod p$, so the intersection must be nonempty by the pigeonhole principle. Choosing $b$ and $c$ such that $b x_{1}+c=x_{1}^{\prime}$ and $b x_{2}+c=x_{2}^{\prime}$ gives the claim.

Note further that if $(b, c)$ and $\left\{x_{1}, x_{2}\right\}$ satisfy the relation, then the same is true for $(-b,-c)$ and $\left\{x_{1}, x_{2}\right\}$ because $R(b x+c)=R(-b x-c)$. Since $b$ is nonzero, this means that each pair $\left\{x_{1}, x_{2}\right\}$ corresponds to at least two pairs ( $b, c$ ). However, since there are $p(p-1)$ pairs ( $b, c$ ) with $b$ nonzero and $p(p-1) / 2$ unordered pairs $\left\{x_{1}, x_{2}\right\}$, each $\left\{x_{1}, x_{2}\right\}$ must correspond to exactly two pairs ( $b, c$ ) and ( $-b,-c$ ) for some ( $b, c$ ).

Now, since the image of $f$ has only $p-1$ elements, there must be some $x_{1}, x_{2}$ such that $f\left(x_{1}\right)=f\left(x_{2}\right)$. Choose any $b, c$ such that $b x_{1}+c=-\left(b x_{2}+c\right)$, so $R\left(b x_{1}+c\right)=R\left(b x_{2}+c\right)$ and so $f\left(x_{1}\right) / R\left(b x_{1}+c\right)=f\left(x_{2}\right) / R\left(b x_{2}+c\right)$. There is such a pair $b, c$ for any nonzero $b$, so there are at least $p-1$ such pairs, and this quantity is greater than 2 for $p \geqslant 5$.

Finally, for the special case that $p=3$, we observe that there must be at least one allowed value for $Q(x)$ for each $x$, so there must exist such a quadratic $Q$ by Lagrange interpolation.

---


---

### reference comment
We may also handle the case $p=3$ as follows. Recall that we may assume $f$ is nonzero and surjective onto $\{1,2\} \bmod 3$, so the image of $f$ must be $(1,1,2)$ or $(1,2,2)$ in some order. Without loss of generality $f(1)=f(2)$, so we either have $(f(0), f(1), f(2))=(1,2,2)$ or $(2,1,1)$. In the first case, take $Q(X)=2 X^{2}+2$, and in the second case take $Q(X)=X^{2}+1$.

In some sense, this is equivalent to the Lagrange interpolation approach, as in each case the polynomial $Q(X)$ can be determined by Lagrange interpolation.

---


---

### reference solution 4
Again, we reduce to the case of $p$ being an odd prime and $f$ being a function $\bmod p$; we will show that there is a quadratic which is nowhere zero such that $Q(x)=f(x)$ has no root. We can handle the case of $p=3$ separately as in Solution 3, so assume that $p \geqslant 5$.

We will prove the following more general statement: let $p \geqslant 5$ be a prime and let $\mathcal{A}_{1}, \mathcal{A}_{2}$, $\ldots, \mathcal{A}_{p}$ be subsets of $\mathbb{Z} / p \mathbb{Z}$ with $\left|\mathcal{A}_{i}\right|=2$ for all $i$. Then there exists a polynomial $Q \in \mathbb{Z} / p \mathbb{Z}[X]$ of degree at most 2 such that $Q(i) \notin \mathcal{A}_{i}$ for all $i$. Indeed, applying this statement to the sets $\mathcal{A}_{i}=\{0, f(i)\}$ (and adding $p X^{2}$ if necessary) produces a quadratic $Q$ satisfying the desired property.

Choose the coefficients of $Q$ uniformly at random from $\mathbb{Z} / p \mathbb{Z}$, and let $T$ be the random variable denoting the number of $i$ for which $Q(i) \in \mathcal{A}_{i}$. Observe that for $k \leqslant 3$, we have

$$
\mathbb{E}\left[\binom{T}{k}\right]=2^{k}\binom{p}{k} p^{-k} .
$$

To see why, let $k \leqslant 3$. If $\mathcal{S} \subseteq \mathbb{Z} / p \mathbb{Z}$ has size $k$ and $\left(a_{i}\right)_{i \in \mathcal{S}}$ is a $k$-tuple, the probability that $Q(i)=a_{i}$ on $\mathcal{S}$ is equal to $p^{-k}$; for $k=3$ this follows by Lagrange interpolation, and for $k<3$\\
it follows from the $k=3$ case by summing. The expectation is therefore equal to the number of $\mathcal{S} \subseteq \mathbb{Z} / p \mathbb{Z}$ of size $k$ times the probability that $Q(i) \in \mathcal{A}_{i}$ for each $i \in \mathcal{S}$, which is equal to the right hand side as each $\mathcal{A}_{i}$ has size 2 .

Now, observe that we have the identity $(t-1)(t-3)(t-4)=-12+12\binom{t}{1}-10\binom{t}{2}+6\binom{t}{3}$, so

$$
\begin{aligned}
\mathbb{E}[(T-1)(T-3)(T-4)] & =-12+12 \mathbb{E}\left[\binom{T}{1}\right]-10 \mathbb{E}\left[\binom{T}{2}\right]+6 \mathbb{E}\left[\binom{T}{3}\right] \\
& =-12+12 \cdot 2-10 \cdot 2\left(1-\frac{1}{p}\right)+6 \cdot \frac{4}{3}\left(1-\frac{1}{p}\right)\left(1-\frac{2}{p}\right) \\
& =-\frac{4}{p}+\frac{16}{p^{2}}
\end{aligned}
$$

This is negative for $p \geqslant 5$. Because $(t-1)(t-3)(t-4) \geqslant 0$ for all integers $t>0$, it then follows that $T=0$ with positive probability, which implies that there must exist some $Q$ with $Q(i) \notin \mathcal{A}_{i}$ for all $i$, as desired.

---


---

### reference comment
We do not have much freedom to choose a different polynomial in place of $R(T)= (T-1)(T-3)(T-4)$ in this argument. Indeed, it can be shown (by comparing coefficients of $\binom{T}{K}$ ) that if $R$ has degree at most 3 , then the expected value of $R(T)$ tends to $\frac{1}{3}(R(4)+2 R(1))$ as $p$ tends to infinity, so $R$ must have both 1 and 4 as roots. In particular, $R$ must be of the form $R(T)=(T-1)(T-4)(T-d)$ for some $d \geqslant 3$, and if $d<4$ then the argument works for any $p$ with $p>4 /(4-d)$.

---
