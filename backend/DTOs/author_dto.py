class AuthorDTO:
    @staticmethod
    def to_dict(author):
        return {
            "authorid": author.authorid,
            "name": author.name
        }