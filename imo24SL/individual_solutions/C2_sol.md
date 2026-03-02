### reference solution 1
We first show by induction that $n=2^{k}$ is a cool number. The base case of $n=2$ is trivial as there is no such $d$.

For induction, assume that $2^{k}$ is a cool number. We construct a numbering of a $2^{k+1} \times 2^{k+1}$ board that satisfies the conditions.

Take the $2^{k+1} \times 2^{k+1}$ board and divide it into four $2^{k} \times 2^{k}$ sub-boards. By assumption, there is some numbering $P$ of a $2^{k} \times 2^{k}$ board that satisfies the required condition; we write down the numbering $P$ in each sub-board. Next, add $2^{2 k}$ to every number in the second sub-board, add $2 \times 2^{2 k}$ to every number in the third sub-board, and add $3 \times 2^{2 k}$ to every number in the fourth sub-board. Then the numbers in the cells of the $2^{k+1} \times 2^{k+1}$ board are the numbers 1 to $2^{2(k+1)}$.

Now locate $2^{2 k}$ from the first sub-board, and swap it with $2^{2 k}+2^{k-1}$ from the second subboard. Locate $3 \times 2^{2 k}$ from the third sub-board, and swap it with $3 \times 2^{2 k}+2^{k-1}$ from the fourth sub-board.

We claim that this numbering of the $2^{k+1} \times 2^{k+1}$ board satisfies the required conditions. For any $d=2^{i}$ where $i<k$, consider any $2^{i} \times 2^{i}$ sub-board. The sum of its cells modulo $2^{i}$ is not changed in the addition step or the swapping step, so the sum is congruent modulo $2^{i}$ to the sum of the corresponding $2^{i} \times 2^{i}$ sub-board in $P$, which is nonzero, as required.

In the case of $d=2^{k}$, we can directly evaluate the sum of the $(b+1)^{\text {th }}$ sub-board for $b \in\{0,1,2,3\}$. The sum is given by

$$
2^{2 k-1}\left(1+2^{2 k}\right)+b 2^{4 k}+(-1)^{b} 2^{k-1} \equiv 2^{k-1} \quad\left(\bmod 2^{k}\right)
$$

Therefore all sub-boards satisfy the required conditions and so $2^{k+1}$ is a cool number, completing the induction.

It remains to show that no other even number is a cool number. Let $n=2^{s} m$ where $s$ is a positive integer and $m$ is an odd integer greater than 1 . For the sake of contradiction, suppose that there is a numbering of the $n \times n$ board satisfying the required conditions.\\
Claim. In the $2^{i}$-division of the board, where $1 \leqslant i \leqslant s$, the sum of numbers in each $2^{i} \times 2^{i}$ sub-board is congruent to $2^{i-1}$ modulo $2^{i}$.

Proof. We prove the claim by induction on $i$. The base case of $i=1$ holds as the sum of numbers in each $2 \times 2$ sub-board must be odd. Next, suppose the claim is true for $2^{i}$. In the $2^{i+1}$-division, each $2^{i+1} \times 2^{i+1}$ sub-board is made up of four $2^{i} \times 2^{i}$ sub-boards, each with a sum congruent to $2^{i-1}$ modulo $2^{i}$. Hence the sum of each $2^{i+1} \times 2^{i+1}$ sub-board is a multiple of $2^{i}$. It cannot be a multiple of $2^{i+1}$ because of the conditions, which means it must be congruent to $2^{i}$ modulo $2^{i+1}$. This proves the claim.

Back to the problem, since $m$ is odd, summing up the $m^{2}$ sums of $2^{s} \times 2^{s}$ sub-boards gives

$$
2^{s-1} m^{2} \equiv 2^{s-1} \quad\left(\bmod 2^{s}\right)
$$

However, the sum of the numbers from 1 to $n^{2}$ is

$$
\frac{n^{2}\left(n^{2}+1\right)}{2}=2^{2 s-1} m^{2}\left(2^{2 s} m^{2}+1\right) \equiv 0 \quad\left(\bmod 2^{s}\right)
$$

This is a contradiction. Therefore $n$ is not a cool number.\\

---


---

### reference comment
In the case of odd $n$, similar arguments show that prime powers are cool numbers. If the definition of cool numbers additionally requires that all $d \times d$ sub-boards in the $d$-division have the same nonzero residue modulo $d$, then the cool numbers are precisely the prime powers.

---
