# Dockerized Python Flask - MongoDB REST API 
  ## Technologies used
    ### Python 3.10.12
    ### Flask 3.0.3
    ### PyMongo 4.7.2
    ### Waitress 3.0.0
    ### Docker - DockerCompose
  ## To use it
    ### Clone the repository and add the following env variables using the terminal
      #### MONGO_DB_URI = "The uri of your mongodb instance"
      #### MONGO_DB_NAME = "The name of your database inside your mongodb instance"
      #### PORT = "optional - The port for you API inside your docker container"
    ### Run
      #### docker compose up
  ## Routes
    ### [GET] localhost:3000/api/v1/stores
    ### [POST] localhost:3000/api/v1/stores/add
      #### json body example
        ##### {
          	"new_store": {
          		"name": "my_store",
          		"location": "Ecuador"
          	}
          }
    ### [PUT] localhost:3000/api/v1/stores/update/<store_id>
      #### json body example
        ##### {
        	"new_store_data": {
        		"name": "store_updated",
        		"location": "Colombia"
        	}
        }
    ### [DELETE] localhost:3000/api/v1/stores/delete/<store_id>
