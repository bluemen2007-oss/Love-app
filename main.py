from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


# Background color
Window.clearcolor = (1, 0.75, 0.82, 1)


class LoveApp(App):

    def build(self):

        self.questions = [
            "What is your name?",
            "How old are you?",
            "What is your favorite hobby?",
            "How much do you love me?"
        ]

        self.answers = []
        self.current = 0

        # Main layout
        self.layout = BoxLayout(
            orientation="vertical",
            padding=[30, 30, 30, 40],
            spacing=20
        )

        # Top space
        top_space = BoxLayout(
            size_hint_y=0.05
        )

        # Title
        self.title_label = Label(
            text="IMPORTANT QUESTIONS",
            font_size=32,
            bold=True,
            size_hint_y=0.18,
            halign="center",
            valign="middle"
        )

        self.title_label.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        # Question
        self.question_label = Label(
            text=self.questions[0],
            font_size=28,
            bold=True,
            size_hint_y=0.25,
            halign="center",
            valign="middle"
        )

        self.question_label.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        # Answer input
        self.answer_input = TextInput(
            multiline=False,
            font_size=24,
            size_hint_y=None,
            height=65,
            padding=[15, 15],
            halign="center"
        )

        # Space
        middle_space = BoxLayout(
            size_hint_y=0.05
        )

        # Next button
        self.next_button = Button(
            text="NEXT",
            font_size=25,
            bold=True,
            size_hint_y=None,
            height=70
        )

        self.next_button.bind(
            on_press=self.next_question
        )

        # Bottom space
        bottom_space = BoxLayout(
            size_hint_y=0.08
        )

        # Add widgets
        self.layout.add_widget(top_space)
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.question_label)
        self.layout.add_widget(self.answer_input)
        self.layout.add_widget(middle_space)
        self.layout.add_widget(self.next_button)
        self.layout.add_widget(bottom_space)

        return self.layout

    def next_question(self, instance):

        # Save answer
        answer = self.answer_input.text.strip()
        self.answers.append(answer)

        self.current += 1

        # Still have questions
        if self.current < len(self.questions):

            self.question_label.text = self.questions[self.current]
            self.answer_input.text = ""

            # Last question
            if self.current == len(self.questions) - 1:
                self.next_button.text = "FINISH"

        # All questions finished
        else:

            self.layout.clear_widgets()

            # Final title
            final_title = Label(
                text="THE END",
                font_size=36,
                bold=True,
                size_hint_y=0.25,
                halign="center",
                valign="middle"
            )

            final_title.bind(
                size=lambda instance, value:
                setattr(instance, "text_size", value)
            )

            # Your final messages
            final_message = Label(
                text=(
                    "Mimiiiiiiiiii bedeeeeeeeeee\n\n"
                    "Toloooooooooo khodaaaaaaaaaaa\n\n"
                    "I LOVE YOU"
                ),
                font_size=30,
                bold=True,
                halign="center",
                valign="middle",
                size_hint_y=0.55
            )

            final_message.bind(
                size=lambda instance, value:
                setattr(instance, "text_size", value)
            )

            self.layout.add_widget(final_title)
            self.layout.add_widget(final_message)


if __name__ == "__main__":
    LoveApp().run()
