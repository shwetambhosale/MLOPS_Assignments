# Hello World - Full Cycle Project

## Overview
This project demonstrates the end-to-end development, containerization, deployment, and CI/CD pipeline setup of a simple "Hello World" application. It covers the following phases:
1. Development of a simple animated "Hello World" app.
2. Dockerizing the application.
3. Deploying the Docker container to an AWS EC2 instance.
4. Setting up a CI/CD pipeline to automate the entire process.

## Phases of Development

### Phase 1: Development of the "Hello World" Application
The project started with the creation of a simple animated "Hello World" web application. I used HTML, CSS, and JavaScript to make the page display "Hello World" with an animation effect. The animation was implemented using CSS keyframes to make the text appear smoothly with a fade-in effect.

#### Technologies Used:
- HTML
- CSS
- JavaScript

### Phase 2: Dockerizing the Application
Once the web application was complete, I moved on to containerizing the application using Docker. The goal was to package the app in a Docker container to ensure that it could be run consistently in any environment.

1. **Dockerfile Creation**: I created a `Dockerfile` to define how the app should be built and run inside the container. The `Dockerfile` included the following steps:
   - Set up a base image (`nginx` in this case, as it’s a static website).
   - Copy the necessary files (HTML, CSS, JavaScript) into the container.
   - Expose the necessary port (usually port 80 for web servers).

2. **Building the Docker Image**: After the Dockerfile was ready, I built the Docker image using the `docker build` command.

3. **Running the Docker Container**: Once the image was built, I used the `docker run` command to run the container locally and verify that everything was working as expected.

#### Technologies Used:
- Docker
- Nginx (as the web server inside the container)

### Phase 3: Deploying to EC2 Instance
After verifying that the Docker container was working correctly, the next step was to deploy the application to an AWS EC2 instance. The following steps were involved:

1. **EC2 Instance Setup**: I launched an EC2 instance on AWS (Amazon Web Services) to serve as the server for the application. I selected an appropriate instance type (like `t2.micro` for cost-effectiveness) and configured the security group to allow HTTP traffic on port 80.

2. **Docker Installation on EC2**: I installed Docker on the EC2 instance to run the container. This was done by SSHing into the EC2 instance and following the necessary steps to install Docker.

3. **Pushing the Docker Image**: After the Docker image was created, I pushed it to Docker Hub (or a private Docker registry), making it available to pull onto the EC2 instance.

4. **Running the Application on EC2**: Once the image was pulled to the EC2 instance, I used the `docker run` command to start the container and serve the "Hello World" application.

#### Technologies Used:
- AWS EC2
- Docker
- Nginx (for serving the static website)

  ![Screenshot (265)](https://github.com/user-attachments/assets/e675bd61-b164-46c0-b959-51ccb49aa144)


### Phase 4: CI/CD Pipeline Setup
To automate the entire process, I set up a Continuous Integration and Continuous Deployment (CI/CD) pipeline. This pipeline automatically builds, tests, and deploys the application whenever new changes are made to the repository.

1. **Version Control**: The project is stored in GitHub, where any code changes are pushed to the repository.

2. **CI/CD Tool**: I used Jenkins to set up the CI/CD pipeline. Jenkins is a powerful automation server that integrates with GitHub to pull changes and trigger the build and deployment process.

3. **Pipeline Configuration**:
   - **Build**: The pipeline begins with building the Docker image using the `Dockerfile`.
   - **Test**: Automated tests are run to ensure that the application is working as expected.
   - **Deploy**: After successful testing, the Docker image is pushed to Docker Hub (or a private registry), and the EC2 instance is updated with the latest version by pulling the new image and restarting the container.

4. **Automation**: Once the pipeline was configured, any changes pushed to the GitHub repository triggered the entire process, from building the Docker image to deploying it on the EC2 instance.

#### Technologies Used:
- Jenkins
- GitHub
- Docker
- AWS EC2

  ![Screenshot 2024-10-02 174651](https://github.com/user-attachments/assets/e272c883-e3a1-4f38-80f8-7e0ebd1a4df0)


## Conclusion
This project was a great learning experience, allowing me to work with various technologies and understand the entire lifecycle of an application from development to deployment. By using Docker, I was able to ensure the application would run consistently across different environments. Deploying to AWS EC2 allowed me to experience real-world cloud deployment. Finally, the CI/CD pipeline setup with Jenkins automated the entire process, ensuring that future updates could be deployed seamlessly.

## Future Enhancements
- Adding automated tests to the pipeline for more robust validation.
- Scaling the application using Kubernetes or AWS ECS for handling traffic spikes.

