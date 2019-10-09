## Introduction to Discrete Probability ##

cyan <- 3
magenta <- 5
yellow <- 7

# Assign a variable `p` as the probability of choosing a cyan ball from the box
beads <- rep(c("cyan", "magenta", "yellow"), times = c(3,5,7))
p <- mean(beads=="cyan")



# `p` is defined as the probability of choosing a cyan ball from a box containing: 3 cyan balls, 5 magenta balls, and 7 yellow balls.
# Using variable `p`, calculate the probability of choosing any ball that is not cyan from the box
cyan <- 3
magenta <- 5
yellow <- 7

# Assign a variable `p` as the probability of choosing a cyan ball from the box
beads <- rep(c("cyan", "magenta", "yellow"), times = c(3,5,7))
p <- mean(beads!="cyan")






# The variable `p_1` is the probability of choosing a cyan ball from the box on the first draw.
p_1 <- cyan / (cyan + magenta + yellow)

# Assign a variable `p_2` as the probability of not choosing a cyan ball on the second draw without replacement.
# conditional probability with independence Pr(2_not_cyan | 1_cyan) = Pr(2_not_cyan)
p_2 <- (magenta + yellow) / (cyan - 1 + magenta + yellow) 

# Calculate the probability that the first draw is cyan and the second draw is not cyan using `p_1` and `p_2`.
# Pr(A) AND Pr(B) = Pr(A)*Pr(B)
p_1 * p_2





# The variable 'p_1' is the probability of choosing a cyan ball from the box on the first draw.
p_1 <- cyan / (cyan + magenta + yellow)

# Assign a variable 'p_2' as the probability of not choosing a cyan ball on the second draw with replacement.
p_2 <- (magenta + yellow) / (cyan + magenta + yellow)

# Calculate the probability that the first draw is cyan and the second draw is not cyan using `p_1` and `p_2`.
p_1*p_2


