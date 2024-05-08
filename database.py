from sqlalchemy import create_engine, text
engine = create_engine("mysql+pymysql://root:xxxx@127.0.0.1/space_invaders?charset=utf8mb4")
with engine.connect()as conn:
    result = conn.execute(text("SELECT * FROM users"))
    print(result.all())
def load_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        users = [dict(row) for row in result.fetchall()]
        return users