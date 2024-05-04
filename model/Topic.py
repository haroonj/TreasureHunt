class Topic:
    def __init__(self):
        self.topics = ["Science", "History & Culture", "Geography", "Sports", "Math"]
        self.objectives = {
            "Science": "Learn about the scientific principles that govern the universe.",
            "History & Culture": "Explore the rich histories and diverse cultures around the world.",
            "Geography": "Discover the various geographical features and landscapes of our planet.",
            "Sports": "Understand the fundamentals of different sports and their historical significance.",
            "Math": "Dive into the concepts and applications of mathematics in everyday life."
        }

    def get_topics(self):
        return self.topics

    def get_objectives(self):
        return self.objectives
