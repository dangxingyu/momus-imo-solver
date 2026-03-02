### reference solution 1
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


---

### reference solution 2
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
