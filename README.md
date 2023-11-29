# blogs_corey

This is a simple blogging website built on django which I use to pactice DevOps concepts like 
1. CI/CD 
2. Containerisation
3. Kubernetes package management using Helm

How to run:
1. Using Docker
   * Setup a .env file with following variables
      ```
      DEBUG= "0"
      DJANGO_SUPERUSER_NAME 
      DJANGO_SUPERUSER_EMAIL
      DJANGO_SUPERUSER_PASSWORD
      DJANGO_SECRET_KEY
      POSTGRES_DB
      POSTGRES_USER
      POSTGRES_PASSWORD
      POSTGRES_HOST
      POSTGRES_PORT
      DATABASE_URL
      REDIS_PORT
      REDIS_HOST
      ```
   * Then use the following docker-compose command
     `$ docker compose up`

2. Using your local development environment.
   * Install the required dependencies 
     `pip install -r requirements.txt`
   
   * Run the development server by 
     `python3 manage.py runserver`  

3. To try out deployment on GKE using helm
   * Override the configuration in helm/blogs/templates/values.yaml
   * Label the storage class standard 
     `kubectl label sc standard app.kubernetes.io/managed-by=Helm`
   
   * Annotate the storage class by 
     `kubectl annotate sc standard meta.helm.sh/release-name=<release-name>`
     `kubectl annotate sc standard meta.helm.sh/release-namespace=default` 
      //you can change the release-namespace to your namespace
      
   * Install the chart by 
     `helm install <release-name> helm/blogs`
