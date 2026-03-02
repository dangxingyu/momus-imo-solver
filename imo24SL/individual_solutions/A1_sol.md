### reference solution 1
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


---

### reference solution 2
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


---

### reference comment
An alternative ending to the previous solution is as follows.\\
By definition we have $S_{n} \leqslant \alpha \frac{n(n+1)}{2}$, on the other hand (5) implies $S_{n} \geqslant \alpha n^{2}-n$ for all $n$ large enough, so $\alpha=0$.

---


---

### reference solution 3
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


---

### reference solution 4
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
