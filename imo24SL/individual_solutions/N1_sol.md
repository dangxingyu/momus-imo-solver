### reference solution 1
It is easy to verify that $n=1,2,4,12$ all work. We must show they are the only possibilities. We write $n=2^{k} m$, where $k$ is a nonnegative integer and $m$ is odd. Since $m \mid n$, either $m+1$ is prime or $m+1 \mid n$.

In the former case, since $m+1$ is even it must be 2 , so $n=2^{k}$. If $k \geqslant 3$, we get a contradiction, since $8 \mid n$ but $9 \nmid n$. Hence $k \leqslant 2$, so $n \in\{1,2,4\}$.

In the latter case, we have $m+1 \mid 2^{k} m$ and $m+1$ coprime to $m$, and hence $m+1 \mid 2^{k}$. This means that $m+1=2^{j}$ with $2 \leqslant j \leqslant k$ (since $j=1$ gives $m=1$, which was considered earlier).

Then we have $2^{k}+1 \nmid n$ : since $2^{k}+1$ is odd, it would have to divide $m$ but is larger than $m$. Hence, by the condition of the problem, $2^{k}+1$ is prime. If $k=2, j$ must be 2 as well, and this gives the solution $n=12$. Also, $2^{k-1}+1 \nmid n$ for $k>2$ : since it is odd, it would have to divide $m$. However, we have no solutions to $2^{k-1}+1 \mid 2^{j}-1$ with $j \leqslant k$ : the left-hand side is greater than the right unless $j=k$, when the left-hand side is just over half the right-hand side.

Since we have $2^{k} \mid n$ and $2^{k}+1 \nmid n$, and $2^{k-1} \mid n$ and $2^{k-1}+1 \nmid n$, we must have $2^{k}+1$ and $2^{k-1}+1$ both prime. However, $2^{a}+1$ is a multiple of three if $a$ is odd, so we must have $2^{k}+1=3$ (impossible as this gives $k=1$ ) or $2^{k-1}+1=3$, which gives $j=k=2$, whence $n=12$.

---


---

### reference solution 2
We proceed as in Solution 1 as far as determining that $n=2^{k}\left(2^{j}-1\right)$ with $j \leqslant k$.\\
Now, we have $2^{j} \mid n$ but $2^{j}+1 \nmid n$, as it is odd and does not divide $2^{j}-1$. Thus $2^{j}+1$ is prime. The theory of Fermat primes tells us we must have $j=2^{h}$ with $h>0$.

Then $2^{2^{h}}-1$ is congruent to 3 or 6 (modulo 9) depending on whether $h$ is odd or even, respectively. In particular it is not divisible by 9 , so $n=2^{k}\left(2^{2^{h}}-1\right)$ is not divisible by 9 ; so we must have $k \leqslant 2$, since if $k \geqslant 3$ then $8 \mid n$ but $9 \nmid n$ with 9 not prime.

---


---

### reference solution 3
Let $p$ be the smallest integer not dividing $n$. Since $p-1$ is a divisor of $n, p$ must be a prime. Let $1 \leqslant r \leqslant p-1$ be the remainder of $n$ modulo $p$. Since $p-r<p$, we have $p-r \mid n$, so we may consider the divisor $d=\frac{n}{p-r}$.

Since $p \mid n-r$, we have $p \mid n+p-r$, whence $p \mid d+1$. Thus $d+1 \nmid n$; so it must be prime. On the other hand, this prime is divisible by $p$, so we conclude $d+1=p$, which means that $n=(p-1)(p-r)$.

Then from $p-2, p-3 \mid n$ we get $(p-2)(p-3) \mid 2(p-r)$, from which we find

$$
(p-2)(p-3) \leqslant 2(p-r) \leqslant 2(p-1)
$$

Solving this quadratic inequality gives $p \leqslant 5$, which means that $n \in\{1,2,4,8,12,16\}$. Of this set, $n=8$ and $n=16$ are not solutions.

---


---

### reference solution 4
We suppose that $n$ is not 1 or 2.\\
Since $n \mid n$ and $n+1 \nmid n$, we know that $n+1$ is prime. Thus it is odd, so $2 \mid n$; as $n>2$, we have $\left.\frac{n}{2} \right\rvert\, n$ and $\frac{n}{2}+1 \nmid n$, so $\frac{n}{2}+1$ is prime. Thus it is also odd, so $4 \mid n$.

We must then have $\left.\frac{n}{4}+1 \right\rvert\, n$ or $\frac{n}{4}+1$ prime.

In the former case, $\frac{n}{4} \left\lvert\, 4\left(\frac{n}{4}+1\right)-n\right.$, so $\left.\frac{n}{4}+1 \right\rvert\, 4$. This means that $n=4$ or $n=12$.\\
In the latter case, $\frac{n}{4}+1$ must be odd if $n \neq 4$. Thus we have $n=8 m$ where $2 m+1,4 m+1$, $8 m+1$ are all prime; $n=8$ does not work, so $3 \mid m$ (otherwise one of those numbers would be divisible by 3). Thus $24 \mid n$, so $25 \mid n$ as 25 is not prime.

Now suppose that $p$ is the least positive integer not dividing $n$ : as in Solution 3 we know that $p$ is prime, and what we have done so far shows that $p \geqslant 7$. If $p^{2}-1=(p-1)(p+1)$ is the product of coprime integers less than $p$, it divides $n$, and $p^{2}$ is not prime so also divides $n$ (a contradiction); $p-1$ and $p+1$ are even and have no common factor higher than 2 , so all odd prime power divisors of their product are less than $p$ and the only case where $p^{2}-1$ is not a product of coprime integers less than $p$ is when one of $p-1$ and $p+1$ is a power of 2 , say $2^{m}$ (with $m \geqslant 3$ ). If $p=2^{m}-1$, then $3 p-1=4\left(3 \times 2^{m-2}-1\right)$ and $3 \times 2^{m-2}-1$ is an odd integer less than $p$, so $3 p-1 \mid n$ and so $3 p \mid n$. Finally, if $p=2^{m}+1$, then $m$ is even and $2 p-1=2^{m+1}+1$ is a multiple of 3 ; the only case where it is a power of 3 is when $m=2$, but we have $m \geqslant 3$, so $2 p-1$ is a product of coprime integers less than $p$ and again we have a contradiction.

---


---

### reference solution 5
As in Solution 4, we deduce that if $n>2$ then $n$ must be even. We write $n=2 \cdot 3^{k} \cdot r$, where $k$ is a nonnegative integer and $3 \nmid r$.

Since $r$ and $2 r$ are both different and nonzero modulo 3, one of them must be congruent to 2 modulo 3 . We'll say that it is $a r$, where $a \in\{1,2\}$.

Since $a r \mid n$, we must have that $a r+1$ is either prime or a factor of $n$. In the first case, ar $+1=3$ because $3 \mid$ ar +1 , and so $n=2 \cdot 3^{k} \cdot r$, where $r=2 / a$ is 1 or 2 . Noting that we must have $k \leqslant 1$ (else $9 \mid n$ but $10 \nmid n$ ), we can examine cases to deduce that $n \in\{2,4,12\}$ are the only possibilities.

Otherwise, $a r+1 \mid n$. Since $a r+1$ is coprime to $r$, we must in fact have that $a r+1 \mid 2 \cdot 3^{k}$, and since $3 \mid$ ar +1 by assumption we deduce that $k \geqslant 1$. In particular, $3^{k}+1$ is an even number that is at least 4 , so is not prime and must divide $n$. As it is coprime to 3 , we must in fact have $3^{k}+1 \mid 2 r$.

Let $q_{1}$ and $q_{2}$ be such that $q_{1}(a r+1)=2 \cdot 3^{k}$ and $q_{2}\left(3^{k}+1\right)=2 r$. We have that $q_{1} a r<2 \cdot 3^{k}$ and $q_{2} 3^{k}<2 r$, and multiplying these together gives $q_{1} q_{2} a<4$.

If $a=2$ then $q_{1}=q_{2}=1$, so $2 r+1=2 \cdot 3^{k}$, which is not possible (considering both sides modulo 2).

If $a=1$ then $r$ must be equivalent to 2 modulo 3 , so $q_{2}\left(3^{k}+1\right)=2 r$ gives that $q_{2}$ is equivalent to 1 modulo 3 , whence $q_{2}=1$. So we deduce that $2 r=3^{k}+1$. Thus, we deduce that $q_{1}\left(3^{k}+3\right)=4 \cdot 3^{k}$, which rearranges to give $3^{k-1}\left(4-q_{1}\right)=q_{1}$, whence $3^{k-1} \leqslant q_{1}<4$ and so $k \leqslant 2$. We can examine cases to deduce that $n=12$ is the only possibility.

---
