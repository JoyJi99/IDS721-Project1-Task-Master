# Task Master

This repo is the source code for IDS721-Project1-Cloud Continuous Delivery of Microservice.

## Target
- Create a Microservice in Flask or Fast API
- Push source code to Github
- Configure Build System to Deploy changes
- Use IaC (Infrastructure as Code) to deploy code
- Use either AWS, Azure, GCP (recommended services include Google App Engine, AWS App Runner or Azure App Services)
- Containerization is optional, but recommended

## Finished
- A simple flask web app has been completed.
- Configured continuous run through github actions
- Dockerize application using Docker and Github Action
- Deploy to AWS Cloud9 (EC2)
- Use IaC (App Runner) to deploy code and check on CloudFormation

## How To Run
1. Install `virtualenv`:
```
$ pip3 install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command (for Mac):
```
$ source env/bin/activate
```

4. Then install the dependencies:
```
$ (env) pip3 install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python3 app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
