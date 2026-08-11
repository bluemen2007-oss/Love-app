from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle


# رنگ صفحه
Window.clearcolor = (1, 0.75, 0.82, 1)


class LoveApp(App):

    def build(self):

        self.questions = [
            "اسم تو چیه؟ ❤️",
            "چند سالته؟ 🎂",
            "سرگرمی مورد علاقه‌ات چیه؟ 🎨",
            "چقدر منو دوست داری؟ 🥺❤️"
        ]

        self.answers = []
        self.current = 0

        # صفحه اصلی
        self.layout = BoxLayout(
            orientation="vertical",
            padding=40,
            spacing=25
        )

        # عنوان
        self.title = Label(
            text="💗 سوالای مهم از تو 💗",
            font_size=30,
            bold=True,
            size_hint_y=0.25
        )

        # سوال
        self.question = Label(
            text=self.questions[0],
            font_size=25,
            bold=True,
            size_hint_y=0.25
        )

        # کادر جواب
        self.answer = TextInput(
            multiline=False,
            font_size=22,
            halign="center",
            size_hint_y=0.2
        )

        # دکمه
        self.button = Button(
            text="بعدی ❤️",
            font_size=24,
            bold=True,
            size_hint_y=0.2
        )

        self.button.bind(on_press=self.next_question)

        self.layout.add_widget(self.title)
        self.layout.add_widget(self.question)
        self.layout.add_widget(self.answer)
        self.layout.add_widget(self.button)

        return self.layout

    def next_question(self, instance):

        # ذخیره جواب
        self.answers.append(self.answer.text)

        # پاک کردن کادر
        self.answer.text = ""

        self.current += 1

        # اگر هنوز سوال داریم
        if self.current < len(self.questions):

            self.question.text = self.questions[self.current]

            # آخرین سوال
            if self.current == len(self.questions) - 1:
                self.button.text = "جواب بده ❤️"

        # پایان سوال‌ها
        else:

            self.layout.clear_widgets()

            final_title = Label(
                text="❤️ جواب آخر ❤️",
                font_size=32,
                bold=True
            )

            final_message = Label(
                text=(
                    "mimiiiiiiiiiii bedeeeeeeeeeeee 😭😭😭\n\n"
                    "toloooooooooo khodaaaaaaaaaaa 😭😭😭\n\n"
                    "❤️ دوستت دارم ❤️"
                ),
                font_size=25,
                bold=True
            )

            self.layout.add_widget(final_title)
            self.layout.add_widget(final_message)


LoveApp().run()