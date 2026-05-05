from dotenv import dotenv_values;

config = dotenv_values(".env")

def main():
    print(f"uvicorn host: {config['UVICORN_HOST']} \nuvicorn port: {config['UVICORN_PORT']}")


if __name__ == "__main__":
    main()
