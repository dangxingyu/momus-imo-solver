### reference solution 1
}
Lemma 1. For any set $\mathcal{S}, \mathcal{S}$ wins if and only if $J(\mathcal{S}, \varnothing)$ wins. Similarly, $\mathcal{S}$ wins if and only if $J(\varnothing, \mathcal{S})$ wins.\\
Proof. Let ( $k, m$ ) be a move on $\mathcal{S}$, and let $\mathcal{T}$ be the result of applying the move. Then we can reduce $J(\mathcal{S}, \varnothing)$ to $J(\mathcal{T}, \varnothing)$ by applying the move ( $k+1,2 m-1$ ).

Conversely, let $(k, m)$ be a move on $J(\mathcal{S}, \varnothing)$. We can express the result of this move as $J(\mathcal{T}, \varnothing)$ for some $\mathcal{T}$. Then we can reduce $\mathcal{S}$ to $\mathcal{T}$ by applying the move ( $\max (k-1,0),(k+1) / 2$ ).

This gives us a natural bijection between games starting with $\mathcal{S}$ and games starting with $J(\mathcal{S}, \varnothing)$ and thus proves the first part of the lemma. The second part follows by a similar argument.\\
Lemma 2. If $\mathcal{S}$ and $\mathcal{T}$ are nonempty and at least one of them loses, then $J(\mathcal{S}, \mathcal{T})$ wins.\\
Proof. If $\mathcal{S}$ is losing, then we can delete $J(\varnothing, \mathcal{T})$ using the move ( $1, t$ ) for some $t \in J(\varnothing, \mathcal{T})$, which leaves the losing set $J(\mathcal{S}, \varnothing)$. Similarly, if $\mathcal{T}$ is losing, then we can delete $J(\mathcal{S}, \varnothing)$ using the move ( $1, s$ ) for some $s \in J(\mathcal{S}, \varnothing$ ), leaving the losing set $J(\varnothing, \mathcal{T})$.\\
Lemma 3. If $\mathcal{S}$ is nonempty and wins, then $J(\mathcal{S}, \mathcal{S})$ loses.\\
Proof. From this position, we can convert any sequence of moves into another valid sequence of moves by replacing ( $k, 2 n-1$ ) with ( $k, 2 n$ ), and vice versa. Thus we may assume that the initial move ( $k, m$ ) has $m$ odd. We want to show that any such move results in a winning position for the other player.

The move $(0, m)$ loses immediately. Otherwise, the move results in the set $J(\mathcal{T}, \mathcal{S})$ for some set $\mathcal{T}$. There are three cases.

If $\mathcal{T}$ is empty then the other player gets the winning set $J(\varnothing, \mathcal{S})$.\\
If $\mathcal{T}$ is losing then the other player can choose the move ( $1, s$ ) for some $s \in J(\varnothing, \mathcal{S})$, which leaves the losing set $J(\mathcal{T}, \varnothing)$.

If $\mathcal{T}$ is nonempty winning then the other player can choose the move ( $k, m+1$ ), which results in the position $J(\mathcal{T}, \mathcal{T})$. We can then proceed by induction on $|\mathcal{S}|$ to show that this is a losing set.

Lemma 4. [2n] wins if and only if [ $n$ ] loses.\\
Proof. Note that $[2 n]=J([n],[n])$. The result then follows directly from the previous two lemmas.

Lemma 5. For any integer $n \geqslant 1,[2 n+1]$ wins.\\
Proof. By Lemma 4, either $[n]$ or $[2 n]$ loses. If $[n]$ loses, then by Lemma 2 we have that $[2 n+1]=J([n+1],[n])$ wins. Otherwise, $[2 n]$ loses, and therefore $[2 n+1]$ wins by choosing the move ( $k, 2 n+1$ ) for sufficiently large $k$ so that only $2 n+1$ is eliminated.

It remains to verify the original answer. We have two cases to consider:

\begin{itemize}
  \item Suppose $N=2^{n}$ for some $n$. For $N=1$, every move is an instant loss for Geoff. Then by Lemma 4, Geoff wins for $N=2^{n}$ if and only if Geoff loses for $N=2^{n-1}$, and thus by induction we have that Geoff wins for $N=2^{n}$ if and only if $n$ is odd.
  \item Otherwise, $N=t 2^{n}$, for some $n$ and some $t>1$ with $t$ odd. By Lemma 5, Geoff wins when $n=0$. Then by Lemma 4, Geoff wins for $N=t 2^{n}$ if and only if Geoff loses for $N=t 2^{n-1}$, and thus by induction on $n$ we have that Geoff wins for $N=t 2^{n}$ if and only if $n$ is even.
\end{itemize}

---


---

### reference comment
We can represent this game as a game on partial binary trees. This representation could be common in rough working, as it facilitates exploration of small cases. If two sets produce trees which are topologically equivalent, then this equivalence leads to a natural bijection between games starting with the two sets. Such equivalences lead to a significant reduction in the number of distinct cases that need to be considered when exploring the game for small $N$.

The construction is as follows. First we begin by considering an infinite binary tree. For each positive integer $n$, we consider the binary representation of $n-1$, starting with the least significant bit and ending with an infinite sequence of leading zeroes. We map this sequence of bits to a path on the binary tree by starting at the root, and then repeatedly choosing the left child if the bit is 0 and the right child if the bit is 1 . We can then truncate each path after reaching a sufficient depth to distinguish the path from all other paths in the tree.\\
\includegraphics[max width=\textwidth, center]{2025_08_20_649828c7c9c163e2491cg-049}

Valid moves in this representation of the game consist of selecting a node with two children, and removing either the left child or the right child (and its descendants). Selecting and removing the entire graph is also an allowed move (which loses instantly).

Two trees have equivalent games if they're topologically identical. This equivalence includes swapping the left and right children of any single node, or removing a node with a single child by merging the edges above and below it (and decreasing the depth of its children by one).

---


---

### reference comment
We can also analyse this game using Grundy values (also known as nim-values or nimbers). This requires a slight modification to the rules, wherein any move that would erase all integers on the board is disallowed, and the first player who cannot move loses. This is clearly equivalent to the original game.

Let $g(\mathcal{S})$ denote the Grundy value of the game starting with the set $\mathcal{S}$. Note that the bijection in Lemma 1 shows that

$$
g(\mathcal{S})=g(J(\mathcal{S}, \varnothing))=g(J(\varnothing, \mathcal{S})) .
$$

For any set $V$, let $\operatorname{mex}(V)$ denote the least nonnegative element that is not an element of $V$. For nonnegative integers $x$ and $y$, define $j(x, y)$ recursively as

$$
j(x, y)=\operatorname{mex}(\{x, y\} \cup\{j(w, y) \mid w<x\} \cup\{j(x, z) \mid z<y\}) .
$$

The values of $j(x, y)$ for small $x$ and $y$ are:

\begin{center}
\begin{tabular}{c|cccccc}
5 & 6 & 7 & 8 & 9 & 1 & 0 \\
4 & 5 & 3 & 6 & 2 & 0 & 1 \\
3 & 4 & 5 & 1 & 0 & 2 & 9 \\
2 & 3 & 4 & 0 & 1 & 6 & 8 \\
1 & 2 & 0 & 4 & 5 & 3 & 7 \\
0 & 1 & 2 & 3 & 4 & 5 & 6 \\
\hline
- & 0 & 1 & 2 & 3 & 4 & 5 \\
\hline
\end{tabular}
\end{center}

We can show that $g(J(\mathcal{S}, \mathcal{T}))=j(g(\mathcal{S}), g(\mathcal{T}))$ for any nonempty sets $\mathcal{S}$ and $\mathcal{T}$. The remainder of the proof follows a similar structure to the given solution.

This page is intentionally left blank

---
