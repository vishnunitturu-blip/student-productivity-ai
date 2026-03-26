from database.db import init_db
from agents.main_agent import run_agent

if __name__ == "__main__":
    print("Starting Student Productivity AI")

    init_db()
    run_agent()
