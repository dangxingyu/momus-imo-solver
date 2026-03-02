### reference solution 1
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


---

### reference solution 2
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
