### reference solution 1
For every positive integer $n$, let $M_{n}=\max \left(a_{1}, a_{2}, \ldots, a_{n}\right)$. We first prove that


\begin{equation*}
\frac{3^{a_{1}}+3^{a_{2}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant\left(\frac{3}{4}\right)^{M_{n}} . \tag{2}
\end{equation*}


For $i=1,2, \ldots, n$, from $\left(\frac{3}{2}\right)^{a_{i}} \leqslant\left(\frac{3}{2}\right)^{M_{n}}$ we can obtain $3^{a_{i}} \leqslant\left(\frac{3}{4}\right)^{M_{n}} \cdot 2^{M_{n}} \cdot 2^{a_{i}}$. By summing up over all $i$,

$$
\sum_{i=1}^{n} 3^{a_{i}} \leqslant\left(\frac{3}{4}\right)^{M_{n}} \cdot 2^{M_{n}} \cdot \sum_{i=1}^{n} 2^{a_{i}} \leqslant\left(\frac{3}{4}\right)^{M_{n}} \cdot\left(\sum_{i=1}^{n} 2^{a_{i}}\right)^{2}
$$

which is equivalent to (2).\\
Now let $\mu=\log _{4 / 3} \frac{1}{\varepsilon}$, so that $\mu$ is the positive real number with $\left(\frac{3}{4}\right)^{\mu}=\varepsilon$. If there is an index $n$ such that $a_{n}>\mu$, then $M_{n} \geqslant a_{n}>\mu$, and hence

$$
\frac{3^{a_{1}}+3^{a_{2}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant\left(\frac{3}{4}\right)^{M_{n}}<\left(\frac{3}{4}\right)^{\mu}=\varepsilon
$$

Otherwise we have $0<a_{i} \leqslant \mu$ for all positive integers $i$, so

$$
\frac{3^{a_{1}}+3^{a_{2}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant \frac{n \cdot 3^{\mu}}{(n \cdot 1)^{2}}=\frac{3^{\mu}}{n}
$$

If $n>\left\lfloor\frac{3^{\mu}}{\varepsilon}\right\rfloor$, this is less than $\varepsilon$.\\

---


---

### reference comment
It is also possible to prove (2) by induction on $n$. The base case $n=1$ is clear. For the induction step, after ordering $a_{1}, a_{2}, \ldots, a_{n}$ in increasing order as $b_{1} \leqslant b_{2} \leqslant \cdots \leqslant b_{n}$, it suffices, for example, to verify that

$$
\frac{3^{b_{1}}+3^{b_{2}}+\cdots+3^{b_{n}}}{\left(2^{b_{1}}+2^{b_{2}}+\cdots+2^{b_{n}}\right)^{2}} \leqslant \frac{3^{b_{1}}+3^{b_{2}}+\cdots+3^{b_{n}}}{\left(2^{b_{1}}+2^{b_{2}}+\cdots+2^{b_{n}}\right)\left(2^{b_{2}}+\cdots+2^{b_{n}}\right)} \leqslant \frac{3^{b_{2}}+\cdots+3^{b_{n}}}{\left(2^{b_{2}}+\cdots+2^{b_{n}}\right)^{2}}
$$

The second inequality is equivalent to $3^{b_{1}} \sum_{i=2}^{n} 2^{b_{i}} \leqslant 2^{b_{1}} \sum_{i=2}^{n} 3^{b_{i}}$, which follows from $\left(\frac{3}{2}\right)^{b_{1}} \leqslant\left(\frac{3}{2}\right)^{b_{i}}$.

---


---

### reference solution 2
We will combine two upper bounds.\\
First, start with the trivial estimate

$$
\frac{3^{a_{1}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant \frac{3^{a_{1}}+\cdots+3^{a_{n}}}{4^{a_{1}}+\cdots+4^{a_{n}}}
$$

By applying Jensen's inequality to the convex function $x^{\log _{3} 4}$ we get

$$
\frac{4^{a_{1}}+\cdots+4^{a_{n}}}{n}=\frac{\left(3^{a_{1}}\right)^{\log _{3} 4}+\cdots+\left(3^{a_{n}}\right)^{\log _{3} 4}}{n} \geqslant\left(\frac{3^{a_{1}}+\cdots+3^{a_{n}}}{n}\right)^{\log _{3} 4}
$$

so

$$
\frac{3^{a_{1}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant \frac{3^{a_{1}}+\cdots+3^{a_{n}}}{4^{a_{1}}+\cdots+4^{a_{n}}} \leqslant\left(\frac{n}{3^{a_{1}}+\cdots+3^{a_{n}}}\right)^{\log _{3} 4-1}
$$

Hence, (1) holds true whenever


\begin{equation*}
3^{a_{1}}+\cdots+3^{a_{n}}>\left(\frac{1}{\varepsilon}\right)^{\frac{1}{\log _{3} 4-1}} \cdot n \tag{3}
\end{equation*}


Second, trivially

$$
\frac{3^{a_{1}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+\cdots+2^{a_{n}}\right)^{2}} \leqslant \frac{3^{a_{1}}+\cdots+3^{a_{n}}}{n^{2}}
$$

so (1) is satisfied if


\begin{equation*}
3^{a_{1}}+\cdots+3^{a_{n}}<\varepsilon \cdot n^{2} \tag{4}
\end{equation*}


If $n>\left(\frac{1}{\varepsilon}\right)^{1+\frac{1}{\log _{3} 4-1}}$ then $\left(\frac{1}{\varepsilon}\right)^{\frac{1}{\log _{3} 4-1}} \cdot n<\varepsilon \cdot n^{2}$, and therefore at least one of (3) and (4) is satisfied.

---


---

### reference solution 3
Define $C=\log _{4 / 3} \frac{2}{\varepsilon}$, so that if $a_{i}>C$ then $3^{a_{i}}<\frac{\varepsilon}{2} \cdot 4^{a_{i}}$. We divide the sequence into "small" and "large" terms by how they compare to $C$ : let

$$
\mathcal{S}_{n}=\left\{i \leqslant n \mid a_{i} \leqslant C\right\} \quad \text { and } \quad \mathcal{L}_{n}=\left\{i \leqslant n \mid a_{i}>C\right\}
$$

Then (1) is equivalent to

$$
\frac{\sum_{i \in \mathcal{S}_{n}} 3^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}}+\frac{\sum_{i \in \mathcal{L}_{n}} 3^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}}<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}
$$

If $\mathcal{L}_{n}$ is nonempty, we have

$$
\frac{\sum_{i \in \mathcal{L}_{n}} 3^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}}<\frac{\varepsilon}{2} \cdot \frac{\sum_{i \in \mathcal{L}_{n}} 4^{a_{i}}}{\left(\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}} \leqslant \frac{\varepsilon}{2}
$$

and this also trivially holds when $\mathcal{L}_{n}$ is empty (in which case the LHS is zero).\\
Now suppose that $n \geqslant \frac{2}{\varepsilon}\left(\frac{3}{2}\right)^{C}$. Note that $3^{a_{i}} \leqslant\left(\frac{3}{2}\right)^{C} 2^{a_{i}}$ for $i \in \mathcal{S}_{n}$, so we have

$$
\frac{\sum_{i \in \mathcal{S}_{n}} 3^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}} \leqslant \frac{\left(\frac{3}{2}\right)^{C} \sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}}{\left(\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}\right)^{2}} \leqslant \frac{\left(\frac{3}{2}\right)^{C}}{\sum_{i \in \mathcal{S}_{n}} 2^{a_{i}}+\sum_{i \in \mathcal{L}_{n}} 2^{a_{i}}}<\frac{\left(\frac{3}{2}\right)^{C}}{n} \leqslant \frac{\varepsilon}{2}
$$

so we have (1).

---


---

### reference solution 4
For every index $i=1,2, \ldots, n$, apply the weighted AM-GM inequality to numbers $2^{a_{i}}$ and $(n-1)$ with weights $\log _{2} \frac{3}{2} \approx 0.585$ and $\log _{2} \frac{4}{3} \approx 0.415$ as

$$
\begin{gathered}
2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}} \geqslant 2^{a_{i}}+(n-1) \\
>\log _{2} \frac{3}{2} \cdot 2^{a_{i}}+\log _{2} \frac{4}{3} \cdot(n-1) \geqslant\left(2^{a_{i}}\right)^{\log _{2} \frac{3}{2}} \cdot(n-1)^{\log _{2} \frac{4}{3}} \\
=\left(\frac{3}{2}\right)^{a_{i}} \cdot(n-1)^{\log _{2} \frac{4}{3}}>\left(\frac{3}{2}\right)^{a_{i}} \cdot(n-1)^{2 / 5}
\end{gathered}
$$

By summing up for $i=1,2, \ldots, n$,

$$
\left(2^{a_{1}}+\cdots+2^{a_{n}}\right)^{2}=\sum_{i=1}^{n} 2^{a_{i}}\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)>(n-1)^{2 / 5} \sum_{i=1}^{n} 3^{a_{i}}
$$

so

$$
\frac{3^{a_{1}}+3^{a_{2}}+\cdots+3^{a_{n}}}{\left(2^{a_{1}}+2^{a_{2}}+\cdots+2^{a_{n}}\right)^{2}}<\frac{1}{(n-1)^{2 / 5}}
$$

If $n \geqslant\left(\frac{1}{\varepsilon}\right)^{5 / 2}+1$ then $\frac{1}{(n-1)^{2 / 5}}<\varepsilon$.

---
