from backend.connection import db
from backend.models.tracks_model import Trackstb
from backend.services.base_service import BaseService
from datetime import datetime

class TrackService(BaseService):
    @staticmethod
    def track_book(user_id, book_id, read_today: bool, current_page, last_page):
        if read_today:
            date_read = datetime.now().strftime("%Y-%m-%d")

        track = Trackstb(user_id=user_id, book_id=book_id, current_page=current_page, last_page=last_page, date=date_read)
        db.session.add(track)

        _, result = BaseService.commit_session(track)

        return result
    
    @staticmethod
    def edit_track(track_id, current_page, last_page):
        track = BaseService.get_by_id(Trackstb, Trackstb.track_id, track_id)

        if track == None:
            return f'Track entry not found'
        
        track.current_page = current_page
        track.last_page = last_page

        _, result = BaseService.commit_session(track)

        return result
    
    @staticmethod
    def delete_track(track_id):
        return BaseService.delete(Trackstb, Trackstb.track_id, track_id)
    
    @staticmethod
    def get_track_by_id(track_id):
        return BaseService.get_by_id(Trackstb, Trackstb.track_id, track_id)
    
    @staticmethod
    def get_all_tracks_by_user(user_id):
        return BaseService.get_by_id(Trackstb, Trackstb.user_id, user_id)