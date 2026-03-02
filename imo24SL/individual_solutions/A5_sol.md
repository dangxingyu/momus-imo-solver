### reference solution 1
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


---

### reference solution 2
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


---

### reference solution 3
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
