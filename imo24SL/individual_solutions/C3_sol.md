### reference solution 1
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


---

### reference comment
Either proof of Lemma 3 can be adapted to show that the configuration in Lemma 1 is the only one which achieves the bound.

---
