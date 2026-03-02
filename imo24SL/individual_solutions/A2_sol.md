### reference solution 1
For a fixed $n$, let $f(n)$ denote the minimum possible value of $S$. Consider the following variant: among all infinite sequences of nonnegative integers $x_{0}, x_{1}, \ldots$, only finitely many of which are nonzero, satisfying $x_{0}+x_{1}+\cdots=n$, let $g(n)$ denote the minimum possible value of

$$
T=2^{0} x_{0}^{2}+2^{1} x_{1}^{2}+2^{2} x_{2}^{2}+\cdots
$$

It is clear that $g(n) \leqslant f(n)$. Conversely, it is easy to see that if a sequence $x_{0}, x_{1}, \ldots$ achieves the minimum of $g(n)$, then $x_{0} \geqslant x_{1} \geqslant \cdots$ and thus $x_{n+1}=x_{n+2}=\cdots=0$. In particular, $f(n)=g(n)$.

Now, we hope to get an inductive formula for $g(n)$.\\
Note that, in order to minimise $T$ for $n \geqslant 1$, we must have $x_{0} \geqslant 1$ since the sequence ( $x_{i}$ ) is nonincreasing. Note that the minimal value of

$$
2^{1} x_{1}^{2}+2^{2} x_{2}^{2}+\cdots=2\left(2^{0} x_{1}^{2}+2^{1} x_{2}^{2}+\cdots\right)
$$

over all infinite sequences of nonnegative integers with $x_{1}+x_{2}+\cdots=m$ is exactly $2 g(m)$. As a result, for $n \geqslant 1$ we have

$$
g(n)=\min _{x_{0} \in\{1,2, \ldots, n\}}\left(x_{0}^{2}+2 g\left(n-x_{0}\right)\right) .
$$

We now prove $g(n)=\frac{n(n+1)}{2}$ by induction. It is clear that $g(0)=0$. Assume that this has been proved for $n=0,1, \ldots, N-1$. Then,


\begin{align*}
x_{0}^{2}+2 g\left(N-x_{0}\right) & =x_{0}^{2}+\left(N-x_{0}\right)\left(N-x_{0}+1\right)  \tag{1}\\
& =2 x_{0}^{2}-(2 N+1) x_{0}+N(N+1) \\
& =\frac{1}{2}\left[\left(2 x_{0}-N\right)\left(2 x_{0}-N-1\right)+N^{2}+N\right]
\end{align*}


The product of two consecutive integers $\left(2 x_{0}-N\right)\left(2 x_{0}-N-1\right)$ is always nonnegative, and it is zero precisely when $2 x_{0}$ is the even number in $\{N, N+1\}$. Thus the minimum of the final expression in equation (1) is $\frac{1}{2}\left(N^{2}+N\right)$, so $g(N)=\frac{N(N+1)}{2}$, completing the inductive proof.

---


---

### reference solution 2
Consider the following table of numbers, where the row and column indices start from 0 , and $a_{i, j}=2^{i}(2 j+1)$ for $i, j \geqslant 0$.

\begin{center}
\begin{tabular}{r|rrrrrrr}
 & $j=0$ & 1 & 2 & 3 & 4 & 5 & $\cdots$ \\
\hline
$i=0$ & 1 & 3 & 5 & 7 & 9 & 11 &  \\
1 & 2 & 6 & 10 & 14 & 18 & 22 &  \\
2 & 4 & 12 & 20 & 28 & 36 & 44 &  \\
3 & 8 & 24 & 40 & 56 & 72 & 88 &  \\
4 & 16 & 48 & 80 & 112 & 144 & 176 &  \\
$\vdots$ &  &  &  &  &  &  &  \\
\end{tabular}
\end{center}

Every number can be written uniquely as a product of a power of 2 and an odd number so every positive integer appears exactly once in the table above. It is easy to see that numbers in each row and each column are strictly increasing. Since the sum of the first $x$ odd positive integers is $x^{2}$, the sum of the first $x_{k}$ numbers in the $k^{\text {th }}$ row is $2^{k} x_{k}^{2}$, the $k^{\text {th }}$ term appearing in $S$.

Thus, the sum $S$ can be interpreted as the result of taking a total of $n$ numbers from the first $n$ rows of the table such that we take the leftmost $x_{k}$ numbers from row $k$ (where $\sum_{k=1}^{n} x_{k}=n$ ), and then computing the sum of these $n$ numbers. In particular, the minimum possible value of $S$ is the same as the sum of the smallest $n$ numbers in this table, since every row and every column of the table is strictly increasing.

Moreover, the smallest $n$ numbers, namely $1,2, \ldots, n$, appear in the first $n$ rows, so the minimum of $S$ is

$$
1+2+\cdots+n=\frac{n(n+1)}{2}
$$

---


---

### reference comment
As can be seen from the table in Solution 2, the equality case of the problem is given by

$$
x_{i}=\left\lfloor\frac{n}{2^{i+1}}+\frac{1}{2}\right\rfloor
$$

So $x_{i}$ is the result of rounding $\frac{n}{2^{i+1}}$ to the nearest integer. This also gives a proof of the identity

$$
n=\sum_{i=0}^{\infty}\left\lfloor\frac{n}{2^{i+1}}+\frac{1}{2}\right\rfloor
$$

which can be separately proven by induction on $n$ : when $n$ is incremented by 1 , exactly one term on the right hand side, namely the one corresponding to $i=\nu_{2}(n)$, increases by 1 while the others remain the same.

---


---

### reference comment
If the condition that the $x_{i}$ are nonnegative integers is relaxed to the $x_{i}$ being nonnegative reals, the problem can be solved by an application of the Cauchy-Schwarz inequality:

$$
\begin{gathered}
\left(2^{0}+2^{-1}+\cdots+2^{-n}\right)\left(2^{0} x_{0}^{2}+2^{1} x_{1}^{2}+\cdots+2^{n} x_{n}^{2}\right) \geqslant\left(x_{0}+\cdots+x_{n}\right)^{2}=n^{2} \\
\Longrightarrow 2^{0} x_{0}^{2}+2^{1} x_{1}^{2}+\cdots+2^{n} x_{n}^{2} \geqslant \frac{n^{2}}{2-2^{-n}}
\end{gathered}
$$

The equality case for this relaxed problem is given by

$$
x_{i}=\frac{2^{-i} n}{2-2^{-n}} \approx\left\lfloor\frac{n}{2^{i+1}}+\frac{1}{2}\right\rfloor
$$

In fact, when the terms in the optimal sequence for the real case are all rounded to the nearest integer, we obtain the optimal sequence for the original problem. While thinking about the real case may guide one towards the equality case of the original problem, it does not seem like it can be easily continued into a full solution.

---
