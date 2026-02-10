# Film

This repository now includes a tiny in-memory film library module to demonstrate how the
assistant can implement code changes. The `Film` and `FilmLibrary` classes can be used to
create and manage a small catalog of movies.

```python
from film import Film, FilmLibrary

library = FilmLibrary()
library.extend([
    Film(title="Spirited Away", year=2001),
    Film(title="The Godfather", year=1972),
])

print(library.list_titles())
# ['Spirited Away', 'The Godfather']
```
