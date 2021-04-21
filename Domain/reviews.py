from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Reviews(Base):
    __tablename__ = "reviews"
    review_id = Column(Integer, primary_key=True, autoincrement=True)
    client_first_name = Column(String, nullable=False)
    review_content = Column(String, nullable=False)
    stars = Column(Float, nullable=False)

    def __str__(self):
        return (f'client_first_name: {self.client_first_name}\n'
                f'review_content: {self.review_content}\n'
                f'stars: {self.stars}\n')

