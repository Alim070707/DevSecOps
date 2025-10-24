#!/usr/bin/env python3
"""
Simple Hello World application with semantic versioning demonstration
"""

import sys

class GreetingApp:
    def __init__(self):
        self.language = "en"
        self.greetings = {
            "en": "Hello",
            "es": "Hola", 
            "fr": "Bonjour",
            "de": "Hallo"
        }
    
    def set_language(self, lang):
        """Set the language for greetings"""
        if lang in self.greetings:
            self.language = lang
            return True
        return False
    
    def greet(self, name="World"):
        """Generate greeting message"""
        greeting = self.greetings.get(self.language, "Hello")
        return f"{greeting}, {name}!"
    
    def get_available_languages(self):
        """Get list of available languages"""
        return list(self.greetings.keys())

def main():
    app = GreetingApp()
    
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    
    print(app.greet(name))
    
    # Show available languages
    if len(sys.argv) > 2 and sys.argv[2] == "--show-languages":
        print(f"Available languages: {', '.join(app.get_available_languages())}")

if __name__ == "__main__":
    main()
