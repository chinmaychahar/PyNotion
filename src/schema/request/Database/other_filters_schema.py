from typing import Optional

from schema.request.Database.common_filter_schema import EqualsFilter, EmptyFilter, ContainsFilter


class CheckboxFilter(EqualsFilter):
    pass


class SelectFilter(EqualsFilter, EmptyFilter):
    pass


class MultiSelectFilter(ContainsFilter, EmptyFilter):
    pass


class StatusFilter(EqualsFilter, EmptyFilter):
    pass


class PeopleFilter(ContainsFilter, EmptyFilter):
    pass


class FileFilter(EmptyFilter):
    pass


class RelationFilter(ContainsFilter, EmptyFilter):
    pass



