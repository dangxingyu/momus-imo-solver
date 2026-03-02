### reference solution 1
It is clear that we may take $g=2$ for $(a, b)=(1,1)$. Supposing that $(a, b)$ satisfies the conditions in the problem, let $N$ be a positive integer such that $\operatorname{gcd}\left(a^{n}+b, b^{n}+a\right)=g$ for all $n \geqslant N$.\\
Lemma. We have that $g=\operatorname{gcd}(a, b)$ or $g=2 \operatorname{gcd}(a, b)$.\\
Proof. Note that both $a^{N}+b$ and $a^{N+1}+b$ are divisible by $g$. Hence

$$
a\left(a^{N}+b\right)-\left(a^{N+1}+b\right)=a b-b=a(b-1)
$$

is divisible by $g$. Analogously, $b(a-1)$ is divisible by $g$. Their difference $a-b$ is then divisible by $g$, so $g$ also divides $a(b-1)+a(a-b)=a^{2}-a$. All powers of $a$ are then congruent modulo $g$, so $a+b \equiv a^{N}+b \equiv 0(\bmod g)$. Then $2 a=(a+b)+(a-b)$ and $2 b=(a+b)-(a-b)$ are both divisible by $g$, so $g \mid 2 \operatorname{gcd}(a, b)$. On the other hand, it is clear that $\operatorname{gcd}(a, b) \mid g$, thus proving the Lemma.

Let $d=\operatorname{gcd}(a, b)$, and write $a=d x$ and $b=d y$ for coprime positive integers $x$ and $y$. We have that

$$
\operatorname{gcd}\left((d x)^{n}+d y,(d y)^{n}+d x\right)=d \operatorname{gcd}\left(d^{n-1} x^{n}+y, d^{n-1} y^{n}+x\right),
$$

so the Lemma tells us that

$$
\operatorname{gcd}\left(d^{n-1} x^{n}+y, d^{n-1} y^{n}+x\right) \leqslant 2
$$

for all $n \geqslant N$. Defining $K=d^{2} x y+1$, note that $K$ is coprime to each of $d, x$, and $y$. By Euler's theorem, for $n \equiv-1(\bmod \varphi(K))$ we have that

$$
d^{n-1} x^{n}+y \equiv d^{-2} x^{-1}+y \equiv d^{-2} x^{-1}\left(1+d^{2} x y\right) \equiv 0 \quad(\bmod K)
$$

so $K \mid d^{n-1} x^{n}+y$. Analogously, we have that $K \mid d^{n-1} y^{n}+x$. Taking such an $n$ which also satisfies $n \geqslant N$ gives us that

$$
K \mid \operatorname{gcd}\left(d^{n-1} x^{n}+y, d^{n-1} y^{n}+x\right) \leqslant 2 .
$$

This is only possible when $d=x=y=1$, which yields the only solution $(a, b)=(1,1)$.\\

---


---

### reference solution 2
After proving the Lemma, one can finish the solution as follows.\\
For any prime factor $p$ of $a b+1, p$ is coprime to $a$ and $b$. Take an $n \geqslant N$ such that $n \equiv-1 (\bmod p-1)$. By Fermat's little theorem, we have that

$$
\begin{aligned}
& a^{n}+b \equiv a^{-1}+b=a^{-1}(1+a b) \equiv 0 \quad(\bmod p) \\
& b^{n}+a \equiv b^{-1}+a=b^{-1}(1+a b) \equiv 0 \quad(\bmod p)
\end{aligned}
$$

then $p$ divides $g$. By the Lemma, we have that $p \mid 2 \operatorname{gcd}(a, b)$, and thus $p=2$. Therefore, $a b+1$ is a power of 2 , and $a$ and $b$ are both odd numbers.

If $(a, b) \neq(1,1)$, then $a b+1$ is divisible by 4 , hence $\{a, b\}=\{-1,1\}(\bmod 4)$. For odd $n \geqslant N$, we have that

$$
a^{n}+b \equiv b^{n}+a \equiv(-1)+1=0 \quad(\bmod 4)
$$

then $4 \mid g$. But by the Lemma, we have that $\nu_{2}(g) \leqslant \nu_{2}(2 \operatorname{gcd}(a, b))=1$, which is a contradiction. So the only solution to the problem is $(a, b)=(1,1)$.

---
