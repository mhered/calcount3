# calcount3
A simple calorie counter app made using the [Atri framework](https://github.com/Atri-Labs/atrilabs-engine) for Hacktoberfest'22

See the [Demo in github pages](https://mhered.github.io/calcount3/)

Note: there seems to be an incompatibility with conda installed in my system, the environment keeps activating itself when I issue `pipenv shell` and then it seems to cause errors:

```
(base)$ mkdir calcount3 && cd calcount3
(base)$ conda deactivate
$ pipenv install atri
$ pipenv shell
(base)$ conda deactivate
$ atri start
```
Sources: 
* Nutritional data of selected foods from https://www.webmd.com/diet/healthtool-food-calorie-counter
* Estimated calories for the different nutrients from https://www.wikihow.com/Calculate-Food-Calories
* Target daily intake of calories and nutrients estimated freely using inputs from https://www.menshealth.com/nutrition/a19537348/how-much-fat-and-carbs-should-you-eat/ and https://www.healthline.com/nutrition/how-many-calories-per-day#calculator 

## Build and deploy app
Update the [demo app](https://mhered.github.io/calcount3/) after `git commit` and `git push` of new source code
Note: atri commands must run from source directory and inside the pipenv environment, so if neeced do:
```bash
$ cd path-to/calcount3
$ pipenv shell
$ conda deactivate
(calcount3)path-to/calcount3$
```
Then build and deploy with:
```bash
$ atri build ssg
$ GIT_USER=<username> atri deploy ssg --gh-pages
```
