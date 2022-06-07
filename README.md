# todo_drf

## Starting Development
Start the app in the environment:

```
pip install djangorestframework
python manage.py migrate
python manage.py runserver

```
## The answer of the task 1

```
http://127.0.0.1:8000/api/

```
## Output of the task 1

```
    {
        "name": "pidgey",
        "height": 3,
        "weight": 18,
        "moves": [
            {
                "move": {
                    "name": "razor-wind",
                    "url": "https://pokeapi.co/api/v2/move/13/"
                },
                "version_group_details": [
                    {
                        "level_learned_at": 0,
                        "move_learn_method": {
                            "name": "machine",
                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                        },
                        "version_group": {
                            "name": "red-blue",
                            "url": "https://pokeapi.co/api/v2/version-group/1/"
                        }
                    },
                    {
                        "level_learned_at": 0,
                        "move_learn_method": {
                            "name": "machine",
                            "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
                        },
                        "version_group": {
                            "name": "yellow",
                            "url": "https://pokeapi.co/api/v2/version-group/2/"
                        }
                    },
                    {
                        "level_learned_at": 29,
                        "move_learn_method": {
                            "name": "level-up",
                            "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
                        },
                        "version_group": {
                            "name": "lets-go-pikachu-lets-go-eevee",
                            "url": "https://pokeapi.co/api/v2/version-group/19/"
                        }
                    }
                ]
            },
```

## The answer of the task 2

```
http://127.0.0.1:8000/api/base-happiness/

```
## Output of the task 2

```
{
    "avg": 54.0,
    "mean": 54.0,
    "median": 50
}
```
