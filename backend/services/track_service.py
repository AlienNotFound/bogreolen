from backend.connection import db
from backend.models import Tracks, Lists, Users, Books
from backend.services.base_service import BaseService
from datetime import datetime
from sqlalchemy import func

class TrackService(BaseService):
    @staticmethod
    def track_book(user_id, book_id, read_today: bool, current_page: int, last_page: int):
        if read_today:
            date_read = datetime.now().strftime("%Y-%m-%d")

        if current_page > last_page:
            return False, 'Current page cannot be higher than Last page.'

        track = Tracks(user_id=user_id, book_id=book_id, current_page=current_page, last_page=last_page, date=date_read)
        db.session.add(track)

        success, result = BaseService.commit_session(track)

        return success, result
    
    @staticmethod
    def edit_track(track_id, current_page: int, last_page: int, date):
        track = BaseService.get_by_id(Tracks, Tracks.track_id, track_id)

        if track == None:
            return f'Track entry not found'

        if current_page > last_page:
            return False, 'Current page cannot be higher than Last page.'
        
        track.current_page = current_page
        track.last_page = last_page
        track.date = date

        success, result = BaseService.commit_session(track)

        return success, result
    
    @staticmethod
    def delete_track(track_id):
        return BaseService.delete(Tracks, Tracks.track_id, track_id)
    
    @staticmethod
    def get_track_by_id(track_id):
        return BaseService.get_by_id(Tracks, Tracks.track_id, track_id)
    
    @staticmethod
    def get_all_tracks_by_user(user_id):
        return BaseService.get_all_by_id(Tracks, Tracks.user_id, user_id)
    
    @staticmethod
    def get_status_by_user(user_id):
        lists = BaseService.get_all_by_id(Lists, Lists.user_id, user_id)

        result = lists

        return result
    
    @staticmethod
    def get_modal_tracks(user_id):

        subq = (
            db.session.query(
                Tracks.book_id,
                func.max(Tracks.track_id).label("max_id")
            )
            .filter(Tracks.user_id == user_id)
            .group_by(Tracks.book_id)
            .subquery()
        )

        result = (
            db.session.query(Tracks, Books, Users)
            .join(Books, Tracks.book_id == Books.book_id)
            .join(Users, Tracks.user_id == Users.user_id)
            .join(subq, Tracks.track_id == subq.c.max_id)
            .all()
        )

        return result