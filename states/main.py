from aiogram.dispatcher.filters.state import State, StatesGroup

class peggy_state(StatesGroup):
    subscribe = State()
    sertificate = State()
    test = State()
    write_to_ser = State()

class Admin(StatesGroup):
    admin_pan = State()
    reklama = State()
    reklam_matn = State()
    reklam_rasm = State()