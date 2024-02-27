# 4.3 Homework

## Building Platform for ML Experiments

1. Install Docker platform on your computer: https://docs.docker.com/get-docker/

2. Follow the Docker tutorial available via Docker Labs and build simple ToDo list manager running in `Node.js`. The Docker tutorial repo is available at https://github.com/docker/getting-started

   1. Play around the Docker Platform: 

      - explore the Images tab: explore Image hieararchy and Layers
      - read in detail about commands used in the Image Layers: https://docs.docker.com/engine/reference/builder/

   2. Follow the tutorial and download the `app.zip` 

   3. Write the Dockerfile as instructed and build the image  

   4. Run the container and experiment with making changes to the app in `src/static/js/app.js` and see the changes within image. 

   5. Read the manual for `docker ps`, a command which helps to monitor the processes related to container, e.g CPU time, processses running for spefic user group, etc. 

   6. Follow instructions to run ubuntu container with the bash command to generate random number and store it to the file inside the container:  

      `docker run -d ubuntu bash -c "shuf -i 1-10000 -n 1 -o /data.txt && tail -f /dev/null"`

      Inspect the output stored within the container 

      `docker exec $(docker ps | grep 'ubuntu' | awk '{print $1}') cat /data.txt`

   7. Learn about the Container Volumes which allows to connect the container with specific filesystem back to the host machine. Work with the bind mounts to learn to control the location on your machine where the data are stored.

   8. Remember that each container should do just one think which it can do well. Learn to link two containers by using container networking, one with SQL database, second with the ToDo app.  

   9. Learn how to use docker compose tool which allows you to set up and share multi-container applications 

   10. Conclude by the seting up the multistage build and explore the layr caching. 

You are ready to learn how to build the experimentation platform for you machine learning project. 

