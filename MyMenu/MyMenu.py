

class MyMenu:
    def __init__(self, f_edit):
        self._screens = {}
        self._f_edit_screen = f_edit
        self._handlers = {}

    async def handle(self, user_id, message_id, text):
        for i in self._handlers.keys():
            if i in text:
                return await self._handlers.get(i)(user_id, message_id, text)

    def add_handler(self, button, func):
        self._handlers[button] = func

    def get_screen(self, screen_name):
        return self._screens[screen_name]

    def add_screens(self, screens):
        self._screens = screens

    async def change_to(self, screen_name, message_id, chat_id, screen=None):
        if screen is None:
            screen = self._screens[screen_name]
        await self._f_edit_screen(
            text=screen[1],
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=screen[0]
        )
