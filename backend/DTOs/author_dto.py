class AuthorDTO:
    @staticmethod
    def to_dict(author):
        return {
            "author_id": author.author_id,
            "name": author.name
        }