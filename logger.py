import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

logging = config.get('console_logging', {})

def log(message):
    # Used for ease of debugging
    if logging:
        print(f"--LOG--: {message}")