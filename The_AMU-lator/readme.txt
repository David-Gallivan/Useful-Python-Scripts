The Amazing AMU-lator

In Introductory Chemistry at UK, I got tired of constantly
having to calculate the molecular mass by hand, problem
after problem, assignment after assignment, for each and
every compound in the equations.

So one evening I took a break from chemistry homework and
challenged myself to program a tool to do this tedious work
for me, hopefully saving time in the long run.

In under an hour I had this done. It accepts a chemical
compound abbreviation at the command line with single-digit
atom counts, no spaces or commas, first letter of each
element capitalized, e.g.
H2O
NaCl
Fe2O3
and prints out the sum of the atoms' masses.

Because I was the end user, I didn't bother to implement
input validation, which would be a useful next step. In
addition, it would be good to expand the parser to allow
two-digit atom counts, and maybe even ion symbols.

AMUs.txt must be in the working directory for the script
to read its data. Source for data in AMUs.txt:
https://www.angelo.edu/faculty/kboudrea/periodic/structure_mass.htm
