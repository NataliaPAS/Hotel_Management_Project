from sqlalchemy.orm import sessionmaker
from Domain.reviews import Reviews


class ReviewSQLModel:

    def __init__(self, engine):
        self.__engine = engine
        self.__my_session = sessionmaker(bind=engine)()

    def create_review(self, client_first_name, review_content, stars):
        self.__my_session.add(Reviews(client_first_name=client_first_name,review_content=review_content, stars=stars))
        self.__my_session.commit()

    def read_review(self):
        return self.__my_session.query(Reviews).all()

    def update_review(self, review_id, client_first_name=None, review_content=None, stars=None):
        my_review = self.__my_session.query(Reviews).filter_by(review_id=review_id).first()
        if my_review:
            self.__my_session.query(Reviews).filter_by(review_id=review_id).update({
                "client_first_name": f"{client_first_name or my_review.client_first_name}",
                "review_content": f"{review_content or my_review.review_content}",
                "stars": f"{stars or my_review.stars}",
            })
            self.__my_session.commit()

    def delete_review(self, review_id):
        self.__my_session.query(Reviews).filter_by(review_id=review_id).delete()
        self.__my_session.commit()

    def find_by_review_id(self, review_id):
        my_review = self.__my_session.query(Reviews).filter_by(review_id=review_id).first()
        return my_review

    def review_id_exists(self, review_id):
        my_review = self.__my_session.query(Reviews).filter_by(review_id=review_id).first()
        return True if my_review else False

    def get_last_review_id(self):
        my_review = self.__my_session.query(Reviews).order_by(Reviews.review_id.desc()).first()
        return my_review.review_id


if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine('mysql+pymysql://root:@localhost:3306/Hotel_Management', echo=False)
    model = ReviewSQLModel(engine=engine)

    model.create_review(client_first_name="natareview", review_content="text review", stars=4)
    model.update_review(review_id=model.get_last_review_id, client_first_name="natareview", review_content="text review verificat", stars=4.7)
    for review in model.read_review():
        print(review)

    # model.delete_review(1)
