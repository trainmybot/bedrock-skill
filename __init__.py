from mycroft import MycroftSkill, intent_file_handler


class Bedrock(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bedrock.intent')
    def handle_bedrock(self, message):
        self.speak_dialog('bedrock')
    
    @intent_file_handler('bedrockUses.intent')
    def handle_bedrock(self, message):
        self.speak_dialog('bedrockUses')


def create_skill():
    return Bedrock()

