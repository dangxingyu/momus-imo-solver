### reference solution 1
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


---

### reference comment
Lemma 1 can also be proven as follows. We start by proving that $f$ must be surjective. Suppose not; then, there must be some $t$ which does not appear in the output of $f$. $P(x, t-f(x))$ tells us that $t \sim x+f(t-f(x))$, and so by assumption $f(t)=x+f(t-f(x))$ for all $x$. But setting $x=f(t)-t$ gives $t=f(t-f(f(t)-t))$, contradicting our assumption about $t$.

Now, choose some $t$ such that $f(t)=0$; such a $t$ must exist by surjectivity. $P(t, t)$ tells us that $f(t)=t$, or in other words $t=0$ and $f(0)=0$. The remainder of the proof is the same as the proof given in

---


---

### reference solution 1


---


---

### reference solution 2
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


---

### reference solution 3
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


---

### reference comment
Lemma 2 also follows from $f(x+d)-f(x) \in\{f(d),-f(-d)\}$ as proven in

---


---

### reference solution 2
Indeed, we also have $f(-x)-f(-x-d) \in\{f(d),-f(-d)\}$, and then subtracting the second from the first we get $g(x+d)-g(x) \in\{g(d),-g(d), 0\}$. Replacing $x+d$ and $x$ with $x$ and $-y$ gives the statement of Lemma 2.

---


---

### reference comment
It is possible to prove using Lemma 2 that $g$ must have image of the form $\{0, c, 2 c\}$ if it has size greater than 2 . Indeed, if $g(x)=c$ and $g(y)=d$ with $0<c<d$, then $g(x+y)=d-c$ as it must be nonnegative, and $g(y)=g((x+y)+(-x))=|d-2 c|$ provided that $d \neq 2 c$.

However, it is not possible to rule out $\{0, c, 2 c\}$ based entirely on the conclusion of Lemma 2; indeed, the function given by

$$
g(x)= \begin{cases}0, & \text { if } x=2 n \text { for } n \in \mathbb{Z} \\ 2, & \text { if } x=2 n+1 \text { for } n \in \mathbb{Z} \\ 1, & \text { if } x \notin \mathbb{Z}\end{cases}
$$

satisfies the conclusion of Lemma 2 (even though there is no function $f$ giving this choice of $g$ ).\\
Note. Solution 1 actually implies that the result also holds over $\mathbb{R}$. The proposal was originally submitted and evaluated over $\mathbb{Q}$ as it is presented here, and the Problem Selection Committee believes that this form is more suitable for the competition because it allows for more varied and interesting approaches once Lemma 1 has been established. Even the variant here defined over $\mathbb{Q}$ was found to be fairly challenging.

---
