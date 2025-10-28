class TrackDTO:
    @staticmethod
    def to_dict(track):
        return {
            "track_id": track.track_id,
            "book_id": track.book_id,
            "user_id": track.user_id,
            "current_page": track.current_page,
            "last_page": track.last_page,
            "date": track.date
        }
    
    @staticmethod
    def overview_dict(track):
        user_list = next((list for list in track.book.lists if list.userid == track.user_id), None)

        return {
            "track_id": track.track_id,
            "book_id": track.book_id,
            "user_id": track.user_id,
            "current_page": track.current_page,
            "last_page": track.last_page,
            "date": track.date,
            "title": track.book.title,
            "book_status": user_list.listname.value if user_list else None
        }
    
    @staticmethod
    def modal_dict(track):
         return {
            "book_id": track.bookid,
            "user_id": track.userid,
            "title": track.book.title,
            "image": track.book.image,
            "book_status": track.listname.value
        }