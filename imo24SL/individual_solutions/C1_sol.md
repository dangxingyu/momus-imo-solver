### reference solution 1
The answer can be achieved by the students finishing in the same order in every race. To show that this is the maximum, we will apply a series of modifications to the results of the races, each of which does not decrease the total score, such that after $k$ such modifications the first $k$ positions are the same in every race. Say that a student is scored on the $b^{\text {th }}$ place if their score is $a-b$ because they came in the top $b$ places in $a$ of the races and $b$ is minimal with this property for that student.

Supposing that the first $k-1$ positions are the same in every race, look at the students scored on the $k^{\text {th }}$ place. If there are no such students, let $\ell>k$ be minimal such that some student $S$ is scored on the $\ell^{\text {th }}$ place. Then, in every race where $S$ appears in any place from the $k^{\text {th }}$ through the $\ell^{\text {th }}$ inclusive (of which there must be at least $\ell$, otherwise $S$ would achieve a higher rating of 0 based on the $n^{\text {th }}$ place), reorder the students in places $k$ through $\ell$ so that $S$ finishes in the $k^{\text {th }}$ place instead (and otherwise the ordering of those students is arbitrary). Now $S$ is scored on the $k^{\text {th }}$ place, their score has gone up by $\ell-k$ and no other scores have gone down (some might have gone up as well).

Now we know that the first $k-1$ positions are the same in every race and at least one student is scored on the $k^{\text {th }}$ place. Pick one such student $S$. In each race where $S$ finishes behind the $k^{\text {th }}$ place, swap them with the student $T$ who finishes in the $k^{\text {th }}$ place, leaving the positions of all other students unchanged. Each such swap increases the score of $S$ by 1 and decreases the score of $T$ by at most 1 , so such swaps do not decrease the total score. At the end of this process, the first $k$ positions are the same in every race and the total score has not decreased.

Repeating this $n$ times yields the required result.\\

---


---

### reference comment
The following simpler approach to modifying results of races is tempting: find pairs of students $S$ and $T$ who are scored on places $k$ and $\ell$ respectively, where $k<\ell$, but where $S$ finishes after $T$ in some race, and swap the positions of those two students in that race so they finish in the same order as the places they are scored on. However, such a swap can decrease the total score; for example, suppose that $k=1$ and $\ell=4$, and in some race $S$ finishes $6^{\text {th }}$ and $T$ finishes $3^{\text {rd }}$; then swapping those students reduces the number of races contributing to $T$ 's score without increasing the number contributing to $S$ 's score.

---


---

### reference solution 2
The answer can be achieved by having the same ranking for all $n$ races.\\
Note that taking $a=b=n$ shows each student has a nonnegative score. Consider a student who has race ranks $r_{1}, r_{2}, \ldots, r_{n}$ and a final score of $s$. We first prove that

$$
\sum_{i} r_{i} \leqslant n(n-s) .
$$

Without loss of generality, suppose that $r_{1} \leqslant r_{2} \leqslant \cdots \leqslant r_{n}$. There must exist some $k$ with $s+1 \leqslant k \leqslant n$ and $k-r_{k}=s$. In order to maximise $\sum_{i} r_{i}$ while retaining the score of $s$, we can\\
replace each of $r_{1}, \ldots, r_{k-1}$ by $r_{k}$, and replace each of $r_{k+1}, \ldots, r_{n}$ by $n$. Then the sum is


\begin{equation*}
\sum_{i} r_{i} \leqslant k r_{k}+(n-k) n=n^{2}-k\left(n-r_{k}\right)=n^{2}-k(n+s-k) \leqslant n^{2}-s_{n} \tag{1}
\end{equation*}


The final inequality follows from the fact that given $s+1 \leqslant k \leqslant n$, the quantity $k(n+s-k)$ is minimised when $k=n$.

The sum of ranks of all students across all races is $\frac{n^{2}(n+1)}{2}$. If the total of all student scores is $t$, then (1) implies

$$
\frac{n^{2}(n+1)}{2} \leqslant n^{3}-t n
$$

This rearranges to $t \leqslant \frac{n(n-1)}{2}$, as required.\\

---


---

### reference solution 3
In each race, assign the student in the $k^{\text {th }}$ place a weight of $1-\frac{k}{n}$. If a student finishes in the top $b$ places in at least $a$ of the races, the total of their weights is at least $a\left(1-\frac{b}{n}\right)=a-b\left(\frac{a}{n}\right) \geqslant a-b$. Thus the sum of a student's weights across all races is at least their score, and so the sum of all weights for all students across all races is at least the sum of all the scores of all students. The sum of weights in each race is $\frac{n-1}{2}$, so the sum of all weights across all races is $\frac{n(n-1)}{2}$. Equality is achieved if and only if, for each student, the values of $b$ and $a$ determining that student's score have $a=n$ and they finish in exactly the $b^{\text {th }}$ place in all $n$ races; that is, if the students are ranked the same in every race.

---


---

### reference solution 4
Given a positive integer $b(S)$ for each student $S$, define $a_{b}(S)$ to be the number of races in which $S$ finished in the top $b(S)$ places, and define $\operatorname{score}_{b}(S)=a_{b}(S)-b(S)$; for a race $r$, let $I_{b}(S, r)$ be 1 if $S$ finished in the top $b(S)$ places in race $r$ and 0 otherwise, so

$$
a_{b}(S)=\sum_{r} I_{b}(S, r)
$$

Then the problem asks for the maximum across all possible results of the races of

$$
\max _{b} \sum_{S} \operatorname{score}_{b}(S)=\max _{b}\left(\sum_{r} \sum_{S} I_{b}(S, r)-\sum_{S} b(S)\right) .
$$

Given $b$, the sum $\sum_{S} I_{b}(S, r)$ is maximised (not necessarily uniquely) for some choice of the rankings in race $r$, which is the same choice for every race. So the maximum possible sum of the scores of all the students occurs when all students are ranked the same in all races, which yields the given answer.

---
