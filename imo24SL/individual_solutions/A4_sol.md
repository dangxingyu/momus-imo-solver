### reference solution 1
Clearly $\mathcal{S}$ must be nonempty. We start with constructions when $1 \leqslant|\mathcal{S}| \leqslant 2$.

\begin{itemize}
  \item If $\mathcal{S}=\left\{2^{k}\right\}$, then take $f(x)=c x-2^{k}$ for any integer $c>2^{k}$.
  \item If $\mathcal{S}=\left\{2^{k}, 2^{\ell}\right\}$ where $k>\ell$, then take $f(x)=\left(2^{k}-2^{\ell}\right)\lfloor\alpha x\rfloor-2^{\ell}$, where $\alpha>2$ is not an integer. This works because $\lfloor\alpha(x+y)\rfloor-(\lfloor\alpha x\rfloor+\lfloor\alpha y\rfloor) \in\{0,1\}$ for all $x$ and $y$, and takes both values; the lower bound on $\alpha$ ensures the values of $f$ are positive.
\end{itemize}

Observe that, inductively,

$$
f(n)=2^{e(1,1)}+2^{e(2,1)}+\cdots+2^{e(n-1,1)}+n f(1) .
$$

Lemma 1. For any positive integers $n$ and $k$,

$$
\{e(1,1), e(2,1), \ldots, e(k-1,1)\} \subset\{e(n, 1), e(n+1,1), \ldots, e(n+k-1,1)\} .
$$

Proof. We work by induction on $k$; in the case $k=1$, the first multiset is empty, which provides our base case.

For the induction step, suppose $k \geqslant 2$ and we know that

$$
\{e(1,1), e(2,1), \ldots, e(k-2,1)\} \subset\{e(n, 1), e(n+1,1), \ldots, e(n+k-2,1)\} .
$$

By definition, $f(n+k)-f(n)-f(k)=2^{e(n, k)}$, and using the first observation we see that\\
$f(n+k)-f(n)-f(k)=\left(2^{e(n, 1)}+2^{e(n+1,1)}+\cdots 2^{e(n+k-1,1)}\right)-\left(2^{e(1,1)}+2^{e(2,1)}+\cdots+2^{e(k-1,1)}\right)$.\\
From the induction hypothesis, we may write

$$
\{e(n, 1), e(n+1,1), \ldots, e(n+k-2,1)\}=\{e(1,1), e(2,1), \ldots, e(k-2,1)\} \cup\{a\}
$$

for some $a$. Thus

$$
2^{e(n, k)}=2^{a}+2^{e(n+k-1,1)}-2^{e(k-1,1)} .
$$

So $\{e(n, k), e(k-1,1)\}=\{a, e(n+k-1,1)\}$. Thus $e(k-1,1)=a$ or $e(k-1,1)=e(n+k-1,1)$, and in either case we have our result.

Lemma 2. The sequence $e(1,1), e(2,1), e(3,1), \ldots$ takes at most two different values.

Proof. Suppose for a contradiction that $k \geqslant 2$ is the least index with $e(k, 1) \neq e(1,1)$, and that some $\ell>k$ has $e(\ell, 1) \notin\{e(k, 1), e(1,1)\}$. By Lemma 1 , any block of $k$ consecutive values of the sequence has at least $k-1$ values equal to $e(1,1)$. This forces

$$
e(\ell-1,1)=e(\ell-2,1)=\cdots=e(\ell-(k-1), 1)=e(1,1)
$$

and

$$
e(\ell+1,1)=e(\ell+2,1)=\cdots=e(\ell+(k-1), 1)=e(1,1) .
$$

But then the block $e(\ell-1,1), e(\ell, 1), e(\ell+1,1), e(\ell+2,1), \ldots, e(\ell+(k-1), 1)$ has length $k+1$ and does not contain $e(k, 1)$, a contradiction.

Finally, for any $a$ and $b$ we have

$$
\begin{aligned}
f(a+b)-f(a)-f(b) & =\left(2^{e(a, 1)}+2^{e(a+1,1)}+\cdots 2^{e(a+b-1,1)}\right)-\left(2^{e(1,1)}+2^{e(2,1)}+\cdots+2^{e(b-1,1)}\right) \\
& =2^{e(i, 1)}
\end{aligned}
$$

for some $a \leqslant i \leqslant a+b-1$. So $|\mathcal{S}| \leqslant 2$.\\

---


---

### reference comment
In the construction of functions, $\alpha>2$ is only necessary if $k=\ell+1$, to make sure $f(1) \neq 0$. Otherwise, any nonintegral $\alpha>1$ suffices.

---


---

### reference solution 2
Subsets of size 1 or 2 can be achieved as in Solution 1, and $\mathcal{S}$ must be nonempty. We consider such a set $\mathcal{S}$ with $|\mathcal{S}| \geqslant 3$ and a corresponding function $f$ in order to achieve a contradiction. We will relate the $e(a, b)$ to values of $e(c, 1)$ with $c+1<a+b$, leading to a proof of Lemma 2 from Solution 1 that does not depend on Lemma 1 from that solution.

Suppose $a>1$. We have $f(a+b)-f(a)-f(b)=2^{e(a, b)}$ and also $f(a)-f(a-1)-f(1)= 2^{e(a-1,1)}$, so

$$
f(a+b)-f(a-1)-f(1)-f(b)=2^{e(a, b)}+2^{e(a-1,1)}
$$

Similarly, $f(a+b)-f(a-1)-f(b+1)=2^{e(a-1, b+1)}$ and $f(b+1)-f(1)-f(b)=2^{e(b, 1)}$, so

$$
f(a+b)-f(a-1)-f(1)-f(b)=2^{e(a-1, b+1)}+2^{e(b, 1)} .
$$

Thus either

$$
e(a, b)=e(a-1, b+1) \quad \text { and } \quad e(a-1,1)=e(b, 1)
$$

or

$$
e(a, b)=e(b, 1) \quad \text { and } \quad e(a-1, b+1)=e(a-1,1) .
$$

For $n \geqslant 4$, we consider these possibilities as ( $a, b$ ) ranges over all pairs with $a+b=n$. If the first case holds for every such pair (that is, if $e(c, 1)=e(d, 1)$ for all $c+d=n-1)$, then all the $e(a, b)$ for $a+b=n$ are equal (and the above equations do not constrain whether or not the value is the same as any $e(c, 1)$ with $c+1<n$ ). Otherwise, the values of $e(a, b)$ with $a+b=n$ are fully determined by the values of $e(c, 1)$ for which $e(c, 1) \neq e(n-1-c, 1)$, and are not all equal.

Specifically, if $e(c, 1)=j$ and $e(n-1-c, 1)=k$ with $j \neq k$, we have $e(c, n-c)=j=e(n-c, c)$ and $e(c+1, n-c-1)=k=e(n-c-1, c+1)$. Every other value of $e(a, b)$ with $a+b=n$ is then determined by the rule that $e(a, b)=e(a-1, b+1)$ if $e(a-1,1)=e(b, 1)$ : if we have $e(c, 1) \neq e(n-1-c, 1)$, and $e\left(c^{\prime}, 1\right) \neq e\left(n-1-c^{\prime}, 1\right)$, but $e(d, 1)=e(n-1-d, 1)$ for all $c<d<c^{\prime}$, then if $c<c^{\prime}-1$ we have $e\left(c^{\prime}-1, n-\left(c^{\prime}-1\right)\right)=e\left(c^{\prime}, n-c^{\prime}\right)$, then if $c<c^{\prime}-2$ we have $e\left(c^{\prime}-2, n-\left(c^{\prime}-2\right)\right)=e\left(c^{\prime}-1, n-\left(c^{\prime}-1\right)\right)=e\left(c^{\prime}, n-c^{\prime}\right)$, and so on until $e(c+1, n-c-1)=e\left(c^{\prime}, n-c^{\prime}\right)$ (yielding a contradiction if $e(n-c-1,1) \neq e\left(c^{\prime}, 1\right)$; such a contradiction also arises trivially if $c+1=c^{\prime}$ and $e(n-c-1,1) \neq e\left(c^{\prime}, 1\right)$ ). If $c$ is the least integer such that $e(c, 1) \neq e(n-1-c, 1)$, the values of $e(a, b)$ with $a<c$ are similarly determined to be equal to $e(c, n-c)$ (and likewise for $a>n-c$ ).

In other words, if we list the values in ascending order of $a$ from 1 to $n-1$, any gaps between the pairs of adjacent values determined when $e(c, 1) \neq e(n-1-c, 1)$ are filled with copies of the previously determined adjacent values, and if the values on either side of such a gap are different, we have a contradiction (including in the degenerate cases where the pairs are adjacent or overlap, if $c+1=c^{\prime}$ ). Note in particular that every value of $e(a, b)$ is a value of $e(c, 1)$ for some $c$ with $c+1 \leqslant a+b$.

If $|\mathcal{S}| \geqslant 3$, that means that $e(c, 1)$ takes at least three different values. Let $m$ be such that $e(m, 1)$ does not equal any $e(c, 1)$ for $c<m$, and there are exactly two different values of $e(c, 1)$ for $c<m$ (and thus $m \geqslant 3$ ).

Because $e(m, 1)$ does not equal any $e(c, 1)$ for $c<m$, we have that all $e(a, b)$ for $a+b=m+1$ are equal, and $e(c, 1)=e(d, 1)$ for all $c+d=m$. We now consider the values of $e(a, b)$ for $a+b=m+2$ determined by the above rules. Since $e(m, 1) \neq e(1,1)$, we have $e(1, m+1)=e(1,1)$ and $e(2, m)=e(m, 1)$. If there were any other $e(d, 1) \neq e(m+1-d, 1)$, consider the one with minimal $d>1$; because $e(m, 1) \neq e(d, 1)$, we arrive at a contradiction. So every $e(c, 1)=e(d, 1)$ for $c+d=m+1$ except for $e(m, 1) \neq e(1,1)$. But these equalities form a path connecting all $e(c, 1)$ for $c<m$ :

$$
e(1,1)=e(m-1,1)=e(2,1)=e(m-2,1)=e(3,1)=\cdots
$$

which contradicts the assumption we made that there were exactly two different values of $e(c, 1)$ for $c<m$.

---


---

### reference solution 3
Constructions for $1 \leqslant|\mathcal{S}| \leqslant 2$ are shown in Solution 1, and $\mathcal{S}$ must be nonempty. We suppose $|\mathcal{S}| \geqslant 3$ to derive a contradiction.\\
Claim 1. $e(a, b), e(b, c)$, and $e(a, c)$ can take at most two different values.\\
Proof. By expanding $f(a+b+c)$ in three different ways, we get

$$
2^{e(a, b)}+2^{e(c, a+b)}=2^{e(b, c)}+2^{e(a, b+c)}=2^{e(a, c)}+2^{e(b, a+c)}
$$

The result follows from the equality of the three multisets of exponents.\\
For Claims 2 to 4 , we fix $k$ and let $N$ be the smallest integer such that $e(a, N-a+1)=k$ for some $a \leqslant N$.\\
Claim 2. For any $b$ with $b \leqslant N$, we must have $e(b, N-b+1)=k$.\\
Proof. Suppose that $e(a, N-a+1)=k$ and $a<b$. Expanding $f(a+(b-a)+N-b+1)$ in two different ways, we see that

$$
2^{e(a, b-a)}+2^{e(b, N-b+1)}=2^{e(N-b+1, b-a)}+2^{e(N-a+1, a)} .
$$

By the minimality of $N$, we must have $e(b, N-b+1)=e(N-a+1, a)$. The case of $a>b$ follows by replacing $a$ and $b$ with $N-a+1$ and $N-b+1$.\\
Claim 3. $e(a, 1)=e(N-a+1,1)$ for any $a$ satisfying $1<a<N$.\\
Proof. By Claim 2, $e(a, N-a+1)=k$. Then by Claim 1, $e(a, N-a+1), e(a, 1)$, and $e(N-a+1,1)$ can take at most two different values. But by the minimality of $N$, we must have $e(a, N-a+1) \neq e(a, 1)=e(N-a+1,1)$.\\
Claim 4. $e(a, 1)=e(N-a, 1)$ for any $a$ satisfying $1 \leqslant a<N$.\\
Proof. By Claim 2, $e(a, N-a+1)=e(a+1, N-a)=k$. Expanding $f(1+a+(N-a))$ in two different ways, we see that

$$
2^{e(1, a)}+2^{e(a+1, N-a)}=2^{e(1, N-a)}+2^{e(N-a+1, a)} .
$$

Therefore $e(1, a)=e(1, N-a)$, as required.\\
If $|\mathcal{S}| \geqslant 3$, then there exist $1<N_{k}<N_{\ell}$ where $N_{k}$ and $N_{\ell}$ are the minimal values corresponding to $k$ and $\ell$. But Claims 3 and 4 imply that $e(a, 1)$ is constant for all $1 \leqslant a<N_{\ell}$, which is a contradiction.

---
