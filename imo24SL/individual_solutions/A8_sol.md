### reference solution 1
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


---

### reference comment
Here is a variant of

---


---

### reference solution 1
Proceed up to proving $b_{n}-n$ is eventually periodic with period $q-p$. Then there is some minimal value of $b_{n}-n$. Suppose $n$ attains this minimal value. Since $b_{n+p}-n-p \leqslant b_{n}-n, n+p$ also attains this minimal value. And since $p$ and $q-p$ are coprime, all $n \geqslant q$ must attain this minimal value. Hence $b_{n+1}=b_{n}+1$ for all $n \geqslant q$. Finish as above.

---


---

### reference comment
It is also possible to solve the problem using a weaker version of Lemma 2 and without Lemma 3. For example, the following lemma plays a similar role.\\
Lemma 2'. Let $b_{n}^{\prime}=\min \left(a_{[n, n+p]}\right)$. Then $b_{n}^{\prime}<b_{n+p}^{\prime}$.\\

---


---

### reference comment
To solve the problem for sequences $a_{n}$ of arbitrary integers, we will use the following lemma.\\
Lemma 4. The sequence $a_{n}$ is either bounded above or bounded below.\\
Proof. Suppose that $a_{n}$ is unbounded above and below. Then there is some $i$ such that $a_{i}<a_{1}-p$. There is also some $j$ such that $a_{j}>\max \left(a_{[1, i]}\right)+q$. Now let $a_{l}$ be minimal amongst $a_{[1, j]}$. Since $a_{l} \leqslant a_{i}, a_{l}<a_{1}-p$ and $a_{l}<a_{j}-k p$. By Lemma $1,1+p<l<j-k p$. So $\min \left(a_{[l-p, l+q-p]}\right)=a_{l}$. By Lemma 1 again, $\max \left(a_{[l-p, l+q-p]}\right) \leqslant a_{l}+(k-1) p<a_{l}+q$, which is a contradiction.

From there, the solution above can be adapted to prove that $a_{n}=n+C$ for all $n$ or $a_{n}=-n+C$ for all $n$, where $C$ can be any constant integer.

---


---

### reference solution 2
For $n, x \geqslant 1$, let the $x$-width of $n$ be $\max \left(a_{[n, n+x]}\right)-\min \left(a_{[n, n+x]}\right)$. We call a positive integer $x$ good if the $x$-width of $n$ is less than or equal to $x$ for all sufficiently large $n$, and we call $x$ very good if the $x$-width of $n$ is equal to $x$ for sufficiently large $n$.\\
Lemma 1. If $p^{\prime}$ is good and $q^{\prime}$ is very good with $p^{\prime}<q^{\prime}<2 p^{\prime}$, then $2 p^{\prime}-q^{\prime}$ is also good.\\
Proof. Note that $0<q^{\prime}-p^{\prime}<p^{\prime}<q^{\prime}$. Let $n$ be a sufficiently large positive integer. Then for $k \in\left[n+q^{\prime}-p^{\prime}, n+p^{\prime}\right]$, we have $a_{k} \geqslant \max \left(a_{\left[n, n+p^{\prime}\right]}\right)-p^{\prime}$ and $a_{k} \geqslant \max \left(a_{\left[n+q^{\prime}-p^{\prime}, n+q^{\prime}\right]}\right)-p^{\prime}$ since $p^{\prime}$ is good, which shows $a_{k} \geqslant \max \left(a_{\left[n, n+q^{\prime}\right]}\right)-p^{\prime}$. Similarly we get $a_{k} \leqslant \min \left(a_{\left[n, n+q^{\prime}\right]}\right)+p^{\prime}$.

Therefore, for all $k \in\left[n+q^{\prime}-p^{\prime}, n+p^{\prime}\right]$ we have $a_{k} \in\left[\max \left(a_{\left[n, n+q^{\prime}\right]}\right)-p^{\prime}, \min \left(a_{\left[n, n+q^{\prime}\right]}\right)+p^{\prime}\right]$. Thus, the $\left(2 p^{\prime}-q^{\prime}\right)$-width of $n+q^{\prime}-p^{\prime}$ is at most $\left(\min \left(a_{\left[n, n+q^{\prime}\right]}\right)+p^{\prime}\right)-\left(\max \left(a_{\left[n, n+q^{\prime}\right]}\right)-p^{\prime}\right)= 2 p^{\prime}-q^{\prime}$. The lemma follows.\\
Lemma 2. Let $p^{\prime}$ be a good number and $q^{\prime}$ a very good number with $p^{\prime}<q^{\prime}$. For sufficiently large $n$, take $s, t \in\left[n, n+q^{\prime}\right]$ such that $\min \left(a_{\left[n, n+q^{\prime}\right]}\right)=a_{s}$ and $\max \left(a_{\left[n, n+q^{\prime}\right]}\right)=a_{t}$. Then $s \in\left[n, n+p^{\prime}\right]$ and $t \in\left[n+q^{\prime}-p^{\prime}, n+q^{\prime}\right]$.\\
Proof. Lemma 2 and Lemma 3 from Solution 1 hold with $p$ and $q$ replaced by $p^{\prime}$ and $q^{\prime}$ by similar arguments. We can deduce the statement about $s$ from Lemma 2 of

---


---

### reference solution 1
We can deduce the statement about $t$ from Lemma 3 of

---


---

### reference solution 1
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


---

### reference solution 1
\section*{Combinatorics}

---
