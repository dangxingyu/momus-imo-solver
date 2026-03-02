### reference solution 1
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


---

### reference solution 2
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


---

### reference comment
The two solutions above differ in approach, but have some overlap in the structure they reveal. Indeed, the $C+n D$ of Solution 1 is the $p_{n}$ of Solution 2, while the $m_{r+1}-m_{r}$ of Solution 1 turns out to be equal to the $k_{r}$ of

---


---

### reference solution 2


---
