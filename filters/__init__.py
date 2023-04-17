from aiogram import Dispatcher

from loader import dp
from .group import IsGroup
from .private import IsPrivate
from .is_admin import AdminFilter
# from .is_admin import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
