"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730487405"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, cell: Point) -> float:
        """Calculates distance between two cells."""
        distance: float = sqrt(((self.x - cell.x) ** 2) + ((self.y - cell.y) ** 2))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Tick."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable() is True:
            return "gray"
        if self.is_infected() is True:
            return "dark orchid"
        if self.is_immune() is True:
            return "dodger blue"

    def contract_disease(self) -> None:
        """Assigns the INFECTED constant to the sickness attribute."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Is the cell vulnerable?"""
        if self.sickness == constants.VULNERABLE:
            return True
        else: 
            return False
    
    def is_infected(self) -> bool:
        """Is the cell infected?"""
        if self.sickness >= constants.INFECTED:  
            return True
        else:
            return False

    def contact_with(self, cell: Cell) -> None:
        """Cell will contract disease if they make contact with another infected cell."""
        if self.is_infected() and cell.is_vulnerable():
            cell.contract_disease()
        if self.is_vulnerable() and cell.is_infected():
            self.contract_disease()
    
    def immunize(self) -> None:
        """Makes a cell immune."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Is the cell immune?"""
        if self.sickness == constants.IMMUNE:
            return True


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if immune_cells < 0:
            raise ValueError("The number of immune cells must be non-negative.")
        if immune_cells >= cells: 
            raise ValueError("The number of immune cells must be less than the total number of cells.")
        if infected_cells <= 0:
            raise ValueError("The number of infected cells must start at greater than zero.")
        if infected_cells >= cells:
            raise ValueError("The number of infected cells must be less than the total number of cells.")
        self.population = []
        i: int = 0
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if i < infected_cells:
                cell.contract_disease()
                i += 1
            self.population.append(cell)
        n: int = 1
        while n <= immune_cells:
            self.population[n].immunize()
            n += 1

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True

    def check_contacts(self) -> None:
        """Checks contact with other cells."""
        for cell in self.population:
            i: int = 0
            while i < len(self.population):
                if self.population[i].location.distance(cell.location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(cell)
                i += 1           