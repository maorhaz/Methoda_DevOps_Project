# Methoda_DevOps_Project

To build the Docker image, you can use the command:
docker build -t main .

To schedule the image to run once a month we can use the command:
crontab -e

And to add:
0 0 1 * * docker run main .

-Cron: command-line utility is a job scheduler on Unix-like operating systems.
we use cron to schedule jobs.
