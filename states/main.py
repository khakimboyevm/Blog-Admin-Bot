from aiogram.dispatcher.filters.state import State, StatesGroup

class peggy_state(StatesGroup):
    subscribe = State()
    sertificate = State()
    test = State()
    write_to_ser = State()

class Admin(StatesGroup):
    admin_pan = State()
    reklama = State()
    choose_text = State()
    choose_image = State()
    choose_video = State()
    reklam_matn = State()
    matn_btn_text = State()
    reklam_matn_url = State()
    matn_url_text = State()
    reklam_rasm = State()
    rasm_btn_text = State()
    reklam_rasm_url = State()
    rasm_url_text = State()
    reklam_video = State()
    video_btn_text = State()
    reklam_video_url = State()
    video_url_text = State()