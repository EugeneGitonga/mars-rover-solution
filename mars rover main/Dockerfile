#Deriving the latest base image
FROM python:3.6
LABEL Maintainer="eugenegitonga"
ADD mars_rover_solution.py .

WORKDIR /app
COPY mars_rover_solution.py ./app

CMD [ "python", "./mars_rover_solution.py"]





