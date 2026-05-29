# Spatial Econometrics Overview

**Name:** Mila Romanso

Spatial econometrics is the study of spatially correlated data and the dependence between observations across geographic space. It extends traditional econometric models by explicitly modeling spatial relationships, which can arise from spillover effects, neighbourhood interactions, or geographic proximity.

## Core concepts

- Spatial dependence: outcomes in one location may be influenced by outcomes in nearby locations.
- Spatial autocorrelation: the pattern of similarity between observations as a function of geographic distance or contiguity.
- Spatial weights matrix: a matrix that defines the structure of spatial relationships between units.

## Four main spatial econometrics models

1. Spatial Lag Model (SLM)
   - Also known as the spatial autoregressive model.
   - Includes a spatially lagged dependent variable to capture the influence of neighboring outcomes on the focal outcome.
   - Equation form: `y = ρW y + Xβ + ε`.

2. Spatial Error Model (SEM)
   - Models spatial correlation in the error term instead of the dependent variable.
   - Useful when omitted spatially correlated variables affect the dependent variable.
   - Equation form: `y = Xβ + u`, with `u = λW u + ε`.

3. Spatial Durbin Model (SDM)
   - Combines spatial lag effects for both the dependent variable and the independent variables.
   - Allows direct effects of covariates and indirect spillovers through neighboring observations.
   - Equation form: `y = ρW y + Xβ + W Xθ + ε`.

4. Spatial Autoregressive Combined Model (SAC)
   - Also called the Spatial Autoregressive Moving Average (SARAR) model.
   - Includes both a spatial lag on the dependent variable and spatial autocorrelation in the error term.
   - Equation form: `y = ρW y + Xβ + u`, with `u = λW u + ε`.

These spatial econometrics models help researchers account for geographic spillovers, improve estimation accuracy, and avoid bias from unmodeled spatial dependence.
