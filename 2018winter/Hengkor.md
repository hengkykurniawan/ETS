# Local Elections and the Mexican Drug War

**Author:** Nunu Nurmilah
**Date:** March 1, 2019
**Name:** Hengkor



## Introduction

Does cracking down on drug trafficking organizations inadvertently cause violence to increase?

In December of 2006, the newly elected President of Mexico Felipe Calderón declared war against organized crime and deployed the military to combat these groups. While the motivation behind this action is contested, the expectation was that a crackdown would fragment and weaken criminal organizations enough to prevent them from undermining political institutions through corruption or violence. However, starting in 2007 Mexico witnessed an unprecedented increase in drug-related violence that still plagues the country.

Prevalent theories about why Mexico became so violent after the crackdown on drug cartels in 2006 point to the crackdown itself. These theories argue that the crackdown did fragment criminal organizations, but did not weaken them sufficiently to usurp their power. This fragmentation, rather than leading to weak criminal organizations trafficking drugs in relative peace, intensified competition in the trafficking market between powerful criminal organizations. This surge in illicit market competition—largely caused by the crackdown—led to drastic increases in violence throughout the country.

Given the partisan nature of Mexican politics, it might be reasonable to assume that local elected officials from the PAN party actively participated in the newly-elected president’s crackdown given the pressure to make their party’s new policy a success. Inversely, local officials from opposition parties had little incentive to cooperate and implement the new policy, especially the PRD, who had just lost the presidency by less than 1% of the votes.

If we accept these assumptions, we should expect that municipalities with PAN elected officials cracked down on organized crime starting in December of 2006, while municipalities ruled by opposition parties did not. Additionally, since we have sufficient evidence that increased enforcement against organized crime led to a rise in violence in Mexico over the past decade, we should expect that municipalities with PAN elected officials experienced higher levels of violence than municipalities controlled by the opposition.

## Research Design

To test the hypothesis proposed above, we can use a regression discontinuity design to look at local elections and compare levels of violence in municipalities where PAN won versus where the opposition won. We can use an RD design if we assume that the outcomes of closely contested elections resulted from idiosyncratic factors, which in the case of Mexico is reasonable. By using an RDD, however, we discard elections that were not closely contested since they could differ systematically from those that were closely contested. We therefore cannot generalize the results of this research onto elections in general. For this analysis, competitive elections are defined as those with a vote spread of 5% or less.

## Results

To implement the RDD described above, this analysis uses data from the Mexican electoral agency (INE) on 152 municipal elections that occurred between 2007 and 2008 where PAN won or lost by a 5% margin or less. Monthly data on municipal homicide rates (homicides per 100,000) are used from the Mexican Office of the President. Finally, the covariate data comes from the Mexican National Statistical Agency (INEGI).

The covariate balance table compares municipalities where PAN won and where PAN lost. The table shows the mean for treated and control groups, along with the standard mean difference and the corresponding p-value. As can be seen, the covariates are fairly balanced.

## Spatial Econometrics Equations

Spatial econometrics models explicitly incorporate spatial dependence through a spatial weights matrix `W`.

- Spatial Lag Model (SLM):  
  `y = ρ W y + X β + ε`

- Spatial Error Model (SEM):  
  `y = X β + u`, with `u = λ W u + ε`

- Spatial Durbin Model (SDM):  
  `y = ρ W y + X β + W X θ + ε`

- Spatial Autoregressive Combined Model (SAC):  
  `y = ρ W y + X β + u`, with `u = λ W u + ε`

In these equations, `y` is the dependent variable vector, `X` is the matrix of explanatory variables, `W` is the spatial weights matrix, `ρ` is the spatial lag coefficient, `λ` is the spatial error coefficient, and `ε` is the vector of independent disturbances.
