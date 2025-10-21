"""Simple film library module for demonstration purposes."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List


@dataclass
class Film:
    """Represents a film entry with a title and release year."""

    title: str
    year: int

    def __post_init__(self) -> None:
        if not self.title:
            raise ValueError("title must be a non-empty string")
        if self.year < 1888:  # year of the earliest known surviving film
            raise ValueError("year must be 1888 or later")


@dataclass
class FilmLibrary:
    """A simple in-memory collection of films keyed by title."""

    _films: Dict[str, Film] = field(default_factory=dict)

    def add(self, film: Film) -> None:
        """Add a film to the library.

        Raises:
            ValueError: If a film with the same title already exists.
        """

        key = film.title.lower()
        if key in self._films:
            raise ValueError(f"Film '{film.title}' already exists in the library")
        self._films[key] = film

    def get(self, title: str) -> Film:
        """Retrieve a film by title."""

        key = title.lower()
        try:
            return self._films[key]
        except KeyError as exc:  # pragma: no cover - simple pass-through
            raise KeyError(f"Film '{title}' is not in the library") from exc

    def list_titles(self) -> List[str]:
        """Return an alphabetically sorted list of film titles."""

        return sorted(film.title for film in self._films.values())

    def extend(self, films: Iterable[Film]) -> None:
        """Add multiple films in one call."""

        for film in films:
            self.add(film)


__all__ = ["Film", "FilmLibrary"]
