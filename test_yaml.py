import yaml
with open('db_creds.yaml', 'r') as file:
    db_credentials = yaml.safe_load(file)

print(db_credentials)