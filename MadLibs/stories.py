class Story:
    """build the story using prompts from the user"""

    def __init__(self, words, text):
        """Build the story with a template"""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Add answers to template"""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """I remember the time I spent at {place}, such beautiful {adjective} {noun}! I remember specifically a mean who loved to {verb} {plural_noun}."""
)
