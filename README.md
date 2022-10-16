# calcount3
A simple calorie counter app made using the [Atri framework](https://github.com/Atri-Labs/atrilabs-engine) for Hacktoberfest'22

Note: there seems to be an incompatibility with conda installed in my system, the environment keeps activating itself when I issue `pipenv shell` and then it seems to cause errors:

```
(base)$ mkdir calcount3 && cd calcount3
(base)$ conda deactivate
$ pipenv install atri
$ pipenv shell
(base)$ conda deactivate
$ atri start
```
