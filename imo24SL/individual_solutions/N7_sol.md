### reference solution 1
We start with a series of straightforward deductions:

\begin{itemize}
  \item From $P(1,1)$, we have $f(1)^{2}=f(1) f(f(1))^{2}$, so $f(1)=f(f(1))^{2}$.
  \item From $P(1, f(1))$, we have $f(f(1))^{2}=f(1) f(f(f(1))) f(f(f(1)))$, so $f(f(f(1)))=1$.
  \item From $P(1, f(f(1)))$, we have $f(f(f(1)))^{2}=f(1) f(f(f(f(1)))) f(f(f(f(1))))$, which simplifies to $1=f(1)^{3}$, so $f(1)=1$.
  \item From $P(1, n)$ we deduce $f(n)=f(f(n))$ for all $n$.
  \item From $P(m, 1)$ we deduce $f(m)=f\left(m^{2}\right)$ for all $m$.
  \item Simplifying $P(m, n)$, we have that
\end{itemize}

$$
f(m n)^{2}=f(m) f(n) f(m f(n))
$$

if and only if $m$ and $n$ are coprime; refer to this as $Q(m, n)$.

\begin{itemize}
  \item From $Q(m, f(n))$, we have that $f(m f(n))=f(m) f(n)$ if and only if $m$ and $f(n)$ are coprime; refer to this as $R(m, n)$.
\end{itemize}

Claim. If $f(a)=1$, then $a=1$.\\
Proof. If $a \neq 1$, then $Q(a, a)$ gives $f(a)^{2} \neq f(a)^{2} f(a f(a))$. If $f(a)=1$, then both sides simplify to 1 , a contradiction.

Claim. If $n \neq 1$ then $\operatorname{gcd}(n, f(n)) \neq 1$.\\
Proof. If $\operatorname{gcd}(n, f(n))=1$, then $Q(f(n), n)$ gives $f(n f(n))^{2}=f(n)^{3}$, and $Q(n, f(n))$ gives $f(n f(n))^{2}=f(n)^{2} f(n f(n))$, which together yield $f(n)=1$ for a contradiction.\\
Claim. For all $n$ we have $\operatorname{rad}(n) \mid f(n)$.\\
Proof. For any prime $p \mid n$, write $n=p^{v} n^{\prime}$ with $p \nmid n^{\prime}$. From $Q\left(p^{v}, n^{\prime}\right)$ we have $f(n)^{2}= f\left(p^{v}\right) f\left(n^{\prime}\right) f\left(p^{v} f\left(n^{\prime}\right)\right)$. Since $\operatorname{gcd}\left(p^{v}, f\left(p^{v}\right)\right) \neq 1$, it follows that $p \mid f\left(p^{v}\right)$, so $p \mid f(n)$, and thus $\operatorname{rad}(n) \mid f(n)$.\\
Claim. If $n$ is coprime to $f(k)$, then $f(n)$ is coprime to $f(k)$.\\
Proof. From $Q(f(k), n)$ we have $f(n f(k))^{2}=f(k) f(n) f(f(k) f(n))$; applying $R(n, k)$ to the LHS, we conclude that $f(k) f(n)=f(f(k) f(n))$. Applying $R(f(n), k)$ we deduce that $f(n)$ is coprime to $f(k)$, as required.

Claim. If $p$ is prime then $f(p)$ is a power of $p$.

Proof. Suppose otherwise. We know that $p \mid f(p)$; let $q \neq p$ be another prime with $q \mid f(p)$.\\
If, for some positive integer $N$, we have $p \nmid f(N)$, then $f(p)$ is coprime to $f(N)$, so $q \nmid f(N)$, so $q \nmid N$; thus, if $q \mid N$, then $p \mid f(N)$ (and in particular, $p \mid f(q)$, by taking $N=q$ ).

Similarly, if $q \nmid f(N)$ then $f(q)$ is coprime to $f(N)$; as $p \mid f(q)$, this means $p \nmid f(N)$, so $p \nmid N$. So if $p \mid N$, then $q \mid f(N)$.

Together with $\operatorname{rad}(n) \mid f(n)$, this means that for any $n$ not coprime to $p q$, we have $p q \mid f(n)$.\\
Let $m=\min \left\{\nu_{p}(f(x)) \mid x\right.$ is not coprime to $\left.p q\right\}$, and let $X$ be a positive integer not coprime to $p q$ such that $\nu_{p}(f(X))=m$. The argument above shows $m \geqslant 1$. We can write $f(X)= p^{m} q^{y} X^{\prime}$, where $y \geqslant 1, p \nmid X^{\prime}$ and $q \nmid X^{\prime}$. Since $f(f(X))=f(X)$ we have $f\left(p^{m} q^{y} X^{\prime}\right)=p^{m} q^{y} X^{\prime}$. Applying $Q\left(p^{m}, q^{y} X^{\prime}\right)$ gives $\left(p^{m} q^{y} X^{\prime}\right)^{2}=f\left(p^{m}\right) f\left(q^{y} X^{\prime}\right) f\left(p^{m} f\left(q^{y} X^{\prime}\right)\right)$. The RHS is divisible by $p^{3 m}$ but the LHS is only divisible by $p^{2 m}$, yielding a contradiction.

Claim. For any integer $n, \operatorname{rad}(f(n))=\operatorname{rad}(n)$.\\
Proof. We already have that $\operatorname{rad}(n) \mid f(n)$, so it remains only to show that no other primes divide $f(n)$. If $p$ is prime and $p \nmid n$, the previous Claim shows that $n$ is coprime to $f(p)$, and thus $f(n)$ is coprime to $f(p)$; that is, $p \nmid f(n)$. So exactly the same primes divide $f(n)$ as divide $n$.

It remains only to exhibit functions that show all values of $f(n)$ with $\operatorname{rad}(f(n))=\operatorname{rad}(n)$ are possible. Given $e(p) \geqslant 1$ for each prime $p$, take

$$
f(n)=\prod_{p \mid n} p^{e(p)}
$$

and we verify by examining exponents of each prime that this satisfies the conditions of the problem.

---


---

### reference comment
A quicker but less straightforward proof that $f(1)=1$ is to let $f(n)=M$ be the least value that $f$ takes; then $P(1, n)$ gives $M^{2}=f(n)^{2}=f(1) f(f(n))^{2} \geqslant M^{3}$ so $M=1$ and $f(1)=1$.

---


---

### reference solution 2
As in Solution 1, we see that there are indeed functions $f$ satisfying the given condition and producing all the given values of $f(n)$, and we follow Solution 1 to show the following facts:

\begin{itemize}
  \item $f(1)=1$.
  \item $f(m)=f\left(m^{2}\right)$ for all $m$.
  \item $f(n)=f(f(n))$ for all $n$.
  \item $f(m n)^{2}=f(m) f(n) f(m f(n))$ if and only if $m$ and $n$ are coprime; refer to this as $Q(m, n)$.
\end{itemize}

Taking $Q(m, n)$ together with $Q(n, m)$ gives that $f(m f(n))=f(n f(m))$ if $m$ and $n$ are coprime.\\
Suppose now that $m$ is coprime to both $n$ and $f(n)$. We have $f(m n)^{2}=f(m) f(n) f(m f(n))$ and squaring both sides gives

$$
\begin{aligned}
f(m n)^{4} & =f(m)^{2} f(n)^{2} f(m f(n))^{2} \\
& =f(m)^{2} f(n)^{2} f(m) f(f(n)) f(m f(f(n))) \\
& =f(m)^{3} f(n)^{3} f(m f(n))
\end{aligned}
$$

Thus $f(m f(n))=f(m) f(n)$, so $f(m n)^{2}=f(m)^{2} f(n)^{2}$, so $f(m n)=f(m) f(n)=f(m f(n))= f(n f(m))$.

If $m$ is coprime to both $n$ and $f(n)$ but however $n$ is not coprime to $f(m)$, we have

$$
\begin{aligned}
f(n f(m))^{2} & \neq f(n) f(f(m)) f(n f(f(m))) \\
& =f(n) f(m) f(n f(m)) \\
& =f(n f(m))^{2},
\end{aligned}
$$

a contradiction. Thus, given that $m$ and $n$ are coprime, we know that $m$ is coprime to $f(n)$ if and only if $n$ is coprime to $f(m)$. In particular, if $p$ and $q$ are different primes, then $p \mid f(q)$ if and only if $q \mid f(p)$, and likewise, for any positive integer $k, p \mid f\left(q^{k}\right)$ if and only if $q \mid f(p)$. More generally, if $p \nmid n$, then $p \mid f(n)$ if and only if $n$ is not coprime to $f(p)$.

Now form a graph whose vertices are the primes, and where there is an edge between primes $p \neq q$ if and only if $p \mid f(q)$ (and so $q \mid f(p)$ ); every vertex has finite degree. For any integer $n$, the primes dividing $f(n)$ are all the primes that are neighbours of any prime $q \mid n$, together possibly with some further primes $p \mid n$.

If $p$ and $q$ are different primes, we have $f(p f(q))=f(q f(p))$. The LHS is divisible by all primes that (in the graph) are neighbours of $p$ or neighbours of neighbours of $q$, and possibly also by $p$ and by some primes that are neighbours of $q$, and a corresponding statement with $p$ and $q$ swapped applies to the RHS. Thus any prime that is a neighbour of a neighbour of $q$ must be one of: $p, q$, distance 1 from $q$, or distance 1 or 2 from $p$. For any prime $r$ that is distance 2 from $q$, there are only finitely many primes $p$ that it is distance 2 or less from, so by choosing a suitable prime $p$ (depending on $q$ ) we conclude that every prime that is a neighbour of a neighbour of $q$ is actually $q$ itself or a neighbour of $q$.

So the connected components of the graph are (finite) complete graphs. If $m$ is divisible only by primes in one component, and $n$ is divisible only by primes in another component, then $f(m n)=f(m) f(n)$. If $n$ is divisible by more than one prime from a component, considering the expression for $f(m n)^{2}$ as applied with successive prime power divisors of $n$ shows that $f(n)$ is divisible by all the primes in that component. However, while $f\left(p^{k}\right)$ is divisible by all the primes in the component of $p$ except possibly for $p$ itself, we do not yet know that $p \mid f\left(p^{k}\right)$. We now consider cases for the order of a component.

For any prime $p$, we cannot have $f\left(p^{k}\right)=1$, because $Q\left(p^{k}, p^{k}\right)$ gives

$$
f\left(p^{2 k}\right)^{2} \neq f\left(p^{k}\right) f\left(p^{k}\right) f\left(p^{k} f\left(p^{k}\right)\right),
$$

and simplifying using $f\left(m^{2}\right)=f(m)$ results in $1 \neq 1$. So for a component of order $1, f\left(p^{k}\right)$ is a positive power of $p$, so has the same set of prime factors as $p$, as required.

Now consider a component of order at least 2. Since $f(f(n))=f(n)$, if the component has order at least 3 , then for any $n \neq 1$ whose prime divisors are in that component, $f(n)$ is divisible by all the primes in that component. If the component has order 2, we saw above that this is true except possibly for $n=p^{k}$. However, if the primes in the component are $p$ and $q$, and $f\left(p^{k}\right)=q^{\ell}$, then $f\left(q^{\ell}\right)=f\left(f\left(p^{k}\right)\right)=f\left(p^{k}\right)=q^{\ell}$, which contradicts $p \mid f\left(q^{\ell}\right)$. So for any component of order at least 2 , and any $n \neq 1$ whose prime divisors are in that component, $f(n)$ is divisible by all the primes in that component.

In a component of order at least 2 , let $m$ be the product of all the primes in that component, and let $t$ be maximal such that $m^{t} \mid f(n)$ for all $n \neq 1$ whose prime divisors are in that component; we have seen that $t \geqslant 1$. If $m$ and $n$ are coprime numbers greater than 1 , all of whose prime divisors are in that component, then $Q(m, n)$ tells us that $m^{3 t / 2} \mid f(m n)$. For any $n^{\prime} \neq 1$, all of whose prime divisors are in that component, $f\left(n^{\prime}\right)$ is divisible by all the primes in that component, so can be expressed as such a product, so $m^{3 t / 2} \mid f\left(f\left(n^{\prime}\right)\right)=f\left(n^{\prime}\right)$. But this means $t \geqslant 3 t / 2$, a contradiction, so all components have order 1 , and we are done.

The activities of the Problem Selection Committee were supported by the University of Cambridge

Supported by:


\end{document}
