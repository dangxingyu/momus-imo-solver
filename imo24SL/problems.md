## Algebra

**A1.** Determine all real numbers $\alpha$ such that
$$
\lfloor \alpha \rfloor + \lfloor 2\alpha \rfloor + \cdots + \lfloor n\alpha \rfloor
$$
is divisible by $n$ for all positive integers $n$.

---

**A2.** Let $n$ be a positive integer. Find the minimum possible value of
$$
S = 2^0x_0^2 + 2^1x_1^2 + \cdots + 2^n x_n^2,
$$
where $x_0, x_1, \dots, x_n$ are nonnegative integers such that
$$
x_0 + x_1 + \cdots + x_n = n.
$$

---

**A3.** Decide whether for every sequence $(a_n)$ of positive real numbers,
$$
\frac{3a_1 + 3a_2 + \cdots + 3a_n}{(2a_1 + 2a_2 + \cdots + 2a_n)^2} < \frac{1}{2024}
$$
is true for at least one positive integer $n$.

---

**A4.** Let $\mathbb{Z}_{>0}$ be the set of all positive integers. Determine all subsets $S \subseteq \{20, 21, 22, \dots\}$ for which there exists a function $f : \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ such that
$$
S = \{f(a+b) - f(a) - f(b) \mid a, b \in \mathbb{Z}_{>0}\}.
$$

---

**A5.** Find all periodic sequences $a_1, a_2, \dots$ of real numbers such that for all $n \geq 1$:
$$
a_{n+2} + a_{2n} = a_n + a_{2n+1}, \quad \text{and} \quad |a_{n+1} - a_n| \leq 1.
$$

---

**A6.** Let $a_0, a_1, a_2, \dots$ be an infinite strictly increasing sequence of positive integers such that for each $n \geq 1$,
$$
a_n \in \left\{ \frac{a_{n-1} + a_{n+1}}{2}, \, \sqrt{a_{n-1} \cdot a_{n+1}} \right\}.
$$
Define a sequence $(b_n)$ of letters as
$$
b_n =
\begin{cases}
A, & \text{if } a_n = \frac{a_{n-1} + a_{n+1}}{2}, \\
G, & \text{otherwise}.
\end{cases}
$$
Prove that there exist positive integers $n_0$ and $d$ such that for all $n \geq n_0$, $b_{n+d} = b_n$.

---

**A7.** Let $f : \mathbb{Q} \to \mathbb{Q}$ be a function such that for all $x, y \in \mathbb{Q}$,
$$
f(x + f(y)) = f(x) + y \quad \text{or} \quad f(f(x) + y) = x + f(y).
$$
Determine the maximum possible number of elements in the set $\{f(x) + f(-x) \mid x \in \mathbb{Q}\}$.

---

**A8.** Let $p \ne q$ be coprime positive integers. Determine all infinite sequences $a_1, a_2, \dots$ of positive integers such that for all $n \geq 1$,
$$
\max(a_n, a_{n+1}, \dots, a_{n+p-1}) - \min(a_n, a_{n+1}, \dots, a_{n+p-1}) = p,
$$
and
$$
\max(a_n, a_{n+1}, \dots, a_{n+q-1}) - \min(a_n, a_{n+1}, \dots, a_{n+q-1}) = q.
$$

---

## Combinatorics

**C1.** Let $n$ be a positive integer. A class of $n$ students run $n$ races, each with a strict ranking. A student is eligible for a rating $(a, b)$ if they place in the top $b$ in at least $a$ of the races. Their final score is the maximum value of $a - b$ across all such ratings. Find the maximum possible sum of all $n$ students' final scores.

---

**C2.** Let $n$ be a positive integer. Fill the integers $1$ to $n^2$ into an $n \times n$ board, one per cell. For every $d \mid n$ with $1 < d < n$, partition the board into non-overlapping $d \times d$ sub-boards. We say $n$ is a **cool number** if, for every such $d$, the sum in each $d \times d$ sub-board is **not** divisible by $d$. Determine all even cool numbers.

---

**C3.** Let $n$ be a positive integer. There are $2n$ knights at a round table, in $n$ partner pairs. Partners can only shake hands when sitting adjacent. Every minute, one adjacent pair swaps seats. Find the minimum number of swaps needed so that **regardless of initial seating**, every pair is adjacent at some moment and can shake hands.

---

**C4.** On a $2024 \times 2023$ board, a snail starts at any cell in the top row and wants to reach any cell in the bottom row, moving step-by-step to adjacent cells. There are 2022 hidden monsters, one in each intermediate row, no two in the same column. If the snail hits a monster, it restarts from the top. Determine the minimum number of attempts needed to guarantee success regardless of monster locations.

---

**C5.** Let $N$ be a positive integer. Geoff and Ceri play a game starting with $\{1, 2, \dots, N\}$. In each move, a player chooses $(k, n)$ with $k \geq 0$ and $n$ on the board, then erases every $s$ such that $2^k \mid n - s$. The last person to erase a number **loses**. Geoff goes first. Determine all $N$ such that Geoff can force a win.

---

**C6.** Let $n, T$ be positive integers. James places $4n$ marbles with weights $1, 2, \dots, 4n$ on a balance so both sides are equal. Andrew can move marbles between sides, as long as the imbalance is always $\leq T$. Determine the minimal $T$ such that Andrew can move **every** marble to the opposite side, regardless of initial placement.

---

**C7.** Let $N$ be a positive integer and let $(a_n)$ be a sequence of positive integers such that for all $n > N$, 
$$
a_n = \text{number of times } a_{n-1} \text{ appears in } (a_1, a_2, \dots, a_{n-1}).
$$
Prove that at least one of the subsequences $(a_1, a_3, a_5, \dots)$ or $(a_2, a_4, a_6, \dots)$ is eventually periodic.

---

**C8.** Let $n$ be a positive integer. Initially, the top-left cell of an $n \times n$ grid is black, and all others white. A move selects a $2 \times 2$ square with exactly one black cell and turns the other three black. Determine all $n$ such that the whole board can be turned black.

## Number Theory

**N1.** Find all positive integers $n$ such that for every positive divisor $d \mid n$, either
$$
d + 1 \mid n \quad \text{or} \quad d + 1 \text{ is prime}.
$$

---

**N2.** Determine all finite nonempty sets $S$ of positive integers such that for every $a, b \in S$, there exists $c \in S$ such that
$$
a \mid b + 2c.
$$

---

**N3.** Determine all sequences $a_1, a_2, \dots$ of positive integers such that for any $1 \leq m \leq n$, the arithmetic and geometric means
$$
\frac{a_m + a_{m+1} + \cdots + a_n}{n - m + 1}, \quad \left( a_m a_{m+1} \cdots a_n \right)^{1 / (n - m + 1)}
$$
are both integers.

---

**N4.** Determine all positive integers $a$ and $b$ such that there exists a positive integer $g$ with
$$
\gcd(an + b, \, bn + a) = g
$$
for all sufficiently large integers $n$.

---

**N5.** Let $S$ be a finite nonempty set of prime numbers. Let $1 = b_1 < b_2 < \cdots$ be the sequence of all positive integers whose prime divisors all belong to $S$. Prove that for all but finitely many $n$, there exist positive integers $a_1, a_2, \dots, a_n$ such that
$$
\frac{a_1}{b_1} + \frac{a_2}{b_2} + \cdots + \frac{a_n}{b_n} = \frac{1}{b_1} + \frac{1}{b_2} + \cdots + \frac{1}{b_n}.
$$

---

**N6.** Let $n$ be a positive integer. A polynomial $P \in \mathbb{Z}[x]$ is called **$n$-good** if there exists a quadratic polynomial $Q \in \mathbb{Z}[x]$ such that
$$
Q(k)(P(k) + Q(k)) \not\equiv 0 \pmod{n}
$$
for all integers $k$. Determine all integers $n$ such that **every** integer-coefficient polynomial is $n$-good.

---

**N7.** Let $\mathbb{Z}_{>0}$ denote the set of positive integers. Let $f : \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ satisfy the condition:
$$
f(mn)^2 = f(m^2) f(f(n)) f(mf(n))
$$
if and only if $\gcd(m, n) = 1$.  

Determine all possible values of $f(n)$ for each $n$.

---