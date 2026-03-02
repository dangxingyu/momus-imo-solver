### reference solution 1
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


---

### reference solution 2
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


---

### reference solution 3
As in Solution 1, we may handle $|\mathcal{S}|=1$ and $\mathcal{S}=\{2,3\}$ separately; otherwise, we can define $\alpha$ as we did in that solution. Also define $e_{p}$ to be the largest nonnegative integer such that $p^{e_{p}} \leqslant b_{n}$ as we did in

---


---

### reference solution 1
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
