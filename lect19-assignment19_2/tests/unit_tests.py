import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("Purple")
        self.assertEquals(response, "")
        
    def test_add_command(self):
        response = functions.get_chatbot_response("!! add 10 5")
        self.assertEquals(response, 15)
    
    def test_hey_command(self):
        response = functions.get_chatbot_response("!! Hey Joshua")
        self.assertEquals(response, "What's up!")
        
    def test_divide_command(self):
        response = functions.get_chatbot_response("!! divide 10 5")
        self.assertEquals(response, 2.0)
        
    def test_say_command(self):
        response = functions.get_chatbot_response("!! say Bum")
        self.assertEquals(response, "Bum")
        
    
    

if __name__ == '__main__':
    unittest.main()
