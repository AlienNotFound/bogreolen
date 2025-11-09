class CommentDTO:
    def to_dict(comment):
        return {
            "comment_id": comment.comment_id,
            "user_id": comment.user_id,
            "review_id": comment.review_id,
            "comment_text": comment.comment
        }