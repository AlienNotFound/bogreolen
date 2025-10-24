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