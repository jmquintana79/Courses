# Code: The rep function and the sample function
beads <- rep(c("red", "blue"), times = c(2,3))    # create an urn with 2 red, 3 blue
beads    # view beads object
sample(beads, 1)    # sample 1 bead at random

# Code: Monte Carlo simulation
# Note that your exact outcome values will differ because the sampling is random.
B <- 10000    # number of times to draw 1 bead
events <- replicate(B, sample(beads, 1))    # draw 1 bead, B times
tab <- table(events)    # make a table of outcome counts
prop.table(tab)    # view table of outcome proportions
