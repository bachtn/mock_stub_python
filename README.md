pytest -vv -p no:warnings

# Fake It Before You Make It
* Object that we can control

## Mock
* 
* Un objet de substitut dans le système, qui décide si un test unitaire passe ou échoue.

## Stub
* Un objet qui simule un autre object pôur le but de poouvoir tester sans avoir besoin d'instantier
l'objet een question
 
* We stub an external dependency (database, API, route, …) or a function that we don't want to execute
because it takes too much time for example (compute_the_diameter_of_the_world_wide_web_graph)
=> I'm interested only in the returned value of the dependency or the function


## Fixture
* Sharee ressources between different function
- Loads all the images only one time instead of loading them each time we execute the test