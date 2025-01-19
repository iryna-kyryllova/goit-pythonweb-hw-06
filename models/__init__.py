from sqlalchemy.orm import configure_mappers

from .groups import Group
from .marks import Mark
from .students import Student
from .subjects import Subject
from .teachers import Teacher

configure_mappers()