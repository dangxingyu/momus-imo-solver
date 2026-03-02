### reference solution 1
We say that an integer sequence $b_{1}, b_{2}, \ldots$ is good if for any pair of positive integers $m \leqslant n$, the arithmetic mean $\frac{b_{m}+b_{m+1}+\cdots+b_{n}}{n-m+1}$ is an integer. Then the condition in the question is equivalent to saying that the sequences ( $a_{i}$ ) and ( $\nu_{p}\left(a_{i}\right)$ ) for all primes $p$ are good.\\
Claim 1. If ( $b_{i}$ ) is a good sequence, then $n-m \mid b_{n}-b_{m}$ for all pairs of integers $m, n$.\\
Proof. This follows from $n-m$ dividing $b_{m}+b_{m+1}+\cdots+b_{n-1}$ and $b_{m+1}+b_{m+2}+\cdots+b_{n}$, and then taking the difference.

Claim 2. If ( $b_{i}$ ) is a good sequence where some integer $b$ occurs infinitely many times, then ( $b_{i}$ ) is constant.\\
Proof. Say $b_{n_{1}}, b_{n_{2}}, b_{n_{3}}, \ldots$ are equal to $b$. Then for all $m$, we have that $b-b_{m}=b_{n_{j}}-b_{m}$ is divisible by infinitely many different integers $n_{j}-m$, so it must be zero. Therefore the sequence is constant.

Now, for a given prime $p$, we look at the sequence $\left(\nu_{p}\left(a_{i}\right)\right)$. Let $k=\nu_{p}\left(a_{1}\right)$. Then Claim 1 tells us that $a_{1} \equiv a_{n p^{k+1}+1}\left(\bmod p^{k+1}\right)$ for all $n$, which implies that $\nu_{p}\left(a_{n p^{k+1}+1}\right)=k$ for all $n$. We now have that $k$ appears infinitely many times in this good sequence, so by Claim 2, the sequence ( $\nu_{p}\left(a_{i}\right)$ ) is constant. This holds for all primes $p$, so ( $a_{i}$ ) must in fact be constant.

---


---

### reference solution 2
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


---

### reference solution 3
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
