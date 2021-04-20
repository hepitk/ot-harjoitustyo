from initialize_database import initialize_database
from services.program_service import program_service


def main():
    initialize_database()
    program_service.start()


if __name__ == "__main__":
    main()
