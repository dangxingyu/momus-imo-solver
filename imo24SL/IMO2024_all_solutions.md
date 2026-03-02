### A1sol1
First we will show that even integers satisfy the condition. If $\alpha=2 m$ where $m$ is an integer then

$$
\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor=2 m+4 m+\cdots+2 m n=m n(n+1)
$$

which is a multiple of $n$.\\
Now we will show that they are the only real numbers satisfying the conditions of the problem. Let $\alpha=k+\epsilon$ where $k$ is an integer and $0 \leqslant \epsilon<1$. Then the number

$$
\begin{aligned}
\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor & =k+\lfloor\epsilon\rfloor+2 k+\lfloor 2 \epsilon\rfloor+\cdots+n k+\lfloor n \epsilon\rfloor \\
& =\frac{k n(n+1)}{2}+\lfloor\epsilon\rfloor+\lfloor 2 \epsilon\rfloor+\cdots+\lfloor n \epsilon\rfloor
\end{aligned}
$$

has to be a multiple of $n$. We consider two cases based on the parity of $k$.\\
Case 1: $k$ is even.\\
Then $\frac{k n(n+1)}{2}$ is always a multiple of $n$. Thus

$$
\lfloor\epsilon\rfloor+\lfloor 2 \epsilon\rfloor+\cdots+\lfloor n \epsilon\rfloor
$$

also has to be a multiple of $n$.\\
We will prove that $\lfloor n \epsilon\rfloor=0$ for every positive integer $n$ by strong induction. The base case $n=1$ follows from the fact that $0 \leqslant \epsilon<1$. Let us suppose that $\lfloor m \epsilon\rfloor=0$ for every $1 \leqslant m<n$. Then the number

$$
\lfloor\epsilon\rfloor+\lfloor 2 \epsilon\rfloor+\cdots+\lfloor n \epsilon\rfloor=\lfloor n \epsilon\rfloor
$$

has to be a multiple of $n$. As $0 \leqslant \epsilon<1$ then $0 \leqslant n \epsilon<n$, which means that the number $\lfloor n \epsilon\rfloor$ has to be equal to 0 .

The equality $\lfloor n \epsilon\rfloor=0$ implies $0 \leqslant \epsilon<1 / n$. Since this has to happen for all $n$, we conclude that $\epsilon=0$ and then $\alpha$ is an even integer.

\section*{Case 2: $k$ is odd.}
We will prove that $\lfloor n \epsilon\rfloor=n-1$ for every natural number $n$ by strong induction. The base case $n=1$ again follows from the fact that $0 \leqslant \epsilon<1$. Let us suppose that $\lfloor m \epsilon\rfloor=m-1$ for every $1 \leqslant m<n$. We need the number

$$
\begin{aligned}
\frac{k n(n+1)}{2}+\lfloor\epsilon\rfloor+\lfloor 2 \epsilon\rfloor+\cdots+\lfloor n \epsilon\rfloor & =\frac{k n(n+1)}{2}+0+1+\cdots+(n-2)+\lfloor n \epsilon\rfloor \\
& =\frac{k n(n+1)}{2}+\frac{(n-2)(n-1)}{2}+\lfloor n \epsilon\rfloor \\
& =\frac{k+1}{2} n^{2}+\frac{k-3}{2} n+1+\lfloor n \epsilon\rfloor
\end{aligned}
$$

to be a multiple of $n$. As $k$ is odd, we need $1+\lfloor n \epsilon\rfloor$ to be a multiple of $n$. Again, as $0 \leqslant \epsilon<1$ then $0 \leqslant n \epsilon<n$, so $\lfloor n \epsilon\rfloor=n-1$ as we wanted.

This implies that $1-\frac{1}{n} \leqslant \epsilon<1$ for all $n$ which is absurd. So there are no other solutions in this case.

---

### A1sol2
As in Solution 1 we check that for even integers the condition is satisfied. Then, without loss of generality we can assume $0 \leqslant \alpha<2$. We set $S_{n}=\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor$.

Notice that

\[
\begin{array}{ll}
S_{n} \equiv 0 & (\bmod n) \\
S_{n} \equiv S_{n}-S_{n-1}=\lfloor n \alpha\rfloor & (\bmod n-1) \tag{2}
\end{array}
\]

Since $\operatorname{gcd}(n, n-1)=1$, (1) and (2) imply that


\begin{equation*}
S_{n} \equiv n\lfloor n \alpha\rfloor \quad(\bmod n(n-1)) \tag{3}
\end{equation*}


In addition,


\begin{equation*}
0 \leqslant n\lfloor n \alpha\rfloor-S_{n}=\sum_{k=1}^{n}(\lfloor n \alpha\rfloor-\lfloor k \alpha\rfloor)<\sum_{k=1}^{n}(n \alpha-k \alpha+1)=\frac{n(n-1)}{2} \alpha+n \tag{4}
\end{equation*}


For $n$ large enough, the RHS of (4) is less than $n(n-1)$. Then (3) forces


\begin{equation*}
0=S_{n}-n\lfloor n \alpha\rfloor=\sum_{k=1}^{n}(\lfloor n \alpha\rfloor-\lfloor k \alpha\rfloor) \tag{5}
\end{equation*}


for $n$ large enough.\\
Since $\lfloor n \alpha\rfloor-\lfloor k \alpha\rfloor \geqslant 0$ for $1 \leqslant k \leqslant n$, we get from (5) that, for all $n$ large enough, all these inequalities are equalities. In particular $\lfloor\alpha\rfloor=\lfloor n \alpha\rfloor$ for all $n$ large enough, which is absurd unless $\alpha=0$.

---

### A1comment
An alternative ending to the previous solution is as follows.\\
By definition we have $S_{n} \leqslant \alpha \frac{n(n+1)}{2}$, on the other hand (5) implies $S_{n} \geqslant \alpha n^{2}-n$ for all $n$ large enough, so $\alpha=0$.

---

### A1sol3
As in other solutions, without loss of generality we may assume that $0 \leqslant \alpha<2$. Even integers satisfy the condition, so we assume $0<\alpha<2$ and we will derive a contradiction.

By induction on $n$, we will simultaneously show that


\begin{gather*}
\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor=n^{2},  \tag{6}\\
\text { and } \quad \frac{2 n-1}{n} \leqslant \alpha<2 . \tag{7}
\end{gather*}


The base case is $n=1$ : If $\alpha<1$, consider $m=\left\lceil\frac{1}{\alpha}\right\rceil>1$, then

$$
\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor m \alpha\rfloor=1
$$

is not a multiple of $m$, so we deduce (7). Hence, $\lfloor\alpha\rfloor=1$ and (6) follows.\\
For the induction step: assume the induction hypothesis to be true for $n$, then by (7)

$$
2 n+1-\frac{1}{n} \leqslant(n+1) \alpha<2 n+2
$$

Hence,

$$
n^{2}+2 n \leqslant\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor+\lfloor(n+1) \alpha\rfloor=n^{2}+\lfloor(n+1) \alpha\rfloor<n^{2}+2 n+2 .
$$

So, necessarily $\lfloor(n+1) \alpha\rfloor=2 n+1$ and

$$
\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor+\lfloor(n+1) \alpha\rfloor=(n+1)^{2}
$$

in order to obtain a multiple of $n+1$. These two equalities give (6) and (7) respectively.\\
Finally, we notice that condition (7) being true for all $n$ gives a contradiction.\\

---

### A1sol4
As in other solutions without loss of generality we will assume that $0<\alpha<2$ and derive a contradiction. For each $n$, we define

$$
b_{n}=\frac{\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor}{n},
$$

which is a nonnegative integer by the problem condition and our assumption. Note that

$$
\lfloor(n+1) \alpha\rfloor \geqslant\lfloor\alpha\rfloor,\lfloor 2 \alpha\rfloor, \ldots,\lfloor n \alpha\rfloor \quad \text { and } \quad\lfloor(n+1) \alpha\rfloor>\lfloor\alpha\rfloor
$$

for all $n>\frac{1}{\alpha}$. It follows that $b_{n+1}>b_{n} \Longrightarrow b_{n+1} \geqslant b_{n}+1$ for $n>\frac{1}{\alpha}$. Thus, for all such $n$,

$$
b_{n} \geqslant n+C
$$

where $C$ is a fixed integer. On the other hand, the definition of $b_{n}$ gives

$$
b_{n}=\frac{\lfloor\alpha\rfloor+\lfloor 2 \alpha\rfloor+\cdots+\lfloor n \alpha\rfloor}{n} \leqslant \frac{\alpha+2 \alpha+\cdots+n \alpha}{n}=\frac{\alpha}{2}(n+1),
$$

which is a contradiction for sufficiently large $n$.

---

### A2sol1
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

### A2sol2
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

### A2comment
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

### A2comment
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

### A3sol1
For every positive integer $n$, let $M_{n}=\max \left(a_{1}, a_{2}, \ldots, a_{n}\right)$. We first prove that


\begin{equation*}
\frac{3^{a_{1}}+3^{a_{2}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant\left(\frac{3}{4}\right)^{M_{n}} . \tag{2}
\end{equation*}


For $i=1,2, \ldots, n$, from $\left(\frac{3}{2}\right)^{a_{i}} \leqslant\left(\frac{3}{2}\right)^{M_{n}}$ we can obtain $3^{a_{i}} \leqslant\left(\frac{3}{4}\right)^{M_{n}} \cdot 2^{M_{n}} \cdot 2^{a_{i}}$. By summing up over all $i$,

$$
\sum_{i=1}^{n} 3^{a_{i}} \leqslant\left(\frac{3}{4}\right)^{M_{n}} \cdot 2^{M_{n}} \cdot \sum_{i=1}^{n} 2^{a_{i}} \leqslant\left(\frac{3}{4}\right)^{M_{n}} \cdot\left(\sum_{i=1}^{n} 2^{a_{i}}\right)^{2}
$$

which is equivalent to (2).\\
Now let $\mu=\log _{4 / 3} \frac{1}{\varepsilon}$, so that $\mu$ is the positive real number with $\left(\frac{3}{4}\right)^{\mu}=\varepsilon$. If there is an index $n$ such that $a_{n}>\mu$, then $M_{n} \geqslant a_{n}>\mu$, and hence

$$
\frac{3^{a_{1}}+3^{a_{2}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant\left(\frac{3}{4}\right)^{M_{n}}<\left(\frac{3}{4}\right)^{\mu}=\varepsilon
$$

Otherwise we have $0<a_{i} \leqslant \mu$ for all positive integers $i$, so

$$
\frac{3^{a_{1}}+3^{a_{2}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant \frac{n \cdot 3^{\mu}}{(n \cdot 1)^{2}}=\frac{3^{\mu}}{n}
$$

If $n>\left\lfloor\frac{3^{\mu}}{\varepsilon}\right\rfloor$, this is less than $\varepsilon$.\\

---

### A3comment
It is also possible to prove (2) by induction on $n$. The base case $n=1$ is clear. For the induction step, after ordering $a_{1}, a_{2}, \ldots, a_{n}$ in increasing order as $b_{1} \leqslant b_{2} \leqslant \cdots \leqslant b_{n}$, it suffices, for example, to verify that

$$
\frac{3^{b_{1}}+3^{b_{2}}+\cdots+3^{b_{n}}}{\left(2^{b_{1}}+2^{b_{2}}+\cdots+2^{b_{n}}\right)^{2}} \leqslant \frac{3^{b_{1}}+3^{b_{2}}+\cdots+3^{b_{n}}}{\left(2^{b_{1}}+2^{b_{2}}+\cdots+2^{b_{n}}\right)\left(2^{b_{2}}+\cdots+2^{b_{n}}\right)} \leqslant \frac{3^{b_{2}}+\cdots+3^{b_{n}}}{\left(2^{b_{2}}+\cdots+2^{b_{n}}\right)^{2}}
$$

The second inequality is equivalent to $3^{b_{1}} \sum_{i=2}^{n} 2^{b_{i}} \leqslant 2^{b_{1}} \sum_{i=2}^{n} 3^{b_{i}}$, which follows from $\left(\frac{3}{2}\right)^{b_{1}} \leqslant\left(\frac{3}{2}\right)^{b_{i}}$.

---

### A3sol2
We will combine two upper bounds.\\
First, start with the trivial estimate

$$
\frac{3^{a_{1}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant \frac{3^{a_{1}}+\cdots+3^{a_{n}}}{4^{a_{1}}+\cdots+4^{a_{n}}}
$$

By applying Jensen's inequality to the convex function $x^{\log _{3} 4}$ we get

$$
\frac{4^{a_{1}}+\cdots+4^{a_{n}}}{n}=\frac{\left(3^{a_{1}}\right)^{\log _{3} 4}+\cdots+\left(3^{a_{n}}\right)^{\log _{3} 4}}{n} \geqslant\left(\frac{3^{a_{1}}+\cdots+3^{a_{n}}}{n}\right)^{\log _{3} 4}
$$

so

$$
\frac{3^{a_{1}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant \frac{3^{a_{1}}+\cdots+3^{a_{n}}}{4^{a_{1}}+\cdots+4^{a_{n}}} \leqslant\left(\frac{n}{3^{a_{1}}+\cdots+3^{a_{n}}}\right)^{\log _{3} 4-1}
$$

Hence, (1) holds true whenever


\begin{equation*}
3^{a_{1}}+\cdots+3^{a_{n}}>\left(\frac{1}{\varepsilon}\right)^{\frac{1}{\log _{3} 4-1}} \cdot n \tag{3}
\end{equation*}


Second, trivially

$$
\frac{3^{a_{1}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant \frac{3^{a_{1}}+\cdots+3^{a_{n}}}{n^{2}}
$$

so (1) is satisfied if


\begin{equation*}
3^{a_{1}}+\cdots+3^{a_{n}}<\varepsilon \cdot n^{2} \tag{4}
\end{equation*}


If $n>\left(\frac{1}{\varepsilon}\right)^{1+\frac{1}{\log _{3} 4-1}}$ then $\left(\frac{1}{\varepsilon}\right)^{\frac{1}{\log _{3} 4-1}} \cdot n<\varepsilon \cdot n^{2}$, and therefore at least one of (3) and (4) is satisfied.

---

### A3sol3
Define $C=\log _{4 / 3} \frac{2}{\varepsilon}$, so that if $a_{i}>C$ then $3^{a_{i}}<\frac{\varepsilon}{2} \cdot 4^{a_{i}}$. We divide the sequence into "small" and "large" terms by how they compare to $C$ : let

$$
\mathcal{S}_{n}=\left\{i \leqslant n \mid a_{i} \leqslant C\right\} \quad \text { and } \quad \mathcal{L}_{n}=\left\{i \leqslant n \mid a_{i}>C\right\}
$$

Then (1) is equivalent to

$$
\frac{\sum_{i \in \mathcal{S}_{n}} 3^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}}+\frac{\sum_{i \in \mathcal{L}_{n}} 3^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}}<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
$$

If $\mathcal{L}_{n}$ is nonempty, we have

$$
\frac{\sum_{i \in \mathcal{L}_{n}} 3^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}}<\frac{\varepsilon}{2} \cdot \frac{\sum_{i \in \mathcal{L}_{n}} 4^{a_{i}}}{\left(\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}} \leqslant \frac{\varepsilon}{2}
$$

and this also trivially holds when $\mathcal{L}_{n}$ is empty (in which case the LHS is zero).\\
Now suppose that $n \geqslant \frac{2}{\varepsilon}\left(\frac{3}{2}\right)^{C}$. Note that $3^{a_{i}} \leqslant\left(\frac{3}{2}\right)^{C} 2^{a_{i}}$ for $i \in \mathcal{S}_{n}$, so we have

$$
\frac{\sum_{i \in \mathcal{S}_{n}} 3^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}} \leqslant \frac{\left(\frac{3}{2}\right)^{C} \sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}} \leqslant \frac{\left(\frac{3}{2}\right)^{C}}{\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}}<\frac{\left(\frac{3}{2}\right)^{C}}{n} \leqslant \frac{\varepsilon}{2}
$$

so we have (1).

---

### A3sol4
For every index $i=1,2, \ldots, n$, apply the weighted AM-GM inequality to numbers $2^{a_{i}}$ and $(n-1)$ with weights $\log _{2} \frac{3}{2} \approx 0.585$ and $\log _{2} \frac{4}{3} \approx 0.415$ as

$$
\begin{gathered}
2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}} \geqslant 2^{a_{i}}+(n-1) \\
>\log _{2} \frac{3}{2} \cdot 2^{a_{i}}+\log _{2} \frac{4}{3} \cdot(n-1) \geqslant\left(2^{a_{i}}\right)^{\log _{2} \frac{3}{2}} \cdot(n-1)^{\log _{2} \frac{4}{3}} \\
=\left(\frac{3}{2}\right)^{a_{i}} \cdot(n-1)^{\log _{2} \frac{4}{3}}>\left(\frac{3}{2}\right)^{a_{i}} \cdot(n-1)^{2 / 5}
\end{gathered}
$$

By summing up for $i=1,2, \ldots, n$,

$$
\left(2^{a_{1}}+\cdots+2^{a_{n}}\right)^{2}=\sum_{i=1}^{n} 2^{a_{i}}\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)>(n-1)^{2 / 5} \sum_{i=1}^{n} 3^{a_{i}}
$$

so

$$
\frac{3^{a_{1}}+3^{a_{2}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)^{2}}<\frac{1}{(n-1)^{2 / 5}}
$$

If $n \geqslant\left(\frac{1}{\varepsilon}\right)^{5 / 2}+1$ then $\frac{1}{(n-1)^{2 / 5}}<\varepsilon$.

---

### A4sol1
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

### A4comment
In the construction of functions, $\alpha>2$ is only necessary if $k=\ell+1$, to make sure $f(1) \neq 0$. Otherwise, any nonintegral $\alpha>1$ suffices.

---

### A4sol2
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

### A4sol3
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

### A5sol1
We rewrite the first condition as


\begin{equation*}
a_{n+2}+a_{n+1}=\left(a_{n+1}+a_{n}\right)\left(a_{n+1}-a_{n}+1\right) . \tag{1}
\end{equation*}


If there exists a positive integer $m$ such that $a_{m+1}+a_{m}=0$, then from equation (1) we have $a_{n+1}+a_{n}=0$ for all positive integers $n \geqslant m$. By the fact that the sequence ( $a_{i+1}+a_{i}$ ) is periodic, we get $a_{i+1}+a_{i}=0$ for every positive integer $i$. Thus the sequence ( $a_{i}$ ) is of the form $c,-c, c,-c, \ldots$ for some $|c| \leqslant \frac{1}{2}$.

Now suppose that $a_{n+1}+a_{n} \neq 0$ for every positive integer $n$. Let $T$ be the period of the sequence. From equation (1) we have

$$
1=\prod_{i=1}^{T} \frac{a_{i+2}+a_{i+1}}{a_{i+1}+a_{i}}=\prod_{i=1}^{T}\left(a_{i+1}-a_{i}+1\right) .
$$

Combining with the second condition $\left|a_{i+1}-a_{i}\right| \leqslant 1$, we have $a_{i+1}-a_{i}+1>0$. Using the AM-GM inequality we get

$$
1=\prod_{i=1}^{T}\left(a_{i+1}-a_{i}+1\right) \leqslant\left(\frac{\sum_{i=1}^{T}\left(a_{i+1}-a_{i}+1\right)}{T}\right)^{T}=1 .
$$

So the equality holds, and thus we get

$$
a_{2}-a_{1}=a_{3}-a_{2}=\cdots=a_{T+1}-a_{T}
$$

which means that $\left(a_{i}\right)$ is a constant sequence.\\
So all sequences satisfying the conditions of the problem are those listed above.

---

### A5sol2
Define $s_{n}=a_{n+1}+a_{n}$ and $d_{n}=a_{n+1}-a_{n}$, so the original sequence is periodic if and only if both these sequences are periodic. Rearranging the given conditions yields $s_{n+1}= s_{n}\left(1+d_{n}\right)$ and $d_{n+1}=d_{n}\left(s_{n}-1\right)$, with $\left|d_{n}\right| \leqslant 1$ for all $n$.

If $s_{n}=0$ for some $n$ then $s_{i}=0$ for all $i \geqslant n$, and for the sequence to be periodic we must have all $s_{i}=0$ and the sequence $c,-c, c,-c, \ldots$, for some $|c| \leqslant \frac{1}{2}$. Similarly, if $d_{n}=0$ for some $n$ and the sequence is periodic, then all $d_{i}=0$ and the sequence is $c, c, c, \ldots$.

We claim those are the only periodic sequences, so suppose for contradiction that we have a periodic sequence where no $s_{i}$ or $d_{i}$ is 0 . Under this hypothesis, we will prove that $\left(s_{n}\right),\left(d_{n}\right)$ have the following properties.

\begin{enumerate}
  \item All $s_{n}$ are positive numbers. As $\left|d_{n}\right| \leqslant 1$ and $s_{n+1}=s_{n}\left(1+d_{n}\right) \neq 0$, it follows that $d_{n}>-1$ and that all $s_{n}$ have the same sign (all positive or all negative). If all $s_{n}$ are negative, then $\left|d_{n+1}\right|=\left|d_{n}\left(s_{n}-1\right)\right|>\left|d_{n}\right|$, so $\left|d_{i}\right|$ is a strictly increasing sequence, contradicting periodicity.
  \item Whenever $d_{n}>0$ we have $0<s_{n}<1$. Suppose for contradiction that we have $d_{n}>0$ and $s_{n} \geqslant 1$ for some $n$. Since $d_{n+1} \neq 0$ we have $s_{n}>1$, and then $d_{n+1}>0, s_{n+1}>s_{n}>1$. Inductively, all $d_{i}>0$ for $i \geqslant n$, and $s_{i+1}>s_{i}$ for $i \geqslant n$, contradicting periodicity.
\end{enumerate}

Now we can get the desired contraction as follows. Suppose that the period of ( $a_{i}$ ) is $T$, then $\sum_{i=1}^{T} d_{i}=a_{T+1}-a_{1}=0$, hence there is an $n$ such that $d_{n}>0$. By property 2 we get $0<s_{n}<1$, and in particular $s_{n}<2$. Suppose that we have $s_{i}<2$. If $d_{i}<0$, then $s_{i+1}=s_{i}\left(1+d_{i}\right)<s_{i}<2$; if $d_{i}>0$, then by property 2 we have $0<s_{i}<1$, and then $s_{i+1}=s_{i}\left(1+d_{i}\right) \leqslant 2 s_{i}<2$. In both cases we get $s_{i+1}<2$, and then by induction we get $s_{k}<2$ for all $k \geqslant n$. But then we have $\left|d_{k+1}\right|=\left|d_{k}\left(s_{k}-1\right)\right|<\left|d_{k}\right|$, which contradicts the fact that ( $d_{k}$ ) is periodic.

So the only periodic sequences are the two listed above.\\

---

### A5sol3
Note that if $a_{n+1}=-a_{n}$ for any $n$, then $a_{n+2}=a_{n}=-a_{n+1}$, yielding the first answer by periodicity. Also, if $a_{n+1}=a_{n}$ for any $n$, then $a_{n+2}=a_{n}=a_{n+1}$, yielding the second answer by periodicity. If $a_{n+2}=a_{n}$ for any $n$, then $a_{n}^{2}=a_{n+1}^{2}$ so $a_{n+1}= \pm a_{n}$ and one of those two cases applies. Henceforth, we will assume that the sequence is neither one of the answers and $a_{n} \neq a_{n+1},-a_{n+1}, a_{n+2}$ for all $n$ for the rest of the solution. Note that the recursion rearranges to


\begin{equation*}
a_{n+2}-a_{n+1}=\left(a_{n+1}^{2}-a_{n+1}\right)-\left(a_{n}^{2}-a_{n}\right)=\left(a_{n+1}-a_{n}\right)\left(a_{n+1}+a_{n}-1\right) . \tag{2}
\end{equation*}


Claim 1. We have that $a_{n} \leqslant \frac{1}{2}$ for all $n$.\\
Proof. First, we cannot have $a_{n}>\frac{1}{2}$ for all $n$. Otherwise, $a_{n+1}+a_{n}-1$ is positive for all $n$, so (2) implies that $a_{n+2}-a_{n+1}$ has the same sign as $a_{n+1}-a_{n}$ for all $n$. This would mean that the sequence is monotonic, contradicting periodicity.

On the other hand, if $a_{n+1} \leqslant \frac{1}{2}$ and $a_{n+2}>\frac{1}{2}$, then

$$
a_{n+1}^{2}=a_{n+2}+a_{n}^{2}-a_{n} \geqslant a_{n+2}-\frac{1}{4}>\frac{1}{4} \Longrightarrow\left|a_{n+1}\right|>\frac{1}{2}
$$

where we use the fact that $t^{2}-t \geqslant-\frac{1}{4}$ for all $t \in \mathbb{R}$. As $a_{n+1} \leqslant \frac{1}{2}$, this means that $a_{n+1}<-\frac{1}{2}$ so $\left|a_{n+1}-a_{n+2}\right|>1$, a contradiction.

The identity (2) now implies that $a_{n+2}-a_{n+1}$ and $a_{n+1}-a_{n}$ are of opposite signs for all $n$, so that $a_{n}<a_{n+1} \Longleftrightarrow a_{n+1}>a_{n+2}$.\\
Claim 2. We have that $a_{n}>0 \Longleftrightarrow a_{n+1} \leqslant 0$ : that is, the signs of the sequence are alternating.

Proof. First, it cannot be the case that $a_{n}>0$ for all $n$. Indeed, then we would have from Claim 1 that $\left|a_{n+1}+a_{n}-1\right|<1$ for all $n$, which by (2) means that $\left|a_{n+1}-a_{n}\right|$ is strictly decreasing in $n$, a contradiction of the sequence's periodicity. It also cannot be the case that $a_{n} \leqslant 0$ for all $n$, as then we would have that $\left|a_{n+1}+a_{n}-1\right|>1$ for all $n$ (noting that by the nonconstant assumption we will never have $a_{n}=a_{n+1}=0$ ) so $\left|a_{n+1}-a_{n}\right|$ is strictly increasing in $n$.

Hence, if the signs of $a_{n}$ are not alternating, then by periodicity there exists $n$ with $a_{n}>0$ and $a_{n+1}, a_{n+2} \leqslant 0$ or $a_{n}, a_{n+1}>0$ and $a_{n+2} \leqslant 0$. In either scenario, we have that

$$
a_{n}^{2}-a_{n}=a_{n+1}^{2}-a_{n+2} \geqslant a_{n+1}^{2} \geqslant 0 \Longrightarrow a_{n}>1
$$

as $a_{n}$ is positive and $a_{n+2}$ is nonpositive.\\
In the former case, we have that $a_{n}-a_{n+1}>1$, a contradiction. In the latter case, as $a_{n+1}>a_{n+2}$, we must have that $a_{n}<a_{n+1}$. But then we have that $a_{n+1}-a_{n+2}>a_{n}-a_{n+2}>1$, a contradiction.

Note now that we cannot have $a_{n+2}>-a_{n+1}>a_{n}$ for any $n$, as we would then have

$$
a_{n+1}^{2}-a_{n}^{2}=a_{n+2}-a_{n}>-a_{n+1}-a_{n}>0 \Longrightarrow a_{n}-a_{n+1}>1,
$$

a contradiction. Similarly, we cannot have $a_{n}>-a_{n+1}>a_{n+2}$ for any $n$, as we would then have

$$
a_{n}^{2}-a_{n+1}^{2}=a_{n}-a_{n+2}>a_{n}+a_{n+1}>0 \Longrightarrow a_{n}-a_{n+1}>1 .
$$

Having ruled out these scenarios, we may conclude that $\left|a_{n+1}\right|$ is not between $\left|a_{n}\right|$ and $\left|a_{n+2}\right|$ for any $n$.

Let $k$ be an index such that $\left|a_{k}\right|$ is maximal. Note that we cannot have $\left|a_{k-2}\right|=\left|a_{k}\right|$, as that would imply that $a_{k-2}=a_{k}$ by Claim 2. We also cannot have $\left|a_{k-2}\right| \leqslant\left|a_{k-1}\right|$, as that would imply that $\left|a_{k-1}\right|$ is between $\left|a_{k-2}\right|$ and $\left|a_{k}\right|$. Hence, we must have that $\left|a_{k-1}\right|<\left|a_{k-2}\right|<\left|a_{k}\right|$. As $\left|a_{k}\right|$ is maximal, we cannot have $a_{k}=0$. If $a_{k}>0$, then we have that $a_{k}-a_{k-2}=a_{k-1}^{2}-a_{k-2}^{2}<0$, a contradiction. If $a_{k}<0$, then we have that $a_{k}-a_{k+2}=a_{k}^{2}-a_{k+1}^{2}>0$, a contradiction.

---

### A6sol1
We will show that the eventual period of sequence $\left(b_{n}\right)$ consists of any fixed number of occurrences of $G$ (possibly zero) followed by a single $A$.

We look at the ratios of consecutive terms of the sequence $\left(a_{n}\right)$. Let $C$ and $D$ be coprime positive integers such that $a_{1} / a_{0}=(C+D) / C$. If $b_{n}=G$ then $a_{n} / a_{n-1}=a_{n+1} / a_{n}$. If $b_{n}=A$ and $a_{n} / a_{n-1}=(C+k D) /(C+(k-1) D)$ for some positive integer $k$ then

$$
\frac{a_{n+1}}{a_{n}}=\frac{2 a_{n}-a_{n-1}}{a_{n}}=\frac{C+(k+1) D}{C+k D} .
$$

Thus, by induction, there is a sequence of positive integers $\left(k_{n}\right)$ for $n \geqslant 1$ which satisfies $a_{n} / a_{n-1}=\left(C+k_{n} D\right) /\left(C+\left(k_{n}-1\right) D\right)$ for all positive integers $n$. Moreover, we have $k_{1}=1$ and

$$
k_{n+1}= \begin{cases}k_{n}, & \text { if } b_{n}=G \\ k_{n}+1, & \text { if } b_{n}=A\end{cases}
$$

If there are only finitely many values of $n$ such that $b_{n}=A$ then the problem statement obviously holds (we can choose $d=1$ ). Thus, we may assume that $b_{n}=A$ for infinitely many $n$. This means that the sequence ( $k_{n}$ ) attains all positive integer values. Given a value $q \geqslant 1$, denote by $m_{q}$ the last index where value $q$ occurs, that is, the index such that $k_{m_{q}}=q$ and $k_{m_{q}+1}=q+1$.

Our aim is to prove that the sequence of differences ( $m_{q+1}-m_{q}$ ) is eventually constant. We first show that it is bounded above. To that end, fix $t \geqslant 1$ (we will choose a suitably large $t$ later on) and consider a sequence $s(t)_{0}, s(t)_{1}, \ldots$ defined for $q \geqslant 1$ by $s(t)_{q}=a_{m_{q}} /(C+q D)^{t}$.

We note two properties of $s(t)_{q}$. First, simple algebra gives

$$
\begin{aligned}
s(t)_{q+1}=\frac{a_{m_{q+1}}}{(C+(q+1) D)^{t}}=\frac{a_{m_{q}}}{(C+(q+1) D)^{t}}\left(\frac{C+(q+1) D}{C+q D}\right)^{m_{q+1}-m_{q}} \\
\quad=\frac{a_{m_{q}}}{(C+q D)^{t}}\left(\frac{C+(q+1) D}{C+q D}\right)^{m_{q+1}-m_{q}-t}=s(t)_{q}\left(\frac{C+(q+1) D}{C+q D}\right)^{m_{q+1}-m_{q}-t} .
\end{aligned}
$$

It follows that

$$
\left.\begin{array}{l}
s(t)_{q}>s(t)_{q+1} \\
s(t)_{q}=s(t)_{q+1} \\
s(t)_{q}<s(t)_{q+1}
\end{array}\right\} \quad \text { if and only if } \quad\left\{\begin{array}{l}
m_{q+1}-m_{q}<t, \\
m_{q+1}-m_{q}=t, \\
m_{q+1}-m_{q}>t .
\end{array}\right.
$$

Second, suppose that $m_{q+1}-m_{q} \geqslant t$ for some positive integer $q$. We claim that in that case $s(t)_{q}$ is a positive integer. Indeed, we have

$$
a_{m_{q}+t}=a_{m_{q}}\left(\frac{C+(q+1) D}{C+q D}\right)^{t},
$$

because $k_{m_{q}+1}=k_{m_{q}+2}=\cdots=k_{m_{q}+t}=q+1$. Since $C+(q+1) D$ and $C+q D$ are coprime we have that

$$
s(t)_{q}=\frac{a_{m_{q}}}{(C+q D)^{t}}
$$

is an integer.\\
We choose $T \geqslant 1$ such that $s(T)_{1}<1$ (which exists since $C+D>1$ ). Then, by induction we can show that $s(T)_{q}<1$ for all $q$. Indeed, since $s(T)_{q}<1$, it is not a positive integer; this means that $m_{q+1}-m_{q}<T$ by the second property above. Hence by the first property above we have $s(T)_{q+1}<s(T)_{q}<1$, as needed.

This means that $m_{q+1}-m_{q}<T$ for all $q$. Thus there is a largest integer $T^{\prime} \leqslant T$ with the property that an equality $m_{q+1}-m_{q}=T^{\prime}$ holds for infinitely many values of $q$.

Therefore, for all sufficiently large values of $q$ we have the inequality $m_{q+1}-m_{q} \leqslant T^{\prime}$, which by the first property implies that the sequence $s\left(T^{\prime}\right)$ is decreasing from some point on. Moreover, we know that the sequence attains infinitely many integer values since there are infinitely many values of $q$ for which we have the equality $m_{q+1}-m_{q}=T^{\prime}$. As a consequence, the sequence $s\left(T^{\prime}\right)$ is constant from some sufficiently large index $Q$ onwards.

This in turn means that the equality $m_{q+1}-m_{q}=T^{\prime}$ holds for all $q \geqslant Q$. Note that $b_{n}=A$ is equivalent to the fact that $n=m_{q}$ for some integer $q$. Thus, the sequence ( $b_{n}$ ) is periodic for $n \geqslant Q$ with period $T^{\prime}$, and the proof is complete.

---

### A6sol2
First, observe that the statement holds immediately if $b_{n}=G$ for all $n$; otherwise, there must be some $n$ for which $b_{n}=A$. Without loss of generality, we may assume that $n=1$, as we can translate the sequence without affecting the statement.

We define an arithmetic sequence $\left(p_{n}\right)$ by taking $p_{0}=a_{0} / \operatorname{gcd}\left(a_{0}, a_{1}\right)$ and $p_{1}=a_{1} / \operatorname{gcd}\left(a_{0}, a_{1}\right)$. Note that $p_{0}<p_{1}$, and hence that ( $p_{n}$ ) is an increasing sequence of positive integers, and also that $p_{2}=a_{2} / \operatorname{gcd}\left(a_{0}, a_{1}\right)$.

We also define a sequence of positive integers $d_{n}=a_{n}-a_{n-1}$ and a sequence of positive rational numbers $q_{n}=a_{n} / a_{n-1}$.

Then the following facts are immediate consequences of the definitions:

\begin{itemize}
  \item if $b_{n}=G$, then $q_{n+1}=q_{n}$ and $d_{n+1}=d_{n} q_{n}$;
  \item if $b_{n}=A$, then $d_{n+1}=d_{n}$;
  \item $q_{1}=p_{1} / p_{0}$;
  \item if $b_{n}=A$ and $q_{n}=p_{i} / p_{i-1}$, then $q_{n+1}=p_{i+1} / p_{i}$.
\end{itemize}

Now, let $k_{i}$ be the number of integers $n$ for which $b_{n}=G$ and $q_{n}=p_{i} / p_{i-1}$. If some $k_{i}$ is infinite then $b_{n}$ is eventually always $G$; otherwise, all values of $k_{i}$ are nonnegative integers.

The sequence of values for $d_{n}$ can be written as

$$
d_{0}, d_{0} \frac{p_{1}}{p_{0}}, \ldots, d_{0}\left(\frac{p_{1}}{p_{0}}\right)^{k_{1}}, d_{0}\left(\frac{p_{1}}{p_{0}}\right)^{k_{1}} \frac{p_{2}}{p_{1}}, \ldots, d_{0}\left(\frac{p_{1}}{p_{0}}\right)^{k_{1}}\left(\frac{p_{2}}{p_{1}}\right)^{k_{2}}, \ldots
$$

and in particular all terms in this sequence are positive integers. Furthermore, $p_{i}$ and $p_{i+1}$ are coprime for all $i$, so the following sequence consists entirely of positive integers:

$$
\begin{aligned}
u_{0} & =d_{0} p_{0}^{-k_{1}} \\
u_{1} & =d_{0} p_{0}^{-k_{1}} p_{1}^{k_{1}-k_{2}} \\
u_{2} & =d_{0} p_{0}^{-k_{1}} p_{1}^{k_{1}-k_{2}} p_{2}^{k_{2}-k_{3}} \\
& \vdots
\end{aligned}
$$

We will prove that $k_{i}$ is eventually constant, which implies that the sequence of $b_{n}$ is eventually periodic with period consisting of $k$ copies of $G$ followed by an $A$ (where $k$ is that constant value).

Observe that either $k_{i}$ is unbounded, or is bounded with eventual maximum $k$ for some constant $k$. In the second case, let $r_{0}$ be minimal such that $k_{r_{0}}=k$; in the first case let $r_{0}=0$. We will construct an infinite sequence of integers as follows:

\begin{itemize}
  \item If $k_{r_{i}+1} \geqslant k_{r_{i}}$, then $r_{i+1}=r_{i}+1$
  \item If $k_{r_{i}+1}<k_{r_{i}}$, then $r_{i+1}$ is the minimal positive integer greater than $r_{i}$ such that $k_{r_{i+1}} \geqslant k_{r_{i}}$. Observe that in the second case, such an $r_{i+1}$ must exist by our construction of $r_{0}$.
\end{itemize}

We claim that $u_{r_{i+1}} \leqslant u_{r_{i}}$ with equality only if $k_{r_{i}+1}=k_{r_{i}}$ (so $r_{i+1}=r_{i}+1$ ). Indeed, if $k_{r_{i}+1} \geqslant k_{r_{i}}$ then

$$
u_{r_{i+1}}=u_{r_{i}+1}=u_{r_{i}} p_{r_{i}}^{k_{r_{i}}-k_{r_{i}+1}} \leqslant u_{r_{i}}
$$

with equality if and only if $k_{r_{i}}=k_{r_{i}+1}$.\\
Otherwise, we have

$$
\frac{u_{r_{i+1}}}{u_{r_{i}}}=p_{r_{i}}^{k_{r_{i}}-k_{r_{i}+1}} p_{r_{i}+1}^{k_{r_{i}+1}-k_{r_{i}+2}} \cdots p_{r_{i+1}-1}^{k_{r_{i+1}-1}-k_{r_{i+1}}}
$$

so we just need to show that the right hand side is strictly less than 1 . But this follows because

$$
\begin{aligned}
p_{r_{i}}^{k_{r_{i}}-k_{r_{i}+1}} p_{r_{i}+1}^{k_{r_{i}+1}-k_{r_{i}+2}} \cdots p_{r_{i+1}-1}^{k_{r_{i+1}-1}-k_{r_{i+1}}} & <p_{r_{i}+1}^{k_{r_{i}}-k_{r_{i}+2}} p_{r_{i}+2}^{k_{r_{i}+2}-k_{r_{i}+3}} \cdots p_{r_{i+1}-1}^{k_{r_{i+1}-1}-k_{r_{i+1}}} \\
& <p_{r_{i}+2}^{k_{r_{i}}-k_{r_{i}+3}} p_{r_{i}+3}^{k_{r_{i}+3}-k_{r_{i}+4}} \cdots p_{r_{i+1}-1}^{k_{i_{i}-1}-k_{r_{i+1}}} \\
& \vdots \\
& <p_{r_{i+1}-1}^{k_{r_{i}-k_{r_{i+1}}}} \\
& \leqslant 1
\end{aligned}
$$

where each inequality besides the last follows from the fact that $p_{j}<p_{j+1}$ and $k_{r_{i}}>k_{j}$ for $j<r_{i+1}$, and the last follows from the fact that $k_{r_{i}} \leqslant k_{r_{i+1}}$.

Finally, the sequence $u_{r_{i}}$ is an infinite nonincreasing sequence of positive integers so must eventually be constant, yielding the claim.

---

### A6comment
The two solutions above differ in approach, but have some overlap in the structure they reveal. Indeed, the $C+n D$ of Solution 1 is the $p_{n}$ of Solution 2, while the $m_{r+1}-m_{r}$ of Solution 1 turns out to be equal to the $k_{r}$ of

---

### A6sol2


---

### A7sol1
We begin by providing an example of a function $f$ for which there are two values of $g(x)$. We take the function $f(x)=\lfloor x\rfloor-\{x\}$, where $\lfloor x\rfloor$ denotes the floor of $x$ (that is, the largest integer less than or equal to $x$ ) and $\{x\}=x-\lfloor x\rfloor$ denotes the fractional part of $x$.

First, we show that $f$ satisfies $P(x, y)$. Given $x, y \in \mathbb{Q}$, we have

$$
\begin{aligned}
& f(x)+y=\lfloor x\rfloor-\{x\}+\lfloor y\rfloor+\{y\}=(\lfloor x\rfloor+\lfloor y\rfloor)+(\{y\}-\{x\}) ; \\
& x+f(y)=\lfloor x\rfloor+\{x\}+\lfloor y\rfloor-\{y\}=(\lfloor x\rfloor+\lfloor y\rfloor)+(\{x\}-\{y\}) .
\end{aligned}
$$

If $\{x\}<\{y\}$, then we have that the fractional part of $f(x)+y$ is $\{y\}-\{x\}$ and the floor is $\lfloor x\rfloor+\lfloor y\rfloor$, so $f(x)+y \rightarrow x+f(y)$. Likewise, if $\{x\}>\{y\}$, then $x+f(y) \rightarrow f(x)+y$. Finally, if $\{x\}=\{y\}$, then $f(x)+y=x+f(y)=\lfloor x\rfloor+\lfloor y\rfloor$ is an integer. In all cases, the relation $P$ is satisfied.

Finally, we observe that if $x$ is an integer then $g(x)=0$, and if $x$ is not an integer then $g(x)=-2$, so there are two values for $g(x)$ as required.

Now, we prove that there cannot be more than two values of $g(x) . P(x, x)$ tells us that $x+f(x) \sim x+f(x)$, or in other words, for all $x$,


\begin{equation*}
f(x+f(x))=x+f(x) \tag{1}
\end{equation*}


We begin with the following lemma.\\
Lemma 1. $f$ is a bijection, and satisfies


\begin{equation*}
f(-f(-x))=x . \tag{2}
\end{equation*}


Proof. We first prove that $f$ is injective. Suppose that $f\left(x_{1}\right)=f\left(x_{2}\right)$; then $P\left(x_{1}, x_{2}\right)$ tells us that $f\left(x_{1}\right)+x_{2} \sim f\left(x_{2}\right)+x_{1}$. Without loss of generality, suppose that $f\left(x_{1}\right)+x_{2} \rightarrow f\left(x_{2}\right)+x_{1}$.

But $f\left(x_{1}\right)=f\left(x_{2}\right)$, so $f\left(f\left(x_{1}\right)+x_{2}\right)=f\left(f\left(x_{2}\right)+x_{2}\right)=f\left(x_{2}\right)+x_{2}$ by (1). Therefore, $f\left(x_{2}\right)+x_{1}=f\left(x_{2}\right)+x_{2}$, as required.

Now, (1) with $x=0$ tells us that $f(f(0))=f(0)$ and so by injectivity $f(0)=0$.\\
Applying $P(x,-f(x))$ tells us that $0 \sim x+f(-f(x))$, so either $0=f(0)=x+f(-f(x))$ or $f(x+f(-f(x)))=0$ which implies that $x+f(-f(x))=0$ by injectivity. Either way, we deduce that $x=-f(-f(x))$, or $x=f(-f(-x))$ by replacing $x$ with $-x$.

Finally, note that bijectivity follows immediately from (2).\\
Since $f$ is bijective, it has an inverse, which we denote $f^{-1}$. Rearranging (2) (after replacing $x$ with $-x)$ gives that $f(-x)=-f^{-1}(x)$. We have $g(x)=f(x)+f(-x)=f(x)-f^{-1}(x)$.

Suppose $g(x)=u$ and $g(y)=v$, where $u \neq v$ are both nonzero. Define $x^{\prime}=f^{-1}(x)$ and $y^{\prime}=f^{-1}(y)$; by definition, we have

$$
\begin{aligned}
& x^{\prime} \rightarrow x \rightarrow x^{\prime}+u \\
& y^{\prime} \rightarrow y \rightarrow y^{\prime}+v .
\end{aligned}
$$

Putting in $P\left(x^{\prime}, y\right)$ gives $x+y \sim x^{\prime}+y^{\prime}+v$, and putting in $P\left(x, y^{\prime}\right)$ gives $x+y \sim x^{\prime}+y^{\prime}+u$. These are not equal since $u \neq v$, and $x+y$ may have only one incoming and outgoing arrow because $f$ is a bijection, so we must have either $x^{\prime}+y^{\prime}+u \rightarrow x+y \rightarrow x^{\prime}+y^{\prime}+v$ or the same with the arrows reversed. Swapping $(x, u)$ and $(y, v)$ if necessary, we may assume without loss of generality that this is the correct direction for the arrows.

Also, we have $-x^{\prime}-u \rightarrow-x \rightarrow-x^{\prime}$ by Lemma 1. Putting in $P\left(x+y,-x^{\prime}-u\right)$ gives $y \sim y^{\prime}+v-u$, and so $y^{\prime}+v-u$ must be either $y^{\prime}+v$ or $y^{\prime}$. This means $u$ must be either 0 or $v$, and this contradicts our assumption about $u$ and $v$.

---

### A7comment
Lemma 1 can also be proven as follows. We start by proving that $f$ must be surjective. Suppose not; then, there must be some $t$ which does not appear in the output of $f$. $P(x, t-f(x))$ tells us that $t \sim x+f(t-f(x))$, and so by assumption $f(t)=x+f(t-f(x))$ for all $x$. But setting $x=f(t)-t$ gives $t=f(t-f(f(t)-t))$, contradicting our assumption about $t$.

Now, choose some $t$ such that $f(t)=0$; such a $t$ must exist by surjectivity. $P(t, t)$ tells us that $f(t)=t$, or in other words $t=0$ and $f(0)=0$. The remainder of the proof is the same as the proof given in

---

### A7sol1


---

### A7sol2
We again start with Lemma 1 , and note $f(0)=0$ as in the proof of that lemma.\\
$P(x,-f(y))$ gives $x+f(-f(y)) \sim f(x)-f(y)$, and using (2) this becomes $x-y \sim f(x)-f(y)$. In other words, either $f(x-y)=f(x)-f(y)$ or $x-y=f(f(x)-f(y))$. In the latter case, we deduce that

$$
\begin{aligned}
f(-(x-y)) & =f(-f(f(x)-f(y))) \\
f(y-x) & =f(-f(f(x)-f(y))) \\
& =f(y)-f(x)
\end{aligned}
$$

Thus, $f(y)-f(x)$ is equal to either $f(y-x)$ or $-f(x-y)$. Replacing $y$ with $x+d$, we deduce that $f(x+d)-f(x) \in\{f(d),-f(-d)\}$.

Now, we prove the following claim.\\
Claim. For any $n \in \mathbb{Z}_{>0}$ and $d \in \mathbb{Q}$, we have that either $g(d)=0$ or $g(d)= \pm g(d / n)$.\\
In particular, if $g(d / n)=0$ then $g(d)=0$.

Proof. We first prove that if $g(d / n)=0$ then $g(d)=0$. Suppose that $g(d / n)=0$. Then $f(d / n)=-f(-d / n)$ and so $f(x+d / n)-f(x)=f(d / n)$ for any $x$. Applying this repeatedly, we deduce that $f(x+d)-f(x)=n f(d / n)$ for any $x$. Applying this with $x=0$ and $x=-d$ and adding gives $f(d)+f(-d)=0$, so $g(d)=0$, and in particular the claim is true whenever $g(d)=0$.

Now, select $n \in \mathbb{Z}_{>0}$ and $d \in \mathbb{Q}$ such that $g(d) \neq 0$, and observe that we must have $g(d / n) \neq$ 0 . Observe that for any $k \in \mathbb{Z}$ we have that $f(k d / n)-f((k-1) d / n) \in\{f(d / n),-f(-d / n)\}$. Let $A_{i}$ be the number of $k \in \mathbb{Z}$ with $i-n<k \leqslant i$ such that this difference equals $f(d / n)$.

We deduce that for any $i \in \mathbb{Z}$,

$$
\begin{aligned}
f(i d / n)-f(i d / n-d) & =\sum_{i-n<k \leqslant i} f(k d / n)-f((k-1) d / n) \\
& =A_{i} f(d / n)-\left(n-A_{i}\right) f(-d / n) \\
& =-n f(-d / n)+A_{i} g(d / n)
\end{aligned}
$$

Since $g(d / n)$ is nonzero, this is a nonconstant linear function of $A_{i}$. However, there are only two possible values for $f(i d / n)-f(i d / n-d)$, so there must be at most two possible values for $A_{i}$ as $i$ varies. And since $A_{i+1}-A_{i} \in\{-1,0,1\}$, those two values must differ by 1 (if there are two values).

Now, we have

$$
\begin{aligned}
f(d)-f(0) & =-n f(-d / n)+A_{n} g(d / n), \quad \text { and } \\
f(0)-f(-d) & =-n f(-d / n)+A_{0} g(d / n)
\end{aligned}
$$

Subtracting these (using the fact that $f(0)=0$ ) we obtain

$$
\begin{aligned}
f(d)+f(-d) & =\left(A_{n}-A_{0}\right) g(d / n) \\
& = \pm g(d / n)
\end{aligned}
$$

where the last line follows from the fact that $g(d)$ is nonzero.\\
It immediately follows that there can only be one nonzero number of the form $g(x)$ up to sign; to see why, if $g(d)$ and $g\left(d^{\prime}\right)$ are both nonzero, then for some $n, n^{\prime} \in \mathbb{Z}_{>0}$ we have $d / n=d^{\prime} / n^{\prime}$. But

$$
g(d)= \pm g(d / n)= \pm g\left(d^{\prime}\right)
$$

Finally, suppose that for some $d, d^{\prime}$ we have $g(d)=c$ and $g\left(d^{\prime}\right)=-c$ for some nonzero $c$. So we have

$$
f(d)+f(-d)-f\left(d^{\prime}\right)-f\left(-d^{\prime}\right)=2 c
$$

which rearranges to become $\left(f(d)-f\left(d^{\prime}\right)\right)-\left(f\left(-d^{\prime}\right)-f(-d)\right)=2 c$.\\
Each of the bracketed terms must be equal to either $f\left(d-d^{\prime}\right)$ or $-f\left(d^{\prime}-d\right)$. However, they cannot be equal since $c$ is nonzero, so $g\left(d-d^{\prime}\right)=f\left(d-d^{\prime}\right)+f\left(d^{\prime}-d\right)= \pm 2 c$. This contradicts the assertion that $g(-x)= \pm c$ for all $x$.

---

### A7sol3
As in Solution 1, we start by establishing Lemma 1 as above, and write $f^{-1}(x)= -f(-x)$ for the inverse of $f$, and $g(x)=f(x)-f^{-1}(x)$.

We now prove the following.\\
Lemma 2. If $g(x) \neq g(y)$, then $g(x+y)= \pm(g(x)-g(y))$.

Proof. Assume $x$ and $y$ are such that $g(x) \neq g(y)$. Applying $P\left(x, f^{-1}(y)\right)$ gives $x+y \sim f(x)+f^{-1}(y)$, and applying $P\left(f^{-1}(x), y\right)$ gives $x+y \sim f^{-1}(x)+f(y)$.

Observe that

$$
\begin{aligned}
\left(f(x)+f^{-1}(y)\right)-\left(f^{-1}(x)+f(y)\right) & =\left(f(x)-f^{-1}(x)\right)-\left(f(y)-f^{-1}(y)\right) \\
& =g(x)-g(y) .
\end{aligned}
$$

By assumption, $g(x) \neq g(y)$, and so $f(x)+f^{-1}(y) \neq f^{-1}(x)+f(y)$. Since $f$ is bijective, this means that these two values must be $f(x+y)$ and $f^{-1}(x+y)$ in some order, and so $g(x+y)=f(x+y)-f^{-1}(x+y)$ must be their difference up to sign, which is either $g(x)-g(y)$ or $g(y)-g(x)$.

Claim. If $x$ and $q$ are rational numbers such that $g(q)=0$ and $n$ is an integer, then $g(x+n q)= g(x)$.

Proof. If $g(b)=0$ and $g(a) \neq g(a+b)$, then the lemma tells us that $g(b)= \pm(g(a+b)-g(a))$, which contradicts our assumptions. Therefore, $g(a)=g(a+b)$ whenever $g(b)=0$.

A simple induction then gives that $g(n b)=0$ for any positive integer $n$, and $g(n b)=0$ for negative $n$ as $g(x)=g(-x)$. The claim follows immediately.

Lemma 3. There cannot be both positive and negative elements in the range of $g$.\\
Proof. Suppose that $g(x)>0$ and $g(y)<0$. Let $\mathcal{S}$ be the set of numbers of the form $m x+n y$ for integers $m, n$. We first show that $g(\mathcal{S})$ has infinitely many elements. Indeed, suppose $g(\mathcal{S})$ is finite, and let $a \in \mathcal{S}$ maximise $g$ and $b \in \mathcal{S}$ maximise $-g$. Then $a+b \in \mathcal{S}$, and $g(a+b)=g(a)-g(b)$ or $g(b)-g(a)$. In the first case $g(a+b)>g(a)$ and in the second case $g(a+b)<g(b)$; in either case we get a contradiction.

Now, we show that there must exist some nonzero rational number $q$ with $g(q)=0$. Indeed, suppose first that $a+f(a)=0$ for all $a$. Then $g(a)=f(a)+f(-a)=0$ for all $a$, and so $g$ takes no nonzero value. Otherwise, there is some $a$ with $a+f(a) \neq 0$, and so (1) yields that $f(q)=0$ for $q=a+f(a) \neq 0$. Noting that $f(-q)=0$ from Lemma 1 tells us that $g(q)=0$, as required.

Now, there must exist integers $s$ and $s^{\prime}$ such that $x s=q s^{\prime}$ and integers $t$ and $t^{\prime}$ such that $y t=q t^{\prime}$. The claim above gives that the value of $g(m x+n y)$ depends only on the values of $m \bmod s$ and $n \bmod t$, so $g(m x+n y)$ can only take finitely many values.

Finally, suppose that $g(x)=u$ and $g(y)=v$ where $u \neq v$ have the same sign. Assume $u, v>0$ (the other case is similar) and assume $u>v$ without loss of generality.\\
$P\left(f^{-1}(x), f^{-1}(y)\right)$ gives $x-y \sim f^{-1}(x)-f^{-1}(y)=f(x)-f(y)-(u-v)$, and $P(x, y)$ gives $x-y \sim f(x)-f(y) . u-v$ is nonzero, so $f(x-y)$ and $f^{-1}(x-y)$ must be $f(x)-f(y)-(u-v)$ and $f(x)-f(y)$ in some order, and since $g(x-y)$ must be nonnegative, we have

$$
f(x)-f(y)-(u-v) \rightarrow x-y \rightarrow f(x)-f(y) .
$$

Then, $P\left(x-y, f^{-1}(y)\right)$ tells us that $(x-y)+y \sim(f(x)-f(y))+(f(y)-v)$, so $x \sim f(x)-v$, contradicting either $v \neq u$ or $v>0$.

---

### A7comment
Lemma 2 also follows from $f(x+d)-f(x) \in\{f(d),-f(-d)\}$ as proven in

---

### A7sol2
Indeed, we also have $f(-x)-f(-x-d) \in\{f(d),-f(-d)\}$, and then subtracting the second from the first we get $g(x+d)-g(x) \in\{g(d),-g(d), 0\}$. Replacing $x+d$ and $x$ with $x$ and $-y$ gives the statement of Lemma 2.

---

### A7comment
It is possible to prove using Lemma 2 that $g$ must have image of the form $\{0, c, 2 c\}$ if it has size greater than 2 . Indeed, if $g(x)=c$ and $g(y)=d$ with $0<c<d$, then $g(x+y)=d-c$ as it must be nonnegative, and $g(y)=g((x+y)+(-x))=|d-2 c|$ provided that $d \neq 2 c$.

However, it is not possible to rule out $\{0, c, 2 c\}$ based entirely on the conclusion of Lemma 2; indeed, the function given by

$$
g(x)= \begin{cases}0, & \text { if } x=2 n \text { for } n \in \mathbb{Z} \\ 2, & \text { if } x=2 n+1 \text { for } n \in \mathbb{Z} \\ 1, & \text { if } x \notin \mathbb{Z}\end{cases}
$$

satisfies the conclusion of Lemma 2 (even though there is no function $f$ giving this choice of $g$ ).\\
Note. Solution 1 actually implies that the result also holds over $\mathbb{R}$. The proposal was originally submitted and evaluated over $\mathbb{Q}$ as it is presented here, and the Problem Selection Committee believes that this form is more suitable for the competition because it allows for more varied and interesting approaches once Lemma 1 has been established. Even the variant here defined over $\mathbb{Q}$ was found to be fairly challenging.

---

### A8sol1
Let $k=\left\lceil\frac{q}{p}\right\rceil$. Note that $k \geqslant 2$.\\
Lemma 1. If $i, j$ and $m$ are positive integers such that $|i-j| \leqslant m p$ then $\left|a_{i}-a_{j}\right| \leqslant m p$.\\
Proof. By the given condition, if $|i-j| \leqslant p$ then $\left|a_{i}-a_{j}\right| \leqslant p$. So the lemma follows from induction on $m$ and the triangle inequality.\\
Lemma 2. For a fixed $n$, suppose that $a_{i}$ is minimal over $i \geqslant n$. Then $i \leqslant n+p-1$.\\
Proof. Suppose for contradiction that $i \geqslant n+p$. Then $\min \left(a_{[i-p, i+q-p]}\right)=a_{i}$. Since $q-p \leqslant (k-1) p$, it follows from Lemma 1 that $\max \left(a_{[i-p, i+q-p]}\right) \leqslant a_{i}+(k-1) p<a_{i}+q$, which is a contradiction.

Lemma 3. For a fixed $n>q$, suppose that $a_{i}$ is maximal over $i \leqslant n$. Then $i \geqslant n-p+1$.\\
Proof. Suppose $a_{j}$ is minimal over $j \geqslant n-q$. Then by Lemma $2, j \leqslant n-q+p-1$. So $\min \left(a_{[n-q, n]}\right)=a_{j}$ and $a_{i} \geqslant \max \left(a_{[n-q, n]}\right)$, which implies that $a_{i} \geqslant a_{j}+q$.

Lemma 2 also implies that if $j \geqslant n$ then $a_{j} \geqslant \min \left(a_{[n, n+p]}\right)$. So if $i<j$, then we have $a_{j} \geqslant a_{i}-p$, which contradicts $a_{i} \geqslant a_{j}+q$. Hence we must have $i>j$.

The above inequality also gives $\left|a_{i}-a_{j}\right| \geqslant q>(k-1) p$, so by Lemma 1 it follows that $|i-j|>(k-1) p$. Therefore $i>j+(k-1) p \geqslant n-q+(k-1) p \geqslant n-p+1$.

Let $b_{n}$ be the minimal value of $a_{i}$ for $i \geqslant n$. By Lemma $2, b_{n+p}>b_{n}$ for all $n$. Hence $b_{n}=\min \left(a_{[n, n+p]}\right)=\min \left(a_{[n, n+q]}\right)$. Let $c_{n}$ be the maximal value of $a_{i}$ for $i \leqslant n$. By Lemma 3, $c_{n-p}>c_{n}$ for all $n>q$. Hence $c_{n}=\max \left(a_{[n-p, n]}\right)=\max \left(a_{[n-q, n]}\right)$ for $n>q$.

So if $n>q$ then $b_{n}=c_{n+p}-p=c_{n+q}-q$. So for $n>q$ we get $b_{n+q-p}+p=c_{n+q}=b_{n}+q$, and hence $b_{n+q-p}=b_{n}+q-p$.

Next note that $b_{n+p} \leqslant a_{n+p} \leqslant b_{n}+p$. So $b_{n+p}-b_{n} \leqslant p$ for all $n>q$, and iterating this $(q-p)$ times gives $b_{n+p(q-p)}-b_{n} \leqslant p(q-p)$. But using $b_{n+q-p}=b_{n}+q-p$ gives $b_{n+p(q-p)}-b_{n}=p(q-p)$. Since equality occurs, we must have $b_{n+p}=b_{n}+p$.

So for $n>q, b_{n+p}=b_{n}+p$ and $b_{n+q-p}=b_{n}+q-p$. Since $p$ and $q-p$ are coprime, $b_{n+1}=b_{n}+1$ for all $n>q$. The only way for $b_{n}$ and $b_{n+1}$ to be different is if $b_{n}=a_{n}$, so we deduce that $a_{n+1}=a_{n}+1$ and there is a constant $C$ such that $a_{n}=n+C$ for all $n>q$.

Finally, suppose $a_{n}=n+C$ for all $n \geqslant N$. Then $p=\max \left(a_{N-1}, N+C+p-1\right)- \min \left(a_{N-1}, N+C\right)$. So $a_{N-1}=N+C+p$ or $N+C-1$. Similarly, $a_{N-1}=N+C+q$ or $N+C-1$. Hence $a_{N-1}=N+C-1$. So, by induction, we have $a_{n}=n+C$ for all positive integers $n$. Since $a_{1} \geqslant 1, C$ is a nonnegative integer.

It is trivial to check that $a_{n}=n+C$ satisfies the given condition.

---

### A8comment
Here is a variant of

---

### A8sol1
Proceed up to proving $b_{n}-n$ is eventually periodic with period $q-p$. Then there is some minimal value of $b_{n}-n$. Suppose $n$ attains this minimal value. Since $b_{n+p}-n-p \leqslant b_{n}-n, n+p$ also attains this minimal value. And since $p$ and $q-p$ are coprime, all $n \geqslant q$ must attain this minimal value. Hence $b_{n+1}=b_{n}+1$ for all $n \geqslant q$. Finish as above.

---

### A8comment
It is also possible to solve the problem using a weaker version of Lemma 2 and without Lemma 3. For example, the following lemma plays a similar role.\\
Lemma 2'. Let $b_{n}^{\prime}=\min \left(a_{[n, n+p]}\right)$. Then $b_{n}^{\prime}<b_{n+p}^{\prime}$.\\

---

### A8comment
To solve the problem for sequences $a_{n}$ of arbitrary integers, we will use the following lemma.\\
Lemma 4. The sequence $a_{n}$ is either bounded above or bounded below.\\
Proof. Suppose that $a_{n}$ is unbounded above and below. Then there is some $i$ such that $a_{i}<a_{1}-p$. There is also some $j$ such that $a_{j}>\max \left(a_{[1, i]}\right)+q$. Now let $a_{l}$ be minimal amongst $a_{[1, j]}$. Since $a_{l} \leqslant a_{i}, a_{l}<a_{1}-p$ and $a_{l}<a_{j}-k p$. By Lemma $1,1+p<l<j-k p$. So $\min \left(a_{[l-p, l+q-p]}\right)=a_{l}$. By Lemma 1 again, $\max \left(a_{[l-p, l+q-p]}\right) \leqslant a_{l}+(k-1) p<a_{l}+q$, which is a contradiction.

From there, the solution above can be adapted to prove that $a_{n}=n+C$ for all $n$ or $a_{n}=-n+C$ for all $n$, where $C$ can be any constant integer.

---

### A8sol2
For $n, x \geqslant 1$, let the $x$-width of $n$ be $\max \left(a_{[n, n+x]}\right)-\min \left(a_{[n, n+x]}\right)$. We call a positive integer $x$ good if the $x$-width of $n$ is less than or equal to $x$ for all sufficiently large $n$, and we call $x$ very good if the $x$-width of $n$ is equal to $x$ for sufficiently large $n$.\\
Lemma 1. If $p^{\prime}$ is good and $q^{\prime}$ is very good with $p^{\prime}<q^{\prime}<2 p^{\prime}$, then $2 p^{\prime}-q^{\prime}$ is also good.\\
Proof. Note that $0<q^{\prime}-p^{\prime}<p^{\prime}<q^{\prime}$. Let $n$ be a sufficiently large positive integer. Then for $k \in\left[n+q^{\prime}-p^{\prime}, n+p^{\prime}\right]$, we have $a_{k} \geqslant \max \left(a_{\left[n, n+p^{\prime}\right]}\right)-p^{\prime}$ and $a_{k} \geqslant \max \left(a_{\left[n+q^{\prime}-p^{\prime}, n+q^{\prime}\right]}\right)-p^{\prime}$ since $p^{\prime}$ is good, which shows $a_{k} \geqslant \max \left(a_{\left[n, n+q^{\prime}\right]}\right)-p^{\prime}$. Similarly we get $a_{k} \leqslant \min \left(a_{\left[n, n+q^{\prime}\right]}\right)+p^{\prime}$.

Therefore, for all $k \in\left[n+q^{\prime}-p^{\prime}, n+p^{\prime}\right]$ we have $a_{k} \in\left[\max \left(a_{\left[n, n+q^{\prime}\right]}\right)-p^{\prime}, \min \left(a_{\left[n, n+q^{\prime}\right]}\right)+p^{\prime}\right]$. Thus, the $\left(2 p^{\prime}-q^{\prime}\right)$-width of $n+q^{\prime}-p^{\prime}$ is at most $\left(\min \left(a_{\left[n, n+q^{\prime}\right]}\right)+p^{\prime}\right)-\left(\max \left(a_{\left[n, n+q^{\prime}\right]}\right)-p^{\prime}\right)= 2 p^{\prime}-q^{\prime}$. The lemma follows.\\
Lemma 2. Let $p^{\prime}$ be a good number and $q^{\prime}$ a very good number with $p^{\prime}<q^{\prime}$. For sufficiently large $n$, take $s, t \in\left[n, n+q^{\prime}\right]$ such that $\min \left(a_{\left[n, n+q^{\prime}\right]}\right)=a_{s}$ and $\max \left(a_{\left[n, n+q^{\prime}\right]}\right)=a_{t}$. Then $s \in\left[n, n+p^{\prime}\right]$ and $t \in\left[n+q^{\prime}-p^{\prime}, n+q^{\prime}\right]$.\\
Proof. Lemma 2 and Lemma 3 from Solution 1 hold with $p$ and $q$ replaced by $p^{\prime}$ and $q^{\prime}$ by similar arguments. We can deduce the statement about $s$ from Lemma 2 of

---

### A8sol1
We can deduce the statement about $t$ from Lemma 3 of

---

### A8sol1
Lemma 3. If $p^{\prime}$ is good and $q^{\prime}$ is very good with $2 p^{\prime}<q^{\prime}$, then there exists a positive integer $r$ such that for all sufficiently large $n$, we have $a_{n+r}-a_{n} \geqslant r$.\\
Proof. Let $r=q^{\prime}-2 p^{\prime}$, and let $s$ and $t$ be as defined in Lemma 2 . Then consider the identity

$$
\left(a_{t}-a_{n+q^{\prime}-p^{\prime}}\right)+\left(a_{n+p^{\prime}+r}-a_{n+p^{\prime}}\right)+\left(a_{n+p^{\prime}}-a_{s}\right)=a_{t}-a_{s}=q^{\prime}
$$

By Lemma 2, we have $s \in\left[n, n+p^{\prime}\right]$ and $t \in\left[n+q^{\prime}-p^{\prime}, n+q^{\prime}\right]$, so $a_{n+p^{\prime}}-s \leqslant p^{\prime}$ and $a_{t}-a_{n+q^{\prime}-p^{\prime}} \leqslant p^{\prime}$. Combining these, we get $a_{n+p^{\prime}+r}-a_{n+p^{\prime}} \geqslant q^{\prime}-2 p^{\prime}=r$. This proves that $a_{n+r}-a_{n} \geqslant r$ for sufficiently large $n$.\\
Lemma 4. Suppose $(p, q) \neq(1,2)$. Then there exists a good number $p^{\prime}$ such that $2 p^{\prime}<q$.\\
Proof. Let $p^{\prime}$ be the smallest good positive integer. Note that $p$ is good, so $p^{\prime}$ exists and is less than $q$.

Suppose for contradiction that $2 p^{\prime} \geqslant q$. If $2 p^{\prime}>q$, then by Lemma $1,2 p^{\prime}-q$ is a good number strictly less than $p^{\prime}$, which contradicts minimality of $p^{\prime}$. If $2 p^{\prime}=q$, then $p^{\prime}<p<2 p^{\prime}$. So we can apply Lemma 1 with $q_{0}=p$ to get that $2 p^{\prime}-p$ is a good number that is strictly less than $p^{\prime}$, which again contradicts minimality.

If $(p, q)=(1,2)$ then the problem is easily solved. Otherwise, Lemmas 3 and 4 combined give us some $r>0$ such that $a_{n+r}-a_{n} \geqslant r$ for $n$ sufficiently large.

By iterating, we get $a_{n+p r}-a_{n} \geqslant p r$ for all sufficiently large $n$, and hence it follows that $a_{n+p}-a_{n}=p$. Similarly we get $a_{n+q}-a_{n}=q$. As $p$ and $q$ are coprime, we deduce that $a_{n+1}-a_{n}=1$ for sufficiently large $n$. Thus we get $a_{n}=n+C$ for sufficiently large $n$, and we can conclude by the same argument as

---

### A8sol1
\section*{Combinatorics}

---

### C1sol1
The answer can be achieved by the students finishing in the same order in every race. To show that this is the maximum, we will apply a series of modifications to the results of the races, each of which does not decrease the total score, such that after $k$ such modifications the first $k$ positions are the same in every race. Say that a student is scored on the $b^{\text {th }}$ place if their score is $a-b$ because they came in the top $b$ places in $a$ of the races and $b$ is minimal with this property for that student.

Supposing that the first $k-1$ positions are the same in every race, look at the students scored on the $k^{\text {th }}$ place. If there are no such students, let $\ell>k$ be minimal such that some student $S$ is scored on the $\ell^{\text {th }}$ place. Then, in every race where $S$ appears in any place from the $k^{\text {th }}$ through the $\ell^{\text {th }}$ inclusive (of which there must be at least $\ell$, otherwise $S$ would achieve a higher rating of 0 based on the $n^{\text {th }}$ place), reorder the students in places $k$ through $\ell$ so that $S$ finishes in the $k^{\text {th }}$ place instead (and otherwise the ordering of those students is arbitrary). Now $S$ is scored on the $k^{\text {th }}$ place, their score has gone up by $\ell-k$ and no other scores have gone down (some might have gone up as well).

Now we know that the first $k-1$ positions are the same in every race and at least one student is scored on the $k^{\text {th }}$ place. Pick one such student $S$. In each race where $S$ finishes behind the $k^{\text {th }}$ place, swap them with the student $T$ who finishes in the $k^{\text {th }}$ place, leaving the positions of all other students unchanged. Each such swap increases the score of $S$ by 1 and decreases the score of $T$ by at most 1 , so such swaps do not decrease the total score. At the end of this process, the first $k$ positions are the same in every race and the total score has not decreased.

Repeating this $n$ times yields the required result.\\

---

### C1comment
The following simpler approach to modifying results of races is tempting: find pairs of students $S$ and $T$ who are scored on places $k$ and $\ell$ respectively, where $k<\ell$, but where $S$ finishes after $T$ in some race, and swap the positions of those two students in that race so they finish in the same order as the places they are scored on. However, such a swap can decrease the total score; for example, suppose that $k=1$ and $\ell=4$, and in some race $S$ finishes $6^{\text {th }}$ and $T$ finishes $3^{\text {rd }}$; then swapping those students reduces the number of races contributing to $T$ 's score without increasing the number contributing to $S$ 's score.

---

### C1sol2
The answer can be achieved by having the same ranking for all $n$ races.\\
Note that taking $a=b=n$ shows each student has a nonnegative score. Consider a student who has race ranks $r_{1}, r_{2}, \ldots, r_{n}$ and a final score of $s$. We first prove that

$$
\sum_{i} r_{i} \leqslant n(n-s) .
$$

Without loss of generality, suppose that $r_{1} \leqslant r_{2} \leqslant \cdots \leqslant r_{n}$. There must exist some $k$ with $s+1 \leqslant k \leqslant n$ and $k-r_{k}=s$. In order to maximise $\sum_{i} r_{i}$ while retaining the score of $s$, we can\\
replace each of $r_{1}, \ldots, r_{k-1}$ by $r_{k}$, and replace each of $r_{k+1}, \ldots, r_{n}$ by $n$. Then the sum is


\begin{equation*}
\sum_{i} r_{i} \leqslant k r_{k}+(n-k) n=n^{2}-k\left(n-r_{k}\right)=n^{2}-k(n+s-k) \leqslant n^{2}-s_{n} \tag{1}
\end{equation*}


The final inequality follows from the fact that given $s+1 \leqslant k \leqslant n$, the quantity $k(n+s-k)$ is minimised when $k=n$.

The sum of ranks of all students across all races is $\frac{n^{2}(n+1)}{2}$. If the total of all student scores is $t$, then (1) implies

$$
\frac{n^{2}(n+1)}{2} \leqslant n^{3}-t n
$$

This rearranges to $t \leqslant \frac{n(n-1)}{2}$, as required.\\

---

### C1sol3
In each race, assign the student in the $k^{\text {th }}$ place a weight of $1-\frac{k}{n}$. If a student finishes in the top $b$ places in at least $a$ of the races, the total of their weights is at least $a\left(1-\frac{b}{n}\right)=a-b\left(\frac{a}{n}\right) \geqslant a-b$. Thus the sum of a student's weights across all races is at least their score, and so the sum of all weights for all students across all races is at least the sum of all the scores of all students. The sum of weights in each race is $\frac{n-1}{2}$, so the sum of all weights across all races is $\frac{n(n-1)}{2}$. Equality is achieved if and only if, for each student, the values of $b$ and $a$ determining that student's score have $a=n$ and they finish in exactly the $b^{\text {th }}$ place in all $n$ races; that is, if the students are ranked the same in every race.

---

### C1sol4
Given a positive integer $b(S)$ for each student $S$, define $a_{b}(S)$ to be the number of races in which $S$ finished in the top $b(S)$ places, and define $\operatorname{score}_{b}(S)=a_{b}(S)-b(S)$; for a race $r$, let $I_{b}(S, r)$ be 1 if $S$ finished in the top $b(S)$ places in race $r$ and 0 otherwise, so

$$
a_{b}(S)=\sum_{r} I_{b}(S, r)
$$

Then the problem asks for the maximum across all possible results of the races of

$$
\max _{b} \sum_{S} \operatorname{score}_{b}(S)=\max _{b}\left(\sum_{r} \sum_{S} I_{b}(S, r)-\sum_{S} b(S)\right) .
$$

Given $b$, the sum $\sum_{S} I_{b}(S, r)$ is maximised (not necessarily uniquely) for some choice of the rankings in race $r$, which is the same choice for every race. So the maximum possible sum of the scores of all the students occurs when all students are ranked the same in all races, which yields the given answer.

---

### C2sol1
We first show by induction that $n=2^{k}$ is a cool number. The base case of $n=2$ is trivial as there is no such $d$.

For induction, assume that $2^{k}$ is a cool number. We construct a numbering of a $2^{k+1} \times 2^{k+1}$ board that satisfies the conditions.

Take the $2^{k+1} \times 2^{k+1}$ board and divide it into four $2^{k} \times 2^{k}$ sub-boards. By assumption, there is some numbering $P$ of a $2^{k} \times 2^{k}$ board that satisfies the required condition; we write down the numbering $P$ in each sub-board. Next, add $2^{2 k}$ to every number in the second sub-board, add $2 \times 2^{2 k}$ to every number in the third sub-board, and add $3 \times 2^{2 k}$ to every number in the fourth sub-board. Then the numbers in the cells of the $2^{k+1} \times 2^{k+1}$ board are the numbers 1 to $2^{2(k+1)}$.

Now locate $2^{2 k}$ from the first sub-board, and swap it with $2^{2 k}+2^{k-1}$ from the second subboard. Locate $3 \times 2^{2 k}$ from the third sub-board, and swap it with $3 \times 2^{2 k}+2^{k-1}$ from the fourth sub-board.

We claim that this numbering of the $2^{k+1} \times 2^{k+1}$ board satisfies the required conditions. For any $d=2^{i}$ where $i<k$, consider any $2^{i} \times 2^{i}$ sub-board. The sum of its cells modulo $2^{i}$ is not changed in the addition step or the swapping step, so the sum is congruent modulo $2^{i}$ to the sum of the corresponding $2^{i} \times 2^{i}$ sub-board in $P$, which is nonzero, as required.

In the case of $d=2^{k}$, we can directly evaluate the sum of the $(b+1)^{\text {th }}$ sub-board for $b \in\{0,1,2,3\}$. The sum is given by

$$
2^{2 k-1}\left(1+2^{2 k}\right)+b 2^{4 k}+(-1)^{b} 2^{k-1} \equiv 2^{k-1} \quad\left(\bmod 2^{k}\right)
$$

Therefore all sub-boards satisfy the required conditions and so $2^{k+1}$ is a cool number, completing the induction.

It remains to show that no other even number is a cool number. Let $n=2^{s} m$ where $s$ is a positive integer and $m$ is an odd integer greater than 1 . For the sake of contradiction, suppose that there is a numbering of the $n \times n$ board satisfying the required conditions.\\
Claim. In the $2^{i}$-division of the board, where $1 \leqslant i \leqslant s$, the sum of numbers in each $2^{i} \times 2^{i}$ sub-board is congruent to $2^{i-1}$ modulo $2^{i}$.

Proof. We prove the claim by induction on $i$. The base case of $i=1$ holds as the sum of numbers in each $2 \times 2$ sub-board must be odd. Next, suppose the claim is true for $2^{i}$. In the $2^{i+1}$-division, each $2^{i+1} \times 2^{i+1}$ sub-board is made up of four $2^{i} \times 2^{i}$ sub-boards, each with a sum congruent to $2^{i-1}$ modulo $2^{i}$. Hence the sum of each $2^{i+1} \times 2^{i+1}$ sub-board is a multiple of $2^{i}$. It cannot be a multiple of $2^{i+1}$ because of the conditions, which means it must be congruent to $2^{i}$ modulo $2^{i+1}$. This proves the claim.

Back to the problem, since $m$ is odd, summing up the $m^{2}$ sums of $2^{s} \times 2^{s}$ sub-boards gives

$$
2^{s-1} m^{2} \equiv 2^{s-1} \quad\left(\bmod 2^{s}\right)
$$

However, the sum of the numbers from 1 to $n^{2}$ is

$$
\frac{n^{2}\left(n^{2}+1\right)}{2}=2^{2 s-1} m^{2}\left(2^{2 s} m^{2}+1\right) \equiv 0 \quad\left(\bmod 2^{s}\right)
$$

This is a contradiction. Therefore $n$ is not a cool number.\\

---

### C2comment
In the case of odd $n$, similar arguments show that prime powers are cool numbers. If the definition of cool numbers additionally requires that all $d \times d$ sub-boards in the $d$-division have the same nonzero residue modulo $d$, then the cool numbers are precisely the prime powers.

---

### C3sol1
Join each pair of knights with a chord across the table. We'll refer to these chords as chains.

First we show that $n(n-1) / 2$ exchanges are required for some arrangements.\\
Lemma 1. If each knight is initially sitting directly opposite her partner, then at least $n(n-1) / 2$ exchanges are required for all knights to meet and shake hands with their partners.

Proof 1. In this arrangement any two chains are initially intersecting. For two knights to be adjacent to each other, it is necessary that their chain does not cross any other chain, and thus every pair of chains must be uncrossed at some time. Each exchange of adjacent knights can only uncross a single pair of intersecting chains, and thus the number of exchanges required is at least the number of pairs of chains, which is $n(n-1) / 2$.

Proof 2. In this arrangement the two knights in each pair are initially separated by $n-1$ seats in either direction around the table, and so each pair must move a total of at least $n-1$ steps so as to be adjacent. There are $n$ pairs, and each exchange moves two knights by a single step. Hence at least $n(n-1) / 2$ moves are required.

We will now prove that $n(n-1) / 2$ exchanges is sufficient in all cases. We'll prove a stronger version of this bound than is required, namely that every knight can shake hands with her partner at the end, after all exchanges have finished.

Begin by adding a pillar at the centre of the table. For each chain that passes through the centre of the table, we arbitrarily choose one side of the chain and say that the pillar lies on that side of the chain. While the pillar may lie on a chain, we will never move a knight if that causes the pillar to cross to the other side of a chain. Say that a chain passes in front of a knight if it passes between that knight and the pillar, and define the length of a chain to be the number of knights it passes in front of. Then each chain has a length between 0 and $n-1$ inclusive.

Say that a chain $C$ encloses another chain $C^{\prime}$ if $C$ and $C^{\prime}$ do not cross, and $C$ passes between $C^{\prime}$ and the pillar. Say that two chains are intersecting if they cross on the table; enclosing if one chain encloses the other; and disjoint otherwise. Let $k, l$ and $m$ denote respectively the number of enclosing, intersecting and disjoint pairs of chains. Then we have

$$
k+l+m=\frac{n(n-1)}{2}
$$

Lemma 2. $2 k+l$ exchanges are sufficient to reach a position with all pairs of knights sitting adjacent to each other.\\
Proof 1. We proceed by induction on $2 k+l$.\\
If every chain has length 0 , then every pair of knights is adjacent and the statement is trivial.

Otherwise, let $A$ and $B$ be a pair of knights whose chain $C_{0}$ has length $q \geqslant 1$. Let $S_{0}=A$, and let $S_{1}, \ldots, S_{q}$ be the knights which $C_{0}$ passes in front of, sitting in that order from $A$ to $B$. We know that $C_{0}$ passes in front of $S_{1}$, and there are three cases for the chain $C_{1}$ for knight $S_{1}$.

If $C_{1}$ passes in front of $S_{0}$ then $C_{0}$ and $C_{1}$ are intersecting, and we can make them disjoint by exchanging the positions of $S_{0}$ and $S_{1}$. This reduces the sum $2 k+l$ by 1 .

If $C_{1}$ passes in front of neither $S_{0}$ nor $B$ then $C_{1}$ is enclosed by $C_{0}$, and we can swap $S_{0}$ and $S_{1}$ to make $C_{0}$ and $C_{1}$ an intersecting pair. This increases $l$ by 1 and decreases $k$ by 1 , and hence reduces the sum $2 k+l$ by 1 .

If this $C_{1}$ passes in front of $B$ then we cannot immediately find a beneficial exchange.\\
In the third case, we look instead at the knights $S_{i}$ and $S_{i+1}$, for each $i$ in turn. Each time, we will either find a beneficial exchange, or find that the chain $C_{i+1}$ for knight $S_{i+1}$ passes in front of $B$. Eventually we will either find a beneficial exchange in one of the first two cases above, or we will find that the chain $C_{q}$ for $S_{q}$ passes in front of $B$, in which case $C_{q}$ and $C_{0}$ are intersecting and we can make $C_{q}$ and $C_{0}$ disjoint by swapping $S_{q}$ and $B$.

Also note that the only times a chain is increased in length is when it is enclosed by another chain. But this cannot happen for a chain containing the pillar, so no chains ever cross the pillar.

Proof 2. We begin by ignoring the seats, and let each knight walk freely to a predetermined destination. Each pair of knights will walk around the table to one of the two points on the circumference midway between their initial locations, such that the chain between them passes between the pillar and the destination. If more than one pair of knights would have the same destination point, then we make small adjustments to the destination points so that each pair has a distinct destination point.

We then imagine each knight walking at a constant speed (which may be different for each knight). They all start and stop walking at the same time. We want to count how many times two knights pass (either in opposite directions, or in the same direction but at different speeds). For any two pairs of knights, the number of passes depends on the relation between their two chains.

If their two chains are intersecting then there will be one pass, involving the two knights for whom the other chain passes between them and the pillar.

If their two chains are enclosing then there will be two passes, with one of the knights with the enclosing chain passing both of the knights with the shorter enclosed chain.

If their two chains are disjoint then there will be no passes.\\
The number of passes is therefore $2 k+l$. If multiple pairs of knights would pass at the same time, we can slightly adjust the walking speeds so that the passes happen at distinct times. We can then convert this sequence of passes into a sequence of seat exchanges in the original problem, which shows that $2 k+l$ exchanges is sufficient.

\section*{Lemma 3. $k \leqslant m$.}
Proof 1. We proceed by induction on $n$. The base case $n=2$ is clear.\\
Consider a chain $C$ of greatest length, and suppose it joins knights $A$ and $B$. Let $x$ be the number of chains that intersect $C$, and let $y$ be the number of chains that are enclosed by $C$. Note that no chain can enclose $C$. Then $C$ passes in front of one knight from each pair whose chain intersects $C$, and both knights in any pair whose chain is enclosed by $C$. Thus the length of $C$ is $x+2 y \leqslant n-1$. The number of chains that form a disjoint pair with $C$ is then

$$
n-1-x-y \geqslant(x+2 y)-x-y=y
$$

Now we can remove $A$ and $B$ and use the induction hypothesis. We need to show that the length of each remaining chain is at most $n-2$ so the chains remain valid. No chain increases in length after removing $A$ and $B$. If any chain $C$ had length $n-1$, then the chain between $A$ and $B$ also had length $n-1$. Then $C$ must have passed in front of exactly one of $A$ or $B$, and so has length $n-2$ after removing $A$ and $B$.\\
Proof 2. Let $k_{C}$ denote the number of chains $C^{\prime}$ such that $C$ encloses $C^{\prime}$.\\
Note that if $C$ encloses $C^{\prime}$, then $k_{C^{\prime}}<k_{C}$.\\
First we will show that there at least $k_{C}$ chains that are disjoint from $C$. Let $x$ be the length of $C$, let $\mathcal{S}$ be the set of $x$ knights that $C$ passes in front of, and let $\mathcal{T}$ be the set of $x$ knights sitting directly opposite them. None of the knights in $\mathcal{T}$ can have a chain that encloses or is enclosed by $C$, and if any knight in $\mathcal{T}$ has a chain that intersects $C$, then her partner must be a knight in $\mathcal{S}$. So we have that

$$
\begin{aligned}
2 k_{C} & =\text { number of knights in } \mathcal{S} \text { whose chain is enclosed by } C \\
& =x-\text { number of knights in } \mathcal{S} \text { whose chain intersects } C \\
& \leqslant x-\text { number of knights in } \mathcal{T} \text { whose chain intersects } C \\
& \leqslant \text { number of knights in } \mathcal{T} \text { whose chain is disjoint from } C \\
& \leqslant 2 \times \text { number of chains that are disjoint from } C .
\end{aligned}
$$

Now let $m_{C}$ denote the number of chains $C^{\prime}$ with $C$ and $C^{\prime}$ disjoint, and $k_{C^{\prime}}<k_{C}$. We will show that $m_{C} \geqslant k_{C}$.

Let $\mathcal{R}$ be a set of $k_{C}$ chains that are disjoint from $C$, such that $\sum_{C^{\prime} \in \mathcal{R}} k_{C^{\prime}}$ is minimal. If every chain $C^{\prime} \in \mathcal{R}$ has $k_{C^{\prime}}<k_{C}$, then we are done. Otherwise, let consider a chain $C^{\prime}$ with $k_{C^{\prime}} \geqslant k_{C}$. There are then at least $k_{C}$ chains $C^{\prime \prime}$ for which the chain $C^{\prime}$ passes between $C^{\prime \prime}$ and the pillar. Each of these chains must have $k_{C^{\prime \prime}}<k_{C^{\prime}}$, and at least one of them is not in $\mathcal{R}$ (otherwise $\mathcal{R}$ would contain $C^{\prime}$ and at least $k_{C}$ other chains), so we can swap this chain with $C^{\prime}$ to obtain a set $\mathcal{R}^{\prime}$ with $\sum_{C^{\prime} \in \mathcal{R}^{\prime}} k_{C^{\prime}}<\sum_{C^{\prime} \in \mathcal{R}} k_{C^{\prime}}$. But this contradicts the minimality of $\mathcal{R}$.

We finish by summing these inequalities over all chains $C$ :

$$
k=\sum_{C} k_{C} \leqslant \sum_{C} m_{C} \leqslant m
$$

By Lemma 3, we have that $2 k+l \leqslant k+l+m=n(n-1) / 2$. Combining this with Lemma 2, we have that $n(n-1) / 2$ exchanges is enough to reach an arrangement where every knight is sitting next to her partner, as desired.

---

### C3comment
Either proof of Lemma 3 can be adapted to show that the configuration in Lemma 1 is the only one which achieves the bound.

---

### C4sol1
First we demonstrate that there is no winning strategy if Turbo has 2 attempts.\\
Suppose that $(2, i)$ is the first cell in the second row that Turbo reaches on his first attempt. There can be a monster in this cell, in which case Turbo must return to the first row immediately, and he cannot have reached any other cells past the first row.

Next, suppose that $(3, j)$ is the first cell in the third row that Turbo reaches on his second attempt. Turbo must have moved to this cell from $(2, j)$, so we know $j \neq i$. So it is possible that there is a monster on $(3, j)$, in which case Turbo also fails on his second attempt. Therefore Turbo cannot guarantee to reach the last row in 2 attempts.

Next, we exhibit a strategy for $n=3$. On the first attempt, Turbo travels along the path

$$
(1,1) \rightarrow(2,1) \rightarrow(2,2) \rightarrow \cdots \rightarrow(2,2023) .
$$

This path meets every cell in the second row, so Turbo will find the monster in row 2 and his attempt will end.

If the monster in the second row is not on the edge of the board (that is, it is in cell $(2, i)$ with $2 \leqslant i \leqslant 2022$ ), then Turbo takes the following two paths in his second and third attempts:

$$
\begin{aligned}
& (1, i-1) \rightarrow(2, i-1) \rightarrow(3, i-1) \rightarrow(3, i) \rightarrow(4, i) \rightarrow \cdots \rightarrow(2024, i) . \\
& (1, i+1) \rightarrow(2, i+1) \rightarrow(3, i+1) \rightarrow(3, i) \rightarrow(4, i) \rightarrow \cdots \rightarrow(2024, i) .
\end{aligned}
$$

The only cells that may contain monsters in either of these paths are ( $3, i-1$ ) and ( $3, i+1$ ). At most one of these can contain a monster, so at least one of the two paths will be successful.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-046}
\captionsetup{labelformat=empty}
\caption{Figure 1: Turbo's first attempt, and his second and third attempts in the case where the monster on the second row is not on the edge. The cross indicates the location of a monster, and the shaded cells are cells guaranteed to not contain a monster.}
\end{center}
\end{figure}

If the monster in the second row is on the edge of the board, without loss of generality we may assume it is in $(2,1)$. Then, on the second attempt, Turbo takes the following path:

$$
(1,2) \rightarrow(2,2) \rightarrow(2,3) \rightarrow(3,3) \rightarrow \cdots \rightarrow(2022,2023) \rightarrow(2023,2023) \rightarrow(2024,2023) .
$$

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-046(1)}
\captionsetup{labelformat=empty}
\caption{Figure 2: Turbo's second and third attempts in the case where the monster on the second row is on the edge. The light gray cells on the right diagram indicate cells that were visited on the previous attempt. Note that not all safe cells have been shaded.}
\end{center}
\end{figure}

If there are no monsters on this path, then Turbo wins. Otherwise, let $(i, j)$ be the first cell on which Turbo encounters a monster. We have that $j=i$ or $j=i+1$. Then, on the third attempt, Turbo takes the following path:

$$
\begin{aligned}
(1,2) & \rightarrow(2,2) \rightarrow(2,3) \rightarrow(3,3) \rightarrow \cdots \rightarrow(i-2, i-1) \rightarrow(i-1, i-1) \\
& \rightarrow(i, i-1) \rightarrow(i, i-2) \rightarrow \cdots \rightarrow(i, 2) \rightarrow(i, 1) \\
& \rightarrow(i+1,1) \rightarrow \cdots \rightarrow(2023,1) \rightarrow(2024,1) .
\end{aligned}
$$

\section*{Now note that}
\begin{itemize}
  \item The cells from $(1,2)$ to $(i-1, i-1)$ do not contain monsters because they were reached earlier than $(i, j)$ on the previous attempt.
  \item The cells $(i, k)$ for $1 \leqslant k \leqslant i-1$ do not contain monsters because there is only one monster in row $i$, and it lies in $(i, i)$ or $(i, i+1)$.
  \item The cells $(k, 1)$ for $i \leqslant k \leqslant 2024$ do not contain monsters because there is at most one monster in column 1 , and it lies in $(2,1)$.
\end{itemize}

Therefore Turbo will win on the third attempt.\\

---

### C4comment
A small variation on Turbo's strategy when the monster on the second row is on the edge is possible. On the second attempt, Turbo can instead take the path

$$
\begin{aligned}
(1,2023) & \rightarrow(2,2023) \rightarrow(2,2022) \rightarrow \cdots \rightarrow(2,3) \rightarrow(2,2) \rightarrow(2,3) \rightarrow \cdots \rightarrow(2,2023) \\
& \rightarrow(3,2023) \rightarrow(3,2022) \rightarrow \cdots \rightarrow(3,4) \rightarrow(3,3) \rightarrow(3,4) \rightarrow \cdots \rightarrow(3,2023) \\
& \rightarrow \cdots \\
& \rightarrow(2022,2023) \rightarrow(2022,2022) \rightarrow(2022,2023) \\
& \rightarrow(2023,2023) \\
& \rightarrow(2024,2023) .
\end{aligned}
$$

If there is a monster on this path, say in cell $(i, j)$, then on the third attempt Turbo can travel straight down to the cell just left of the monster instead of following the path traced out in the second attempt.

$$
\begin{aligned}
(1, j-1) & \rightarrow(2, j-1) \rightarrow \cdots \rightarrow(i-1, j-1) \rightarrow(i, j-1) \\
& \rightarrow(i, j-2) \rightarrow \cdots \rightarrow(i, 2) \rightarrow(i, 1) \\
& \rightarrow(i+1,1) \rightarrow \cdots \rightarrow(2023,1) \rightarrow(2024,1) .
\end{aligned}
$$

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-047}
\captionsetup{labelformat=empty}
\caption{Figure 3: Alternative strategy for Turbo's second and third attempts.}
\end{center}
\end{figure}

---

### C5sol1
}
Lemma 1. For any set $\mathcal{S}, \mathcal{S}$ wins if and only if $J(\mathcal{S}, \varnothing)$ wins. Similarly, $\mathcal{S}$ wins if and only if $J(\varnothing, \mathcal{S})$ wins.\\
Proof. Let ( $k, m$ ) be a move on $\mathcal{S}$, and let $\mathcal{T}$ be the result of applying the move. Then we can reduce $J(\mathcal{S}, \varnothing)$ to $J(\mathcal{T}, \varnothing)$ by applying the move ( $k+1,2 m-1$ ).

Conversely, let $(k, m)$ be a move on $J(\mathcal{S}, \varnothing)$. We can express the result of this move as $J(\mathcal{T}, \varnothing)$ for some $\mathcal{T}$. Then we can reduce $\mathcal{S}$ to $\mathcal{T}$ by applying the move ( $\max (k-1,0),(k+1) / 2$ ).

This gives us a natural bijection between games starting with $\mathcal{S}$ and games starting with $J(\mathcal{S}, \varnothing)$ and thus proves the first part of the lemma. The second part follows by a similar argument.\\
Lemma 2. If $\mathcal{S}$ and $\mathcal{T}$ are nonempty and at least one of them loses, then $J(\mathcal{S}, \mathcal{T})$ wins.\\
Proof. If $\mathcal{S}$ is losing, then we can delete $J(\varnothing, \mathcal{T})$ using the move ( $1, t$ ) for some $t \in J(\varnothing, \mathcal{T})$, which leaves the losing set $J(\mathcal{S}, \varnothing)$. Similarly, if $\mathcal{T}$ is losing, then we can delete $J(\mathcal{S}, \varnothing)$ using the move ( $1, s$ ) for some $s \in J(\mathcal{S}, \varnothing$ ), leaving the losing set $J(\varnothing, \mathcal{T})$.\\
Lemma 3. If $\mathcal{S}$ is nonempty and wins, then $J(\mathcal{S}, \mathcal{S})$ loses.\\
Proof. From this position, we can convert any sequence of moves into another valid sequence of moves by replacing ( $k, 2 n-1$ ) with ( $k, 2 n$ ), and vice versa. Thus we may assume that the initial move ( $k, m$ ) has $m$ odd. We want to show that any such move results in a winning position for the other player.

The move $(0, m)$ loses immediately. Otherwise, the move results in the set $J(\mathcal{T}, \mathcal{S})$ for some set $\mathcal{T}$. There are three cases.

If $\mathcal{T}$ is empty then the other player gets the winning set $J(\varnothing, \mathcal{S})$.\\
If $\mathcal{T}$ is losing then the other player can choose the move ( $1, s$ ) for some $s \in J(\varnothing, \mathcal{S})$, which leaves the losing set $J(\mathcal{T}, \varnothing)$.

If $\mathcal{T}$ is nonempty winning then the other player can choose the move ( $k, m+1$ ), which results in the position $J(\mathcal{T}, \mathcal{T})$. We can then proceed by induction on $|\mathcal{S}|$ to show that this is a losing set.

Lemma 4. [2n] wins if and only if [ $n$ ] loses.\\
Proof. Note that $[2 n]=J([n],[n])$. The result then follows directly from the previous two lemmas.

Lemma 5. For any integer $n \geqslant 1,[2 n+1]$ wins.\\
Proof. By Lemma 4, either $[n]$ or $[2 n]$ loses. If $[n]$ loses, then by Lemma 2 we have that $[2 n+1]=J([n+1],[n])$ wins. Otherwise, $[2 n]$ loses, and therefore $[2 n+1]$ wins by choosing the move ( $k, 2 n+1$ ) for sufficiently large $k$ so that only $2 n+1$ is eliminated.

It remains to verify the original answer. We have two cases to consider:

\begin{itemize}
  \item Suppose $N=2^{n}$ for some $n$. For $N=1$, every move is an instant loss for Geoff. Then by Lemma 4, Geoff wins for $N=2^{n}$ if and only if Geoff loses for $N=2^{n-1}$, and thus by induction we have that Geoff wins for $N=2^{n}$ if and only if $n$ is odd.
  \item Otherwise, $N=t 2^{n}$, for some $n$ and some $t>1$ with $t$ odd. By Lemma 5, Geoff wins when $n=0$. Then by Lemma 4, Geoff wins for $N=t 2^{n}$ if and only if Geoff loses for $N=t 2^{n-1}$, and thus by induction on $n$ we have that Geoff wins for $N=t 2^{n}$ if and only if $n$ is even.
\end{itemize}

---

### C5comment
We can represent this game as a game on partial binary trees. This representation could be common in rough working, as it facilitates exploration of small cases. If two sets produce trees which are topologically equivalent, then this equivalence leads to a natural bijection between games starting with the two sets. Such equivalences lead to a significant reduction in the number of distinct cases that need to be considered when exploring the game for small $N$.

The construction is as follows. First we begin by considering an infinite binary tree. For each positive integer $n$, we consider the binary representation of $n-1$, starting with the least significant bit and ending with an infinite sequence of leading zeroes. We map this sequence of bits to a path on the binary tree by starting at the root, and then repeatedly choosing the left child if the bit is 0 and the right child if the bit is 1 . We can then truncate each path after reaching a sufficient depth to distinguish the path from all other paths in the tree.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-049}

Valid moves in this representation of the game consist of selecting a node with two children, and removing either the left child or the right child (and its descendants). Selecting and removing the entire graph is also an allowed move (which loses instantly).

Two trees have equivalent games if they're topologically identical. This equivalence includes swapping the left and right children of any single node, or removing a node with a single child by merging the edges above and below it (and decreasing the depth of its children by one).

---

### C5comment
We can also analyse this game using Grundy values (also known as nim-values or nimbers). This requires a slight modification to the rules, wherein any move that would erase all integers on the board is disallowed, and the first player who cannot move loses. This is clearly equivalent to the original game.

Let $g(\mathcal{S})$ denote the Grundy value of the game starting with the set $\mathcal{S}$. Note that the bijection in Lemma 1 shows that

$$
g(\mathcal{S})=g(J(\mathcal{S}, \varnothing))=g(J(\varnothing, \mathcal{S})) .
$$

For any set $V$, let $\operatorname{mex}(V)$ denote the least nonnegative element that is not an element of $V$. For nonnegative integers $x$ and $y$, define $j(x, y)$ recursively as

$$
j(x, y)=\operatorname{mex}(\{x, y\} \cup\{j(w, y) \mid w<x\} \cup\{j(x, z) \mid z<y\}) .
$$

The values of $j(x, y)$ for small $x$ and $y$ are:

\begin{center}
\begin{tabular}{c|cccccc}
5 & 6 & 7 & 8 & 9 & 1 & 0 \\
4 & 5 & 3 & 6 & 2 & 0 & 1 \\
3 & 4 & 5 & 1 & 0 & 2 & 9 \\
2 & 3 & 4 & 0 & 1 & 6 & 8 \\
1 & 2 & 0 & 4 & 5 & 3 & 7 \\
0 & 1 & 2 & 3 & 4 & 5 & 6 \\
\hline
- & 0 & 1 & 2 & 3 & 4 & 5 \\
\hline
\end{tabular}
\end{center}

We can show that $g(J(\mathcal{S}, \mathcal{T}))=j(g(\mathcal{S}), g(\mathcal{T}))$ for any nonempty sets $\mathcal{S}$ and $\mathcal{T}$. The remainder of the proof follows a similar structure to the given solution.

This page is intentionally left blank

---

### C6sol1
We must have $T \geqslant 4 n$, as otherwise we can never move the marble of weight $4 n$. We will show that $T=4 n$ by showing that, for any initial configuration, there is a sequence of moves, never increasing the absolute value of the difference above $4 n$, that results in every marble ending up on the opposite side of the scale. Because moves are reversible, it suffices to do the following: exhibit at least one configuration $C$ for which this can be achieved, and show that any initial configuration can reach such a configuration $C$ by some sequence of moves.

Consider partitioning the weights into pairs ( $t, 4 n+1-t$ ). Suppose that each side of the balance contains $n$ of those pairs. If one side of the balance contains the pair ( $t, 4 n+1-t$ ) for $1 \leqslant t<2 n$ and the other side contains ( $2 n, 2 n+1$ ), then the following sequence of moves swaps those pairs between the sides without ever increasing the absolute value of the difference above $4 n$.


\begin{gather*}
t, 4 n+1-t \mid 2 n, 2 n+1  \tag{1}\\
t, 2 n, 4 n+1-t \mid 2 n+1  \tag{2}\\
t, 2 n \mid 2 n+1,4 n+1-t  \tag{3}\\
t, 2 n, 2 n+1 \mid 4 n+1-t  \tag{4}\\
2 n, 2 n+1 \mid t, 4 n+1-t \tag{5}
\end{gather*}


Applying this sequence twice swaps any two pairs ( $t, 4 n+1-t$ ) and ( $t^{\prime}, 4 n+1-t^{\prime}$ ) between the sides. So we can achieve an arbitrary exchange of pairs between the sides, and $C$ can be any configuration where each side of the balance contains $n$ of those pairs.

We now show that any initial configuration can reach one where each side has $n$ of those pairs. Consider a configuration where one side has total weight $A-s$ and the other has total weight $A+s$, for some $0 \leqslant s \leqslant 2 n$, and where some pair is split between the two sides. (If no pair is split between the two sides, they must have equal weights and we are done.) Valid moves include moving any weight $w$ with $1 \leqslant w \leqslant 2 n+s$ from the $A+s$ side to the $A-s$ side, and moving any weight $w$ with $1 \leqslant w \leqslant 2 n-s$ from the $A-s$ side to the $A+s$ side. Suppose the pair ( $t, 4 n+1-t$ ), with $t \leqslant 2 n$, is split between the sides. If $t$ is on the $A+s$ side, or on the $A-s$ side and $t \leqslant 2 n-s$, it can be moved to the other side. Otherwise, $t$ is on the $A-s$ side and $t \geqslant 2 n-s+1$, so $4 n+1-t \leqslant 2 n+s$ is on the $A+s$ side and can be moved to the other side. So we can unite the two weights from that pair without splitting any other pair, and repeating this we reach a configuration where no pair is split between the sides.

---

### C6sol2
As in Solution 1, $T \geqslant 4 n$. Let $\delta$ be the weight of the left side minus the weight of the right side. A configuration is called legal if $|\delta| \leqslant 4 n$, and a move is legal if it results in a legal configuration. We will show that if $\delta=0$ then there is a sequence of legal moves after which every marble is on the opposite side.

We treat the $n=1$ case separately. The initial configuration has marbles 1,4 on one side and 2,3 on the other. So moving marbles 2, 4, 3, 1 in that order is legal and every marble ends on the opposite side. Now assume $n \geqslant 2$.

Marbles of weight at most $2 n$ are called small. We will make use of the following lemmas:\\
Lemma 1. If a pair of legal configurations differ only in the locations of small marbles then there is a sequence of legal moves to get from one to the other.\\
Proof. At first we only move marbles in the wrong position if they are not on the lighter side. (In the case of a tie, neither side is lighter.) Such a move is always legal. Since this reduces the number of marbles in the wrong position, eventually it will no longer be possible to perform such a move.

Then the only marbles in the wrong position are on the lighter side. So moving one marble in the wrong position at a time will always increase $|\delta|$, and $|\delta| \leqslant 4 n$ at the end. Hence every move is legal.

Lemma 2. Let $k \in \mathbb{N}$. A positive integer can be expressed as a sum of distinct positive integers up to $k$ if and only if it is at most $k(k+1) / 2$.\\
Proof. The maximum possible sum of distinct positive integers up to $k$ is $k(k+1) / 2$. For the other direction we use induction on $k$. The case $k=1$ is trivial. Assume the statement is true for $k-1$. For positive integers up to $k$ we only need a single term. For larger integers, including $k$ in the expression means we are done by the inductive hypothesis.

Also note that $n(2 n+1) \geqslant 4 n$ for $n \geqslant 2$.\\
Let $2 n<m \leqslant 4 n$. Marbles of weight greater than $m$ are called big and marbles from $2 n+1$ to $m$ are called medium.

Suppose all big marbles are on the correct side (that is, opposite where they started), $m$ is on the incorrect side and the configuration is legal. Then the following steps give a sequence of legal moves after which $m$ is on the correct side and the big marbles were never moved.

Assume $m$ is on the left. In Step 2, we rearrange the small marbles so we can move $m$. But this is only possible if the weight of big and medium marbles on the right is not too large. So we may need to move some medium marbles from the right first, which we do in Step 1.

Step 1 Skip to Step 2 if the total weight of medium and big marbles on the right side is at most $n(4 n+1)+2 n-m$. Since the big marbles are in the correct position and $m$ is in the incorrect position, the big marbles on the right can weigh at most $n(4 n+1)-m$. So there must be a medium marble $m^{\prime}<m$ on the right.\\
From the first assumption, it is legal to move all small marbles to the left. Then by Lemma 2 we can move some of the small marbles to the right so the right side has weight exactly $n(4 n+1)+2 n$. Then moving $m^{\prime}$ is legal. Repeat this step. Since the total weight of medium marbles on the right decreases, this step will occur a bounded number of times.

Step 2 Let the total weight of the right side be $n(4 n+1)+2 n-m+x$ and the weight of small marbles on the right side be $y$. Note that $y \geqslant x$. If $x \leqslant 0$ then moving $m$ is legal.\\
Otherwise, by Lemma 2 there is a set of small marbles of weight $y-x$. By Lemma 1, there is a sequence of legal moves of small marbles such that the right side has weight exactly $n(4 n+1)+2 n-m$. Now moving $m$ is legal.

Applying the process above for $m=4 n, 4 n-1, \ldots, 2 n+1$ will move all nonsmall marbles to the opposite side. Then Lemma 1 completes the proof.

---

### C7sol1
Let $M>\max \left(a_{1}, \ldots, a_{N}\right)$. We first prove that some integer appears infinitely many times. If not, then the sequence contains arbitrarily large integers. The first time each integer larger than $M$ appears, it is followed by a 1 . So 1 appears infinitely many times, which is a contradiction.

Now we prove that every integer $x \geqslant M$ appears at most $M-1$ times. If not, consider the first time that any $x \geqslant M$ appears for the $M^{\text {th }}$ time. Up to this point, each appearance of $x$ is preceded by an integer which has appeared $x \geqslant M$ times. So there must have been at least $M$ numbers that have already appeared at least $M$ times before $x$ does, which is a contradiction.

Thus there are only finitely many numbers that appear infinitely many times. Let the largest of these be $k$. Since $k$ appears infinitely many times there must be infinitely many integers greater than $M$ which appear at least $k$ times in the sequence, so each integer $1,2, \ldots, k-1$ also appears infinitely many times. Since $k+1$ doesn't appear infinitely often there must only be finitely many numbers which appear more than $k$ times. Let the largest such number be $l \geqslant k$. From here on we call an integer $x$ big if $x>l$, medium if $l \geqslant x>k$ and small if $x \leqslant k$. To summarise, each small number appears infinitely many times in the sequence, while each big number appears at most $k$ times in the sequence.

Choose a large enough $N^{\prime}>N$ such that $a_{N^{\prime}}$ is small, and in $a_{1}, \ldots, a_{N^{\prime}}$ :

\begin{itemize}
  \item every medium number has already made all of its appearances;
  \item every small number has made more than $\max (k, N)$ appearances.
\end{itemize}

Since every small number has appeared more than $k$ times, past this point each small number must be followed by a big number. Also, by definition each big number appears at most $k$ times, so it must be followed by a small number. Hence the sequence alternates between big and small numbers after $a_{N^{\prime}}$.\\
Lemma 1. Let $g$ be a big number that appears after $a_{N^{\prime}}$. If $g$ is followed by the small number $h$, then $h$ equals the amount of small numbers which have appeared at least $g$ times before that point.\\
Proof. By the definition of $N^{\prime}$, the small number immediately preceding $g$ has appeared more than $\max (k, N)$ times, so $g>\max (k, N)$. And since $g>N$, the $g^{\text {th }}$ appearance of every small number must occur after $a_{N}$ and hence is followed by $g$. Since there are $k$ small numbers and $g$ appears at most $k$ times, $g$ must appear exactly $k$ times, always following a small number after $a_{N}$. Hence on the $h^{\text {th }}$ appearance of $g$, exactly $h$ small numbers have appeared at least $g$ times before that point.

Denote by $a_{[i, j]}$ the subsequence $a_{i}, a_{i+1}, \ldots, a_{j}$.\\
Lemma 2. Suppose that $i$ and $j$ satisfy the following conditions:\\
(a) $j>i>N^{\prime}+2$,\\
(b) $a_{i}$ is small and $a_{i}=a_{j}$,\\
(c) no small value appears more than once in $a_{[i, j-1]}$.

Then $a_{i-2}$ is equal to some small number in $a_{[i, j-1]}$.

Proof. Let $\mathcal{I}$ be the set of small numbers that appear at least $a_{i-1}$ times in $a_{[1, i-1]}$. By Lemma 1, $a_{i}=|\mathcal{I}|$. Similarly, let $\mathcal{J}$ be the set of small numbers that appear at least $a_{j-1}$ times in $a_{[1, j-1]}$. Then by Lemma $1, a_{j}=|\mathcal{J}|$ and hence by (b), $|\mathcal{I}|=|\mathcal{J}|$. Also by definition, $a_{i-2} \in \mathcal{I}$ and $a_{j-2} \in \mathcal{J}$.

Suppose the small number $a_{j-2}$ is not in $\mathcal{I}$. This means $a_{j-2}$ has appeared less than $a_{i-1}$ times in $a_{[1, i-1]}$. By (c), $a_{j-2}$ has appeared at most $a_{i-1}$ times in $a_{[1, j-1]}$, hence $a_{j-1} \leqslant a_{i-1}$. Combining with $a_{[1, i-1]} \subset a_{[1, j-1]}$, this implies $\mathcal{I} \subseteq \mathcal{J}$. But since $a_{j-2} \in \mathcal{J} \backslash \mathcal{I}$, this contradicts $|\mathcal{I}|=|\mathcal{J}|$. So $a_{j-2} \in \mathcal{I}$, which means it has appeared at least $a_{i-1}$ times in $a_{[1, i-1]}$ and one more time in $a_{[i, j-1]}$. Therefore $a_{j-1}>a_{i-1}$.

By (c), any small number appearing at least $a_{j-1}$ times in $a_{[1, j-1]}$ has also appeared $a_{j-1}-1 \geqslant a_{i-1}$ times in $a_{[1, i-1]}$. So $\mathcal{J} \subseteq \mathcal{I}$ and hence $\mathcal{I}=\mathcal{J}$. Therefore, $a_{i-2} \in \mathcal{J}$, so it must appear at least $a_{j-1}-a_{i-1}=1$ more time in $a_{[i, j-1]}$.

For each small number $a_{n}$ with $n>N^{\prime}+2$, let $p_{n}$ be the smallest number such that $a_{n+p_{n}}=a_{i}$ is also small for some $i$ with $n \leqslant i<n+p_{n}$. In other words, $a_{n+p_{n}}=a_{i}$ is the first small number to occur twice after $a_{n-1}$. If $i>n$, Lemma 2 (with $j=n+p_{n}$ ) implies that $a_{i-2}$ appears again before $a_{n+p_{n}}$, contradicting the minimality of $p_{n}$. So $i=n$. Lemma 2 also implies that $p_{n} \geqslant p_{n-2}$. So $p_{n}, p_{n+2}, p_{n+4}, \ldots$ is a nondecreasing sequence bounded above by $2 k$ (as there are only $k$ small numbers). Therefore, $p_{n}, p_{n+2}, p_{n+4}, \ldots$ is eventually constant and the subsequence of small numbers is eventually periodic with period at most $k$.

Note. Since every small number appears infinitely often, Solution 1 additionally proves that the sequence of small numbers has period $k$. The repeating part of the sequence of small numbers is thus a permutation of the integers from 1 to $k$. It can be shown that every permutation of the integers from 1 to $k$ is attainable in this way.

---

### C7sol2
We follow Solution 1 until after Lemma 1. For each $n>N^{\prime}$ we keep track of how many times each of $1,2, \ldots, k$ has appeared in $a_{1}, \ldots, a_{n}$. We will record this information in an updating ( $k+1$ )-tuple

$$
\left(b_{1}, b_{2}, \ldots, b_{k} ; j\right)
$$

where each $b_{i}$ records the number of times $i$ has appeared. The final element $j$ of the $(k+1)$ tuple, also called the active element, represents the latest small number that has appeared in $a_{1}, \ldots, a_{n}$.

As $n$ increases, the value of ( $b_{1}, b_{2}, \ldots, b_{k} ; j$ ) is updated whenever $a_{n}$ is small. The ( $k+1$ )tuple updates deterministically based on its previous value. In particular, when $a_{n}=j$ is small, the active element is updated to $j$ and we increment $b_{j}$ by 1 . The next big number is $a_{n+1}=b_{j}$. By Lemma 1, the next value of the active element, or the next small number $a_{n+2}$, is given by the number of $b$ terms greater than or equal to the newly updated $b_{j}$, or


\begin{equation*}
\left|\left\{i \mid 1 \leqslant i \leqslant k, b_{i} \geqslant b_{j}\right\}\right| . \tag{1}
\end{equation*}


Each sufficiently large integer which appears $i+1$ times must also appear $i$ times, with both of these appearances occurring after the initial block of $N$. So there exists a global constant $C$ such that $b_{i+1}-b_{i} \leqslant C$. Suppose that for some $r, b_{r+1}-b_{r}$ is unbounded from below. Since the value of $b_{r+1}-b_{r}$ changes by at most 1 when it is updated, there must be some update where $b_{r+1}-b_{r}$ decreases and $b_{r+1}-b_{r}<-(k-1) C$. Combining with the fact that $b_{i}-b_{i-1} \leqslant C$ for all $i$, we see that at this particular point, by the triangle inequality


\begin{equation*}
\min \left(b_{1}, \ldots, b_{r}\right)>\max \left(b_{r+1}, \ldots, b_{k}\right) \tag{2}
\end{equation*}


Since $b_{r+1}-b_{r}$ just decreased, the new active element is $r$. From this point on, if the new active element is at most $r$, by (1) and (2), the next element to increase is once again from $b_{1}, \ldots, b_{r}$. Thus only $b_{1}, \ldots, b_{r}$ will increase from this point onwards, and $b_{k}$ will no longer increase, contradicting the fact that $k$ must appear infinitely often in the sequence. Therefore $\left|b_{r+1}-b_{r}\right|$ is bounded.

Since $\left|b_{r+1}-b_{r}\right|$ is bounded, it follows that each of $\left|b_{i}-b_{1}\right|$ is bounded for $i=1, \ldots, k$. This means that there are only finitely many different states for ( $b_{1}-b_{1}, b_{2}-b_{1}, \ldots, b_{k}-b_{1} ; j$ ). Since the next active element is completely determined by the relative sizes of $b_{1}, b_{2}, \ldots, b_{k}$ to each other, and the update of $b$ terms depends on the active element, the active element must be eventually periodic. Therefore the small numbers subsequence, which is either $a_{1}, a_{3}, a_{5}, \ldots$ or $a_{2}, a_{4}, a_{6}, \ldots$, must be eventually periodic.

---

### C8sol1
We first prove by induction that it is possible the colour the whole board black for $n=2^{k}$. The base case of $k=1$ is trivial. Assume the result holds for $k=m$ and consider the case of $k=m+1$. Divide the $2^{m+1} \times 2^{m+1}$ board into four $2^{m} \times 2^{m}$ sub-boards. Colour the top left $2^{m} \times 2^{m}$ sub-board using the inductive hypothesis. Next, colour the centre $2 \times 2$ square with a single operation. Finally, each of the remaining $2^{m} \times 2^{m}$ sub-board can be completely coloured using the inductive hypothesis, starting from the black square closest to the centre. This concludes the induction.

Now we prove that if such a colouring is possible for $n$ then $n$ must be a power of 2 . Suppose it is possible to colour an $n \times n$ board where $n>1$. Identify the top left corner of the board by $(0,0)$ and the bottom right corner by $(n, n)$. Whenever an operation takes place in a $2 \times 2$ square centred on ( $i, j$ ), we immediately draw an " X ", joining the four cells' centres (see Figure 4). Also, identify this $\mathbf{X}$ by $(i, j)$. The first operation implies there's an $\mathbf{X}$ at $(1,1)$. Since the whole board is eventually coloured, every cell centre must be connected to at least one X . The collection of all $\mathrm{X}_{\mathrm{S}}$ forms a graph $G$.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-057}
\captionsetup{labelformat=empty}
\caption{Figure 4: L-trominoes placements corresponding to colouring operations (left) and the corresponding X diagram (right).}
\end{center}
\end{figure}

\section*{Claim 1. The graph $G$ is a tree.}
Proof. Since every operation requires a pre-existing black cell, each newly drawn X apart from the first must connect to an existing X . So all Xs are connected to the first X and $G$ must be connected. Now, suppose $G$ has a cycle. Consider the newest X involved in the cycle, it must connect to previous $\mathrm{X}_{\mathrm{s}}$ at at least two points. But this implies the corresponding operation will colour at most two cells, which is a contradiction.

Note that in the following arguments, Claims 2 to 4 only require the condition that $G$ is a tree and every cell is connected to $G$.\\
Claim 2. If there's an X at $(i, j)$, then $1 \leqslant i, j \leqslant n-1$ and $i \equiv j(\bmod 2)$.\\
Proof. The inequalities $1 \leqslant i, j \leqslant n-1$ are clear. Call an X at $(i, j)$ good if $i \equiv j(\bmod 2)$, or bad if $i \not \equiv j(\bmod 2)$. The first X at $(i, j)=(1,1)$ is good. Suppose some $\mathrm{X}_{\mathrm{s}}$ are bad. Since $G$ is connected, there must exist a good X connecting to a bad X . But this can only occur if they connect at two points, creating a cycle. This is a contradiction, thus all $\mathrm{X}_{\mathrm{s}}$ are good.

Call an X at $(i, j)$ odd if $i \equiv j \equiv 1(\bmod 2)$, even if $i \equiv j \equiv 0(\bmod 2)$.\\
Claim 3. The integer $n$ must be even. Furthermore, there must be $4(n / 2-1)$ odd $\mathrm{X}_{\mathrm{S}}$ connecting the cells on the perimeter of the board as shown in Figure 5.\\
Proof. If $n$ is odd, the four corners of the bottom left cell are $(n, 0),(n-1,0),(n-1,1)$ and $(n, 1)$, none of which satisfies the conditions of Claim 2. So the bottom left cell cannot connect to any X . If $n$ is even, each cell on the edge of the board has exactly one corner satisfying the conditions of Claim 2, so the X connecting it is uniquely determined. Therefore the cells on the perimeter of the board are connected to $\mathrm{X}_{\mathrm{s}}$ according to Figure 5.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-058}
\captionsetup{labelformat=empty}
\caption{Figure 5: Highlighting the permitted points for \$\textbackslash mathrm\{X}\_\{\textbackslash mathrm\{s\}\}\$ (left) and $\mathrm{X}_{\mathrm{s}}$ on the perimeter (right).\}\end{center}
\end{figure}

Divide the $n \times n$ board into $n^{2} / 4$ blocks of $2 \times 2$ squares. Call each of these blocks a big-cell. We say a big-cell is filled if it contains an odd X on its interior, empty otherwise. By Claim 3, each big-cell on the perimeter must be filled.\\
Claim 4. Every big-cell is filled.\\
Proof. Recall that $\mathrm{X}_{\mathrm{s}}$ can only be at $(i, j)$ with $i \equiv j(\bmod 2)$. Suppose a big-cell centred at $(i, j)$ is empty. Then in order for its four cells to be coloured, there must be four even $\mathrm{X}_{\mathrm{s}}$ on $(i-1, j-1),(i+1, j-1),(i-1, j+1)$ and $(i+1, j+1)$, "surrounding" the big-cell (see Figure 6).

By Claim 3, no empty big-cell can be on the perimeter. So if there exist some empty bigcells, the boundary between empty and filled big-cells must consist of a number of closed loops. Each closed loop is made up of several line segments of length 2, each of which separates a filled big-cell from an empty big-cell.

Since every empty big-cell is surrounded by even $\mathrm{X}_{\mathrm{s}}$ and every filled big-cell contains an odd X , the two end points of each such line segment must be connected by $\mathrm{X}_{\mathrm{s}}$. Since these line segments form at least one closed loop, it implies the existence of a cycle made up of $\mathrm{X}_{\mathrm{s}}$ (see Figure 6). This is a contradiction, thus no big-cell can be empty.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-059}
\captionsetup{labelformat=empty}
\caption{Figure 6: An empty big-cell surrounded by even \$\textbackslash mathrm\{X}\_\{\textbackslash mathrm\{s\}\}\$ (left) and the boundary between empty and filled $\mathrm{X}_{\mathrm{s}}$ creating a cycle (right).\}\end{center}
\end{figure}

Therefore every big-cell is filled by an odd $\mathbf{X}$, and the connections between them are provided by even $\mathrm{X}_{\mathrm{s}}$. We can now reduce the $n \times n$ problem to an $n / 2 \times n / 2$ problem in the following way. Perform a dilation of the board by a factor of $1 / 2$ with respect to $(0,0)$. Each big-cell is shrunk to a regular cell. For the $\mathrm{X}_{\mathrm{s}}$, replace each odd X at $(i, j)$ by the point $(i / 2, j / 2)$, and replace each even $\mathbf{X}$ at $(i, j)$ by an $\mathbf{X}$ at $(i / 2, j / 2)$.

We claim the new resulting graph of $\mathrm{X}_{\mathrm{s}}$ is a tree that connects all cells of an $n / 2 \times n / 2$ board. First, two connected $\mathrm{X}_{\mathrm{s}}$ in the original $n \times n$ board are still connected after their replacements (noting that some $\mathrm{X}_{\mathrm{S}}$ have been replaced by single points). For each cell in the $n / 2 \times n / 2$ board, its centre corresponds to an odd X from a filled big-cell in the original $n \times n$ board, so it must be connected to the graph. Finally, suppose there exists a cycle in the new graph. The cycle consists of $\mathrm{X}_{\mathrm{s}}$ that correspond to even $\mathrm{X}_{\mathrm{s}}$ in the original graph connecting big-cells, forming a cycle of big-cells. Since in every big-cell, the four unit squares were connected by an odd X , this implies the existence of a cycle in the original graph, which is a contradiction.

Thus the new graph of $\mathrm{X}_{\mathrm{s}}$ must be a tree that connects all cells of an $n / 2 \times n / 2$ board, which are the required conditions for Claims 2 to 4 . Hence we can repeat our argument, halving the dimensions of the board each time, until we reach the base case of a $1 \times 1$ board (where the tree is a single point). Therefore $n$ must be a power of 2 , completing the solution.

---

### C8sol2
As in Solution 1, it is possible the colour the whole board black for $n=2^{k}$.\\
The colouring operation is equivalent to the placement of L -trominoes. For each L -tromino we place on the board, we draw an arrow and a node as shown in Figure 7. We also draw a node in the top left corner of the board.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-060(1)}
\captionsetup{labelformat=empty}
\caption{Figure 7: Tromino with corresponding arrow and node drawn.}
\end{center}
\end{figure}

Claim 1. The arrows and nodes form a directed tree rooted at the top left corner.\\
Proof. The proof is similar to the proof of Claim 1 in Solution 1, with the additional note that the directions of the arrows inherit the order of the colouring operations, so they must be pointing away from the top left node.

Note that since all edges of the tree are diagonal, the nodes can only lie on points $(i, j)$ with $i+j \equiv 0(\bmod 2)$. This implies that we can only place down L-trominoes of one particular parity: that is, with the centre of the $\mathbf{L}$-tromino on a point with $i+j \equiv 0(\bmod 2)$. In the remainder of the proof, we will implicitly use this parity property when determining possible positions of L-trominoes.

Next, we show that certain configurations of edges of the tree are impossible.\\
Claim 2. There cannot be two edges in a "parallel" configuration (see Figure 8).\\
Proof. In such a configuration, the two edges can either be directed in the same direction or opposite directions. If they point in the same direction (see Figure 8), then the L -trominoes corresponding to the two edges overlap.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-060}
\captionsetup{labelformat=empty}
\caption{Figure 8: Parallel configuration (left) and two parallel edges, case 1 (right).}
\end{center}
\end{figure}

If they point in opposite directions, then we get the diagram in Figure 9. The cells marked ( $\star$ ) must lie inside the $n \times n$ board, so they must be covered by L-trominoes. There is only one possible way to cover these with a L -tromino of the right parity. But this makes the arrows form a cycle, which cannot happen. So we have a contradiction.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-060(2)}
\captionsetup{labelformat=empty}
\caption{Figure 9: Two parallel edges, case 2.}
\end{center}
\end{figure}

Claim 3. There cannot be three edges in a "zigzag" configuration, shown in Figure 10.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-061(1)}
\captionsetup{labelformat=empty}
\caption{Figure 10: Zigzag configuration.}
\end{center}
\end{figure}

Proof. Assume for contradiction that there is a zigzag. Then take the zigzag with maximal distance from the root of the tree (measured by distance along the graph from the root to the middle edge of the zigzag).

We may assume without loss of generality that the middle edge is directed down-right. Then the right edge must be directed up-right, since no two arrows can point to the same node. Next, we draw in the corresponding L -trominoes, and consider the cell marked ( $\star$ ). There are two possible ways to cover it with an L -tromino, because of the parity of L -tromino centres.

We could choose the centre of the L -tromino to be the top right corner of the cell (see Figure 11). This immediately gives another zigzag.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-061}
\captionsetup{labelformat=empty}
\caption{Figure 11: Zigzag configuration, case 1.}
\end{center}
\end{figure}

The other possibility is if we choose the centre of the L -tromino to be the bottom left corner of the cell (see Figure 12). Then we need to cover the cell marked (**) with an L -tromino. If

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-061(2)}
\captionsetup{labelformat=empty}
\caption{Figure 12: Zigzag configuration, case 2.}
\end{center}
\end{figure}

we placed the centre of the L-tromino on the top left corner of the cell, this would give two parallel edges, contradicting Claim 2. So we must place the centre of the L -tromino on the bottom right corner of the cell, which gives a zigzag.

In each case, we get another zigzag further away from the root of the tree, which contradicts our assumption of maximality. So there cannot be any zigzags.

We now colour the nodes of the tree. Colour the root node yellow. For all other nodes, we colour it white if it has an arrow coming out of it in a different direction to the arrow going in, and black otherwise.\\
Claim 4. Any child of a black node is white.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-062}
\captionsetup{labelformat=empty}
\caption{Figure 13: Black node configuration.}
\end{center}
\end{figure}

Proof. Suppose we have a black node with a child. Then the arrow exiting the black node must be in the same direction as the arrow entering it by the definition of our colouring, giving the left diagram of Figure 13.

The cell marked ( $\star$ ) must be covered by an L -tromino. If the centre of this L -tromino is the bottom left corner, then this would give an arrow leaving the black node in a different direction, which cannot happen. So the centre of the L -tromino must instead be the top right corner, which gives an arrow leaving the upper node in a different direction. Thus the upper node must be white.

Claim 5. Every white node has three children, all of which are black.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-062(1)}
\captionsetup{labelformat=empty}
\caption{Figure 14: White node configuration.}
\end{center}
\end{figure}

Proof. Refer to Figure 14. Suppose we have a white node, as in the leftmost diagram. The cell marked ( $\star$ ) must be covered by an L -tromino. If the centre of this L -tromino is the bottom right corner of the cell, then this would form a zigzag, which by Claim 3 is not allowed. So the centre must be the top left corner.

Next, the cell marked ( $\star \star$ ) must be covered by an L -tromino. If the centre of this L -tromino is the top right corner, this would form a zigzag, so the centre must be the bottom left corner instead. Thus we have shown that any white node has three children.

Finally, note that if any of the child nodes had three children of their own, then this would give parallel edges in the diagram, which contradicts Claim 2. Therefore the child nodes of the white node must all be black.

We now know that the node colours alternate between black and white as you go down the tree, so all white nodes lie on points with coordinates $(2 i, 2 j)$, and all black nodes lie on points with coordinates $(2 i+1,2 j+1)$.

Now (assuming $n>1$ ) we will construct a new board whose cells are $2 \times 2$ squares of our current board. We replace the root node and its child with a single big cell and a big root node,

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-063}
\captionsetup{labelformat=empty}
\caption{Figure 15: Replacing with larger cells and L-trominoes.}
\end{center}
\end{figure}

and we replace each white node and its three children with a big L-tromino, big arrow and big node as shown in Figure 15.

Every black node is the child of the root node or a white node, so every L-tromino is involved in exactly one replacement. Also, the parent of any white node is a black node, whose parent, in turn, is a white node or the root. So the starting point of every big arrow will be on a big node. Therefore we obtain an L-tromino tiling forming a tree.

This shows for $n>1$ that if an $n \times n$ board can be tiled by L-trominoes forming a tree, then $n$ is even, and an $n / 2 \times n / 2$ board can also be tiled by L-trominoes forming a tree. Since a $1 \times 1$ board can trivially be tiled, we conclude that the only values of $n$ for which an $n \times n$ board can be tiled are $n=2^{k}$.

\section*{Geometry}

---

### G1sol1
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

### G1sol2
Let $A F$ and $D E$ meet $\omega$ at $X$ and $Y$, respectively, and let $T$ be as in

---

### G1sol1
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

### G1comment
The statement remains true without the length and angle conditions on cyclic quadrilateral $A B C D$ however additional care is required to consider different cases based on the ordering of points on lines $D E$ and $A F$. It is also possible for $T$ to be on the external angle bisector of $\angle X A Y$.

---

### G1sol3
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

### G2sol1
Let $A^{\prime}$ be the reflection of $A$ in $I$, then $A^{\prime}$ lies on the angle bisector $A P$. Lines $A^{\prime} X$ and $A^{\prime} Y$ are the reflections of $A C$ and $A B$ in $I$, respectively, and so they are the tangents to $\omega$ from $X$ and $Y$. As is well-known, $P B=P C=P I$, and since $\angle B A P=\angle P A C>30^{\circ}$, $P B=P C$ is greater than the circumradius. Hence $P I>\frac{1}{2} A P>A I$; we conclude that $A^{\prime}$ lies in the interior of segment $A P$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-067}

We have $\angle A P B=\angle A C B$ in the circumcircle and $\angle A C B=\angle A^{\prime} X C$ because $A^{\prime} X \| A C$. Hence, $\angle A P B=\angle A^{\prime} X C$, and so quadrilateral $B P A^{\prime} X$ is cyclic. Similarly, it follows that $C Y A^{\prime} P$ is cyclic.

Now we are ready to transform $\angle K I L+\angle Y P X$ to the sum of angles in triangle $A^{\prime} C B$. By a homothety of factor 2 at $A$ we have $\angle K I L=\angle C A^{\prime} B$. In circles $B P A^{\prime} X$ and $C Y A^{\prime} P$ we have $\angle A P X=\angle A^{\prime} B C$ and $\angle Y P A=\angle B C A^{\prime}$, therefore

$$
\angle K I L+\angle Y P X=\angle C A^{\prime} B+(\angle Y P A+\angle A P X)=\angle C A^{\prime} B+\angle B C A^{\prime}+\angle A^{\prime} B C=180^{\circ} .
$$

---

### G2comment
The constraint $A B<A C<B C$ was added by the Problem Selection Committee in order to reduce case-sensitivity. Without that, there would be two more possible configurations according to the possible orders of points $A, P$ and $A^{\prime}$, as shown in the pictures below. The solution for these cases is broadly the same, but some extra care is required in the degenerate case when $A^{\prime}$ coincides with $P$ and line $A P$ is a common tangent to circles $B P X$ and $C P Y$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-068}

---

### G2sol2
Let $B C=a, A C=b, A B=c$ and $s=\frac{a+b+c}{2}$, and let the radii of the incircle, $B$-excircle and $C$-excircle be $r, r_{b}$ and $r_{c}$, respectively. Let the incircle be tangent to $A C$ and $A B$ at $B_{0}$ and $C_{0}$, respectively; let the $B$-excircle be tangent to $A C$ at $B_{1}$, and let the $C$-excircle be tangent to $A B$ at $C_{1}$. As is well-known, $A B_{1}=s-c$ and area $(\triangle A B C)=r s=r_{c}(s-c)$.

Let the line through $X$, parallel to $A C$ be tangent to the incircle at $E$, and the line through $Y$, parallel to $A B$ be tangent to the incircle at $D$. Finally, let $A P$ meet $B B_{1}$ at $F$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-069}

It is well-known that points $B, E$, and $B_{1}$ are collinear by the homothety between the incircle and the $B$-excircle, and $B E \| I K$ because $I K$ is a midline in triangle $B_{0} E B_{1}$. Similarly, it follows that $C, D$, and $C_{1}$ are collinear and $C D \| I L$. Hence, the problem reduces to proving $\angle Y P A=\angle C B E$ (and its symmetric counterpart $\angle A P X=\angle D C B$ with respect to the vertex $C$ ), so it suffices to prove that $F Y P B$ is cyclic. Since $A C P B$ is cyclic, that is equivalent to $F Y \| B_{1} C$ and $\frac{B F}{F B_{1}}=\frac{B Y}{Y C}$.

By the angle bisector theorem we have

$$
\frac{B F}{F B_{1}}=\frac{A B}{A B_{1}}=\frac{c}{s-c} .
$$

The homothety at $C$ that maps the incircle to the $C$-excircle sends $Y$ to $B$, so

$$
\frac{B C}{Y C}=\frac{r_{c}}{r}=\frac{s}{s-c} .
$$

So,

$$
\frac{B Y}{Y C}=\frac{B C}{Y C}-1=\frac{s}{s-c}-1=\frac{c}{s-c}=\frac{B F}{F B_{1}},
$$

which completes the solution.

---

### G3sol1
}
(a) Notice that the condition $\angle P D C=\angle A D B$ is equivalent to $\angle A D P=\angle B D C$, and $\angle E D Q=\angle A D B$ is equivalent to $\angle E D A=\angle Q D B$. From line $A B$ being tangent to circle $C M E$, and circles $A M D E$ and $C D M E$ we read $\angle E C M=\angle E M A=\angle E D A=\angle Q D B$ and $\angle M E C=\angle B M C=\angle B D C=\angle A D P$.\\
Using $\angle A D P=\angle M E C$, the points $D, E, K$, and $P$ are concyclic, which gives that $\angle E P K=\angle E D A=\angle E C M$. From that, we can see that $K P \| M C$. It can be shown similarly that $C, D, Q$, and $L$ are concyclic, $\angle L Q C=\angle M E C$ and therefore $L Q \| M E$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-070}\\
(b) Let rays $D A$ and $D B$ intersect circle $C D E$ at $R$ and $S$, respectively. We now observe that $\angle S E C=\angle S D C=\angle M E C$, so points $E, M$, and $S$ are collinear. We similarly obtain that $C, M$, and $R$ are collinear.\\
From $\angle S R C=\angle S E C=\angle B M C$ we can see that $R S \| A B$. Since $M$ bisects $A B$, it follows that $K L \| R S$.\\
(c) Consider the homothety at $D$ that sends $R S$ to $K L$. Because $K P \| R C$ and $L Q \| S E$, that homothety sends the concurrent lines $D M, R C$, and $S E$ to $D M, K P$, and $L Q$, so these lines are also concurrent.

\section*{

---

### G3sol2
}
(a) As in Solution 1, we show the following: $\angle E C M=\angle E M A=\angle E D A=\angle E P K$; $\angle M E C=\angle B M C=\angle B D C=\angle L Q C$; the points $C, D, Q$, and $L$ are concyclic; the points $D, E, K$, and $P$ are concyclic; $K P \| M C$; and $L Q \| M E$.\\
(b) Notice that triangles $E K P$ and $E M C$ are homothetic at $E$, so their circumcircles $C M E$ and $D E K P$ are tangent to each other at $E$. Similarly, circle $C D Q L$ is tangent to circle $C M E$ at $C$.

Suppose that the tangents to circle $C M E$ at $C$ and $E$ intersect at point $X$. (The case when $C E$ is a diameter in circle $C M E$ can be considered as a limit case.) Moreover, let $E X$ and $C X$ intersect circles $D E A M$ and $B C D M$ again at $A_{1} \neq E$ and $B_{1} \neq C$, respectively.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-071}

We have $X E=X C$ because they are the tangents from $X$ to circle $C M E$. Moreover, in circle $D E A M$, chords $A M$ and $A_{1} E$ are tangent to circle $C M E$, so $A_{1} E=A M$. Similarly, we have $B_{1} C=B M$, hence $A_{1} E=A M=B M=B_{1} C$. We conclude $X A_{1}=X B_{1}$, so the powers of $X$ with respect to circles $D E A M$ and $B C D M$ are equal. Therefore, $X$ lies on the radical axis of these two circles, which is $D M$.

Now notice that by $X C=X E$, point $X$ has equal powers to circles $C D Q L$ and $D E K P$, so $D X$ is the radical axis of these circles. Point $M$ lies on $D X$, so $M E \cdot M K=M C \cdot M L$; we conclude that $C, E, K$, and $L$ are concyclic. Hence, by $\angle M K L=\angle E C M=\angle K M A$ we have $K L \| A B$.\\
(c) As $\angle E P K=\angle E M A=\angle Q L K$, we have that $K L Q P$ is cyclic. The radical axes between circles $D E K P, C D Q L$ and $K L Q P$ are $D M, K P$ and $L Q$, so they are concurrent at the radical centre of the three circles.

\section*{

---

### G3sol3
}
(b) We present another proof that $K L \| A B$.

Let $A D \cap L Q=I, B D \cap K P=H, A B \cap L Q=U$ and $A B \cap K P=V$. Since

$$
\angle D H P=\angle D L M=180^{\circ}-\angle C L D=180^{\circ}-\angle C Q D=\angle D Q E,
$$

point $H$ lies on circle $D P Q$. Similarly, we obtain that point $I$ lies on this circle. Hence, $\angle L I H=\angle Q D B=\angle E D A=\angle E M A$, and $L Q \| M E$ implies that $H I \| A B$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-072}

Let $A M=B M=d$, then we have

$$
\frac{B U}{I H}=\frac{B L}{L H}=\frac{B M}{M V}=\frac{d}{d+A V} \quad \text { and } \quad \frac{A V}{I H}=\frac{A K}{K I}=\frac{A M}{M U}=\frac{d}{d+B U} .
$$

Hence, $B U \cdot(d+A V)=A V \cdot(d+B U)$, so $B U=A V$. Therefore, $\triangle M L U \cong \triangle V K M$ which implies $K L\|A B\| H I$.\\
(c) Lines $M K, M L, K P$ and $L Q$ enclose a parallelogram. Line $D M$ passes through the midpoint of $K L$, which the centre of the parallelogram, and passes through the vertex $M$. Therefore, $D M$ passes through the opposite vertex, which is the intersection of $K P$ and $L Q$.

---

### G4sol1
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

### G4sol2
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

### G4sol3
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

### G5sol1
Let $\Gamma$ be circle $A B C$ and $\omega$ be circle $A Y Z$. Let $O, M$, and $S$ be the centres of $\Gamma, \Omega$, and $\omega$, respectively. Let $A K$ intersect $\Gamma$ again at $P$, and let the angle bisector of $\angle Z A Y$ intersect $\omega$ again at $N$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-076}

By power of a point from $K$ to $\Gamma$ and $\Omega$, we have that $K A \cdot K P=K B \cdot K C=K Y \cdot K Z$, so $P$ also lies on $\omega$. The pairwise common chords of $\Gamma, \Omega$, and $\omega$ are then $A P \perp O S, B C \perp O M$, and $Y Z \perp M S$, so we have that $\angle O M S=\angle C K Y=\angle Y K A=\angle M S O$. As $M$ lies on $\Gamma$ and $O M=O S, S$ also lies on $\Gamma$. Note that $N$ lies on $M S$ as $N Y=N Z$, so

$$
\angle P A N=\frac{1}{2} \angle P S N=\frac{1}{2} \angle P S M=\frac{1}{2} \angle P A M .
$$

Thus, $A N$ bisects $\angle P A M$ in addition to $\angle Z A Y$, which means that $\angle Z A K=\angle I A Y$ as $K$ lies on $A P$ and $I$ lies on $A M$.

---

### G5sol2
Define $M$ and $P$ as in Solution 1, and recall that $A Y P Z$ is cyclic. Let $Q$ be the second intersection of the line parallel to $B C$ through $P$ with circle $A B C$ and let $J$ be the incentre of triangle $A P Q$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-077}

Since $P Q$ is parallel to $B C$ and $\angle B A P<\angle P A C$, the angle bisector of $\angle A P Q$ is parallel to the angle bisector of $\angle A K C$. Hence, $P J$ is parallel to $Y Z$. As $M$ is the midpoint of $\wideparen{P Q}$ on circle $A P Q$, we have that $M P=M J$. Then since segments $Y Z$ and $P J$ are parallel and have a common point $M$ on their perpendicular bisectors, $P J Y Z$ is cyclic with $J Y=P Z$. It follows that $J$ also lies on circle $A Y P Z$ and that $\angle Z A P=\angle J A Y=\angle I A Y$.

---

### G5comment
The proof of the analogous case of $\angle W A K=\angle I A X$ is slightly different. In this case, $J$ should be defined as the $A$-excentre of $A P Q$ so that $P J$ is the external bisector of $\angle A P Q$ and $P J \| W X$. The proof is otherwise exactly the same.

---

### G5sol3
As in the previous solutions, let $M$ be the centre of $\Omega$. Let $L$ be the intersection of $A M$ and $B C$, and let $L^{\prime}$ be the reflection of $L$ over $Y Z$. Let the circle $M Y Z$ intersect $A M$ again at $T$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-078}

Note that as $M$ is the midpoint of $\wideparen{B C}$ on circle $A B C$ and $L$ is the foot of the bisector of $\angle B A C$, we have that $M A \cdot M L=M I^{2}=M Y^{2}$. It follows by power of a point that $M Y$ is tangent to circle $A L Y$, so $\angle L A Y=\angle L Y M$. Using directed angles, we then have that

$$
\Varangle A Y T=\Varangle M T Y-\Varangle M A Y=\Varangle M Z Y-\Varangle L Y M=\Varangle Z Y M-\Varangle L Y M=\Varangle Z Y L=\Varangle L^{\prime} Y Z,
$$

where we use the fact that $M Y=M Z$ and that $L$ and $L^{\prime}$ are symmetric about $Y Z$. Thus, $Y T$ and $Y L^{\prime}$ are isogonal in $\angle A Y Z$. Analogously, we have that $Z T$ and $Z L^{\prime}$ are isogonal in $\angle Y Z A$. This means that $T$ and $L^{\prime}$ are isogonal conjugates in triangle $A Y Z$, which allows us to conclude that $\angle Z A K=\angle I A Y$ since $L^{\prime}$ lies on $A K$ and $T$ lies on $A I$.

---

### G5comment
Owing to the condition $\angle B A K<\angle K A C$, points $L^{\prime}$ and $T$ lie inside triangle $A Y Z$. However, if one tries to write down the same proof for $\angle W A K=\angle I A X$, the analogues $L_{1}^{\prime}$ and $T_{1}$ of $L^{\prime}$ and $T$ would lie outside triangle $A W X$. Thus, the solution has been written using directed angles so that it applies directly to this case as well. It is also possible that $L_{1}^{\prime}$ lies on circle $A W X$ and $T_{1}$ is a point at infinity. In this case, it is straightforward to interpret the directed angle chase to prove the isogonality, and the isogonality also follows from this scenario being a limit case of other configurations.

Note. The original proposal remarks that this problem is a special case of a more general property:\\
$A$ convex quadrilateral $A B C D$ is inscribed in a circle $\omega$. The bisectors between $A C$ and $B D$ intersect $\omega$ at four points, forming a convex quadrilateral PQRS. Then the conditions

$$
X A \cdot X C=X B \cdot X D \quad \text { and } \quad \npreceq(X P, X Q)=\Varangle(X S, X R)
$$

on point $X$ are equivalent.\\
The Problem Selection Committee believes that the proof of this generalisation is beyond the scope of the competition and considers the original problem to be more suitable.

This page is intentionally left blank

---

### G6sol1
Let $N$ be the midpoint of $\widetilde{B A C}$ on $\Gamma$, and let $N X$ and $N Y$ intersect $B C$ at $W$ and $Z$, respectively.\\
Claim. Quadrilateral $W X Y Z$ is cyclic, and its circumcentre is $J$.\\
Proof. As $N$ is the midpoint of $\widehat{B A C}, W$ and $Z$ lie on $B C$, and $X$ and $Y$ are the second intersections of $N W$ and $N Z$ with $\Gamma$, we have that $W X Y Z$ is cyclic.

Let the parallel to $B C$ through $N$ intersect $T U$ and $T V$ at $U^{\prime}$ and $V^{\prime}$, respectively. Then $U^{\prime}$ is the intersection of the tangents to $\Gamma$ at $N$ and $X$, so $U^{\prime} N=U^{\prime} X$. As $N U^{\prime} \| B C, U^{\prime} N X$ is similar to $U W X$, so $U W=U X$ as well. Hence, the perpendicular bisector of $W X$ is the internal bisector of $\angle X U W$, which is the external bisector of $\angle V U T$. Analogously, the perpendicular bisector of $Y Z$ is the external bisector of $\angle T V U$. This means that the circumcentre of $W X Y Z$ is the intersection of the external bisectors of $\angle V U T$ and $\angle T V U$, which is $J$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-080}

Let $A N$ intersect $B C$ at $L$, so $X Y$ passes through $L$ as well. By power of a point from $L$ to $\Gamma$ and circle $W X Y Z$, we have that $L A \cdot L N=L X \cdot L Y=L W \cdot L Z$, so $W A N Z$ is also cyclic. Thus, $A$ is the Miquel point of quadrilateral $W X Y Z$. As $W X Y Z$ is cyclic with circumcentre $J$ and its opposite sides $W X$ and $Y Z$ intersect at $N$, we have that $A N \perp A J$. Since $A N$ is the external bisector of $\angle B A C$, this implies that $A J$ is the internal bisector of $\angle B A C$.

---

### G6sol2
Let the internal and external angle bisectors of $\angle B A C$ intersect $B C$ at $K$ and $L$, respectively. Let $A K$ intersect circle $A B C$ again at $M$, and let $D$ be the intersection of the tangents to $\Gamma$ at $B$ and $C$. Let $\Omega$ be the $T$-excircle of $T U V$, and let $\omega$ be the incircle of $D B C$. Claim. The points $T, K$, and $D$ are collinear.\\
Proof. Note that $B C$ and $X Y$ are the polars of $T$ and $D$ with respect to $\Gamma$. By La Hire's Theorem, $T D$ is the polar of $L$ with respect to $\Gamma$. As $(B, C ; K, L)=-1, K$ also lies on the polar of $L$, thus proving the collinearity.\\
Claim. The incentre of $D B C$ is $M$.\\
Proof. We have that $\angle M B C=\angle M A C=\frac{1}{2} \angle B A C=\frac{1}{2} \angle D B C$, so $B M$ bisects $\angle D B C$. Similarly, $C M$ bisects $\angle B C D$, so $M$ is the incentre of $D B C$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-081}

Claim. The intersection of the common external tangents of $\Omega$ and $\omega$ is $K$.\\
Proof. Let $K^{\prime}$ be the intersection of the common external tangents of $\Omega$ and $\omega$. As $\Omega$ and $\omega$ are both tangent to $B C$ and lie on the same side of $B C$ opposite to $A, K^{\prime}$ lies on $B C$. As $T$ is the intersection of the common external tangents of $\Gamma$ and $\Omega$ and $D$ is the intersection of the common external tangents of $\Gamma$ and $\omega$, by Monge's theorem $K^{\prime}$ lies on $T D$. As $K^{\prime}$ lies on both $B C$ and $T D$, it is the same point as $K$.

Hence, $K$ is collinear with the centres of $\Omega$ and $\omega$, which are $M$ and $J$, respectively. As $K$ and $M$ both lie on the bisector of $\angle B A C$, so does $J$.

Note. It can be shown that circles $A U V$ and $A B C$ are tangent and that the tangents from $U$ and $V$ to circle $A B C$ different from $T U$ and $T V$ intersect at a point $W$ on line $T K$. Reframing the problem in terms of quadrilateral $T U W V$ using these properties, we obtain the following problem:

Let $A B C D$ be a convex quadrilateral with an incircle $\omega$, and let $A C$ and $B D$ intersect at $P$. Point $E$ lies on $\omega$ such that the circumcircle of $A C E$ is tangent to $\omega$. Prove that if $B$ and $E$ lie on the same side of line $A C$, then the centre of the excircle of triangle $A B C$ opposite the vertex $B$ lies on line $E P$.

While this is an appealing statement, the Problem Selection Committee is uncertain about its difficulty and whether it has solutions that do not proceed by reducing to the original problem. Thus, it is believed that the original statement is more suitable for the competition.

---

### G7sol1
}
\begin{center}
\includegraphics[max width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-082}
\end{center}

Let $O$ be the circumcentre of $\triangle A B C$. First we note from standard properties of the Miquel point $S$ we have:

\begin{itemize}
  \item $\triangle S M_{C} M_{B} \sim \triangle S B C \sim \triangle S P Q ; \quad(*)$
  \item $I$ and $S$ are inverses with respect to circle $A B C$;
  \item $\angle O S X=90^{\circ}$.
\end{itemize}

Claim 1. $\angle M_{A} P B=\angle C D A$.\\
Proof. From the above we have $\triangle O M_{A} I \sim \triangle O S M_{A}$ and

$$
\angle M_{A} P B=\angle M_{A} P X=\angle M_{A} S X=90^{\circ}+\angle M_{A} S O=90^{\circ}+\angle O M_{A} I=\angle M_{A} B A=\angle C D A \text {. }
$$

Claim 2. $\quad \frac{M_{C} B}{B P}=\frac{M_{B} C}{C Q}=\frac{A I}{I D}$.\\
Proof. Observe that $\angle P M_{C} M_{A}=\angle B M_{C} M_{A}=\angle D A C$ and $\angle M_{C} M_{A} B=\angle I C D$. Combining these with Claim 1 shows $M_{C} P M_{A} B \sim A D C I$. Therefore, $\frac{M_{C} B}{B P}=\frac{A I}{I D}$. Similarly, $\frac{M_{B} C}{C Q}=\frac{A I}{I D}$.

Claim 3. $\quad \frac{D P}{D Q}=\frac{I B}{I C}$.\\
Proof. Firstly, observe that $\angle I C B=\angle A M_{B} M_{C}$ and $\angle C B I=\angle M_{B} M_{C} A$ which gives that $\triangle I B C \sim \triangle A M_{C} M_{B}$. This, combined with Claim 2, is enough to show $\triangle D P Q \sim \triangle I B C$ by linearity, proving the claim.\\
Claim 4. $\frac{I P}{I Q}=\frac{I B}{I C}$.\\
Proof. Combining $\triangle I B M_{C} \sim \triangle I C M_{B}$ with Claim 2 shows $I B M_{C} P \sim I C M_{B} Q$ giving the result.

Finally, we have that

$$
\frac{S P}{S Q}=\frac{S B}{S C}=\frac{B M_{C}}{C M_{B}}=\frac{I B}{I C}
$$

from (*) and $\triangle I B M_{C} \sim \triangle I C M_{B}$. Putting this together with Claims 3 and 4, we have that

$$
\frac{I B}{I C}=\frac{D P}{D Q}=\frac{I P}{I Q}=\frac{S P}{S Q}
$$

which shows that circle $S I D$ is an Apollonius circle with respect to $P$ and $Q$, giving the desired conclusion.

---

### G7comment
The condition $A B<A C$ ensures $S \neq X$. We also need to avoid the case $\angle B A C=60^{\circ}$ as then $B M_{C} \| C M_{B}$.

---

### G7sol2
We use Claim 1 from

---

### G7sol1
We will show that $P$ and $Q$ are inverses in circle $S I D$ which implies the result. Perform an inversion in circle $B I C$ and denote the inverse of a point $\bullet$ by $\bullet^{\prime}$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-084}

Claim 1. $\quad S^{\prime}=J$ where $J$ is the reflection of $I$ across $B C$.\\
Proof. We have that $S$ and $I$ are inverses in circle $A B C$. Inverting this assertion in circle $B I C$ shows that $S^{\prime}$ and $I$ are inverses with respect to line $B C$, which is just a reflection in line $B C$.

Let $Y=M_{B} M_{C} \cap B C$. From $\angle I M_{C} M_{B}=\angle M_{B} M_{C} A$ and $\angle A M_{B} M_{C}=\angle M_{C} M_{B} I$, we see that $A$ and $I$ are reflections in line $M_{B} M_{C}$ so $Y A=Y I$. We have that circle $S I D$ maps to circle $A I J$ which, from the previous comment, has centre $Y$. Inverting the conclusion that $P$ and $Q$ are inverses with respect to circle $S I D$ in circle $B I C$, it suffices to show $P^{\prime}$ and $Q^{\prime}$ are inverses with respect to circle $A I J$ or equivalently, that $Y P^{\prime} \cdot Y Q^{\prime}=Y A^{2}$.\\
Claim 2. Circle $X S M_{A}$ maps to line $Y J$ under the inversion in circle $B I C$.\\
Proof. Since circle $B I C$ has centre $M_{A}$, the inverse of this circle is a line. By Claim 1, this line passes through $J$ hence it suffices to prove that circle $X S M_{A}$ passes through $Y^{\prime}$. From inverting line $B C$ in circle $B I C$, we have that $B C M_{A} Y^{\prime}$ is cyclic so

$$
Y S \cdot Y X=Y B \cdot Y C=Y Y^{\prime} \cdot Y M_{A} .
$$

where we have used that $Y, S$ and $X$ are collinear by a standard property of the Miquel point. Hence $Y^{\prime}$ lies on circle $X S M_{A}$ as required.

Let $A_{1}$ be the reflection of $A$ in the perpendicular bisector of $B C$. Using Claim 1 from Solution 1,

$$
\angle P^{\prime} B M_{A}=\angle M_{A} P B=\angle C D A=180^{\circ}-\angle A C M_{A}=180^{\circ}-\angle M_{A} B A_{1} .
$$

Hence, $P^{\prime}, B$, and $A_{1}$ are collinear. Similarly $Q^{\prime}, C$, and $A_{1}$ are collinear. Let $P_{1}$ and $Q_{1}$ be the reflections of $P^{\prime}$ and $Q^{\prime}$ across $B C$. As $P^{\prime}$ and $Q^{\prime}$ lie on line $Y J$, it follows that $P_{1}$ and $Q_{1}$ lie on line $Y I$. Also from the previous collinearities, we get $B P_{1} \| A C$ and $C Q_{1} \| A B$.

We have now reduced the problem to the following:\\
Claim 3 (Inverted Problem). Let $A B C$ be a triangle with incentre $I$. Let $Y$ be the point on $B C$ such that $Y A=Y I$. Let $P_{1}$ and $Q_{1}$ be points on $Y I$ such that $B P_{1} \| A C$ and $C Q_{1} \| A B$. Then $Y A^{2}=Y P_{1} \cdot Y Q_{1}$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-085}

Proof. Let $Y I$ intersect $A B$ and $A C$ at $E$ and $F$, respectively. From the parallel lines, we get that $\triangle B E P_{1}$ and $\triangle C Q_{1} F$ are homothetic with centre $Y$. Thus we have

$$
\frac{Y E}{Y P_{1}}=\frac{Y Q_{1}}{Y F} \Longrightarrow Y P_{1} \cdot Y Q_{1}=Y E \cdot Y F
$$

Moreover, $A I$ bisects $\angle E A F$ and $Y A=Y I$ so the circle centred at $Y$ with radius $Y A$ is the Apollonius circle of $\triangle A E F$ with respect to the feet of the internal and external angle bisectors at $A$. This gives $Y E \cdot Y F=Y A^{2}$. Combining these results proves the claim.

---

### G7sol3
As in Solution 1, let $O$ be the circumcentre of $\triangle A B C$. Let $X I$ intersect circle $X S M_{A}$ again at $Z \neq X$ and let $Y=B C \cap M_{B} M_{C}$. Let $X^{*}$ be the inverse of $X$ in circle $A B C$. We will use the properties of Miquel point $S$ noted at the top of Solution 1 and in addition, that $S$ lies on line $X Y$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-086}

Claim 1. YSAD is cyclic.\\
Proof. From $O M_{A} \perp B C$ and $Y S \perp O S$ we have $\angle D Y S=180^{\circ}-\angle S O M_{A}$. From inverting collinear points $A, I$ and $M_{A}$ in circle $A B C$ we get $A S M_{A} O$ is cyclic which gives

$$
\angle S O M_{A}=\angle S A M_{A}=\angle S A D \Longrightarrow \angle S A D+\angle D Y S=180^{\circ}
$$

proving the claim.\\
Claim 2. $\quad X^{*}$ lies on circle BIC which has centre $M_{A}$.\\
Proof. This follows immediately from inverting circle $S B C X$ in circle $A B C$.\\
Claim 3. $Z$ lies on circle SID.\\
Proof. We have that

$$
\angle I Z S=\angle X M_{A} S=\angle O M_{A} S-\angle O M_{A} X=\angle M_{A} I O-\angle M_{A} X^{*} O=\angle D I O-\angle M_{A} X^{*} O
$$

where in the penultimate step we inverted in circle $A B C$ to get the angle equalities.

From Brocard's Theorem applied to cyclic quadrilateral $B M_{C} M_{B} C$, we get $Y, I$, and $X^{*}$ collinear and $\angle Y X^{*} O=90^{\circ}$. This gives that

$$
\angle M_{A} X^{*} O=90^{\circ}-\angle I X^{*} M_{A}=90^{\circ}-\angle M_{A} I X^{*}=90^{\circ}-\angle A I Y
$$

where the second equality is by Claim 2. We have that $A$ and $I$ are reflections in line $M_{B} M_{C}$. Hence,

$$
90^{\circ}-\angle A I Y=90^{\circ}-\angle Y A D=90^{\circ}-\angle Y S D=\angle D S O
$$

where the second step is by Claim 1, and in the last step we are using $O S \perp Y S$. Putting these together,

$$
\angle I Z S=\angle D I O-\angle D S O=\angle I D S
$$

proving the claim.\\
Let the tangents from $S$ and $Z$ to circle $X S M_{A}$ intersect at $K$. Observe from the standard Ceva-Menelaus configuration,

$$
-1=(X Y, X I ; X B, X C) \stackrel{X}{=}(S, Z ; P, Q) .
$$

This shows that $K$ lies on line $P Q$. We then have

$$
\angle Z K S=180^{\circ}-2 \angle S X Z=2\left(90^{\circ}-\angle S X I\right)=2\left(180^{\circ}-\angle S I Z\right),
$$

where we are using $\angle I S X=90^{\circ}$. As $K$ lies on the perpendicular bisector of $S Z$, this is enough to show that $K$ is the centre of circle $S I D Z$ completing the proof.

---

### G7sol4
Solution 1 solves the problem by establishing $\frac{S P}{S Q}=\frac{I P}{I Q}=\frac{D P}{D Q}$, which implies that circle $S I D$ is an Apollonius circle with respect to $P$ and $Q$. We demonstrate an alternate approach that only requires us to show two of the ratios $\frac{S P}{S Q}, \frac{I P}{I Q}$, and $\frac{D P}{D Q}$ to be equal. This can arise from missing some of the observations in Solution 1, for example not proving Claim 3.\\
Claim. Given we have shown two of the ratios listed above to be equal, it suffices to show that circle $S I D$ is orthogonal to circle $S X M_{A}$, which the same circle as $S P Q$.\\
Proof. Supposing we have shown the orthogonality, if $\frac{S P}{S Q}=\frac{I P}{I Q}$ or $\frac{S P}{S Q}=\frac{D P}{D Q}$, then we immediately have that circle $S I D$ is an Apollonius circle with respect to $P$ and $Q$. If $\frac{I P}{I Q}=\frac{D P}{D Q}$ and $S$ does not lie on the Apollonius circle $\mathcal{C}$ defined by this common ratio, then $I$ and $D$ lie on two distinct circles orthogonal to circle $S P Q$, namely circle $S I D$ and $\mathcal{C}$. This implies that $I$ and $D$ are inverses with respect to circle $S P Q$, which is a contradiction as both $I$ and $D$ lie inside circle $S P Q$.

Throughout this solution, we will use the properties of $S$ from the beginning of

---

### G7sol1
Define $O$ and $Y$ as in previous solutions, and let $E$ be the second intersection of circles $S O M_{A}$ and $S M_{B} M_{C}$.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-088}

\section*{Lemma. We have that $O E \perp A Y$.}
Proof. Let $M_{A}^{\prime}, B^{\prime}$, and $C^{\prime}$ be the respective reflections of $M_{A}, B$, and $C$ over line $M_{B} M_{C}$. As noted in Solution 3, $A$ and $I$ are reflections across $M_{B} M_{C}$. Because $M_{A}$ is the centre of circle $B I C$, it follows that $M_{A}^{\prime}$ is the centre of circle $A B^{\prime} C^{\prime}$. On the other hand, $Y$ lies on $M_{B} M_{C}$, so we have that $Y B \cdot Y C=Y B^{\prime} \cdot Y C^{\prime}$. Thus, $Y$ lies on the radical axis of circles $A B C$ and $A B^{\prime} C^{\prime}$, so $O M_{A}^{\prime} \perp A Y$. Finally, note that the inverses of circles $S O M_{A}$ and $S M_{B} M_{C}$ in circle $A B C$ are line $I M_{A}$ and circle $I M_{B} M_{C}$ respectively, so $E$ and $M_{A}^{\prime}$ are inverses in circle $A B C$. Thus, $E$ lies on $O M_{A}^{\prime}$ and the lemma follows.

Let $\mathcal{T}$ denote the composition of an inversion at $S$ with radius $\sqrt{S I \cdot S O}$ with a reflection across line $S I$. By standard properties of the Miquel point, $\mathcal{T}$ swaps $X$ and $Y$ and any points $Z_{1}$ and $Z_{2}$ on circle $A B C$ with $I \in Z_{1} Z_{2}$. Hence, $\mathcal{T}$ swaps the pairs $\left(A, M_{A}\right),\left(B, M_{B}\right),\left(C, M_{C}\right)$, $(O, I)$, and $(X, Y)$. As $D=A I \cap B C$ and $E$ is the intersection of circles $S O M_{A}$ and $S M_{B} M_{C}$, we have that $\mathcal{T}(D)=E$. Thus, $\mathcal{T}$ maps circles SID and SXM ${ }_{A}$ to lines $O E$ and $A Y$, so by the Lemma, circles SID and SXM ${ }_{A}$ are orthogonal, as required.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-089}

---

### G8sol1
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

### G8sol2
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

### G8comment
While we have written the solution using harmonic bundles for the sake of brevity, there are ways to prove Claim 2 and obtain the final contradiction without the use of projective geometry. Claim 2 can be proven using an application of Menelaus's theorem, and the final contradiction can be obtained using the fact that an excircle of a triangle is always larger than its incircle.

---

### G8sol3
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

### G8comment
The condition $A B<A C<B C$ is used in an essential way in the solutions. In Solution 1, it is used in the proof of Claim 3 to ensure that $X$ lies in the interior of triangle $I B C$. In Solution 2, it is used in the final step to ensure that $\angle A B C$ and $\angle B C A$ cannot be obtuse. In Solution 3, it is used to exclude the case $\ell=t$. If the condition is removed, then the problem is no longer true: whenever $\angle A B C$ or $\angle B C A$ is obtuse, there exists a choice of $D$ on $B C$ such that $I_{B} J_{B} J_{C} I_{C}$ is cyclic but $A I, I_{B} J_{C}$, and $J_{B} I_{C}$ do not concur. This counterexample configuration can be constructed using Solution 3 by letting $X$ be the intersection of $t$ with $\Gamma$ that lies on the same side of $B C$ as $A$ and constructing $I_{B}, I_{C}, J_{B}$, and $J_{C}$ as described in the solution, from which we can reconstruct $D$.

Conversely, the problem holds whenever $\angle A B C$ and $\angle B C A$ are both not obtuse, as can be seen from

---

### G8sol2
This is thus the weakest possible condition on triangle $A B C$ that is necessary for the problem to be true.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-097}

When $X$ lies on the tangent to circle $I B C$ at $I$, there is no contradiction in the proof of Claim 3 in Solution 1: circles $I I_{B} J_{C}$ and $I J_{B} I_{C}$ are distinct, and $X$ is the radical centre of circles $I I_{B} J_{C}, I J_{B} I_{C}$, and $I_{B} J_{B} I_{C} J_{C}$. There is also no contradiction in the final step of Solution 2, and indeed $I_{B} I_{C}$ and $B C$ intersect at the foot of the altitude from $A$ to $B C$.

There are no configuration issues with the direction (1) $\Longrightarrow$ (2). This implication holds without any constraint on triangle $A B C$, and the proofs in Solutions 1 and 2 apply without any modification.

\section*{Number Theory}

---

### N1sol1
It is easy to verify that $n=1,2,4,12$ all work. We must show they are the only possibilities. We write $n=2^{k} m$, where $k$ is a nonnegative integer and $m$ is odd. Since $m \mid n$, either $m+1$ is prime or $m+1 \mid n$.

In the former case, since $m+1$ is even it must be 2 , so $n=2^{k}$. If $k \geqslant 3$, we get a contradiction, since $8 \mid n$ but $9 \nmid n$. Hence $k \leqslant 2$, so $n \in\{1,2,4\}$.

In the latter case, we have $m+1 \mid 2^{k} m$ and $m+1$ coprime to $m$, and hence $m+1 \mid 2^{k}$. This means that $m+1=2^{j}$ with $2 \leqslant j \leqslant k$ (since $j=1$ gives $m=1$, which was considered earlier).

Then we have $2^{k}+1 \nmid n$ : since $2^{k}+1$ is odd, it would have to divide $m$ but is larger than $m$. Hence, by the condition of the problem, $2^{k}+1$ is prime. If $k=2, j$ must be 2 as well, and this gives the solution $n=12$. Also, $2^{k-1}+1 \nmid n$ for $k>2$ : since it is odd, it would have to divide $m$. However, we have no solutions to $2^{k-1}+1 \mid 2^{j}-1$ with $j \leqslant k$ : the left-hand side is greater than the right unless $j=k$, when the left-hand side is just over half the right-hand side.

Since we have $2^{k} \mid n$ and $2^{k}+1 \nmid n$, and $2^{k-1} \mid n$ and $2^{k-1}+1 \nmid n$, we must have $2^{k}+1$ and $2^{k-1}+1$ both prime. However, $2^{a}+1$ is a multiple of three if $a$ is odd, so we must have $2^{k}+1=3$ (impossible as this gives $k=1$ ) or $2^{k-1}+1=3$, which gives $j=k=2$, whence $n=12$.

---

### N1sol2
We proceed as in Solution 1 as far as determining that $n=2^{k}\left(2^{j}-1\right)$ with $j \leqslant k$.\\
Now, we have $2^{j} \mid n$ but $2^{j}+1 \nmid n$, as it is odd and does not divide $2^{j}-1$. Thus $2^{j}+1$ is prime. The theory of Fermat primes tells us we must have $j=2^{h}$ with $h>0$.

Then $2^{2^{h}}-1$ is congruent to 3 or 6 (modulo 9) depending on whether $h$ is odd or even, respectively. In particular it is not divisible by 9 , so $n=2^{k}\left(2^{2^{h}}-1\right)$ is not divisible by 9 ; so we must have $k \leqslant 2$, since if $k \geqslant 3$ then $8 \mid n$ but $9 \nmid n$ with 9 not prime.

---

### N1sol3
Let $p$ be the smallest integer not dividing $n$. Since $p-1$ is a divisor of $n, p$ must be a prime. Let $1 \leqslant r \leqslant p-1$ be the remainder of $n$ modulo $p$. Since $p-r<p$, we have $p-r \mid n$, so we may consider the divisor $d=\frac{n}{p-r}$.

Since $p \mid n-r$, we have $p \mid n+p-r$, whence $p \mid d+1$. Thus $d+1 \nmid n$; so it must be prime. On the other hand, this prime is divisible by $p$, so we conclude $d+1=p$, which means that $n=(p-1)(p-r)$.

Then from $p-2, p-3 \mid n$ we get $(p-2)(p-3) \mid 2(p-r)$, from which we find

$$
(p-2)(p-3) \leqslant 2(p-r) \leqslant 2(p-1)
$$

Solving this quadratic inequality gives $p \leqslant 5$, which means that $n \in\{1,2,4,8,12,16\}$. Of this set, $n=8$ and $n=16$ are not solutions.

---

### N1sol4
We suppose that $n$ is not 1 or 2.\\
Since $n \mid n$ and $n+1 \nmid n$, we know that $n+1$ is prime. Thus it is odd, so $2 \mid n$; as $n>2$, we have $\left.\frac{n}{2} \right\rvert\, n$ and $\frac{n}{2}+1 \nmid n$, so $\frac{n}{2}+1$ is prime. Thus it is also odd, so $4 \mid n$.

We must then have $\left.\frac{n}{4}+1 \right\rvert\, n$ or $\frac{n}{4}+1$ prime.

In the former case, $\frac{n}{4} \left\lvert\, 4\left(\frac{n}{4}+1\right)-n\right.$, so $\left.\frac{n}{4}+1 \right\rvert\, 4$. This means that $n=4$ or $n=12$.\\
In the latter case, $\frac{n}{4}+1$ must be odd if $n \neq 4$. Thus we have $n=8 m$ where $2 m+1,4 m+1$, $8 m+1$ are all prime; $n=8$ does not work, so $3 \mid m$ (otherwise one of those numbers would be divisible by 3). Thus $24 \mid n$, so $25 \mid n$ as 25 is not prime.

Now suppose that $p$ is the least positive integer not dividing $n$ : as in Solution 3 we know that $p$ is prime, and what we have done so far shows that $p \geqslant 7$. If $p^{2}-1=(p-1)(p+1)$ is the product of coprime integers less than $p$, it divides $n$, and $p^{2}$ is not prime so also divides $n$ (a contradiction); $p-1$ and $p+1$ are even and have no common factor higher than 2 , so all odd prime power divisors of their product are less than $p$ and the only case where $p^{2}-1$ is not a product of coprime integers less than $p$ is when one of $p-1$ and $p+1$ is a power of 2 , say $2^{m}$ (with $m \geqslant 3$ ). If $p=2^{m}-1$, then $3 p-1=4\left(3 \times 2^{m-2}-1\right)$ and $3 \times 2^{m-2}-1$ is an odd integer less than $p$, so $3 p-1 \mid n$ and so $3 p \mid n$. Finally, if $p=2^{m}+1$, then $m$ is even and $2 p-1=2^{m+1}+1$ is a multiple of 3 ; the only case where it is a power of 3 is when $m=2$, but we have $m \geqslant 3$, so $2 p-1$ is a product of coprime integers less than $p$ and again we have a contradiction.

---

### N1sol5
As in Solution 4, we deduce that if $n>2$ then $n$ must be even. We write $n=2 \cdot 3^{k} \cdot r$, where $k$ is a nonnegative integer and $3 \nmid r$.

Since $r$ and $2 r$ are both different and nonzero modulo 3, one of them must be congruent to 2 modulo 3 . We'll say that it is $a r$, where $a \in\{1,2\}$.

Since $a r \mid n$, we must have that $a r+1$ is either prime or a factor of $n$. In the first case, ar $+1=3$ because $3 \mid$ ar +1 , and so $n=2 \cdot 3^{k} \cdot r$, where $r=2 / a$ is 1 or 2 . Noting that we must have $k \leqslant 1$ (else $9 \mid n$ but $10 \nmid n$ ), we can examine cases to deduce that $n \in\{2,4,12\}$ are the only possibilities.

Otherwise, $a r+1 \mid n$. Since $a r+1$ is coprime to $r$, we must in fact have that $a r+1 \mid 2 \cdot 3^{k}$, and since $3 \mid$ ar +1 by assumption we deduce that $k \geqslant 1$. In particular, $3^{k}+1$ is an even number that is at least 4 , so is not prime and must divide $n$. As it is coprime to 3 , we must in fact have $3^{k}+1 \mid 2 r$.

Let $q_{1}$ and $q_{2}$ be such that $q_{1}(a r+1)=2 \cdot 3^{k}$ and $q_{2}\left(3^{k}+1\right)=2 r$. We have that $q_{1} a r<2 \cdot 3^{k}$ and $q_{2} 3^{k}<2 r$, and multiplying these together gives $q_{1} q_{2} a<4$.

If $a=2$ then $q_{1}=q_{2}=1$, so $2 r+1=2 \cdot 3^{k}$, which is not possible (considering both sides modulo 2).

If $a=1$ then $r$ must be equivalent to 2 modulo 3 , so $q_{2}\left(3^{k}+1\right)=2 r$ gives that $q_{2}$ is equivalent to 1 modulo 3 , whence $q_{2}=1$. So we deduce that $2 r=3^{k}+1$. Thus, we deduce that $q_{1}\left(3^{k}+3\right)=4 \cdot 3^{k}$, which rearranges to give $3^{k-1}\left(4-q_{1}\right)=q_{1}$, whence $3^{k-1} \leqslant q_{1}<4$ and so $k \leqslant 2$. We can examine cases to deduce that $n=12$ is the only possibility.

---

### N2sol1
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

### N2sol2
As in Solution 1, we reduce to the case where all elements of $\mathcal{S}$ are odd. Since all one-element sets satisfy the given conditions, we show that if $|\mathcal{S}| \geqslant 2$, then $|\mathcal{S}|=2$ and $\mathcal{S}=\{t, 3 t\}$ for some positive integer $t$.

Let $d$ be the largest element. For any $e \in \mathcal{S}$ with $e \neq d$ there must be a $f \in \mathcal{S}$ such that $d \mid e+2 f$. This implies $2 f \equiv-e(\bmod d)$, hence $2 f \equiv d-e(\bmod d)$. Now $d-e$ is even (because all elements in $\mathcal{S}$ are odd) and $d$ is odd, so $\frac{d-e}{2}$ is an integer and we have $f \equiv \frac{d-e}{2} (\bmod d)$. Further, $0<\frac{d-e}{2}<d$, while we must also have $0<f \leqslant d$, so $f=\frac{d-e}{2}$. We conclude that for any $e \in \mathcal{S}$ with $e \neq d$ the integer $\frac{d-e}{2}$ is also in $\mathcal{S}$ and not equal to $d$.

Denote by $e_{1}<e_{2}<\cdots<e_{k}<d$ the elements of $\mathcal{S}$, where $k \geqslant 1$. Then $\frac{d-e_{1}}{2}>\frac{d-e_{2}}{2}> \cdots>\frac{d-e_{k}}{2}$ are also elements of $\mathcal{S}$, none of them equal to $d$. Hence we must have $e_{1}=\frac{d-e_{k}}{2}$ and\\
$e_{k}=\frac{d-e_{1}}{2}$, so $2 e_{1}+e_{k}=d=2 e_{k}+e_{1}$. We conclude $e_{1}=e_{k}$, so $k=1$, and also $d=2 e_{k}+e_{1}=3 e_{1}$. Hence $\mathcal{S}=\left\{e_{1}, 3 e_{1}\right\}$ for some positive integer $e_{1}$.

---

### N2sol3
As in Solution 1, we reduce to the case where all elements of $\mathcal{S}$ are odd. Since all one-element sets satisfy the given conditions, we show that if $|\mathcal{S}| \geqslant 2$, then $|\mathcal{S}|=2$ and $\mathcal{S}=\{t, 3 t\}$ for some positive integer $t$.

Let $d$ be the largest element, and let $e \in \mathcal{S}$ be any other element. We will say that $x \in \mathcal{S} (\bmod d)$ if the unique element $y$ in $\{1, \ldots, d\}$ such that $x \equiv y(\bmod d)$ is an element of $\mathcal{S}$. Note that by the choice of $d$ being the largest element, if $x \neq d$, then $x \not \equiv 0(\bmod d)$. The given condition implies that if $b \in \mathcal{S}$, then $-\frac{b}{2} \in \mathcal{S}(\bmod d)$. Repeating this gives $-\frac{b}{2} \in \mathcal{S} \Rightarrow \frac{b}{4} \in \mathcal{S} (\bmod d)$, and by iterating, we have $b \in \mathcal{S} \Rightarrow \frac{b}{(-2)^{k}} \in \mathcal{S}(\bmod d)$ for all $k$. Since $d$ is odd, there is some $g$ such that $(-2)^{g} \equiv 1(\bmod d)$, so by setting $k=g-1$, we get that

$$
\text { for all } d \neq e \in \mathcal{S},-2 e \in \mathcal{S} \quad(\bmod d) \text {. }
$$

Now, if $e>\frac{d}{2}$, then $-2 e \in \mathcal{S}(\bmod d)$ and $d-2 e<0$, so $2 d-2 e \in \mathcal{S}$, contradicting the lack of even elements. Then $e<\frac{d}{2}$ for any $e \in \mathcal{S} \backslash\{d\}$, so we have $e \in \mathcal{S} \Rightarrow d-2 e \in \mathcal{S}$. Since $d-2 e \neq d$, we must have $d-2 e<\frac{d}{2}$, which rearranges to $e>\frac{d}{4}$.

Let $\lambda \in(0,1)$ be a positive real number and suppose we have proved that $e>\lambda d$ for any $e \in \mathcal{S} \backslash\{d\}$. Then $d-2 e>\lambda d$, which rearranges to $e<\frac{(1-\lambda) d}{2}$. Then $d-2 e<\frac{(1-\lambda) d}{2}$, which rearranges to $e>\frac{(1+\lambda) d}{4}$. Defining $\lambda_{0}=\frac{1}{4}$ and $\lambda_{i}=\frac{1+\lambda_{i-1}}{4}$ for $i \geqslant 1$, we have shown that for all $e \in \mathcal{S} \backslash\{d\}$ and all $\lambda_{i}, e>\lambda_{i} d$. Now note that the sequence $\lambda_{i}$ is increasing and bounded above by $\frac{1}{3}$, so it converges to some limit $\ell$, which satisfies $\ell=\frac{1+\ell}{4}$, so $\ell=\frac{1}{3}$. Hence $e \geqslant \frac{d}{3}$, but then $d-2 e \geqslant \frac{d}{3}$ implies $e \leqslant \frac{d}{3}$, so $e$ must be $\frac{d}{3}$, and we are done.

---

### N2comment
We can finish Solution 3 alternatively as follows: after showing that if $e \in \mathcal{S} \backslash\{d\}$ then $d-2 e \in \mathcal{S} \backslash\{d\}$, note that

$$
(d-2 e)-\frac{d}{3}=\frac{2 d}{3}-2 e=-2\left(e-\frac{d}{3}\right)
$$

So consider $e \in \mathcal{S} \backslash\{d\}$ maximising $\left|e-\frac{d}{3}\right|$. If $e \neq \frac{d}{3}$, them the above shows that $\left|(d-2 e)-\frac{d}{3}\right|>\left|e-\frac{d}{3}\right|$, which is a contradiction. Thus $\mathcal{S} \backslash\{d\}$ is empty or equal to $\left\{\frac{d}{3}\right\}$, which completes the proof.

---

### N3sol1
We say that an integer sequence $b_{1}, b_{2}, \ldots$ is good if for any pair of positive integers $m \leqslant n$, the arithmetic mean $\frac{b_{m}+b_{m+1}+\cdots+b_{n}}{n-m+1}$ is an integer. Then the condition in the question is equivalent to saying that the sequences ( $a_{i}$ ) and ( $\nu_{p}\left(a_{i}\right)$ ) for all primes $p$ are good.\\
Claim 1. If ( $b_{i}$ ) is a good sequence, then $n-m \mid b_{n}-b_{m}$ for all pairs of integers $m, n$.\\
Proof. This follows from $n-m$ dividing $b_{m}+b_{m+1}+\cdots+b_{n-1}$ and $b_{m+1}+b_{m+2}+\cdots+b_{n}$, and then taking the difference.

Claim 2. If ( $b_{i}$ ) is a good sequence where some integer $b$ occurs infinitely many times, then ( $b_{i}$ ) is constant.\\
Proof. Say $b_{n_{1}}, b_{n_{2}}, b_{n_{3}}, \ldots$ are equal to $b$. Then for all $m$, we have that $b-b_{m}=b_{n_{j}}-b_{m}$ is divisible by infinitely many different integers $n_{j}-m$, so it must be zero. Therefore the sequence is constant.

Now, for a given prime $p$, we look at the sequence $\left(\nu_{p}\left(a_{i}\right)\right)$. Let $k=\nu_{p}\left(a_{1}\right)$. Then Claim 1 tells us that $a_{1} \equiv a_{n p^{k+1}+1}\left(\bmod p^{k+1}\right)$ for all $n$, which implies that $\nu_{p}\left(a_{n p^{k+1}+1}\right)=k$ for all $n$. We now have that $k$ appears infinitely many times in this good sequence, so by Claim 2, the sequence ( $\nu_{p}\left(a_{i}\right)$ ) is constant. This holds for all primes $p$, so ( $a_{i}$ ) must in fact be constant.

---

### N3sol2
As in Claim 1 of Solution 1, we have that $a_{i+r} \equiv a_{i}(\bmod r)$, which tells us that the sequence $a_{i}$ is periodic modulo $p$ with period $p$. Also, by a similar argument, we have that $a_{i+r} / a_{i}$ is the $r^{\text {th }}$ power of a rational number.

Now suppose that for some $i \not \equiv j(\bmod p)$ we have $a_{i}, a_{j} \not \equiv 0(\bmod p)$. As $p$ and $p-1$ are coprime, we can find some $i^{\prime} \equiv i(\bmod p), j^{\prime} \equiv j(\bmod p)$ such that $p-1 \mid i^{\prime}-j^{\prime}$. Then $a_{i^{\prime}} / a_{j^{\prime}}$ is a perfect $(p-1)^{\text {th }}$ power, so

$$
a_{i^{\prime}}=t u^{p-1}, \quad a_{j^{\prime}}=t v^{p-1}
$$

for some positive integers $t, u, v$ not divisible by $p$. By Fermat's little theorem, $u^{p-1}$ and $v^{p-1}$ must be 1 modulo $p$. So we must have

$$
a_{i} \equiv a_{i^{\prime}} \equiv t \equiv a_{j^{\prime}} \equiv a_{j}(\bmod p) .
$$

Thus all values of $a_{i}$ that are not divisible by $p$ are congruent modulo $p$.\\
For the sum of $p$ consecutive values to be divisible by $p$, this means that all the $a_{i}$ are congruent modulo $p$. Since this is true for all primes $p$, the sequence must therefore be constant.

---

### N3sol3
Fix an arbitrary index $m$. First, we show that $a_{m}$ divides $a_{n}$ for sufficiently large $n$. Let $n$ be sufficiently large that $n>\nu_{p}\left(a_{m}\right)+m$ for every prime $p$. By Claim 1 of Solution 1, we have

$$
\nu_{p}\left(a_{m}\right) \equiv \nu_{p}\left(a_{n}\right) \quad(\bmod n-m)
$$

Since $\nu_{p}\left(a_{m}\right)<n-m$, it follows that $\nu_{p}\left(a_{m}\right) \leqslant \nu_{p}\left(a_{n}\right)$. This holds for every prime $p$, so $a_{m} \mid a_{n}$.\\
Next, suppose that there is some index $k$ such that $a_{m}$ does not divide $a_{k}$. By the previous, there is a maximal such $k$. Then $a_{k+1}, a_{k+2}, \ldots$ are all divisible by $a_{m}$. But now applying the first condition gives

$$
a_{m} \mid a_{k}+a_{k+1}+\cdots+a_{k+a_{m}-1}
$$

so $a_{m}$ divides $a_{k}$, a contradiction. Therefore every term $a_{n}$ is divisible by $a_{m}$.\\
As $m$ was arbitrary, we now have $a_{m} \mid a_{n}$ and vice versa for all $m, n$. So the sequence must be constant.

---

### N4sol1
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

### N4sol2
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

### N5sol1
If $\mathcal{S}$ has only one element $p$, then $b_{i}=p^{i-1}$ and we can easily find $a_{1}, \ldots, a_{n}$ with $2=\left\lceil\sum_{i=0}^{n-1} \frac{1}{p^{i}}\right\rceil=\sum_{i=0}^{n-1} \frac{a_{i}}{p^{i-1}}$ by taking $a_{1}=a_{2}=\cdots=a_{n-1}=1$ and choosing $a_{n}= p^{n-1}-\left(p+p^{2}+\ldots+p^{n-2}\right)$.

More generally, observe that the sum of $\frac{1}{b_{i}}$ over all $i$ is

$$
\begin{aligned}
\sum_{i} \frac{1}{b_{i}} & =\prod_{i}\left(1+\frac{1}{p_{i}}+\frac{1}{p_{i}^{2}}+\ldots\right) \\
& =\prod_{p \in \mathcal{S}} \frac{p}{p-1}
\end{aligned}
$$

In particular, if $n$ is large enough, then

$$
\left\lceil\sum_{j=1}^{n} \frac{1}{b_{j}}\right\rceil=\left\lceil\prod_{p \in \mathcal{S}} \frac{p}{p-1}\right\rceil
$$

For the remainder of the proof, we will only consider $n$ large enough that this equality holds.\\
Next, we handle the special case $\mathcal{S}=\{2,3\}$, for which this product is 3 . Start by setting

$$
a_{i}= \begin{cases}1, & \text { if } 2 b_{i} \leqslant b_{n} \\ 2, & \text { if } 2 b_{i}>b_{n}\end{cases}
$$

Then,

$$
\sum_{\substack{i \leqslant n \\ \nu_{3}\left(b_{i}\right)=t}} \frac{a_{i}}{b_{i}}= \begin{cases}\frac{2}{3^{t}}, & \text { if } b_{n} \geqslant 3^{t} \\ 0, & \text { otherwise }\end{cases}
$$

As a result,

$$
\begin{aligned}
\sum_{i \leqslant n} \frac{a_{i}}{b_{i}} & =\sum_{\substack{t \geqslant 0 \\
3^{t} \leqslant b_{n}}} \frac{2}{3^{t}} \\
& =3-\frac{1}{3^{T}}
\end{aligned}
$$

where $T$ is the largest $t \geqslant 0$ with $3^{t} \leqslant b_{n}$. Thus, increasing $a_{j}$ by one (where $b_{j}=3^{T}$ ) gives a sequence of $a_{i}$ that works.

Otherwise, we may assume that $|\mathcal{S}|>1$ and $\mathcal{S} \neq\{2,3\}$, which means that the product $\prod_{p \in \mathcal{S}} \frac{p}{p-1}$ is not an integer. Indeed,

\begin{itemize}
  \item if $|\mathcal{S}|>2$ then 2 divides the denominator at least twice and so divides the denominator of the overall fraction;
  \item if $|\mathcal{S}|=2$ and $2 \notin \mathcal{S}$ then 2 divides the denominator and not the numerator;
  \item if $\mathcal{S}=\{2, p\}$ then the product is $2 p /(p-1)$ which is not an integer for $p>3$.
\end{itemize}

It follows that for some fixed $\alpha>0$, we have that

$$
\left\lceil\prod_{p \in \mathcal{S}} \frac{p}{p-1}\right\rceil=\prod_{p \in \mathcal{S}} \frac{p}{p-1}+\alpha
$$

from which it follows that

$$
\left\lceil\sum_{i=1}^{n} \frac{1}{b_{i}}\right\rceil-\sum_{i=1}^{n} \frac{1}{b_{i}}>\alpha
$$

It will now suffice to prove the following claim.\\
Claim. Suppose that $n$ is large enough, and let $e_{p}$ be the largest nonnegative integer such that $p^{e_{p}} \leqslant b_{n}$. Let $M=\prod_{p \in \mathcal{S}} p^{e_{p}}$. If $u$ is a positive integer such that $u / M>\alpha$, then there exist nonnegative integers $a_{i}$ such that

$$
\sum_{i} \frac{a_{i}}{b_{i}}=\frac{u}{M} .
$$

The problem statement follows after replacing $a_{i}$ with $a_{i}+1$ for each $i$.\\
To prove this, choose some constant $c$ such that $\sum_{p \in \mathcal{S}} p^{-c}<\alpha$, and suppose $n$ is large enough that $p^{c}<b_{n}$ for each $p \in \mathcal{S}$; in particular, $p^{c} \mid M$ with $M$ defined as above.

For each $p \in \mathcal{S}$, let $i_{p}$ be such that $b_{i_{p}}=p^{e_{p}}$ and choose the smallest nonnegative integer $a_{i_{p}}$ satisfying

$$
p^{e_{p}-c} \left\lvert\, a_{i_{p}}\left(\frac{M}{p^{e_{p}}}\right)-u .\right.
$$

Such an $a_{i_{p}}$ must exist and be at most $p^{e_{p}-c}$; indeed, $\frac{M}{p^{e_{p}}}$ is an integer coprime to $p$, so we can take $a_{i_{p}}$ to be equal to $u$ times its multiplicative inverse modulo $p^{e_{p}-c}$. The sum of the contributions to the sum from the $a_{i_{p}}$ is at most

$$
\sum_{p \in \mathcal{S}} \frac{p^{e_{p}-c}}{p^{e_{p}}}=\sum_{p \in \mathcal{S}} p^{-c}<\alpha
$$

So, we have

$$
\frac{u}{M}=\sum_{p \in \mathcal{S}} \frac{a_{i_{p}}}{p^{e_{p}}}+\frac{r}{\prod_{p \in \mathcal{S}} p^{c}},
$$

where $r$ is an integer because of our choice of $a_{i_{p}}$ and $r$ is nonnegative because of the bound on $u$. Simply choose $a_{i}=r$ where $b_{i}=\prod_{p \in \mathcal{S}} p^{c}$ to complete the proof.

---

### N5sol2
We reduce to the claim as in Solution 1, and provide an alternative approach for constructing the $a_{i}$.

Let $p_{0} \in \mathcal{S}$ be the smallest prime in $\mathcal{S}$. Let $z_{0}=u / M$. We construct a sequence $z_{0}, z_{1}$, $z_{2}, \ldots$ and values of $a_{i}$ by the following iterative process: to construct $z_{j+1}$,

\begin{itemize}
  \item select the largest prime $p \in \mathcal{S}$ dividing the denominator of $z_{j}$, and let $\mu$ be the number of times $p$ divides the denominator of $z_{j}$;
  \item choose the largest $\nu$ such that $p_{0}^{\nu} p^{\mu} \leqslant b_{n}$, and let $i \leqslant n$ be such that $b_{i}=p_{0}^{\nu} p^{\mu}$;
  \item choose $0 \leqslant a_{i}<p$ such that the denominator of $z_{k}-a_{i} / b_{i}$ has at most $\mu-1$ factors of $p$, and let $z_{k+1}=z_{k}-a_{i} / b_{i}$;
  \item continue until $p_{0}$ is the only prime dividing the denominator of $z_{k}$.
\end{itemize}

Note that we can always choose $a_{i}$ in step 3 ; by construction, $z_{k} b_{i}$ has no factors of $p$ in its denominator, so must be realised as an element of $\mathbb{Z}_{p}$.

Each time we do this, $b_{i}>M / p_{0}$ by construction, so

$$
\frac{a_{i}}{b_{i}}<\frac{p p_{0}}{M} \leqslant \frac{p_{0} p_{1}}{M},
$$

where $p_{1}$ is the largest prime in $\mathcal{S}$. And the number of times we do this operation is at most

$$
\sum_{\substack{p \in \mathcal{S} \\ p \ngtr p_{0}}} e_{p} \leqslant|\mathcal{S}| \log _{2}(M),
$$

so the sum of the $a_{i} / b_{i}$ we have assigned is at most $|\mathcal{S}| p_{0} p_{1} \log _{2}(M) / M$.\\
Choose $n$ large enough that $\log _{2}(M) / M<\alpha$; after subtracting the above choices of $a_{i} / b_{i}$ from $u / M$, we have a quantity of the form $r / p_{0}^{e_{p_{0}}}$, where $r$ is an integer by construction and $r$ is positive by the above bounds. Simply set $a_{i}=r$ where $b_{i}=p_{0}^{e_{0}}$ to complete the proof.

---

### N5sol3
As in Solution 1, we may handle $|\mathcal{S}|=1$ and $\mathcal{S}=\{2,3\}$ separately; otherwise, we can define $\alpha$ as we did in that solution. Also define $e_{p}$ to be the largest nonnegative integer such that $p^{e_{p}} \leqslant b_{n}$ as we did in

---

### N5sol1
We will show that, for $n$ sufficiently large, we may choose some $j \leqslant n$, and positive integers $a_{i}$, such that

$$
\sum_{i \neq j} \frac{a_{i}}{b_{i}}-\sum_{i \neq j} \frac{1}{b_{i}}<\alpha .
$$

and all $\frac{a_{i}}{b_{i}}$ are integer multiples of $\frac{1}{b_{j}}$. We then set $a_{j}$ to be the least positive integer such that the sum on the left is an integer, which will obviously have the required value.

Concretely, choose $j$ such that $b_{j}=\prod_{p \in \mathcal{S}} p^{\left\lfloor e_{p} /|\mathcal{S}|\right\rfloor}$, which is less than $b_{n}$ by construction. For $i \neq j$, set $a_{i}=b_{i} / \operatorname{gcd}\left(b_{i}, b_{j}\right)$. We have

$$
\sum_{i \neq j} \frac{a_{i}}{b_{i}}-\sum_{i \neq j} \frac{1}{b_{i}}<\sum_{\substack{i \neq j \\ a_{i}>1}} \frac{a_{i}}{b_{i}} .
$$

If $a_{i}>1$, then there must be some $p \in \mathcal{S}$ for which $p^{\left\lfloor e_{p}|\mathcal{S}|\right]+1} \mid b_{i}$, and so

$$
\frac{a_{i}}{b_{i}}=\frac{1}{\operatorname{gcd}\left(b_{i}, b_{j}\right)} \leqslant \frac{1}{p^{\left\lfloor e_{p} /|\mathcal{S}|\right]}}<\frac{p}{b_{n}^{1 /|\mathcal{S}|}},
$$

where the last inequality follows from the fact that $p^{e_{p}+1}>b_{n}$.\\
Now $n \leqslant \prod_{p \in \mathcal{S}}\left(\log _{p}\left(b_{n}\right)+1\right) \leqslant\left(2 \log b_{n}\right)^{|\mathcal{S}|}$, so

$$
\sum_{\substack{i \neq j \\ a_{i}>1}} \frac{a_{i}}{b_{i}} \leqslant \frac{\left(2 \log b_{n}\right)^{|\mathcal{S}|}}{b_{n}^{1 /|\mathcal{S}|}},
$$

and so we can choose $n$ large enough that this quantity is less than $\alpha$, as required.

---

### N6sol1
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

### N6comment
In fact, there is no need to pass from polynomials $P$ to functions $f$, as any function mod $p$ is a polynomial. Concretely, instead of passing from $f$ to $g$, we would have instead replaced $P(X)$ with $P(X)+1-(X-u)^{p-1}$, which is a polynomial that is unchanged except at $X=u$.

---

### N6sol2
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

### N6comment
By Wilson's theorem, we know that the product of the nonzero elements mod $p$ is -1 ; however, this fact was not necessary for the solution so we chose to present the solution without needing to state it.

---

### N6comment
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

### N6sol3
As in Solution 1, we will reduce to the case of $p$ being an odd prime and $f$ being a function $\bmod p$ with no roots which is surjective onto the set of nonzero residues $\bmod p$, although we make no assumption about the values of $x_{1}$ and $x_{2}$ with $f\left(x_{1}\right)=f\left(x_{2}\right)$.

We will again consider quadratics of the form $Q_{a, b, c}(X)=a R(b X+c)$, where $R(X)=X^{2}-r$ for an arbitrary fixed quadratic nonresidue $r, a$ and $b$ are nonzero $\bmod p$, and $c$ is any residue $\bmod p$.

For each fixed $b$ and $c$, there must be $n$ pairs ( $a, x$ ) such that $a R(b x+c)=f(x)$, because there must be exactly one value of $a$ for each $x$. If any $a$ appears in no such pair then we are done, so assume otherwise. In other words, there must be exactly one $a$ such that there are two such $x$, and for all other $a$ there is only one such $x$.

Thus, for each ( $b, c$ ), there is exactly one unordered pair $\left\{x_{1}, x_{2}\right\}$ such that for some $a$ we have $f\left(x_{i}\right)=a R\left(b x_{i}+c\right)$; in other words, there is exactly one unordered pair $\left\{x_{1}, x_{2}\right\}$ such that $f\left(x_{1}\right) / R\left(b x_{1}+c\right)=f\left(x_{2}\right) / R\left(b x_{2}+c\right)$.

Now, we show that for each unordered pair $\left\{x_{1}, x_{2}\right\}$ there must be at least one pair ( $b, c$ ) such that $f\left(x_{1}\right) / R\left(b x_{1}+c\right)=f\left(x_{2}\right) / R\left(b x_{2}+c\right)$. Indeed, let $t=f\left(x_{1}\right) / f\left(x_{2}\right)$. There must be some $x_{1}^{\prime}, x_{2}^{\prime}$ such that $R\left(x_{1}^{\prime}\right) / R\left(x_{2}^{\prime}\right)=t$; this is because $R(X)$ and $t R(X)$ both take $\frac{p+1}{2}$ nonzero values $\bmod p$, so the intersection must be nonempty by the pigeonhole principle. Choosing $b$ and $c$ such that $b x_{1}+c=x_{1}^{\prime}$ and $b x_{2}+c=x_{2}^{\prime}$ gives the claim.

Note further that if $(b, c)$ and $\left\{x_{1}, x_{2}\right\}$ satisfy the relation, then the same is true for $(-b,-c)$ and $\left\{x_{1}, x_{2}\right\}$ because $R(b x+c)=R(-b x-c)$. Since $b$ is nonzero, this means that each pair $\left\{x_{1}, x_{2}\right\}$ corresponds to at least two pairs ( $b, c$ ). However, since there are $p(p-1)$ pairs ( $b, c$ ) with $b$ nonzero and $p(p-1) / 2$ unordered pairs $\left\{x_{1}, x_{2}\right\}$, each $\left\{x_{1}, x_{2}\right\}$ must correspond to exactly two pairs ( $b, c$ ) and ( $-b,-c$ ) for some ( $b, c$ ).

Now, since the image of $f$ has only $p-1$ elements, there must be some $x_{1}, x_{2}$ such that $f\left(x_{1}\right)=f\left(x_{2}\right)$. Choose any $b, c$ such that $b x_{1}+c=-\left(b x_{2}+c\right)$, so $R\left(b x_{1}+c\right)=R\left(b x_{2}+c\right)$ and so $f\left(x_{1}\right) / R\left(b x_{1}+c\right)=f\left(x_{2}\right) / R\left(b x_{2}+c\right)$. There is such a pair $b, c$ for any nonzero $b$, so there are at least $p-1$ such pairs, and this quantity is greater than 2 for $p \geqslant 5$.

Finally, for the special case that $p=3$, we observe that there must be at least one allowed value for $Q(x)$ for each $x$, so there must exist such a quadratic $Q$ by Lagrange interpolation.

---

### N6comment
We may also handle the case $p=3$ as follows. Recall that we may assume $f$ is nonzero and surjective onto $\{1,2\} \bmod 3$, so the image of $f$ must be $(1,1,2)$ or $(1,2,2)$ in some order. Without loss of generality $f(1)=f(2)$, so we either have $(f(0), f(1), f(2))=(1,2,2)$ or $(2,1,1)$. In the first case, take $Q(X)=2 X^{2}+2$, and in the second case take $Q(X)=X^{2}+1$.

In some sense, this is equivalent to the Lagrange interpolation approach, as in each case the polynomial $Q(X)$ can be determined by Lagrange interpolation.

---

### N6sol4
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

### N6comment
We do not have much freedom to choose a different polynomial in place of $R(T)= (T-1)(T-3)(T-4)$ in this argument. Indeed, it can be shown (by comparing coefficients of $\binom{T}{K}$ ) that if $R$ has degree at most 3 , then the expected value of $R(T)$ tends to $\frac{1}{3}(R(4)+2 R(1))$ as $p$ tends to infinity, so $R$ must have both 1 and 4 as roots. In particular, $R$ must be of the form $R(T)=(T-1)(T-4)(T-d)$ for some $d \geqslant 3$, and if $d<4$ then the argument works for any $p$ with $p>4 /(4-d)$.

---

### N7sol1
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

### N7comment
A quicker but less straightforward proof that $f(1)=1$ is to let $f(n)=M$ be the least value that $f$ takes; then $P(1, n)$ gives $M^{2}=f(n)^{2}=f(1) f(f(n))^{2} \geqslant M^{3}$ so $M=1$ and $f(1)=1$.

---

### N7sol2
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
