import datetime
from selectors import SelectSelector
from typing import List, Optional
from dataclasses import dataclass

from typing import Optional


@dataclass
class Quote:
    text: Optional[str] = None
    tags: Optional[List[str]] = None

    def __str__(self) -> str:
        return f'"{self.text}"\nTags: {", ".join(self.tags)}'

    def to_dict(self) -> dict:
        """Convert Quote object to dictionary"""
        return {
            'text': self.text,
            'tags': self.tags
        }


@dataclass
class Author:
    name: Optional[str] = None
    born_date: Optional[datetime.datetime] = None
    born_location: Optional[str] = None
    description: Optional[str] = None
    quotes: Optional[List[Quote]] = None

    def __str__(self) -> str:
        return f"""
        Author: {self.name}
        Born: {self.born_date} in {self.born_location}
        Number of quotes: {len(self.quotes)}
        """

    def append_quotes(self, quote) -> None:
        """Add a new quote to the author's collection"""
        self.quotes.append(quote)

    def get_quotes_by_tag(self, tag: str) -> List[Quote]:
        """Get all quotes that have a specific tag"""
        return [quote for quote in self.quotes if tag in quote.tags]

    def to_dict(self) -> dict:
        """Convert Author object to dictionary format"""
        return {
            'name': self.name,
            'born_date': self.born_date,
            'born_location': self.born_location,
            'description': self.description,
            'quotes': [quote.to_dict() for quote in self.quotes] if self.quotes else self.quotes
        }
