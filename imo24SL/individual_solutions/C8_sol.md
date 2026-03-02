### reference solution 1
We first prove by induction that it is possible the colour the whole board black for $n=2^{k}$. The base case of $k=1$ is trivial. Assume the result holds for $k=m$ and consider the case of $k=m+1$. Divide the $2^{m+1} \times 2^{m+1}$ board into four $2^{m} \times 2^{m}$ sub-boards. Colour the top left $2^{m} \times 2^{m}$ sub-board using the inductive hypothesis. Next, colour the centre $2 \times 2$ square with a single operation. Finally, each of the remaining $2^{m} \times 2^{m}$ sub-board can be completely coloured using the inductive hypothesis, starting from the black square closest to the centre. This concludes the induction.

Now we prove that if such a colouring is possible for $n$ then $n$ must be a power of 2 . Suppose it is possible to colour an $n \times n$ board where $n>1$. Identify the top left corner of the board by $(0,0)$ and the bottom right corner by $(n, n)$. Whenever an operation takes place in a $2 \times 2$ square centred on ( $i, j$ ), we immediately draw an " X ", joining the four cells' centres (see Figure 4). Also, identify this $\mathbf{X}$ by $(i, j)$. The first operation implies there's an $\mathbf{X}$ at $(1,1)$. Since the whole board is eventually coloured, every cell centre must be connected to at least one X . The collection of all $\mathrm{X}_{\mathrm{S}}$ forms a graph $G$.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-057}
\captionsetup{labelformat=empty}
\caption{Figure 4: L-trominoes placements corresponding to colouring operations (left) and the corresponding X diagram (right).}
\end{center}
\end{figure}

\section*{Claim 1. The graph $G$ is a tree.}
Proof. Since every operation requires a pre-existing black cell, each newly drawn X apart from the first must connect to an existing X . So all Xs are connected to the first X and $G$ must be connected. Now, suppose $G$ has a cycle. Consider the newest X involved in the cycle, it must connect to previous $\mathrm{X}_{\mathrm{s}}$ at at least two points. But this implies the corresponding operation will colour at most two cells, which is a contradiction.

Note that in the following arguments, Claims 2 to 4 only require the condition that $G$ is a tree and every cell is connected to $G$.\\
Claim 2. If there's an X at $(i, j)$, then $1 \leqslant i, j \leqslant n-1$ and $i \equiv j(\bmod 2)$.\\
Proof. The inequalities $1 \leqslant i, j \leqslant n-1$ are clear. Call an X at $(i, j)$ good if $i \equiv j(\bmod 2)$, or bad if $i \not \equiv j(\bmod 2)$. The first X at $(i, j)=(1,1)$ is good. Suppose some $\mathrm{X}_{\mathrm{s}}$ are bad. Since $G$ is connected, there must exist a good X connecting to a bad X . But this can only occur if they connect at two points, creating a cycle. This is a contradiction, thus all $\mathrm{X}_{\mathrm{s}}$ are good.

Call an X at $(i, j)$ odd if $i \equiv j \equiv 1(\bmod 2)$, even if $i \equiv j \equiv 0(\bmod 2)$.\\
Claim 3. The integer $n$ must be even. Furthermore, there must be $4(n / 2-1)$ odd $\mathrm{X}_{\mathrm{S}}$ connecting the cells on the perimeter of the board as shown in Figure 5.\\
Proof. If $n$ is odd, the four corners of the bottom left cell are $(n, 0),(n-1,0),(n-1,1)$ and $(n, 1)$, none of which satisfies the conditions of Claim 2. So the bottom left cell cannot connect to any X . If $n$ is even, each cell on the edge of the board has exactly one corner satisfying the conditions of Claim 2, so the X connecting it is uniquely determined. Therefore the cells on the perimeter of the board are connected to $\mathrm{X}_{\mathrm{s}}$ according to Figure 5.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-058}
\captionsetup{labelformat=empty}
\caption{Figure 5: Highlighting the permitted points for \$\textbackslash mathrm\{X}\_\{\textbackslash mathrm\{s\}\}\$ (left) and $\mathrm{X}_{\mathrm{s}}$ on the perimeter (right).\}\end{center}
\end{figure}

Divide the $n \times n$ board into $n^{2} / 4$ blocks of $2 \times 2$ squares. Call each of these blocks a big-cell. We say a big-cell is filled if it contains an odd X on its interior, empty otherwise. By Claim 3, each big-cell on the perimeter must be filled.\\
Claim 4. Every big-cell is filled.\\
Proof. Recall that $\mathrm{X}_{\mathrm{s}}$ can only be at $(i, j)$ with $i \equiv j(\bmod 2)$. Suppose a big-cell centred at $(i, j)$ is empty. Then in order for its four cells to be coloured, there must be four even $\mathrm{X}_{\mathrm{s}}$ on $(i-1, j-1),(i+1, j-1),(i-1, j+1)$ and $(i+1, j+1)$, "surrounding" the big-cell (see Figure 6).

By Claim 3, no empty big-cell can be on the perimeter. So if there exist some empty bigcells, the boundary between empty and filled big-cells must consist of a number of closed loops. Each closed loop is made up of several line segments of length 2, each of which separates a filled big-cell from an empty big-cell.

Since every empty big-cell is surrounded by even $\mathrm{X}_{\mathrm{s}}$ and every filled big-cell contains an odd X , the two end points of each such line segment must be connected by $\mathrm{X}_{\mathrm{s}}$. Since these line segments form at least one closed loop, it implies the existence of a cycle made up of $\mathrm{X}_{\mathrm{s}}$ (see Figure 6). This is a contradiction, thus no big-cell can be empty.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-059}
\captionsetup{labelformat=empty}
\caption{Figure 6: An empty big-cell surrounded by even \$\textbackslash mathrm\{X}\_\{\textbackslash mathrm\{s\}\}\$ (left) and the boundary between empty and filled $\mathrm{X}_{\mathrm{s}}$ creating a cycle (right).\}\end{center}
\end{figure}

Therefore every big-cell is filled by an odd $\mathbf{X}$, and the connections between them are provided by even $\mathrm{X}_{\mathrm{s}}$. We can now reduce the $n \times n$ problem to an $n / 2 \times n / 2$ problem in the following way. Perform a dilation of the board by a factor of $1 / 2$ with respect to $(0,0)$. Each big-cell is shrunk to a regular cell. For the $\mathrm{X}_{\mathrm{s}}$, replace each odd X at $(i, j)$ by the point $(i / 2, j / 2)$, and replace each even $\mathbf{X}$ at $(i, j)$ by an $\mathbf{X}$ at $(i / 2, j / 2)$.

We claim the new resulting graph of $\mathrm{X}_{\mathrm{s}}$ is a tree that connects all cells of an $n / 2 \times n / 2$ board. First, two connected $\mathrm{X}_{\mathrm{s}}$ in the original $n \times n$ board are still connected after their replacements (noting that some $\mathrm{X}_{\mathrm{S}}$ have been replaced by single points). For each cell in the $n / 2 \times n / 2$ board, its centre corresponds to an odd X from a filled big-cell in the original $n \times n$ board, so it must be connected to the graph. Finally, suppose there exists a cycle in the new graph. The cycle consists of $\mathrm{X}_{\mathrm{s}}$ that correspond to even $\mathrm{X}_{\mathrm{s}}$ in the original graph connecting big-cells, forming a cycle of big-cells. Since in every big-cell, the four unit squares were connected by an odd X , this implies the existence of a cycle in the original graph, which is a contradiction.

Thus the new graph of $\mathrm{X}_{\mathrm{s}}$ must be a tree that connects all cells of an $n / 2 \times n / 2$ board, which are the required conditions for Claims 2 to 4 . Hence we can repeat our argument, halving the dimensions of the board each time, until we reach the base case of a $1 \times 1$ board (where the tree is a single point). Therefore $n$ must be a power of 2 , completing the solution.

---


---

### reference solution 2
As in Solution 1, it is possible the colour the whole board black for $n=2^{k}$.\\
The colouring operation is equivalent to the placement of L -trominoes. For each L -tromino we place on the board, we draw an arrow and a node as shown in Figure 7. We also draw a node in the top left corner of the board.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-060(1)}
\captionsetup{labelformat=empty}
\caption{Figure 7: Tromino with corresponding arrow and node drawn.}
\end{center}
\end{figure}

Claim 1. The arrows and nodes form a directed tree rooted at the top left corner.\\
Proof. The proof is similar to the proof of Claim 1 in Solution 1, with the additional note that the directions of the arrows inherit the order of the colouring operations, so they must be pointing away from the top left node.

Note that since all edges of the tree are diagonal, the nodes can only lie on points $(i, j)$ with $i+j \equiv 0(\bmod 2)$. This implies that we can only place down L-trominoes of one particular parity: that is, with the centre of the $\mathbf{L}$-tromino on a point with $i+j \equiv 0(\bmod 2)$. In the remainder of the proof, we will implicitly use this parity property when determining possible positions of L-trominoes.

Next, we show that certain configurations of edges of the tree are impossible.\\
Claim 2. There cannot be two edges in a "parallel" configuration (see Figure 8).\\
Proof. In such a configuration, the two edges can either be directed in the same direction or opposite directions. If they point in the same direction (see Figure 8), then the L -trominoes corresponding to the two edges overlap.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-060}
\captionsetup{labelformat=empty}
\caption{Figure 8: Parallel configuration (left) and two parallel edges, case 1 (right).}
\end{center}
\end{figure}

If they point in opposite directions, then we get the diagram in Figure 9. The cells marked ( $\star$ ) must lie inside the $n \times n$ board, so they must be covered by L-trominoes. There is only one possible way to cover these with a L -tromino of the right parity. But this makes the arrows form a cycle, which cannot happen. So we have a contradiction.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-060(2)}
\captionsetup{labelformat=empty}
\caption{Figure 9: Two parallel edges, case 2.}
\end{center}
\end{figure}

Claim 3. There cannot be three edges in a "zigzag" configuration, shown in Figure 10.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-061(1)}
\captionsetup{labelformat=empty}
\caption{Figure 10: Zigzag configuration.}
\end{center}
\end{figure}

Proof. Assume for contradiction that there is a zigzag. Then take the zigzag with maximal distance from the root of the tree (measured by distance along the graph from the root to the middle edge of the zigzag).

We may assume without loss of generality that the middle edge is directed down-right. Then the right edge must be directed up-right, since no two arrows can point to the same node. Next, we draw in the corresponding L -trominoes, and consider the cell marked ( $\star$ ). There are two possible ways to cover it with an L -tromino, because of the parity of L -tromino centres.

We could choose the centre of the L -tromino to be the top right corner of the cell (see Figure 11). This immediately gives another zigzag.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-061}
\captionsetup{labelformat=empty}
\caption{Figure 11: Zigzag configuration, case 1.}
\end{center}
\end{figure}

The other possibility is if we choose the centre of the L -tromino to be the bottom left corner of the cell (see Figure 12). Then we need to cover the cell marked (**) with an L -tromino. If

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-061(2)}
\captionsetup{labelformat=empty}
\caption{Figure 12: Zigzag configuration, case 2.}
\end{center}
\end{figure}

we placed the centre of the L-tromino on the top left corner of the cell, this would give two parallel edges, contradicting Claim 2. So we must place the centre of the L -tromino on the bottom right corner of the cell, which gives a zigzag.

In each case, we get another zigzag further away from the root of the tree, which contradicts our assumption of maximality. So there cannot be any zigzags.

We now colour the nodes of the tree. Colour the root node yellow. For all other nodes, we colour it white if it has an arrow coming out of it in a different direction to the arrow going in, and black otherwise.\\
Claim 4. Any child of a black node is white.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-062}
\captionsetup{labelformat=empty}
\caption{Figure 13: Black node configuration.}
\end{center}
\end{figure}

Proof. Suppose we have a black node with a child. Then the arrow exiting the black node must be in the same direction as the arrow entering it by the definition of our colouring, giving the left diagram of Figure 13.

The cell marked ( $\star$ ) must be covered by an L -tromino. If the centre of this L -tromino is the bottom left corner, then this would give an arrow leaving the black node in a different direction, which cannot happen. So the centre of the L -tromino must instead be the top right corner, which gives an arrow leaving the upper node in a different direction. Thus the upper node must be white.

Claim 5. Every white node has three children, all of which are black.

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-062(1)}
\captionsetup{labelformat=empty}
\caption{Figure 14: White node configuration.}
\end{center}
\end{figure}

Proof. Refer to Figure 14. Suppose we have a white node, as in the leftmost diagram. The cell marked ( $\star$ ) must be covered by an L -tromino. If the centre of this L -tromino is the bottom right corner of the cell, then this would form a zigzag, which by Claim 3 is not allowed. So the centre must be the top left corner.

Next, the cell marked ( $\star \star$ ) must be covered by an L -tromino. If the centre of this L -tromino is the top right corner, this would form a zigzag, so the centre must be the bottom left corner instead. Thus we have shown that any white node has three children.

Finally, note that if any of the child nodes had three children of their own, then this would give parallel edges in the diagram, which contradicts Claim 2. Therefore the child nodes of the white node must all be black.

We now know that the node colours alternate between black and white as you go down the tree, so all white nodes lie on points with coordinates $(2 i, 2 j)$, and all black nodes lie on points with coordinates $(2 i+1,2 j+1)$.

Now (assuming $n>1$ ) we will construct a new board whose cells are $2 \times 2$ squares of our current board. We replace the root node and its child with a single big cell and a big root node,

\begin{figure}[h]
\begin{center}
  \includegraphics[width=\textwidth]{2025_08_20_649828c7c9c163e2491cg-063}
\captionsetup{labelformat=empty}
\caption{Figure 15: Replacing with larger cells and L-trominoes.}
\end{center}
\end{figure}

and we replace each white node and its three children with a big L-tromino, big arrow and big node as shown in Figure 15.

Every black node is the child of the root node or a white node, so every L-tromino is involved in exactly one replacement. Also, the parent of any white node is a black node, whose parent, in turn, is a white node or the root. So the starting point of every big arrow will be on a big node. Therefore we obtain an L-tromino tiling forming a tree.

This shows for $n>1$ that if an $n \times n$ board can be tiled by L-trominoes forming a tree, then $n$ is even, and an $n / 2 \times n / 2$ board can also be tiled by L-trominoes forming a tree. Since a $1 \times 1$ board can trivially be tiled, we conclude that the only values of $n$ for which an $n \times n$ board can be tiled are $n=2^{k}$.

\section*{Geometry}

---
