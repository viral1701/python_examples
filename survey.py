class AnonymousSurvey():
    """ Collect anonymous answers to a survey question """

    def __init__(self, question):
            """ Store a question, and prepare to store responses. """
            self.question = question
            self.responses = []
    
    def show_question(self):
        d